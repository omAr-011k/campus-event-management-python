def welcome ():
        print ("""
                ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
                ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
                ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
                ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
                ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
                 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝

    """)
        
# Main Menu
def main_menu():
    while True :
     print("\n=====  Smart Campus Event Management System =====")
     print("1. Event Organizer")
     print("2. Participant")
     print("3. Administrator")
     print("4. Venue Manager")
     print ("Logout ..")
     role = int(input("Select your role (1-4): "))
     if role == 1:
        import event_organizer
     elif role == 2:
        import participant
     elif role == 3:
        import Administrator
     elif role == 4:
        import VenueManager
     elif role == 5 :
        print("\n===== THANKS TO USE OUR PROJECT =====")
        exit()   
     else:
        print("Invalid choice. Please try again.")
        

welcome ()  
main_menu()