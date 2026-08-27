# Day 013: Atomic Safe File Writer & Backup Manager

- **Date:** 2026-08-27
- **Category:** File & Data Handling
- **Difficulty:** Intermediate

---

# Atomic Safe File Writer & Backup Manager

## Background
Directly writing to production files can cause corruption if power is lost or the process crashes mid-write.
Atomic writing creates a temporary sibling file and performs an OS-level atomic rename (`os.replace`) upon successful write.

## Requirements
Implement `atomic_write_file` and `AtomicFileWriter` context manager in `solution.py`:
1. `atomic_write_file(filepath: str, content: str, make_backup: bool = False, encoding: str = 'utf-8') -> None`:
   - Writes content to a temporary file in the same directory as `filepath`.
   - Flushes and syncs (`os.fsync`) to disk.
   - If `make_backup` is True and `filepath` already exists, creates a `.bak` backup copy.
   - Replaces the target file atomically using `os.replace`.
   - Ensures temporary files are cleaned up if an exception occurs.

2. `class AtomicFileWriter`:
   - Context manager syntax:
     ```python
     with AtomicFileWriter("data.json") as f:
         f.write('{"status": "ok"}')
     ```
   - Only commits file upon clean context exit; discards partial writes on error.

## Run Tests
```bash
python test_solution.py
```
