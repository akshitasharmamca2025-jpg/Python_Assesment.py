import pandas as pd

# Simulating a CSV structure
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Attendance %': [85, 60, 92, 45]}
df = pd.DataFrame(data)

# Filter students with attendance below 75%
low_attendance = df[df['Attendance %'] < 75]
print("Students with low attendance:")
print(low_attendance)