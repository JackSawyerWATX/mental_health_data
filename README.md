# Mental Health Data — Cleaning Script

This repository contains a small data-cleaning script and the source CSV used for a quick exploration of mental health care access.

Files
- `Mental_Health_Care_in_the_Last_4_Weeks.csv`: Source dataset (CSV).
- `mental_health.py`: Simple Python script that loads, cleans, filters, and prints the cleaned data.

Purpose
- Provide a minimal example that reads the CSV, removes incomplete rows, filters for the state of Washington, and prints the cleaned table to the console for inspection.

How it works
- The script uses `pandas` to load the CSV.
- It drops rows where any of the important columns `Indicator`, `Group`, `State`, or `Value` are missing.
- It filters the rows to only include `State == 'Washington'`.
- It adjusts pandas display options so the entire cleaned table is printed (no row/column truncation).

Usage
1. Ensure you have Python 3.8+ installed.
2. Install `pandas` if you do not already have it:

```powershell
python -m pip install pandas
```

3. Run the script from the repository folder (PowerShell example):

```powershell
cd "c:\Users\jonat\OneDrive\Documents\mental_health_data"
python mental_health.py
```

What the output shows
- The printed output is the cleaned `DataFrame` after dropping rows with missing values in the key columns and after filtering to Washington.
- The script sets `display.max_rows`, `display.max_columns`, and `display.max_colwidth` so the DataFrame is fully visible in the console.

Possible improvements
- Make the state filter a command-line argument instead of hard-coded.
- Save the cleaned data to a new CSV (e.g., `cleaned_mental_health.csv`).
- Add basic validation for the CSV path and better error handling.
- Add a small unit test or a `--preview` flag to print only the head of the cleaned DataFrame for very large files.

Contact
- If you want me to add any of the improvements above (arg parsing, saving output, or tests), say which and I'll implement them.
