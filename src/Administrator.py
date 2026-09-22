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
        # codes
        def administrator_menu():
            print("\n=====  administrator menu  =====\n")
            print ("1. Approving or rejecting proposals .")
            print ("2. Viewing system statistics (total events, most popular event, number of users).")
            print ("3. Generating reports  of event data.")
            print ("4. Manage user roles (promote participant to organizer, etc.) .")
            print ("5. Exit .")
            chosee = int(input("\n Write your chose's number ---> "))

            if chosee == 1:
                approving_or_rejecting_proposals()
            
            elif chosee == 2:    
                Viewing_system_statistics() 

            elif chosee == 3:
                Generating_reports() 

            elif chosee == 4:
                Manage_user_roles() 

            elif chosee == 5:
                administrator_menu()
            else:
                print ("invaled number , plase try agian. ")
                administrator_menu()    

        def approving_or_rejecting_proposals():
            print("\n=== Approve/Reject Event Proposals ===\n")
            
            try:
                pending_file = "Approving_or_rejecting.txt"
                approved_file = "Approved_events.txt"

                with open(pending_file, "r") as file:
                    events = [line.strip() for line in file.readlines() if line.strip()]  #list Comprehension

                if not events:
                    print("There are no events to review.")
                    return 

                approved_events = [] 
                remaining_events = []
                for event in events:
                    print(f"\nEvent: {event}")
                    ques = input("Approve this event? (yes/no): ").lower().strip()

                    while ques not in ["y", "yes", "n", "no"]:
                        print("Invalid input. Please enter 'yes' or 'no'. ")
                        print(f"\nEvent: {event} ") 
                        ques = input("Approve this event? (yes/no): ").lower().strip()

                    if ques in ["y", "yes"]:
                        approved_events.append(event)
                        print("Event approved ✅.")
                    else:
                        print("Event rejected and deleted permanently ❌.")

                
                if approved_events:
                    with open(approved_file, "a") as file:
                        for event in approved_events:
                            file.write(event + "\n")

            
                with open(pending_file, "w") as file:
                    for event in remaining_events:
                        file.write(event + "\n")            
            

                print("\nProcess completed successfully ")

            except FileNotFoundError:
                print("Error: The file 'Approving_or_rejecting.txt' does not exist.")
            except PermissionError:
                print("Error: Permission denied. Cannot access files.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")     


        def Viewing_system_statistics():
            print("\n=== System Statistics ===")
            
            try:
                # Count total events from approved events file
                with open("Approved_events.txt", "r") as file:
                    total_events = len(file.readlines())
                    print(f"Total Approved Events: {total_events}")

                # Count total participants from participants file
                with open("participants.txt", "r") as file:
                    total_participants = len(file.readlines())
                    print(f"Total Registered Participants: {total_participants}")

                # Find most popular event (event with most registrations)
                event_participants = {}
                with open("participants.txt", "r") as file:
                    for line in file:
                        if ',' in line:
                            event_name = line.split(',')[0].strip()
                            event_participants[event_name] = event_participants.get(event_name, 0) + 1

                if event_participants:
                    most_popular = max(event_participants.items(), key=lambda x: x[1])
                    print(f"Most Popular Event: '{most_popular[0]}' with {most_popular[1]} participants")
                else:
                    print("Most Popular Event: No events have participants yet")

            except FileNotFoundError as e:
                print(f"Error: {e.filename} not found. Statistics may be incomplete.")
            except Exception as e:
                print(f"An error occurred while generating statistics: {e}")

        def Generating_reports():
            print("\n=== Generate Reports ===")
            print("1. Events Report")
            print("2. Participants Report")
            print("3. Organizers Report")
            print("4. Back to Main Menu")
            
            try:
                choice = int(input("Select report type (1-4): "))
                
                if choice == 1:
                    # Generate events report
                    try:
                        with open("Approved_events.txt", "r") as file:
                            events = file.readlines()
                        
                        with open("events_report.txt", "w") as report_file:
                            report_file.write("=== EVENTS REPORT ===\n")
                            report_file.write(f"Total Events: {len(events)}\n\n")
                            report_file.write("Event Details:\n")
                            report_file.write("----------------\n")
                            for event in events:
                                report_file.write(event)
                        
                        print("Events report generated successfully as 'events_report.txt'")
                        
                    except FileNotFoundError:
                        print("Error: No approved events found to generate report")

                elif choice == 2:
                    # Generate participants report
                    try:
                        with open("participants.txt", "r") as file:
                            participants = file.readlines()
                        
                        # Count participants per event
                        event_counts = {}
                        for line in participants:
                            if ',' in line:
                                event = line.split(',')[0].strip()
                                event_counts[event] = event_counts.get(event, 0) + 1
                        
                        with open("participants_report.txt", "w") as report_file:
                            report_file.write("=== PARTICIPANTS REPORT ===\n")
                            report_file.write(f"Total Participants: {len(participants)}\n\n")
                            report_file.write("Participants per Event:\n")
                            report_file.write("----------------------\n")
                            for event, count in event_counts.items():
                                report_file.write(f"{event}: {count} participants\n")
                        
                        print("Participants report generated successfully as 'participants_report.txt'")
                        
                    except FileNotFoundError:
                        print("Error: No participants found to generate report")

                elif choice == 3:
                    # Generate organizers report
                    try:
                        with open("organizers.txt", "r") as file:
                            organizers = file.readlines()
                        
                        with open("organizers_report.txt", "w") as report_file:
                            report_file.write("=== ORGANIZERS REPORT ===\n")
                            report_file.write(f"Total Organizers: {len(organizers)}\n\n")
                            report_file.write("Organizer List:\n")
                            report_file.write("---------------\n")
                            for organizer in organizers:
                                report_file.write(organizer)
                        
                        print("Organizers report generated successfully as 'organizers_report.txt'")
                        
                    except FileNotFoundError:
                        print("Error: No organizers found to generate report")

                elif choice == 4:
                    return
                else:
                    print("Invalid choice. Please try again.")
                    Generating_reports()
                    
            except ValueError:
                print("Please enter a valid number (1-4)")
                Generating_reports()

        def Manage_user_roles():
            print("\n=== Manage_user_roles ===")
            #"""Promote a participant to organizer role by moving 
            # their name from participants.txt to organizers.txt"""
            print("\n=====  Enter '1' if you want to \nPromote User from Participant to Organizer\n =====")
            print("\n=====  Enter '2' if you want to \nDemote User from Organizer to Participant \n =====")
            chosen_1 = int(input("Enter your choice: "))

            while chosen_1 not in [1, 2]:
                    print("Invalid choice, please enter 1 or 2.")
                    print("\n=====  Enter '1' if you want to \nPromote User from Participant to Organizer\n =====")
                    print("\n=====  Enter '2' if you want to \nDemote User from Organizer to Participant \n =====")
                    chosen_1 = int(input("Enter your choice: "))

            if chosen_1 == 1:
                print("\n=== Promote User to Organizer ===")
            
                try:
                    # 1. Get user input
                    username = input("Enter username to promote: ").strip().lower()
                    
                    # 2. Read current participants
                    with open("participants.txt", "r", encoding="utf-8") as file:
                        participants = [line.strip().lower() for line in file if line.strip()]
                    
                    # 3. Validate user exists
                    if username not in participants:
                        print("Error: User not found in participants list ⚠️ ")
                        return
                    
                    # 4. Update files
                    # Remove from participants
                    with open("participants.txt", "w", encoding="utf-8") as file:
                        for name in participants:
                            if name != username:  # write only the names that do not match with the input 
                                file.write(name + "\n")
                    
                    # Add to organizers
                    with open("organizers.txt", "a", encoding="utf-8") as file:
                        file.write(username + "\n")
                    
                    print(f"Successfully promoted {username} to organizer ✅ ")
                    
                except FileNotFoundError:
                    print("Error: Required file not found")
                except PermissionError:
                    print("Error: Permission denied when accessing files")
                except Exception as e:
                    print(f"Unexpected error: {e}")
            
            if chosen_1 == 2:
                print("\n=== Demote User to Participant ===")
                
                try:
                    username_2 = input("Enter user's name to demote: ").strip().lower()
                    
                    with open("organizers.txt", "r", encoding="utf-8") as file:
                        names = [name.strip().lower() for name in file if name.strip()]
                    
                    # 3. Validate user exists
                    if username_2 not in names:
                        print("Error: User not found in organizers list ⚠️ ")
                        return
                    
                    # 4. Update files
                    # Remove from organizers
                    with open("organizers.txt", "w", encoding="utf-8") as file:
                        for name in names:
                            if name != username_2:  # write only the names that do not match with the input 
                                file.write(name + "\n")
                    
                    # Add to participants
                    with open("participants.txt", "a", encoding="utf-8") as file:
                        file.write(username_2 + "\n")
                    
                    print(f"Successfully demoted {username_2} to participant ✅ ")
                
                except FileNotFoundError:
                    print("Error: Required file not found")
                except PermissionError:
                    print("Error: Permission denied when accessing files")
                except Exception as e:
                    print(f"Unexpected error: {e}")

        administrator_menu()

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