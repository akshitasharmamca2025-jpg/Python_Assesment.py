import pandas as pd

# This script assumes a 'data.csv' exists with 'Department' and 'Salary' columns
def analyze_employees():
    try:
        df = pd.read_csv('employees.csv')
        print("Avg Salary per Dept:\n", df.groupby('Department')['Salary'].mean())
        print("\nHighest Salary Employee:\n", df.loc[df['Salary'].idxmax()])
    except FileNotFoundError:
        print("CSV file not found.")

analyze_employees()