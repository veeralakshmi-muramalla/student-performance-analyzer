
import pandas as pd
import matplotlib.pyplot as plt

# Student data
data = {
    "Name": ["Anu", "Balu", "Charan", "Divya", "Esha"],
    "Python": [85, 72, 45, 92, 65],
    "Java": [78, 68, 38, 88, 70],
    "DBMS": [90, 75, 42, 95, 60]
}

df = pd.DataFrame(data)

# Calculate average marks
subjects = ["Python", "Java", "DBMS"]
df["Average"] = df[subjects].mean(axis=1).round(2)

# Determine pass or fail
df["Result"] = df[subjects].apply(
    lambda row: "Pass" if (row >= 40).all() else "Fail",
    axis=1
)

# Display student report
print("\n===== STUDENT PERFORMANCE ANALYZER =====")
print(df.to_string(index=False))

# Find the topper
topper = df.loc[df["Average"].idxmax()]

print("\nTop Performer:", topper["Name"])
print("Average Marks:", topper["Average"])

# Class average
print("\nClass Average:", round(df["Average"].mean(), 2))

# Save report
df.to_csv("student_report.csv", index=False)
print("\nReport saved as student_report.csv")

# Create marks chart
df.plot(
    x="Name",
    y=subjects,
    kind="bar",
    figsize=(9, 5)
)

plt.title("Student Marks Analysis")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.legend(title="Subjects")
plt.tight_layout()
plt.savefig("student_analysis.png")
plt.show()