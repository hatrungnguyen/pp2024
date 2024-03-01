def get_course_details():
    course_name = input("Enter the course name: ")
    course_code = input("Enter the course code: ")
    return course_name, course_code

def get_student_details():
    student_name = input("Enter the student name: ")
    student_id = input("Enter the student ID: ")
    return student_name, student_id

def get_mark_details():
    course_code = input("Enter the course code: ")
    student_id = input("Enter the student ID: ")
    mark = float(input("Enter the mark: "))
    return course_code, student_id, mark