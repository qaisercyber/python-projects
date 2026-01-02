#Take two numbers from the user (main)

#Ask from the user for the operation(main)
#check if the input is valid (are inputs numbers and are operations correct)(main)
#Make calculations
#Store calculations in a list
#Users will be allowed to view the history
#Users will also be allowed to exit the program safely

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a/b

def show_menue():
    print("-----Basic Calculator.....")
    print("Enter the number for choosing the operation")
    print("1 for addition")
    print("2 for subtraction")
    print("3 for multiplication")
    print("4 for division")
    print("5 to show history")
    print("6 to clear history")
    print("7 to exit")


def main():
    history = []
    while True:
        show_menue()
        choice = int(input("Enter any number of your choice:"))
        if choice==7:
            print("Exiting the program")
            break
        if choice==5:
            print("\n ---Showing the history----")
            if not history:
                print("No calculation yet")
            else:
                for record in history:
                    print(record)


        if choice==6:
            print("clearing history:")
            history.clear()
            print("History cleared successfully")
            continue
        try:
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))

            if choice==1:
                result = add(number1, number2)
                symbol = '+'

            elif choice==2:
                result = subtract(number1, number2)
                symbol = '-'
            elif choice==3:
                result = multiply(number1,number2)

                symbol = '*'
            elif choice==4:
                result = divide(number1, number2)
                symbol = '/'

            else:
                print("Invalid choice")
                continue



            result = round(result,2)
            print(f"{number1} {symbol} {number2}={result}")
            history.append(f"{number1} , {number2} , {symbol} , {result}")
        except ValueError:
            print("Invalid number")
            continue

if __name__ == "__main__":
    main()






