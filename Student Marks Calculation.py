import pandas as pd

# Creating a DataFrame with student marks in multiple subjects
data = {
    'Student_Name': ['Arjun', 'Deepa', 'Sagar', 'Meera'],
    'Maths': [85, 45, 92, 70],
    'Science': [78, 52, 88, 65],
    'English': [90, 48, 95, 72]
}

df = pd.DataFrame(data)

# Function to calculate percentage and assign grades
def calculate_grade(row):
    # Calculate Total (Sum of Maths, Science, English)
    total = row['Maths'] + row['Science'] + row['English']
    # Calculate Percentage (Assuming each subject is out of 100)
    percentage = (total / 300) * 100
    
    # Assign Grade based on percentage
    if percentage >= 90:
        grade = 'A+'
    elif percentage >= 75:
        grade = 'A'
    elif percentage >= 60:
        grade = 'B'
    elif percentage >= 50:
        grade = 'C'
    else:
        grade = 'Fail'
        
    # Returning multiple values as a Series to create new columns
    return pd.Series([total, round(percentage, 2), grade])

# Using apply() to add new columns to the DataFrame
# axis=1 ensures the function is applied to each row
df[['Total_Marks', 'Percentage', 'Grade']] = df.apply(calculate_grade, axis=1)

print("--- Student Performance Report ---")
print(df)

"""
Expected Output:
--- Student Performance Report ---
  Student_Name  Maths  Science  English  Total_Marks  Percentage Grade
0        Arjun     85       78       90          253       84.33     A
1        Deepa     45       52       48          145       48.33  Fail
2        Sagar     92       88       95          275       91.67    A+
3        Meera     70       65       72          207       69.00     B
"""