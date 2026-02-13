"""
Task 2: Employee Salary Analyzer
Objective:
- Read employee data
- Calculate average salary
- Department-wise average salary
- Highest & lowest paid employee
- Print formatted business report
"""

import pandas as pd


def analyze_salary(file_path: str) -> None:
    """
    Reads employee salary data and prints formatted report.
    """

    try:
        # Load data
        df = pd.read_csv(file_path)
        print("Employee data loaded successfully.\n")

        # Basic validation
        required_columns = {"employee_id", "name", "department", "salary"}
        if not required_columns.issubset(df.columns):
            raise ValueError("Missing required columns in employee_data.csv")

        # Ensure salary is numeric
        df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

        # Remove rows where salary is missing
        df = df.dropna(subset=["salary"])

        # Calculations
        average_salary = df["salary"].mean()
        department_salary = df.groupby("department")["salary"].mean()
        highest_paid = df.loc[df["salary"].idxmax()]
        lowest_paid = df.loc[df["salary"].idxmin()]

        # Print Report
        print("=" * 50)
        print("         EMPLOYEE SALARY REPORT")
        print("=" * 50)

        print(f"\nOverall Average Salary: ₹ {average_salary:,.2f}")

        print("\nDepartment-wise Average Salary:")
        print("-" * 40)
        for dept, salary in department_salary.items():
            print(f"{dept:<15} : ₹ {salary:,.2f}")

        print("\nHighest Paid Employee:")
        print("-" * 40)
        print(f"Name       : {highest_paid['name']}")
        print(f"Department : {highest_paid['department']}")
        print(f"Salary     : ₹ {highest_paid['salary']:,.2f}")

        print("\nLowest Paid Employee:")
        print("-" * 40)
        print(f"Name       : {lowest_paid['name']}")
        print(f"Department : {lowest_paid['department']}")
        print(f"Salary     : ₹ {lowest_paid['salary']:,.2f}")

        print("\nReport Generated Successfully.")
        print("=" * 50)

    except Exception as e:
        print("Error occurred during salary analysis:")
        print(e)


if __name__ == "__main__":
    input_path = "employee_data.csv"
    analyze_salary(input_path)
