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
            self.marks[courseId] = mark
    def studentmark(self, courseId):

        if courseId in self.marks:
            mark = self.marks[courseId]
            print(f"Student {self.studentName}: {mark}")
        else:
            print(f"Student {self.studentName}: no mark for {courseId}")



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
    def run(self):

            while True:
                print("""Menu:
                   0. Input number of students
                   1. Input number of courses
                   2. Input student information
                   3. Input course information
                   4. Show courses
                   5. Show students
                   6. Input marks
                   7. Exit""")
                option = int(input("Enter your choice(Do not enter character): "))


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
                        course_info = self.courseinfoermation()
                        self.courses.append(course_info)
                elif option == 4:
                    self.listcourses()
                elif option == 5:
                    self.liststudets()
                elif option == 6:
                    course_id = input("Enter the course id to input marks: ")
                    self.input_mark(course_id)
                elif option == 7:
                    print("Thanks for using .")
                    break

                else:
                    print("Wrong!Please choose from the list")









if __name__ == "__main__":
    resul = University()
    resul.run()



