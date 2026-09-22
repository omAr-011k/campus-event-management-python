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
        
        # Constants
        #These are filenames used to store events and participant registrations as plain text. The event data goes in events.txt,
        # and participant info in participants.txt.s
        EVENTS_FILE = "events.txt"
        PARTICIPANTS_FILE = "participants.txt"

        # Main menu
        #This is the main interface for event organizers. It displays a menu with options until the user selects
        #"Exit".
        #these are all the functions
        #create_event() - Create a new event.
        #update_event() - Edit an existing event.
        #cancel_event() - Delete an event.
        #view_participants() - View participants of an event.
        #Exit - Exit the menu.
        def event_organizer_menu():
            while True:
                print("\n=== Event Organizer Menu ===")
                print("1. Create a new event")
                print("2. Update event details")
                print("3. Cancel an event")
                print("4. View registered participants")
                print("5. Exit")
                choice = input("Select an option (1-5): ")

                if choice == '1':
                    create_event()
                elif choice == '2':
                    update_event()
                elif choice == '3':
                    cancel_event()
                elif choice == '4':
                    view_participants()
                elif choice == '5':
                    print("Exiting Event Organizer Menu. Goodbye!")
                    break
                else:
                    print("Invalid option. Please try again.")

        #date format check: dd/mm/yy
        #Checks if a given date string is in the format dd/mm/yy.
        #Logic:
        #Checks total length = 8
        #Checks slashes at position 2 and 5
        #Verifies that day, month, and year parts are digits
        #Example: "05/07/25" → Valid
        #Example: "5-07-2025" → Invalid
        def is_valid_date(date_str):
            if len(date_str) != 8:
                return False
            if date_str[2] != '/' or date_str[5] != '/':
                return False
            day = date_str[:2]
            month = date_str[3:5]
            year = date_str[6:]
            return day.isdigit() and month.isdigit() and year.isdigit()

        # File reading
        #This reads and returns all lines from the given file as a list of strings (without newline characters).
        #If the file doesn't exist, it creates an empty file and returns an empty list.
        def read_file(filename):
            try:
                with open(filename, "r") as file:
                    return [line.strip() for line in file.readlines()]
            except:
                open(filename, "w").close()  # Create empty file if not exists
                return []

        # File writing
        #This writes a list of strings (lines) into a file, replacing its contents.
        #Each line is written with a newline (\n).
        def write_file(filename, lines):
            try:
                with open(filename, "w") as file:
                    for line in lines:
                        file.write(line + "\n")
            except:
                print("Error writing to file.")

        # Add line to file
        #This appends a single line of text to a file without overwriting existing content.
        def add_line(filename, line):
            try:
                with open(filename, "a") as file:
                    file.write(line + "\n")
            except:
                print("Error appending to file.")

        # Create new event
        #This lets the user update an existing event by:
        #Asking for the event title.
        #Searching for that title in events.txt.
        #If found, it asks for new date, location, description, and capacity.
        #Replaces the old entry with the updated one.
        def create_event():
            title = input("Enter event title: ")

            while True:
                date = input("Enter event date (dd/mm/yy): ")
                if is_valid_date(date):
                    break
                else:
                    print("Invalid date format. Please use dd/mm/yy.")

            location = input("Enter event location: ")
            description = input("Enter event description: ")
            capacity = input("Enter event capacity: ")

            event_line = title + "," + date + "," + location + "," + description + "," + capacity

            with open("Approving_or_rejecting.txt", "a") as file:
                file.write(f"Event Title: {title}\n")
                print(f"Event '{title}' has been submitted for approval.")
                
            add_line(EVENTS_FILE, event_line)
            print("Event created successfully!")

        # Update event
        #This lets the user update an existing event by:
        #Asking for the event title.
        #Searching for that title in events.txt.
        #If found, it asks for new date, location, description, and capacity.
        #Replaces the old entry with the updated one.
        def update_event():
            print("\n--- Update Event Details ---")
            events = read_file(EVENTS_FILE)
            title = input("Enter event title to update: ")

            found = False
            updated_events = []
            for event in events:
                details = event.split(",")
                if details[0] == title:
                    print("Current details:", event)

                    while True:
                        new_date = input("Enter new date (dd/mm/yy): ")
                        if is_valid_date(new_date):
                            break
                        else:
                            print("Invalid date format. Please use dd/mm/yy.")

                    new_location = input("Enter new location: ")
                    new_description = input("Enter new description: ")
                    new_capacity = input("Enter new capacity: ")

                    updated_line = title + "," + new_date + "," + new_location + "," + new_description + "," + new_capacity
                    updated_events.append(updated_line)
                    found = True
                else:
                    updated_events.append(event)

            if found:
                write_file(EVENTS_FILE, updated_events)
                print("Event updated successfully!")
            else:
                print("Event not found!")

        # Cancel event
        #This removes an event:
        #Asks for the event title.
        #Reads all events and filters out the one that matches the title.
        #Writes the remaining events back to the file.
        def cancel_event():
            print("\n--- Cancel an Event ---")
            events = read_file(EVENTS_FILE)
            title = input("Enter event title to cancel: ")
            new_events = []

            found = False
            for event in events:
                if event.startswith(title + ","):
                    found = True
                    continue
                new_events.append(event)

            if found:
                write_file(EVENTS_FILE, new_events)
                print("Event cancelled successfully!")
            else:
                print("Event not found!")

        # View participants
        #Displays the list of participants registered for a specific event:
        #Asks for the event title.
        #Reads all lines from participants.txt.
        #Splits each line into event, participant name and shows only those matching the input title.
        def view_participants():
            print("\n--- View Registered Participants ---")
            participants = read_file(PARTICIPANTS_FILE)
            event_title = input("Enter event title: ")

            found = False
            for entry in participants:
                if ',' in entry:
                    evt, name = entry.split(",", 1)
                    if evt == event_title:
                        print("- " + name)
                        found = True

            if not found:
                print("No participants found for this event.")

        # Run the program
        #This is the entry point of the program. It starts the organizer menu loop when the script runs.
        event_organizer_menu()

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