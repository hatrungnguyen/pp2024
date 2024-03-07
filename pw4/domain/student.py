import numpy as np

class Student:
    def __init__(self, studentId, studentName, studentDob):
        self.studentId = studentId
        self.studentName = studentName
        self.studentDob = studentDob
        self.marks = {}

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