import math
import numpy as np
import curses



class Course:
    def __init__(self,courseId, courseName):
        self.courseID = courseId
        self.courseName = courseName


class Student:
    def __init__(self, studentId, studentName, studentDob):
        self.studentId = studentId
        self.studentName = studentName
        self.studentDob = studentDob
        self.marks = {}

    def inputmark(self, courseId):

            mark = input(f"Mark for {self.studentName} in course {courseId}")
            rounded_mark = math.floor(mark * 10) / 10
            self.marks[courseId] = rounded_mark
    def studentmark(self, courseId):

        if courseId in self.marks:
            mark = self.marks[courseId]
            print(f"Student {self.studentName}: {mark}")
        else:
            print(f"Student {self.studentName}: no mark for {courseId}")

    def caculated_Gpa(self):
        if len(self.marks) == 0:
            return 0.0
        marks = np.array(list(self.marks.values()))
        gpa = np.mean(marks)
        return gpa



class University:
    def __init__(self):
        self.students = []
        self.courses = []

    def numofstudent(self):
        return int(input("Number of students in class:"))

    def studentinformation(self):

        studentId = input("Enter student id:")
        studentName = input("Enter student name:")
        studentDob = input("Enter student DoB:")
        return Student(studentId, studentName, studentDob)
    def numofcourse(self):
        return int(input("Number of course:"))

    def courseinfoermation(self):

        courseId = input("Enter course id:")
        courseName = input("Enter course name:")
        return Course(courseName, courseId)

    def input_mark(self, courseId):
        for student in self.students:
            student.inputmark(courseId)

    def listcourses(self):
        if len(self.courses) == 0:
            print("No courses")
        else:
            print("Courses list")
            for i, course in enumerate(self.courses):
                print(f"{i + 1}. id: {course.courseID}, Name:{course.courseName}")

    def liststudets(self):
        if len(self.students) == 0:
            print("No Studets")
        else:
            print("Student list:")
            for i, student in enumerate(self.students):
                print(f"{i + 1}. id : {student.studentId}, name : {student.studentName},DoB : {student.studentDob}")

    def student_mark(self, studentId):
        for student in self.students:
            student.studentmark(studentId)


    def caculated_GPA(self, studentID):
        for student in self.students:
            if student.studentId == studentID:
                GPA = student.caculated_Gpa()
                print(f"GPA for {student.studentName} = {GPA}")
                break
            else:
                print(f"Student {student.studentId} not found")


    def GPA_descending(self):
        self.students.sort(key=lambda student : student.caculated_Gpa(), reverse=True)
        print("GPA descending:")
        for i, student in enumerate(self.students):
            print(f"{i + 1}. name: {student.studentName}. Id: {student.studentId}")

    def run(self):
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)

        while True:
            stdscr.clear()
            stdscr.addstr("Menu:\n")
            stdscr.addstr("0. Input number of students\n")
            stdscr.addstr("1. Input number of courses\n")
            stdscr.addstr("2. Input student information\n")
            stdscr.addstr("3. Input course information\n")
            stdscr.addstr("4. Show courses\n")
            stdscr.addstr("5. Show students\n")
            stdscr.addstr("6. Input marks\n")
            stdscr.addstr("7. Exit\n")
            stdscr.addstr("Enter your choice (Do not enter character): ")

            option = int(stdscr.getstr().decode())

            if option == 0:
                num_students = self.numofstudent()
            elif option == 1:
                num_courses = self.numofcourse()
            elif option == 2:
                for i in range(num_students):
                    student_info = self.studentinformation()
                    self.students.append(student_info)
            elif option == 3:
                for _ in range(num_courses):
                    course_info = self.courseinformation()
                    self.courses.append(course_info)


            elif option == 4:
                self.listcourses()
                stdscr.getch()
            elif option == 5:
                self.liststudents()
                stdscr.getch()
            elif option == 6:
                course_id = input("Enter the course id to input marks: ")
                self.input_mark(course_id)
            elif option == 7:
                stdscr.addstr("Thanks for using.\n")
                stdscr.refresh()
                curses.nocbreak()
                stdscr.keypad(False)
                curses.echo()
                curses.endwin()
                break
            else:
                stdscr.addstr("Wrong! Please choose from the list\n")
                stdscr.refresh()
                stdscr.getch()










if __name__ == "__main__":
    resul = University()
    resul.run()



