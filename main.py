from adminmodule import Admin
from customermodule import Customer


# Room Details
rooms = [
    {
        "room_no": 101,
        "room_type": "Single",
        "price": 1000,
        "status": "Available"
    },

    {
        "room_no": 102,
        "room_type": "Double",
        "price": 2000,
        "status": "Available"
    },

    {
        "room_no": 103,
        "room_type": "Deluxe",
        "price": 3000,
        "status": "Available"
    }
]


# Object Creation
admin = Admin(rooms)
customer = Customer(rooms)


# Main Menu
while True:

    print("\n========== HOTEL MANAGEMENT SYSTEM ==========")
    print("1. Admin")
    print("2. Customer")
    print("3. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        admin.login()

    elif choice == "2":
        customer.customer_menu()

    elif choice == "3":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice!")
        