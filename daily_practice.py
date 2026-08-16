"""
daily_practice.py
Automated daily Python practice generator, test scaffold builder, and GitHub commit engine.
"""

import argparse
import datetime
import json
import logging
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import exercise_bank

# Base Directory
BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "practice-log.txt"
CONFIG_FILE = BASE_DIR / "config.json"
README_FILE = BASE_DIR / "README.md"


def setup_logger() -> logging.Logger:
    """Configures structured, timestamped logger to both console and practice-log.txt."""
    logger = logging.getLogger("DailyPythonPractice")
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers if re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # File Handler
        file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.INFO)
        logger.addHandler(file_handler)

        # Console Handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.INFO)
        logger.addHandler(console_handler)

    return logger


def load_config() -> dict:
    """Loads configuration from config.json with robust fallbacks."""
    default_config = {
        "github_username": "rohitmali9860-web",
        "repo_name": "daily-python-practice",
        "repo_path": str(BASE_DIR),
        "remote_url_https": "https://github.com/rohitmali9860-web/daily-python-practice.git",
        "remote_url_ssh": "git@github.com:rohitmali9860-web/daily-python-practice.git",
        "preferred_auth": "HTTPS",
        "branch": "main",
        "auto_push": True,
        "commit_prefix": "Day",
        "author_name": "rohitmali9860-web",
        "author_email": ""
    }

    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                loaded = json.load(f)
                default_config.update(loaded)
        except Exception as e:
            logging.getLogger("DailyPythonPractice").warning(f"Failed to read config.json: {e}")

    return default_config


def run_git_command(args: List[str], cwd: Path, logger: logging.Logger) -> Tuple[bool, str]:
    """
    Executes a git command safely and captures output/errors.
    """
    cmd = ["git"] + args
    try:
        result = subprocess.run(
            cmd,
            cwd=str(cwd),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30
        )
        output = result.stdout.strip()
        err = result.stderr.strip()

        if result.returncode == 0:
            return True, output if output else err
        else:
            return False, err if err else output
    except Exception as e:
        return False, str(e)


def ensure_git_initialized(repo_dir: Path, config: dict, logger: logging.Logger) -> bool:
    """Ensures git repository is initialized with configured remote and branch."""
    git_dir = repo_dir / ".git"
    if not git_dir.exists():
        logger.info("Initializing new Git repository...")
        ok, out = run_git_command(["init"], repo_dir, logger)
        if not ok:
            logger.error(f"Failed to initialize git repository: {out}")
            return False

        # Set default branch to main
        run_git_command(["branch", "-M", config.get("branch", "main")], repo_dir, logger)

    # Check remote origin
    ok, remotes = run_git_command(["remote", "-v"], repo_dir, logger)
    remote_url = config.get("remote_url_https") if config.get("preferred_auth") == "HTTPS" else config.get("remote_url_ssh")
    
    if "origin" not in remotes:
        logger.info(f"Adding git remote origin: {remote_url}")
        run_git_command(["remote", "add", "origin", remote_url], repo_dir, logger)
    
    return True


def get_existing_days(repo_dir: Path) -> List[int]:
    """Finds all existing dayNNN directories and returns sorted integer day numbers."""
    day_dirs = []
    pattern = re.compile(r"^day(\d{3,})$", re.IGNORECASE)
    
    if repo_dir.exists():
        for item in repo_dir.iterdir():
            if item.is_dir():
                match = pattern.match(item.name)
                if match:
                    day_dirs.append(int(match.group(1)))
                    
    return sorted(day_dirs)


def is_already_generated_today(repo_dir: Path, today_str: str) -> Optional[int]:
    """
    Checks if today's date already exists in the root README.md index table.
    Returns the day number if already generated, otherwise None.
    """
    if not README_FILE.exists():
        return None

    try:
        content = README_FILE.read_text(encoding="utf-8")
        # Match lines like: | [Day 001](day001/) | 2026-08-16 |
        pattern = re.compile(r"\|\s*\[Day\s*(\d+)\][^\n]+\|\s*" + re.escape(today_str) + r"\s*\|")
        match = pattern.search(content)
        if match:
            return int(match.group(1))
    except Exception:
        pass

    return None


def init_root_readme_if_needed():
    """Creates the root README.md documentation and progress tracker if missing."""
    if not README_FILE.exists():
        content = """# 🚀 Daily Python Practice

An automated, hands-on repository for daily Python development and engineering exercises.

Every morning at **9:00 AM**, a new real-world challenge is scaffolded with specifications, type-annotated starter code, and automated unit tests.

---

## 🎯 Topic Domains
- 🧱 **OOP & Design Patterns**: Encapsulation, inheritance, dunder methods, dataclasses, design patterns.
- 🏷️ **GS1 & Barcode Utilities**: Modulo-10 check digits, GS1 Application Identifiers, Code 128, DataMatrix formatting.
- ⚡ **Flask & API Mini-Features**: Custom auth decorators, sliding-window rate limiters, schema validators, error handlers.
- 💾 **File & Data Handling**: Atomic file writes, structured log parsers, streaming CSV aggregators, SQLite DAOs.
- 🧮 **Algorithms & Data Structures**: LRU Cache, Prefix Trees (Tries), priority queues, binary search variations.

---

## 🛠️ Daily Workflow
1. **Morning Run (9:00 AM)**: The automated scheduler scaffolds `dayNNN/` with `solution.py` and `test_solution.py`.
2. **Implement Logic**: Open `dayNNN/solution.py` and fill in the logic marked with `TODO:`.
3. **Verify with Tests**:
   ```bash
   cd dayNNN
   python test_solution.py
   ```
4. **Push Solution**:
   ```bash
   git add .
   git commit -m "Day NNN: Solved <Topic>"
   git push origin main
   ```

---

## 📈 Practice Progress Index

| Day | Date | Category | Challenge | Status |
| :--- | :--- | :--- | :--- | :--- |
"""
        README_FILE.write_text(content, encoding="utf-8")


