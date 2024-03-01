class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_students(self):
        return self.students