import logging


# ------------------ Logging Configuration ------------------
logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ------------------ Custom Exceptions ------------------
class AppError(Exception):
    """Base exception for application"""
    pass


class InvalidCommandError(AppError):
    pass


class CalculationError(AppError):
    pass


# ------------------ Application Logic ------------------
def divide_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b == 0:
            raise CalculationError("Division by zero is not allowed.")
        print("Result:", a / b)
    except ValueError:
        raise CalculationError("Invalid numeric input.")


def greet_user():
    name = input("Enter your name: ").strip()
    if not name:
        raise AppError("Name cannot be empty.")
    print(f"Hello, {name}!")


# ------------------ Command Dispatcher ------------------
def execute_command(command):
    if command == "divide":
        divide_numbers()
    elif command == "greet":
        greet_user()
    else:
        raise InvalidCommandError(f"Unknown command: {command}")


# ------------------ Centralized Error Handler ------------------
def main():
    print("🛠️ ROBUST CLI APP")
    print("Commands: greet | divide | exit")

    while True:
        try:
            command = input("\n> ").strip().lower()

            if command == "exit":
                print("👋 Exiting application.")
                break

            execute_command(command)

        except AppError as e:
            print(f"❌ Error: {e}")
            logging.error(e)

        except Exception as e:
            # Catch-all for unexpected errors
            print("❌ Unexpected error occurred.")
            logging.exception(e)


# ------------------ Entry Point ------------------
if __name__ == "__main__":
    main()
