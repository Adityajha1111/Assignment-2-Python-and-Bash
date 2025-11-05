students = {}

while True:
    print("\n1. Add Student\n2. Update Grade\n3. Display All\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print("Student added successfully!")

    elif choice == 2:
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print("Grade updated successfully!")
        else:
            print("Student not found!")

    elif choice == 3:
        print("\nAll Student Grades:")
        for name, grade in students.items():
            print(f"{name}: {grade}")

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
