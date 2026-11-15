class Admin:

    def __init__(self, rooms):
        self.username = "admin"
        self.password = "1234"
        self.rooms = rooms

    # Admin Login
    def login(self):

        print("\n========== ADMIN LOGIN ==========")

        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if username == self.username and password == self.password:
            print("\nAdmin Login Successful!")
            self.admin_menu()

        else:
            print("\nInvalid Username or Password!")

    # Admin Menu
    def admin_menu(self):

        while True:

            print("\n========== ADMIN MENU ==========")
            print("1. Add Room")
            print("2. View Rooms")
            print("3. Search Room")
            print("4. Update Room")
            print("5. Delete Room")
            print("6. Logout")

            choice = input("Enter Your Choice: ")

            if choice == "1":
                self.add_room()

            elif choice == "2":
                self.view_rooms()

            elif choice == "3":
                self.search_room()

            elif choice == "4":
                self.update_room()

            elif choice == "5":
                self.delete_room()

            elif choice == "6":
                print("\nAdmin Logged Out!")
                break

            else:
                print("\nInvalid Choice!")

    # Add Room
    def add_room(self):

        print("\n========== ADD ROOM ==========")

        try:
            room_no = int(input("Enter Room Number: "))

            for room in self.rooms:
                if room["room_no"] == room_no:
                    print("Room Already Exists!")
                    return

            room_type = input("Enter Room Type: ")
            price = float(input("Enter Room Price: "))

            room = {
                "room_no": room_no,
                "room_type": room_type,
                "price": price,
                "status": "Available"
            }

            self.rooms.append(room)

            print("\nRoom Added Successfully!")

        except ValueError:
            print("Invalid Details!")

    # View Rooms
    def view_rooms(self):

        print("\n========== ROOM DETAILS ==========")

        if not self.rooms:
            print("No Rooms Available!")
            return

        for room in self.rooms:

            print("-------------------------")
            print("Room Number:", room["room_no"])
            print("Room Type:", room["room_type"])
            print("Price:", room["price"])
            print("Status:", room["status"])

    # Search Room
    def search_room(self):

        try:
            room_no = int(input("Enter Room Number: "))

            for room in self.rooms:

                if room["room_no"] == room_no:

                    print("\nRoom Found!")
                    print("Room Number:", room["room_no"])
                    print("Room Type:", room["room_type"])
                    print("Price:", room["price"])
                    print("Status:", room["status"])
                    return

            print("\nRoom Not Found!")

        except ValueError:
            print("Invalid Room Number!")

    # Update Room
    def update_room(self):

        try:
            room_no = int(input("Enter Room Number to Update: "))

            for room in self.rooms:

                if room["room_no"] == room_no:

                    if room["status"] == "Booked":
                        print("Booked Room Cannot Be Updated!")
                        return

                    room_type = input("Enter New Room Type: ")
                    price = float(input("Enter New Room Price: "))

                    room["room_type"] = room_type
                    room["price"] = price

                    print("\nRoom Updated Successfully!")
                    return

            print("\nRoom Not Found!")

        except ValueError:
            print("Invalid Details!")

    # Delete Room
    def delete_room(self):

        try:
            room_no = int(input("Enter Room Number to Delete: "))

            for room in self.rooms:

                if room["room_no"] == room_no:

                    if room["status"] == "Booked":
                        print("Booked Room Cannot Be Deleted!")
                        return

                    self.rooms.remove(room)

                    print("\nRoom Deleted Successfully!")
                    return

            print("\nRoom Not Found!")

        except ValueError:
            print("Invalid Room Number!")