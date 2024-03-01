class University:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.students = []

    def add_course(self, course):
        self.courses.append(course)

    def add_student(self, student):
        self.students.append(student)

    def get_courses(self):
        return self.courses

    def get_students(self):
        return self.students