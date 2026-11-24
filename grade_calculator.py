# STUDENT GRADE CALCULATOR
# Developer: Sabari

print("===== STUDENT GRADE CALCULATOR =====")

# Student details
name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")

# Subject names
subjects = [
    "Tamil",
    "English",
    "Python",
    "Computer Science",
    "Mathematics"
]

# Get marks
marks = []

for subject in subjects:
    while True:
        try:
            mark = float(input("Enter " + subject + " Mark: "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Enter marks between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

# Calculate results
total = sum(marks)
average = total / 5
percentage = (total / 500) * 100

# Grade calculation
if any(mark < 35 for mark in marks):
    grade = "F"
    result = "FAIL"
elif average >= 90:
    grade = "A+"
    result = "PASS"
elif average >= 80:
    grade = "A"
    result = "PASS"
elif average >= 70:
    grade = "B"
    result = "PASS"
elif average >= 60:
    grade = "C"
    result = "PASS"
elif average >= 50:
    grade = "D"
    result = "PASS"
else:
    grade = "E"
    result = "PASS"

# Display marksheet
print("\n===== STUDENT MARKSHEET =====")
print("Student Name:", name)
print("Roll Number:", roll_number)

for i in range(len(subjects)):
    print(subjects[i], ":", marks[i])

print("Total Marks:", total, "/ 500")
print("Average:", round(average, 2))
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Result:", result)

print("==============================")