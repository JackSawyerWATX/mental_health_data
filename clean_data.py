import pandas as pd
from pathlib import Path

def main():
    base = Path(__file__).parent
    csv_path = base / "Mental_Health_Care_in_the_Last_4_Weeks.csv"

    print("CSV:", csv_path)

    try:
        df = pd.read_csv(csv_path, header=0, sep=",", encoding="utf-8", engine="python")
    except FileNotFoundError:
        print("Error: CSV file not found at", csv_path)
        return
    except Exception as e:
        print("Error reading CSV:", e)
        return

    # Diagnostics
    print("Loaded shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print("Missing values per column:\n", df.isna().sum())
    # Only drop rows missing these key columns (don't drop because of unrelated empty cells)
    key_cols = ["Indicator", "Group", "State", "Value"]
    existing_key_cols = [c for c in key_cols if c in df.columns]
    if existing_key_cols:
        cleaned = df.dropna(subset=existing_key_cols)
        print(f"\nDropped rows missing {existing_key_cols}: {df.shape[0] - cleaned.shape[0]} rows removed")
    else:
        print("\nWarning: expected key columns not found; falling back to dropping rows that are all-NA")
        cleaned = df.dropna(how="all")
        print("Rows removed:", df.shape[0] - cleaned.shape[0])

    # Configure pandas to print the full table (rows, columns, and full cell contents).
    # WARNING: if your CSV is very large this will print a lot of lines.
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    print()
    print(df)

    print("Cleaned shape:", cleaned.shape)
    print(cleaned.head())

if __name__ == "__main__":
    main()

# Optionally save
# cleaned.to_csv(base / "cleaned_mental_health.csv", index=False)