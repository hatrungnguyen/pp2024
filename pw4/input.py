import math

def input_mark(student, course_id):
    mark = input(f"Mark for {student.stuentName} in {course_id}")
    rounded_mark = math.floor(float(mark) * 10) / 10
    student.marks[course_id] = rounded_mark

def number_student():
    return int(input("Enter number student:"))

def student_info():
    student_id = input("Enter ID:")
    student_name = input("Enter name:")
    student_birthday = input("Enter Dob:")
    return student_id,student_name,student_birthday

def number_course():
    return int(input("Number courses: "))

def course_info():
    course_id = input("Enter id:")
    course_name = input("Enter name:")
    return course_id, course_name

