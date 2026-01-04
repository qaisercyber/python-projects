students = {}

def add_student():
    name = input("Enter student name: ").strip()
    if name in students:
        print("Student already exists")
        return
    grades = []
    n= int(input("Enter number of grades: "))
    for i in range(n):
        grade = int(input(f"Enter grade {i+1}:"))
        grades.append(grade)
    students[name] = grades
    print("Student added successfully")

def update_student():
    name = input("Enter the name of student to update").strip()
    if name not in students:
        print("Student does not exist")
        return
    print("current grades" , students[name])
    students[name].clear()
    n = int(input("How many new grades"))
    for i in range(n):
        grade = int(input(f"Enter grade {i+1}:"))
        students[name].append(grade)
    print("Student updated successfully")

def delete_student():
    name = input("Enter the name of student to delete").strip()
    if name in students:
        del students[name]
        print(f"Student {name} deleted successfully")
    else:
        print("Student does not exist")

def print_students():
    if not students:
        print("Student list empty")
        return
    print("Student Record")
    print("-"*20)
    for name , grades in students.items():
        avg = sum(grades)/len(grades) if grades else 0
        print(f"Name: {name}")
        print(f"Grades: {grades}")
        print(f"Average Grade : {avg}")
        print("-"*20)

def show_menu():
    print("\n Student Record manager")
    print("-"*20)
    print("1. Add student")
    print("2. Update student")
    print("3. Delete student")
    print("4. Print students")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        if choice == "2":
            update_student()
        if choice == "3":
            delete_student()
        if choice == "4":
            print_students()
        if choice == "5":
            print("Thank you for using this program")
            break
        else:
            print("Please enter a valid option")

if __name__ == "__main__":
    main()




