students = []
courses = []
marks = {}     

def input_number_of_students():
    n = int(input("Number of students: "))
    print()
    for _ in range(n):
        input_student_info()

def input_student_info():
    print("Enter student information:")
    sid = input("  Student ID: ")
    name = input("  Name: ")
    dob = input("  Date of Birth: ")
    students.append({
        "id": sid,
        "name": name,
        "dob": dob
    })
    print()

def input_number_of_courses():
    n = int(input("Number of courses: "))
    print()
    for _ in range(n):
        input_course_info()

def input_course_info():
    print("Enter course information:")
    cid = input("  Course ID: ")
    name = input("  Course Name: ")
    courses.append({
        "id": cid,
        "name": name
    })
    print()

def input_marks_for_course():
    print("Courses:")
    for c in courses:
        print(f"  {c['id']} - {c['name']}")

    course_id = input("Select course ID: ")
    print()

    for s in students:
        m = float(input(f"Enter mark for student {s['name']} ({s['id']}): "))
        marks[(s["id"], course_id)] = m

    print("Marks recorded.\n")


def list_students():
    print("\n Student List ")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}")
    print()


def list_courses():
    print("\n Course List ")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")
    print()


def show_marks_for_course():
    print("Courses:")
    for c in courses:
        print(f"  {c['id']} - {c['name']}")

    course_id = input("Select course ID: ")
    print()

    print(f" Marks for course {course_id} ")
    for s in students:
        key = (s["id"], course_id)
        if key in marks:
            print(f"{s['name']} ({s['id']}): {marks[key]}")
        else:
            print(f"{s['name']} ({s['id']}): N/A")
    print()



def main():
    while True:
        print(" Student Mark Management ")
        print("1. Number of students")
        print("2. Number of courses")
        print("3. Marks for a course")
        print("4. List students")
        print("5. List courses")
        print("6. Marks for a course")
        print("0. Out")

        choice = input("Choose an option: ")
        print()

        if choice == "1":
            input_number_of_students()
        elif choice == "2":
            input_number_of_courses()
        elif choice == "3":
            input_marks_for_course()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            show_marks_for_course()
        elif choice == "0":
            break
        else:
            print("Not valid\n")


if __name__ == "__main__":
    main()
