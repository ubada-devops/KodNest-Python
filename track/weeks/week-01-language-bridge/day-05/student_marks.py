# Problem 5: Student Marks Analyzer

# Read total number of subjects
num_subjects = int(input())

total_marks = 0
passed = True

# Input marks for each subject
for i in range(1, num_subjects + 1):
    mark = int(input())
    total_marks += mark
    if mark < 35:
        passed = False

average_marks = total_marks / num_subjects if num_subjects > 0 else 0

print("Total Marks:", total_marks)
print("Average Marks:", f"{average_marks:.2f}")

if passed:
    print("Result: Passed")
else:
    print("Result: Failed")
