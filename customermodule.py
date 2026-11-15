class Customer:

    def __init__(self, rooms):

        self.customers = []
        self.bookings = []
        self.rooms = rooms

    # Customer Menu
    def customer_menu(self):

        while True:

            print("\n========== CUSTOMER MENU ==========")
            print("1. Register")
            print("2. Login")
            print("3. Back to Main Menu")

            choice = input("Enter Your Choice: ")

            if choice == "1":
                self.register()

            elif choice == "2":
                self.login()

            elif choice == "3":
                break

            else:
                print("Invalid Choice!")

    # Registration
    def register(self):

        print("\n========== CUSTOMER REGISTRATION ==========")

        name = input("Enter Your Name: ")
        username = input("Create Username: ")

        for customer in self.customers:

            if customer["username"] == username:
                print("Username Already Exists!")
                return

        password = input("Create Password: ")
        phone = input("Enter Phone Number: ")

        customer = {
            "name": name,
            "username": username,
            "password": password,
            "phone": phone
        }

        self.customers.append(customer)

        print("\nRegistration Successful!")

    # Login
    def login(self):

        print("\n========== CUSTOMER LOGIN ==========")

        username = input("Enter Username: ")
        password = input("Enter Password: ")

        for customer in self.customers:

            if (customer["username"] == username and
                    customer["password"] == password):

                print("\nLogin Successful!")
                print("Welcome", customer["name"])

                self.customer_dashboard(customer)
                return

        print("\nInvalid Username or Password!")

    # Customer Dashboard
    def customer_dashboard(self, customer):

        while True:

            print("\n========== CUSTOMER DASHBOARD ==========")
            print("1. View Available Rooms")
            print("2. Search Room")
            print("3. Book Room")
            print("4. Cancel Booking")
            print("5. Logout")

            choice = input("Enter Your Choice: ")

            if choice == "1":
                self.view_rooms()

            elif choice == "2":
                self.search_room()

            elif choice == "3":
                self.book_room(customer)

            elif choice == "4":
                self.cancel_booking(customer)

            elif choice == "5":
                print("\nCustomer Logged Out!")
                break

            else:
                print("Invalid Choice!")

    # View Available Rooms
    def view_rooms(self):

        print("\n========== AVAILABLE ROOMS ==========")

        found = False

        for room in self.rooms:

            if room["status"] == "Available":

                print("-------------------------")
                print("Room Number:", room["room_no"])
                print("Room Type:", room["room_type"])
                print("Price:", room["price"])

                found = True

        if not found:
            print("No Rooms Available!")

    # Search Room
    def search_room(self):

        try:
            room_no = int(input("Enter Room Number: "))

            for room in self.rooms:

                if room["room_no"] == room_no:

                    print("\nRoom Found!")
                    print("Room Type:", room["room_type"])
                    print("Price:", room["price"])
                    print("Status:", room["status"])
                    return

            print("Room Not Found!")

        except ValueError:
            print("Invalid Room Number!")

    # Book Room
    def book_room(self, customer):

        self.view_rooms()

        try:
            room_no = int(input("\nEnter Room Number to Book: "))

            for room in self.rooms:

                if room["room_no"] == room_no:

                    if room["status"] == "Available":

                        room["status"] = "Booked"

                        booking = {
                            "username": customer["username"],
                            "room_no": room_no,
                            "price": room["price"]
                        }

                        self.bookings.append(booking)

                        print("\nRoom Booked Successfully!")
                        print("Customer:", customer["name"])
                        print("Room Number:", room_no)
                        print("Amount:", room["price"])

                    else:
                        print("\nRoom Already Booked!")

                    return

            print("\nInvalid Room Number!")

        except ValueError:
            print("Invalid Room Number!")

    # Cancel Booking
    def cancel_booking(self, customer):

        try:
            room_no = int(input("Enter Room Number to Cancel: "))

            for booking in self.bookings:

                if (booking["room_no"] == room_no and
                        booking["username"] == customer["username"]):

                    for room in self.rooms:

                        if room["room_no"] == room_no:
                            room["status"] = "Available"
                            break

                    self.bookings.remove(booking)

                    print("\nBooking Cancelled Successfully!")
                    return

            print("\nBooking Not Found!")

        except ValueError:
            print("Invalid Room Number!")
            