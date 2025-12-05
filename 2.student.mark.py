class Student:
    def __init__(self, sid, name, dob):
        self.__id = sid
        self.__name = name
        self.__dob = dob    
    def display(self):
        print(f"ID: {self.__id}, Name: {self.__name}, DoB: {self.__dob}")
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name

class Course:
    def __init__(self, cid, name):
        self.__id = cid
        self.__name = name
    def display(self):
        print(f"Course ID: {self.__id}, Name: {self.__name}")
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name

class MarkManager:
    def __init__(self):
        self.__student = []
        self.__course = []
        self.__mark = {}
    def input_student(self):
        n = int(input("Number of student: "))
        print()
        for _ in range(n):
          self.input_student_info()
    def input_student_info(self):
        print("Enter student information ")
        sid = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter date of birth: ")
        self.__student.append(Student(sid, name, dob))
        print()
    def list_student(self):
        print("\n - Student list:")
        for s in self.__student :
            s.display()
        print()
    def input_course(self):
        n = int(input("Enter number of course: "))
        print()
        for _ in range(n):
            self.input_course_info()
    def input_course_info(self):
        print("Enter course infomation")
        cid = input(" Enter course id: ")
        name = input(" Enter course name: ")
        self.__course.append(Course(cid, name))
        print()
    def list_course(self):
        print("\n - Course list :")
        for s in self.__course :
            s.display()
        print()
    
    def input_mark(self):
        print("Course: ")
        for c in self.__course :
            print(f" {c.get_id()} - {c.get_name()}")
            
        course_id = input("Select course: ")        
        print()
        
        for s in self.__student:
            m = float(input(f"Enter mark for student {s.get_name()} ({s.get_id()}): "))
            self.__mark[(s.get_id(), course_id)] = m
        print("Mark recorded. \n")
        
    def show_mark(self):
        print("Course:")
        for c in self.__course:
            print(f"{c.get_id()} - {c.get_name()}")
            
        course_id = input("Select course ID: ")
        print()
        print("Mark for course: {course_id} : ")
        for s in self.__student :
            key = (s.get_id(), course_id)
            if key in self.__mark:
                print(f"{s.get_name()} ({s.get_id()}): {self.__mark[key]}")
            else :
                print(f"{s.get_name()} ({s.get_id()}): Wrong")
        print()
        

def main():
    system = MarkManager()
    while True:
        print(" Student Mark Management System ")
        print("1. Input Students")
        print("2. Input Courses")
        print("3. Input Marks for a Course")
        print("4. List Students")
        print("5. List Courses")
        print("6. Show Marks for a Course")
        print("0. Exit\n")

        choice = input("Choose an option: ")
        print()

        if choice == "1":
            system.input_student()
        elif choice == "2":
            system.input_course()
        elif choice == "3":
            system.input_mark()
        elif choice == "4":
            system.list_student()
        elif choice == "5":
            system.list_course()
        elif choice == "6":
            system.show_mark()
        elif choice == "0":
            break
        else:
            print("Invalid option!\n")

if __name__ == "__main__":
    main()