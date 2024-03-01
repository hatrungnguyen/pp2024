from input import get_mark_details, get_course_details, get_student_details
from ouput import display_mark_details, display_course_details, display_student_details
from domain.student import Student
from domain.course import Course
from domain.university import University


def main():
    unversity = input("Enter unversity name:")
    unversity = University(unversity)

    course_name, course_code = get_course_details()
    course = Course(course_name, course_code)
    unversity.add_course(course)

    student_name, student_id = get_student_details()
    student = Student(student_name, student_id)
    unversity.add_student(student)

    student.enroll_course(course)
    course.add_student(student)

    course_code, student_id, mark = get_mark_details()
    course = None
    student =None

    for c in unversity.get_courses():
        if c.code == course_code:
            course = c
            break

    for s in  unversity.get_students():
        if s.student_id == student_id:
            student = s
            break

    if course and student:
        display_course_details(course.name, course.code)
        display_student_details(student.name, student.student_id)
        display_mark_details(course.code, student.student_id, mark)
    else:
        print("Not found information")


if __name__ == "__main__":
    main()