# Movie Ticket Booking System
# Author: Ankit Kumar

# Seat layout: 5 rows × 5 columns
seats = [["O" for _ in range(5)] for _ in range(5)]

ticket_price = 150  # price per ticket

def show_seats():
    print("\nSCREEN THIS WAY")

    for i in range(5):
        row = ""
        for j in range(5):
            row += seats[i][j] + " "
        print(f"Row {i+1}: {row}")
    print("\nO = Available | X = Booked\n")

def book_ticket():
    show_seats()
    total_tickets = int(input("How many tickets do you want to book? "))

    booked = []

    for t in range(total_tickets):
        print(f"\nSelect Seat {t+1}")
        row = int(input("Enter row (1-5): ")) - 1
        col = int(input("Enter column (1-5): ")) - 1

        if seats[row][col] == "X":
            print("Seat already booked. Choose another seat.")
            continue
        else:
            seats[row][col] = "X"
            booked.append((row+1, col+1))
            print("Seat booked successfully.")

    total_price = total_tickets * ticket_price

    print("\nBooking Summary")
    print("Booked Seats:", booked)
    print(f"Ticket Price: Rs {ticket_price}")
    print(f"Total Amount: Rs {total_price}")
   
def main():
    print("Welcome to the Movie Ticket Booking System")

    while True:
        print("\nMenu:")
        print("1. Show Seats")
        print("2. Book Tickets")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_seats()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            print("Thank you for using the booking system.")
            break
        else:
            print("Invalid choice. Try again.")

main()
