import pandas as pd


student_data = pd.DataFrame({
    'Roll Number': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Deepika Padukone', 'Shah Rukh Khan', 'Amitabh Bachchan', 'Ranbir Kapoor', 
            'Alia Bhatt', 'Hrithik Roshan', 'Katrina Kaif', 'Priyanka Chopra', 'Prabhas', 'Vijay'
    ],
    'Gender': ['F', 'M', 'M', 'M', 'F', 'M', 'F', 'F', 'M', 'M'],
    'Marks1': [85, 72, 90, 68, 95, 78, 88, 62, 8, 75],
    'Marks2': [88, 75, 12, 70, 40, 82, 85, 65, 79, 80],
    'Marks3': [9, 78, 8, 65, 98, 80, 91, 70, 5, 82]
})

df = student_data
print(df)
print("\n")

print("Create a new column with total marks")
df["Total Marks"] = df["Marks1"]+df["Marks2"]+df["Marks3"]
print(df)
print("\n")

print("Find the lowest marks in Marks1:",df["Marks1"].min())
print("\n")

print("Find the Highest marks in Marks2:",df["Marks2"].max())
print("\n")

print("Find the average marks in Marks3",df["Marks3"].mean())
print("\n")

print("Find student name with highest average:")
df["Average Marks"] = df['Total Marks']/3
top = df['Average Marks'].idxmax()
print(df.loc[top, "Name"])
print(df.loc[top, "Average Marks"])
print("\n")

print("Find how many students failed in Marks2 (<40)")
count = 0
for mark in df["Marks2"]:
    if mark < 40:
        count += 1 
print("Number of students failed:",count)
print("\n")

