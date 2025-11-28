import datetime
import os
DATA_FILE = "expiry_data.txt"

# LOAD DATA

def load_data():
    data = []
    if not os.path.exists(DATA_FILE):
        return data

    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                name, category, date = line.strip().split("|")
                data.append({
                    "name": name,
                    "category": category,
                    "expiry": datetime.datetime.strptime(date, "%Y-%m-%d").date()
                })
    except Exception:
        print("Error reading storage! Data may be corrupted.")

    return data

# SAVE DATA

def save_data(data):
    with open(DATA_FILE, "w") as file:
        for item in data:
            file.write(f"{item['name']}|{item['category']}|{item['expiry']}\n")


# ADD ITEM

def add_item(data):
    name = input("Enter item name: ")
    category = input("Enter category (Food/Medicine): ")
    date = input("Enter expiry date (YYYY-MM-DD): ")

    try:
        exp = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        data.append({
            "name": name,
            "category": category,
            "expiry": exp
        })
        save_data(data)
        print(" Item added successfully!")
    except:
        print(" Invalid date format!")

# SHOW ALL ITEMS

def show_items(data):
    if not data:
        print("No items stored.")
        return

    print("\n ALL ITEMS ")
    for item in data:
        print(f"{item['name']} ({item['category']}) → {item['expiry']}")


# SHOW EXPIRED ITEMS

def show_expired(data):
    today = datetime.date.today()
    print("\n EXPIRED ITEMS ")
    found = False

    for item in data:
        if item["expiry"] < today:
            print(f" {item['name']} expired on {item['expiry']}")
            found = True

    if not found:
        print(" No expired items found.")

# SHOW ITEMS EXPIRING SOON

def expiring_soon(data):
    today = datetime.date.today()
    soon_limit = today + datetime.timedelta(days=7)

    print("\n EXPIRING SOON (within 7 days) ")
    found = False

    for item in data:
        if today <= item["expiry"] <= soon_limit:
            print(f" {item['name']} expiring on {item['expiry']}")
            found = True

    if not found:
        print(" No near-expiry items.")

# MAIN MENU

def main():
    data = load_data()

    while True:
        print("\n EXPIRY TRACKER ")
        print("1. Add Item")
        print("2. Show All Items")
        print("3. Show Expired")
        print("4. Expiring Soon (7 days)")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_item(data)
        elif choice == "2":
            show_items(data)
        elif choice == "3":
            show_expired(data)
        elif choice == "4":
            expiring_soon(data)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

main()
