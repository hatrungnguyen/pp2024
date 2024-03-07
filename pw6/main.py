import curses
from input import  *
from output import *
from domain.course import Course
from domain.student import Student
from domain.university import University
import pickle
import gzip


File = 'data.pickle.gz'

def save(data):
    with gzip.open(File, 'rb') as file:
        pickle.dump(data, file)
def load():
    try:
        with gzip.open(File, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return  University()

if __name__ == "__main__":
    result = load()
    stdscr = make_curses()

    while True:
        menu(stdscr)
        option = int(stdscr.getstr().decode())

        if option == 0:
            num_student = number_student()
        elif option == 1:
            num_courses = number_course()
        elif option == 2:
            for i in range(num_student):
                student_id, student_name, student_birthday = student_info()
                student = Student(student_id, student_name, student_birthday)
                result.students.append(student)
            save(result)



        elif option ==3:
            for i in range(num_courses):
                course_id, course_name = course_info()
                course = Course(course_id, course_name)
                result.courses.append(course)
            save(result)



        elif option == 4:
            result.listcourses()
            stdscr.getch()
        elif option == 5:
            result.liststudets()
            stdscr.getch()
        elif option == 6:
            course_id = input("Enter course ID to marks:")
            result.input_mark(course_id)
            save(result)

        elif option== 7:
            close_curse(stdscr)
            break
        else:
            stdscr.addstr("chosse again!!!!")
            stdscr.refresh()
            stdscr.getch()