#  Project-01 || Student Management System
#  Using Python

import json


def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

students = load_students()


while True:
    print("\n===== Student Management System =====\n")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Total Students")
    print("7. Clear Students")
    print("8. Exit")

    choice = input("Enter your choice: ")

    # 1. ADD_STUDENTS
    if choice == "1":

        # Validate ID
        try:
            student_id = int(input("Enter student ID: "))
        except ValueError:
            print("Student ID must be an integer.")
            continue

        # Validate Name
        name = input("Enter student name: ").strip()
        if not name:
            print("Student name cannot be empty.")
            continue

        # Validate Age
        try:
            age = int(input("Enter student age: "))
        except ValueError:
            print("Student age must be an integer.")
            continue

        # Prevent zero or negative age
        if age <= 0:
            print("Student age must be greater than zero.")
            continue

        if age > 120:
            print("Student age must be 120 or less.")
            continue

        # Validate Course
        course = input("Enter student course: ").strip()
        if not course:
            print("Student course cannot be empty.")
            continue


        student = {
                 "id": student_id,
                 "name": name,
                 "age": age,
                 "course": course
        }

        found = False

        for existing_student in students:
            if existing_student["id"] == student_id:
                 found = True
                 print(f'\nStudent ID {existing_student["id"]} already exists.')
                 break

        if not found:
            students.append(student)
            print(f'Student ID {student["id"]} added successfully!')
            save_students()


    # 2. VIEW_STUDENTS
    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            print(f'Total Students: {len(students)}')
            print("\nStudent List:\n")

            for student in students:
                print("-----------------------------------")
                print(f'ID        : {student["id"]}')
                print(f'Name      : {student["name"]}')
                print(f'Age       : {student["age"]}')
                print(f'Course    : {student["course"]}')
                print("-----------------------------------")


    # 3. SEARCH_STUDENTS
    elif choice == "3":

        if not students:
            print("No students found.")
            continue

        try:
            search_id = int(input("Enter student ID to search: "))
        except ValueError:
            print("Student ID must be an integer.")
            continue

        found = False

        for student in students:
            if student["id"] == search_id:
                print("\nStudent Details\n")
                print("-----------------------------------")
                print(f'ID        : {student["id"]}')
                print(f'Name      : {student["name"]}')
                print(f'Age       : {student["age"]}')
                print(f'Course    : {student["course"]}')
                print("-----------------------------------")
                found = True
                break

        if not found:
            print("Student not found.")


    # 4. UPDATE_STUDENTS
    elif choice == "4":

        if not students:
            print("No students found.")
            continue

        # Validate ID
        try:
            update_id = int(input("Enter student ID to update: "))
        except ValueError:
            print("Student ID must be an integer.")
            continue



        found = False

        for student in students:
            if student["id"] == update_id:

                print("\nStudent Details\n")
                print("-----------------------------------")
                print(f'ID        : {student["id"]}')
                print(f'Name      : {student["name"]}')
                print(f'Age       : {student["age"]}')
                print(f'Course    : {student["course"]}')
                print("-----------------------------------")

                # Validate Name
                name = input("Enter new name: ").strip()
                if not name:
                    print("Student name cannot be empty.")
                    continue

                # Validate Age
                try:
                    age = int(input("Enter new age: "))
                except ValueError:
                    print("Student age must be an integer.")
                    continue

                # Prevent zero or negative age
                if age <= 0:
                    print("Student age must be greater than zero.")
                    continue

                if age > 120:
                    print("Student age must be 120 or less.")
                    continue

                # Validate Course
                course = input("Enter new course: ").strip()
                if not course:
                    print("Student course cannot be empty.")
                    continue

                # Update Student
                student["name"] = name
                student["age"] = age
                student["course"] = course

                save_students()

                print(f'Student ID {student["id"]} updated successfully!')
                found = True
                break

        if not found:
            print("Student not found.")


    # 5. DELETE_STUDENTS
    elif choice == "5":

        if not students:
            print("No students found.")
            continue

        try:
            delete_id = int(input("Enter student ID to delete: "))
        except ValueError:
            print("Student ID must be an integer.")
            continue

        found = False

        for student in students:
            if student["id"] == delete_id:
                students.remove(student)
                print(f'Student ID {student["id"]} deleted successfully!')
                save_students()
                found = True
                break

        if not found:
            print("Student not found.")


    # 6. TOTAL_STUDENTS
    elif choice == "6":
        print("======== Statistics =======")
        print(f"Total Students : {len(students)}")
        print("===========================")

    # 7. CLEAR_STUDENTS
    elif choice == "7":
        students.clear()
        print("All students are cleared successfully!")
        save_students()

    # 8. EXIT
    elif choice == "8":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice.")
        print("Please enter a number between 1 and 8.")



