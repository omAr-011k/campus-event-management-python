admins = {
    "Wijdan": 111,
    "Audry": 222,
    "Omar": 333,
    "Tahmid": 444
}

user = input("write your name please ...  ").strip()

admin = None
for admin_name in admins.keys():
    if admin_name.lower() == user.lower():
        admin = admin_name
        break

if admin: 
    password = int(input("please Enter your password ...  "))

    if password == admins[admin]:  
        print(f"welcome back Mr {admin} \n")



        # codes
       


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
                        print(f"Your new password for {admin} ")
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