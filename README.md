# 🚀 Daily Python Practice

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
1. **Morning Run (9:00 AM)**: The automated scheduler scaffolds `dayNNN/` with `solution.py` and `test_solution.py` and commits to GitHub.
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

## ⚙️ Setup & Scheduled Task Registration

### 1. Register Task Scheduler (Runs 9:00 AM daily + catch-up on boot)
Open PowerShell and run:
```powershell
powershell -ExecutionPolicy Bypass -File C:\Users\Rohit\daily-python-practice\setup_task.ps1
```

### 2. Manual Test Run
You can trigger a challenge generation manually at any time:
```powershell
cd C:\Users\Rohit\daily-python-practice
python daily_practice.py
```
Or double-click `run_daily.bat`.

---

## 📈 Practice Progress Index

| Day | Date | Category | Challenge | Status |
| :--- | :--- | :--- | :--- | :--- |
| [Day 001](day001/) | 2026-08-16 | GS1 / Barcode Utilities | EAN-13 & UPC-A Check Digit Calculator | 🟡 Scaffolded |
| [Day 002](day 002/) | 2026-08-16 | OOP Practice | Bank Account & Transaction Engine (OOP) | 🟡 Scaffolded |
| [Day 003](day003/) | 2026-08-17 | GS1 / Barcode Utilities | GS1 Application Identifier (AI) Barcode Parser | 🟡 Scaffolded |
| [Day 004](day004/) | 2026-08-18 | Flask Mini-Features | Flask Auth & Sliding-Window Rate Limiter Decorators | 🟡 Scaffolded |
| [Day 005](day005/) | 2026-08-19 | File & Data Handling | Atomic Safe File Writer & Backup Manager | 🟡 Scaffolded |
