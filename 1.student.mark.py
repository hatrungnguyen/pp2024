def numofstudent():
    return int(input("Number of students in class:"))
def studentinformation():
    students = {}
    students["id"] = input("Enter student id:")
    students["name"] = input("Enter student name:")
    students["Dob"] = input("Enter student DoB:")

    return students
def numofcourse():
    return int(input("Number of course:"))
def courseinfoermation():
    course = {}
    course["id"] = input("Enter course id:")
    course["name"] = input("Enter course name:")
    return course
def inputmark(students,course_id):
    for student in students:
        mark = input(f"Mark for {student['name']} in course {course_id}")
        student["marks"][course_id] = mark
def listcourses(courses):
    if len(courses) == 0:
        print("No courses")
    else:
        print("Courses list")
        for i, course in enumerate(courses):
            print(f"{i+1}. id: {course['id']}, Name:{course['name']}")
def liststudets(students):
    if len(students) == 0:
        print("No Studets")
    else:
        print("Student list:")
        for i, student in enumerate(students):
            print(f"{i+1}. id : {student['id']}, name : {student['name']},DoB : {student['Dob']}")
def studentmark(students, course_id):
    for student in students:
        if course_id in student["marks"]:
            mark = student["marks"][course_id]
            print(f"Student {student['name']}: {mark}")
        else:
            print(f"Student {student['name']}: no mark for {course_id}")


def main():
    students = []
    courses = []

    while True:
        print(""" 0.input number students
        1. input number courses
        2.input infor students
        3.input infor courses
        6.input mark
        4.show courese
        5.show studets
        7.exit""")
        option = int(input("Take tour choice :"))

        if option == 0:
            num_students = numofstudent()
        elif option == 1:
            num_courses = numofcourse()
        elif option == 2:
            for i in range(num_students):
                student_infor = studentinformation()
                student_infor['marks'] = {}
                students.append(student_infor)
        elif option == 3:
            for _ in range(num_courses):
                course_info = courseinfoermation()
                courses.append(course_info)
        elif option == 4:
            listcourses(courses)
        elif option == 5:
            liststudets(students)
        elif option == 7:
            print("Thanks for using")
            break
        elif option == 6:
            course_id = input("Enter the course id to input marks: ")
            inputmark(students, course_id)
        else:
            print("Wrong!Please choose from the list")

if __name__ == "__main__":
    main()