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
        
        # THE MAIN MENU (Venue Manager) ------------------------------
        def main_menu():
            while True:
                print("\n===== Venue Manager Menu =====")
                print("1. View upcoming events scheduled for each venue")
                print("2. Mark venue as unavailable for maintenance or other reasons")
                print("3. Approve/reject venue bookings requests")
                print("4. Suggest alternative venues")
                print("5. Logout")

                try:
                    choice = int(input("Enter your choice (1-5): "))
                    if choice == 1:
                        view_upcoming_events()
                    elif choice == 2:
                        mark_venue_unavailable()
                    elif choice == 3:
                        approve_reject_bookings()
                    elif choice == 4:
                        suggest_alternative_venues()
                    elif choice == 5:
                        print("\nThank you for visiting us...")
                        break 
                    else:
                        print("\nInvalid choice. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 5.")

        # 1. View upcoming events
        def view_upcoming_events():
            print("\n>>> UPCOMING EVENTS <<<")
            try:
                with open("upcoming_events.txt", 'r') as file:
                    print(file.read())
            except FileNotFoundError:
                print("Error: Events file not found.")
            except Exception as e:
                print(f"An error occurred: {e}")

        # 2. Mark venue unavailable
        def mark_venue_unavailable():
            try:
                with open("venues.txt", "r") as file:
                    venues = [line.strip() for line in file.readlines()]
            except FileNotFoundError:
                print("Venues file not found.")
                return

            print("\nCurrent Venues:")
            for i, venue in enumerate(venues, start=1):
                print(f"{i}. {venue.split(',')[0]}") 
            
            venue_name = input("Enter the exact name of the venue to mark as unavailable: ").strip()
            reason = input("Enter the reason for unavailability (e.g., maintenance): ").strip()
            start_date = input("Enter start date (YYYY-MM-DD): ").strip()
            end_date = input("Enter end date (YYYY-MM-DD): ").strip()
            
            updated_venues = []
            venue_found = False
            
            for venue in venues:
                parts = [p.strip() for p in venue.split(',')]
                base_name = parts[0]
                
                if base_name.lower() == venue_name.lower():
                    venue_found = True
                    if len(parts) > 1 and parts[1].lower() == "unavailable":
                        print(f"Venue '{venue_name}' is already marked unavailable.")
                        updated_venues.append(venue)
                    else:
                        updated_venue = f"{base_name}, Unavailable, {reason}, {start_date}, {end_date}"
                        updated_venues.append(updated_venue)
                else:
                    updated_venues.append(venue)
            
            if not venue_found:
                print(f"Venue '{venue_name}' not found.")
                return
            
            try:
                with open('venues.txt', 'w') as file:
                    file.write("\n".join(updated_venues))
                print(f"Venue '{venue_name}' marked unavailable from {start_date} to {end_date}.")
            except Exception as e:
                print(f"Error saving venues: {e}")

        # 3. Approve/reject bookings
        def approve_reject_bookings():
            try:
                with open("venue_requests.txt", "r") as file:
                    requests = [line.strip().split(",") for line in file if line.strip()]
            except FileNotFoundError:
                print("\nNo booking requests found.")
                return

            if not requests:
                print("\nNo pending requests to process.")
                return

            updated_requests = []
            for req in requests:
                if len(req) < 4:  # Ensure request has all fields
                    continue
                    
                print(f"\nRequest ID: {req[0]}, Event: {req[1]}, Venue: {req[2]}, Status: {req[3]}")
                while True:
                    choice = input("Approve (A) / Reject (R) / Skip (S): ").strip().lower()
                    if choice == "a":
                        req[3] = "approved"
                        break
                    elif choice == "r":
                        req[3] = "rejected"
                        break
                    elif choice == "s":
                        break
                    else:
                        print("Invalid choice. Please enter A, R, or S.")
                updated_requests.append(",".join(req))

            try:
                with open("venue_requests.txt", "w") as file:
                    file.write("\n".join(updated_requests))
                print("\nBooking requests updated.")
            except Exception as e:
                print(f"Error saving requests: {e}")

        # 4. Suggest alternatives
        def suggest_alternative_venues():
            print("\n>>> SUGGESTED ALTERNATIVE VENUES <<<")
            try:
                with open("alternative_venues.txt", 'r') as file:
                    print(file.read())
            except FileNotFoundError:
                print("Error: Alternative venues file not found.")
            except Exception as e:
                print(f"An error occurred: {e}")

        # Run the program
        main_menu()

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