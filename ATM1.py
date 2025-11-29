import time  # for delays
from colorama import Fore, Style, init  # for colored terminal text
import pyttsx3  # Text-to-Speech conversion library

init(autoreset=True)
speaker = pyttsx3.init()

# Helper: Animation
def animate(text):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(0.02)
    print()

# Helper: Voice Output
def speak(text):
    speaker.say(text)
    speaker.runAndWait()

# ATM CLASS (Updated)
class ATM:  # ATM with PIN authentication and transaction history
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.authenticated = False
        self.transactions = []  # store last 5 transactions

    def add_transaction(self, message):
        self.transactions.append(message)
        if len(self.transactions) > 5:
            self.transactions.pop(0)

    def authenticate(self, entered_pin):
        if entered_pin == self.pin:
            self.authenticated = True
            return True
        return False

    def check_balance(self):
        if self.authenticated:
            return self.balance
        return None

    def withdraw(self, amount):
        if not self.authenticated:
            return "Not authenticated"
        if amount <= 0:
            return "Invalid amount"
        if amount > self.balance:
            return "Insufficient balance"

        self.balance -= amount
        msg = f"Withdrawn ₹{amount}. New balance: ₹{self.balance}"
        self.add_transaction(msg)
        return msg

    def deposit(self, amount):
        if not self.authenticated:
            return "Not authenticated"
        if amount <= 0:
            return "Invalid amount"

        self.balance += amount
        msg = f"Deposited ₹{amount}. New balance: ₹{self.balance}"
        self.add_transaction(msg)
        return msg

    def logout(self):
        self.authenticated = False
        return "Logged out"


# MAIN PROGRAM
if __name__ == "__main__":  # Main ATM Program

    atm = ATM(pin="1234", balance=5000)

    animate(Fore.CYAN + "\n WELCOME TO AI SMART ATM")
    speak("Welcome to AI Smart ATM")

    while True:
        print(Fore.MAGENTA + "\n--- MAIN MENU ---")
        print(Fore.YELLOW + "1. Login with PIN")
        print("2. Exit")

        choice = input("\nEnter your choice: ")

        # LOGIN
        if choice == "1":
            pin = input("Enter PIN: ")

            if atm.authenticate(pin):
                print(Fore.GREEN + "✔ Login Successful")
                speak("Login successful")

                while True:
                    print(Fore.CYAN + "\n--- AUTHENTICATED MENU ---")
                    print("1. Check Balance")
                    print("2. Withdraw")
                    print("3. Deposit")
                    print("4. View Last 5 Transactions")
                    print("5. Logout")

                    option = input("\nEnter option: ")

                    if option == "1":
                        bal = atm.check_balance()
                        print(Fore.GREEN + f"Your Balance: ₹{bal}")
                        speak(f"Your balance is {bal} rupees")

                    elif option == "2":
                        amount = float(input("Enter amount: "))
                        res = atm.withdraw(amount)
                        print(Fore.YELLOW + res)
                        speak(res)

                    elif option == "3":
                        amount = float(input("Enter amount: "))
                        res = atm.deposit(amount)
                        print(Fore.YELLOW + res)
                        speak(res)

                    elif option == "4":
                        print(Fore.CYAN + "\n LAST 5 TRANSACTIONS:")
                        if not atm.transactions:
                            print("No transactions yet.")
                        else:
                            for t in atm.transactions:
                                print(Fore.GREEN + "• " + t)

                    elif option == "5":
                        print(Fore.RED + atm.logout())
                        speak("Logged out")
                        break

                    else:
                        print(Fore.RED + "Invalid option!")

            else:
                print(Fore.RED + " Invalid PIN")
                speak("Incorrect pin")

        # EXIT
        elif choice == "2":
            animate(Fore.GREEN + "\nThank you for using Smart ATM")
            speak("Thank you for using Smart ATM")
            break

        else:
            print(Fore.RED + "Invalid choice! Try again.")
