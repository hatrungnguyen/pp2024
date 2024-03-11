import curses
from input import  *
from output import *
from domain.course import Course
from domain.student import Student
from domain.university import University
import pickle
import gzip
import threading
import tkinter as tk
from tkinter import messagebox

File = 'zipto1.gz'
lock = threading.Lock()
def save(data):
    with gzip.open(File, 'wb') as file:
        pickle.dump(data, file)
def load():
    try:
        with gzip.open(File, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return University()

def data_thread(data):
    lock.acquire()
    save(data)
    lock.release()



def save_data(result, num_student, num_course):
    for i in range(num_student):
        student_id, student_name, student_birthday = student_info()
        student = Student(student_id, student_name, student_birthday)
        result.students.append(student)


    for i in range(num_course):
        course_id, course_name = course_info()
        course =Course(course_id, course_name)
        result.courses.append(course)

    threading.Thread(target=data_thread, args=(result,)).start()
    messagebox.showinfo("Saved", "Data Saved")

def list_courses(result):
    courses = result.listcourses()
    messagebox.showinfo("Courses", "List of courses:\n\n" + "\n".join(courses))

def list_students(result):
    students = result.liststudets()
    messagebox.showinfo("Students", "List of students:\n\n" + "\n".join(students))

def input_mark(result):
    course_id = input("Enter course ID to mark:")
    result.input_mark(course_id)
    threading.Thread(target=data_thread, args=(result,)).start()
    messagebox.showinfo("Marks Input", "Marks have been inputted successfully.")










def main():
    result = load()
    root = tk.Tk
    root.title("Management System for USTH")

    def handle_save_data():
        num_student = number_student()
        num_course = number_course()
        save_data(result, num_student, num_course)

    def handle_list_course():
        list_courses(result)

    def handle_list_students():
        list_students(result)

    def handle_input_mark():
        input_mark(result)

    def hadle_exit():
        root.destroy()

    button_save_data = tk.Button(root, text="Save Data", command= handle_save_data)
    button_save_data.pack()

    button_list_courses = tk.Button(root, text="List COurses", command=handle_list_course)
    button_list_courses.pack()

    button_list_students = tk.Button(root, text="List Students", command= handle_list_students)
    button_list_students.pack()

    button_input_mark = tk.Button(root, text="Input Marks", command= handle_input_mark)
    button_input_mark.pack()

    button_exit = tk.Button(root, text="Exit" , command=hadle_exit)
    button_exit.pack()

    root.mainloop()

if __name__ == "__main__":
    main()