import time
from colorama import Fore, init

# Helper: Animation Text

def animate(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()



#  UNIT CONVERSION MODULE

def conversion_menu():
    print(Fore.CYAN + "\n UNIT CONVERSIONS") # 
    print("1. Hours → Minutes")
    print("2. Minutes → Seconds")
    print("3. Kilometers → Meters")
    print("4. Celsius → Fahrenheit")
    print("5. Fahrenheit → Celsius")
    print("6. Back")

    choice = input(Fore.YELLOW + "Enter choice: ")

    if choice == "1":
        hrs = float(input("Enter hours: "))
        print(Fore.GREEN + f"{hrs} hrs = {hrs * 60} minutes")

    elif choice == "2":
        mins = float(input("Enter minutes: "))
        print(Fore.GREEN + f"{mins} min = {mins * 60} seconds")

    elif choice == "3":
        km = float(input("Enter km: "))
        print(Fore.GREEN + f"{km} km = {km * 1000} meters")

    elif choice == "4":
        c = float(input("Enter Celsius: "))
        print(Fore.GREEN + f"{c}°C = {(c * 9/5) + 32}°F")

    elif choice == "5":
        f = float(input("Enter Fahrenheit: "))
        print(Fore.GREEN + f"{f}°F = {(f - 32) * 5/9}°C")

    elif choice == "6":
        return

    else:
        print(Fore.RED + "Invalid Choice!")



#  MAIN MENU + CALCULATOR

def calculator():

    history = []

    animate(Fore.CYAN + "\n CALCULATOR + UNIT CONVERTER ")
    print(Fore.MAGENTA + "-" * 50)

    while True:
        print(Fore.GREEN + "\n Select an option:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Show History")
        print("6. Unit Conversion")
        print("7. Exit")

        choice = input(Fore.YELLOW + "\nEnter choice: ")

        if choice == "7":
            animate(Fore.RED + "\nThanks for using Calculator! ")
            break

        if choice == "6":
            conversion_menu()
            continue

        if choice == "5":
            print(Fore.CYAN + "\n HISTORY:")
            if not history:
                print("No history yet.")
            else:
                for line in history:
                    print(Fore.YELLOW + line)
            continue

        if choice in ("1", "2", "3", "4"):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except:
                print(Fore.RED + "Invalid input!")
                continue

            animate(" Calculating...")

            if choice == "1":
                result = num1 + num2
                history.append(f"{num1} + {num2} = {result}")
                print(Fore.GREEN + f"Result = {result}")

            elif choice == "2":
                result = num1 - num2
                history.append(f"{num1} - {num2} = {result}")
                print(Fore.GREEN + f"Result = {result}")

            elif choice == "3":
                result = num1 * num2
                history.append(f"{num1} × {num2} = {result}")
                print(Fore.GREEN + f"Result = {result}")

            elif choice == "4":
                if num2 == 0:
                    print(Fore.RED + "Cannot divide by zero!")
                else:
                    result = num1 / num2
                    history.append(f"{num1} ÷ {num2} = {result}")
                    print(Fore.GREEN + f"Result = {result}")

        else:
            print(Fore.RED + "Invalid choice!")



#  RUN PROGRAM

calculator()
