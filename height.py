student_heights = input("Enter the Height of students: ").split()
print (student_heights)

# Len function by for loop
height_of_student = 0
for elements in student_heights:
    height_of_student += 1
print(height_of_student)

# sum function by for loop
height_student = 0
for height in student_heights:
    height_student += int(height)
print(height_student)

avg = height_student/height_of_student
print(round(avg))