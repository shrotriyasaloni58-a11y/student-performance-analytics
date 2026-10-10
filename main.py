import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Student.csv")

marks = df[["Python", "Statistics", "Mathematics"]].to_numpy()
df["Total"] = np.sum(marks, axis=1)
df["Average"] = np.mean(marks, axis=1)

print(df)

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

df["Grade"] = df["Average"].apply(calculate_grade)

print(df[["Name", "Average", "Grade"]])

def calculate_result(row):
    if (
        row["Python"] >= 40
        and row["Statistics"] >= 40
        and row["Mathematics"] >= 40
    ):
        return "Pass"
    else:
        return "Fail"

df["Result"] = df.apply(calculate_result, axis=1)

print(df[["Name", "Average", "Grade", "Result"]])

top_students = df.sort_values(

    by = "Average",

    ascending = False

).head(5)

print("\nTop 5 Performing Students:")

print(top_students[["Name", "Average", "Grade", "Result"]])


class_average = df["Average"].mean()

highest_average = df["Average"].max()

lowest_average = df["Average"].min()

pass_count = (df["Result"] == "Pass").sum()

fail_count = (df["Result"] == "Fail").sum()

print("\n--- Overall Class Statistics ---")

print(f"Class Average: {class_average:.2f}")

print(f"Highest Student Average: {highest_average:.2f}")

print(f"Lowest Student Average: {lowest_average:.2f}")

print(f"Students Passed: {pass_count}")

print(f"Students Failed: {fail_count}")


subjects = ["Python", "Statistics", "Mathematics"]

subject_averages = df[subjects].mean()
subject_averages = round(subject_averages, 2)

print("\n--- Subject-Wise Average Marks ---")

print(subject_averages)

best_subject = subject_averages.idxmax()

weakest_subject = subject_averages.idxmin()

print("\nBest Performing Subject: ",best_subject)

print("Weakest Performing Subject: ",weakest_subject)

print("\n--- Department-Wise Performance ---")

department_averages = df.groupby("Department")["Average"].mean()
print(department_averages.round(2))

print("\n --- Students Who Need Improvement ---")
students_need_help = df[df["Average"] < 60]

print(
    students_need_help[
        ['Name', 'Department', 'Average', 'Grade', 'Result']
    ]
)

df.to_csv("student_analysis_report.csv", index=False)

print("\nAnalysis report saved successfully!")

print("\n--- Data Quality Check ---")

print("Missing values in each column:")

print(df.isnull().sum())

print("\nDuplicate rows: ", df.duplicated().sum())

subjects = ["Python", "Statistics", "Mathematics"]

subject_averages = df[subjects].mean()

plt.figure(figsize=(8,5))

plt.bar(subjects, subject_averages)

plt.title("Average Marks of Subjects")

plt.xlabel("Subjects")

plt.ylabel("Average Marks")
plt.ylim(0,100)
plt.show()
