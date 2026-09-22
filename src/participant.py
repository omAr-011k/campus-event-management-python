admins = {
    "Wijdan": 111,
    "Audry": 222,
    "Omar": 333,
    "Tahmid": 444
}

user = input("write your name please ('only admin') ...  ").strip()

admin = None
for admin_name in admins.keys():
    if admin_name.lower() == user.lower():
        admin = admin_name
        break

if admin: 
    password = int(input("please Enter your password ...  "))

    if password == admins[admin]:  
        print(f"welcome back Mr {admin} your password {password}\n")
        # File names
        EVENTS_FILE = "events.txt"
        REGISTRATIONS_FILE = "registrations.txt"


        def main():
            initialize_files()
            print("\nSMART CAMPUS EVENT MANAGEMENT SYSTEM")
            participant_menu()


        def initialize_files():
            """This is for to create file if there's no file inside to register and name of the events"""
            for filename in [EVENTS_FILE, REGISTRATIONS_FILE]:
                try:
                    open(filename, "r").close()
                except FileNotFoundError:
                    open(filename, "w").close()


        def participant_menu():
            while True:
                print("\nPARTICIPANT MENU")
                print("1. View All Events")
                print("2. Register for Event")
                print("3. Cancel Registration")
                print("4. View Event Participants")
                print("5. Exit")

                choice = input("Enter your choice (1-5): ")

                if choice == "1":
                    view_events()
                elif choice == "2":
                    register_participant()
                elif choice == "3":
                    cancel_registration()
                elif choice == "4":
                    view_participants()
                elif choice == "5":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")


        def view_events():
            try:
                with open(EVENTS_FILE, "r") as file:
                    print("\nALL EVENTS:")
                    print("ID | Event Name | Date | Location | Available Spots")
                    print("-" * 60)
                    for line in file:
                        event = line.strip().split(",")
                        if len(event) >= 6:  # Ensure proper format
                            # Calculate available spots
                            capacity = int(event[5])
                            registered = count_registrations(event[0])
                            available = capacity - registered

                            print(f"{event[0]} | {event[1]:<15} | {event[2]} | {event[3]:<10} | {available}/{capacity}")
            except FileNotFoundError:
                print("No events found. The system may not have any events yet.")


        def register_participant():
            view_events()
            event_id = input("\nEnter event ID to register for: ")
            participant_name = input("Enter your name: ").strip()

            if not participant_name:
                print("Name cannot be empty!")
                return

            try:
                # To check the event exist or not
                with open(EVENTS_FILE, "r") as file:
                    events = [line.strip().split(",")[0] for line in file]

                if event_id not in events:
                    print("Event not found!")
                    return

                # The max capacity of the auditorium
                with open(EVENTS_FILE, "r") as file:
                    for line in file:
                        if line.startswith(event_id + ","):
                            capacity = int(line.strip().split(",")[5])
                            break

                registered = count_registrations(event_id)
                if registered >= capacity:
                    print("Event is full!")
                    return

                # Participant who register
                with open(REGISTRATIONS_FILE, "a") as file:
                    file.write(f"{event_id},{participant_name}\n")

                print(f"{participant_name} successfully registered for event {event_id}!")

            except Exception as e:
                print(f"Error: {e}")


        def cancel_registration():
            event_id = input("Enter event ID to cancel registration: ")
            participant_name = input("Enter your name: ").strip()

            try:
                # This part is to ready people who register inside txt file
                with open(REGISTRATIONS_FILE, "r") as file:
                    registrations = file.readlines()

                # Same as above but this is for canceling register
                new_registrations = [
                    reg for reg in registrations
                    if not (reg.startswith(f"{event_id},{participant_name}") or
                    reg.startswith(f"{event_id}, {participant_name}"))
                ]

                # Same thing but to update the file that who register and unregister their events
                with open(REGISTRATIONS_FILE, "w") as file:
                    file.writelines(new_registrations)

                print("Registration cancelled successfully!")

            except Exception as e:
                print(f"Error: {e}")


        def view_participants():
            event_id = input("Enter event ID to view participants: ")

            try:
                with open(REGISTRATIONS_FILE, "r") as file:
                    print(f"\nPARTICIPANTS FOR EVENT {event_id}:")
                    print("-" * 30)
                    found = False
                    for line in file:
                        if line.startswith(event_id + ","):
                            print(line.split(",")[1].strip())
                            found = True
                    if not found:
                        print("No participants found for this event.")
            except FileNotFoundError:
                print("No registrations found.")


        def count_registrations(event_id):
            try:
                with open(REGISTRATIONS_FILE, "r") as file:
                    return sum(1 for line in file if line.startswith(event_id + ","))
            except FileNotFoundError:
                return 0

        main()

    elif password != admins[admin]:
        print("wrong .. can not find your password.")
        qu2 = input("do you want to reset your password? (Y/N):   ").lower().strip()

        while True:
            try:
                if qu2 in ["yes", "y"]:
                    newpassword = int(input("write your new password here ..."))
                    confirm_password = int(input("confirm your new password here ..."))

                    if newpassword == confirm_password:
                        admins[admin] = confirm_password
                        print("successful update.")
                        print(f"Your new password for {admin} is: {newpassword}")
                        break
                    else:
                        print("Passwords don't match. Please try again.")
                elif qu2 in ["no", "n"]:
                    print("Goodbye!")
                    exit()
            except ValueError:
                print("Invalid input. Password must be a number.")

else:  
    print("\nAccess denied. You are not an authorized admin.")
    print("Please contact the system administrator if you believe this is an error.")