def append_to_root_readme(day_str: str, date_str: str, category: str, title: str):
    """Appends a new day entry to the tracking table in root README.md."""
    init_root_readme_if_needed()
    
    row = f"| [{day_str}]({day_str.lower()}/) | {date_str} | {category} | {title} | 🟡 Scaffolded |\n"
    
    with open(README_FILE, "a", encoding="utf-8") as f:
        f.write(row)


def create_day_scaffold(
    day_num: int,
    exercise: dict,
    date_str: str,
    repo_dir: Path,
    logger: logging.Logger
) -> Path:
    """Generates the dayNNN directory with README.md, solution.py, and test_solution.py."""
    day_folder_name = f"day{day_num:03d}"
    day_dir = repo_dir / day_folder_name
    day_dir.mkdir(parents=True, exist_ok=True)

    # 1. Write day README.md
    readme_header = f"""# Day {day_num:03d}: {exercise['title']}

- **Date:** {date_str}
- **Category:** {exercise['category']}
- **Difficulty:** {exercise['difficulty']}

---

"""
    full_readme = readme_header + exercise["readme"]
    (day_dir / "README.md").write_text(full_readme, encoding="utf-8")

    # 2. Write solution.py (Scaffold template with TODOs)
    (day_dir / "solution.py").write_text(exercise["solution_scaffold"].strip() + "\n", encoding="utf-8")

    # 3. Write test_solution.py (Test suite)
    (day_dir / "test_solution.py").write_text(exercise["test_code"].strip() + "\n", encoding="utf-8")

    logger.info(f"Scaffolded {day_folder_name}: {exercise['title']} ({exercise['category']})")
    return day_dir


def main():
    parser = argparse.ArgumentParser(description="Automated Daily Python Practice Generator")
    parser.add_argument("--force", action="store_true", help="Force generation even if today's challenge already exists")
    parser.add_argument("--dry-run", action="store_true", help="Generate files without git commit or push")
    parser.add_argument("--day", type=int, default=None, help="Force a specific day number")
    args = parser.parse_args()

    logger = setup_logger()
    config = load_config()
    repo_dir = Path(config.get("repo_path", BASE_DIR))
    repo_dir.mkdir(parents=True, exist_ok=True)

    today_str = datetime.date.today().strftime("%Y-%m-%d")
    logger.info(f"--- Starting Daily Python Practice Run for {today_str} ---")

    # Check duplicate generation for today
    if not args.force and not args.day:
        existing_day_today = is_already_generated_today(repo_dir, today_str)
        if existing_day_today is not None:
            logger.info(
                f"Today's practice challenge (Day {existing_day_today:03d}) has already been scaffolded for {today_str}. "
                "Use --force to generate another challenge."
            )
            return 0

    # Determine Day Number
    existing_days = get_existing_days(repo_dir)
    if args.day:
        day_num = args.day
    else:
        day_num = (max(existing_days) + 1) if existing_days else 1

    day_str = f"Day {day_num:03d}"

    # Pick exercise from bank
    exercise = exercise_bank.get_exercise_by_day(day_num)
    logger.info(f"Selected Exercise for {day_str}: '{exercise['title']}' [{exercise['category']}]")

    # Scaffold files
    day_dir = create_day_scaffold(day_num, exercise, today_str, repo_dir, logger)

    # Update Root README
    append_to_root_readme(f"Day {day_num:03d}", today_str, exercise["category"], exercise["title"])
    logger.info("Updated root README.md progress table.")

    if args.dry_run:
        logger.info("[DRY-RUN] Files created successfully. Skipping git commit and push.")
        return 0

    # Ensure Git initialized
    ensure_git_initialized(repo_dir, config, logger)

    # Git Add
    ok_add, out_add = run_git_command(["add", "."], repo_dir, logger)
    if not ok_add:
        logger.error(f"Git add failed: {out_add}")

    # Git Commit
    commit_msg = f"Day {day_num:03d}: {exercise['title']} - {today_str}"
    ok_commit, out_commit = run_git_command(["commit", "-m", commit_msg], repo_dir, logger)
    
    if ok_commit:
        logger.info(f"Git commit created: \"{commit_msg}\"")
    else:
        if "nothing to commit" in out_commit.lower():
            logger.info("Nothing new to commit.")
        else:
            logger.warning(f"Git commit notice: {out_commit}")

    # Git Push
    if config.get("auto_push", True):
        branch = config.get("branch", "main")
        logger.info(f"Attempting git push to origin/{branch}...")
        ok_push, out_push = run_git_command(["push", "-u", "origin", branch], repo_dir, logger)
        
        if ok_push:
            logger.info(f"SUCCESS: Pushed {day_str} to origin/{branch} successfully.")
        else:
            logger.warning(
                f"NOTICE: Commit was saved locally, but git push to origin/{branch} did not complete: {out_push}. "
                "This is normal if the remote repository has not yet been created on GitHub or if you are offline. "
                "It will be pushed automatically on the next run."
            )

    logger.info(f"--- Completed Daily Python Practice Run for {day_str} ---")
    return 0


if __name__ == "__main__":
    sys.exit(main())
