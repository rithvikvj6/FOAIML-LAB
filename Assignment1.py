import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Student": ["Arun", "Priya", "Rahul", "Divya", "Kumar"],
    "Hours_Studied": [2, 4, 3, 5, 6],
    "Marks": [45, 65, 55, 80, 90]
}
df = pd.DataFrame(data)
print("Student Dataset:")
print(df)
print("\nFirst 5 records:")
print(df.head())
print("\nDataset information:")
df.info()
print("\nStatistical summary:")
print(df.describe())
marks = df["Marks"].to_numpy()
print("\nMean Marks:", np.mean(marks))
print("Median Marks:", np.median(marks))
print("Standard Deviation:", np.std(marks))
print("\nMissing values:")
print(df.isnull().sum())
plt.bar(df["Student"], df["Marks"])
plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Student Marks Analysis")
plt.show()

print("\nML workbench setup verified successfully!")