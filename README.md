# Mental Health Data — Cleaning & Diagnostics

This repository contains a small set of example scripts and a CSV used for exploring a short mental-health access dataset.

Files
- `Mental_Health_Care_in_the_Last_4_Weeks.csv`: Source dataset (CSV).
- `mental_health.py`: Minimal example that filters the dataset to Washington and prints a cleaned view.
- `clean_data.py`: Updated script that safely loads the CSV, prints diagnostics, and prints the entire DataFrame (no aggressive dropping). Includes error handling if the file cannot be read.
- `test.py`: small example/test script (contains example pandas usage).

Purpose
- Provide a couple of small scripts that demonstrate loading and inspecting the CSV. `clean_data.py` was updated to be safer and more verbose so you can diagnose why rows were being dropped.

What changed in `clean_data.py`
- Uses `pandas.read_csv` with explicit encoding and engine.
- Adds error handling for missing/unreadable CSV files.
- Prints diagnostics: loaded shape, column names, and missing-value counts per column.
- Sets pandas display options and prints the full DataFrame. (Warning: this will print a lot of lines for large files.)
- Keeps a safer cleaning step that only drops rows missing a few key columns if they exist; otherwise falls back to dropping all-empty rows.

Usage
1. Ensure you have Python 3.8+ installed.
2. Install `pandas` if needed:

```powershell
python -m pip install pandas
```

3. Run the updated cleaner (PowerShell example):

```powershell
cd "c:\Users\jonat\OneDrive\Documents\mental_health_data"
python clean_data.py
```

Notes on output
- The script will print diagnostics first (shape, columns, missing counts), then the full loaded `DataFrame`, and finally a short summary of cleaned rows (if key columns exist).
- If you see an empty DataFrame printed, check the diagnostics that immediately precede it (shape and missing counts) and make sure the CSV loaded correctly.

Suggested next steps / improvements
- Add a `--preview` flag to limit output (e.g., `--head 50`).
- Add `--state` and `--output cleaned.csv` arguments to control filtering and to save the cleaned data.
- Replace prints with logging for better control over verbosity.

If you want, I can implement any of the suggested improvements (arg parsing, preview flag, saving output). Tell me which one to do next.
