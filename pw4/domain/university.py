class University:
    def __init__(self):
        self.students = []
        self.courses = []

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

    def caculated_GPA(self, studentID):
        for student in self.students:
            if student.studentId == studentID:
                GPA = student.caculated_Gpa()
                print(f"GPA for {student.studentName} = {GPA}")
                break
            else:
                print(f"Student {student.studentId} not found")