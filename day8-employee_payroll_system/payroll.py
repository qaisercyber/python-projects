from abc import ABC, abstractmethod


# ------------------ Abstract Base Class ------------------
class Employee(ABC):
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    def __str__(self):
        return f"{self.emp_id} - {self.name}"


# ------------------ Full-Time Employee ------------------
class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


# ------------------ Part-Time Employee ------------------
class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


# ------------------ Contract Employee ------------------
class ContractEmployee(Employee):
    def __init__(self, emp_id, name, contract_amount):
        super().__init__(emp_id, name)
        self.contract_amount = contract_amount

    def calculate_salary(self):
        return self.contract_amount


# ------------------ Payroll System ------------------
class PayrollSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print("Employee added successfully.")

    def process_payroll(self):
        if not self.employees:
            print("No employees in system.")
            return

        print("\n PAYROLL REPORT")
        print("-" * 40)
        for emp in self.employees:
            print(f"{emp} | Salary: {emp.calculate_salary()}")
        print("-" * 40)


# ------------------ Menu ------------------
def show_menu():
    print("\n EMPLOYEE PAYROLL SYSTEM")
    print("1. Add Full-Time Employee")
    print("2. Add Part-Time Employee")
    print("3. Add Contract Employee")
    print("4. Process Payroll")
    print("5. Exit")


# ------------------ Main Program ------------------
def main():
    payroll = PayrollSystem()

    while True:
        show_menu()
        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            salary = float(input("Enter Monthly Salary: "))
            emp = FullTimeEmployee(emp_id, name, salary)
            payroll.add_employee(emp)

        elif choice == "2":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            rate = float(input("Enter Hourly Rate: "))
            hours = float(input("Enter Hours Worked: "))
            emp = PartTimeEmployee(emp_id, name, rate, hours)
            payroll.add_employee(emp)

        elif choice == "3":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            amount = float(input("Enter Contract Amount: "))
            emp = ContractEmployee(emp_id, name, amount)
            payroll.add_employee(emp)

        elif choice == "4":
            payroll.process_payroll()

        elif choice == "5":
            print("Exiting Payroll System.")
            break

        else:
            print(" Invalid choice. Try again.")


# ------------------ Entry Point ------------------
if __name__ == "__main__":
    main()
