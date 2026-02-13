"""
Task 1: Data Cleaning Script
Objective:
- Read CSV file
- Remove null rows
- Handle missing values
- Replace wrong values
- Standardize date format
- Save cleaned CSV
"""

import pandas as pd


def clean_data(input_file: str, output_file: str) -> None:
    """
    Cleans the given CSV file and saves the cleaned version.
    """

    try:
        # Read CSV
        df = pd.read_csv(input_file)
        print("CSV file loaded successfully.")

        # Initial shape
        print(f"Initial Shape: {df.shape}")

        # Remove completely empty rows
        df = df.dropna(how="all")

        # Handle Missing Values
        if 'age' in df.columns:
            df['age'] = df['age'].fillna(df['age'].median())

        if 'salary' in df.columns:
            df['salary'] = df['salary'].fillna(df['salary'].mean())

        if 'name' in df.columns:
            df['name'] = df['name'].fillna("Unknown").str.strip()

        # Replace Wrong Values (Negative age/salary)
        if 'age' in df.columns:
            df.loc[df['age'] < 0, 'age'] = df['age'].median()

        if 'salary' in df.columns:
            df.loc[df['salary'] < 0, 'salary'] = df['salary'].mean()

        # Standardize Date Format
        if 'joining_date' in df.columns:
            df['joining_date'] = pd.to_datetime(
                df['joining_date'],
                errors='coerce'
            )
            df['joining_date'] = df['joining_date'].dt.strftime('%Y-%m-%d')

        # Final shape
        print(f"Final Shape: {df.shape}")

        # Save Cleaned Data
        df.to_csv(output_file, index=False)

        print("Data cleaning completed successfully.")
        print(f"Cleaned file saved as: {output_file}")

    except Exception as e:
        print("Error occurred during data cleaning:")
        print(e)


if __name__ == "__main__":
    input_path = "sample_data.csv"
    output_path = "cleaned_data.csv"

    clean_data(input_path, output_path)
