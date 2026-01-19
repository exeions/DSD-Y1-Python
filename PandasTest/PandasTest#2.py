import pandas as pd

data = {
    "Name": ["Alex", "Jamie", "Sam", "Taylor"],
    "Attendance": [85, 90, 95, 65],
    "Grade": ["A", "B", "A", "C"],
    "Passed": [True, True, True, False]
}

df = pd.DataFrame(data)
df2 = pd.read_csv('students.csv')

print(df2.head())
print(df2.info())

print(len(df2["StudentID"])) ## I have filtered this and counted the length.

print(df2["Attendance"].mean())

print(df2["Attendance"].min())

print(df2["Attendance"].max())