'''You're building a login system. A user enters a username and password.
If both are correct → print "Welcome!"
If username is correct but password is wrong → print "Wrong password. X attempts remaining." (they get 3 attempts total)
If username itself is wrong → print "User not found."
After 3 failed password attempts → print "Account locked.'''

stored_username = "alice"
stored_password = "abc123"
def login():
    login_attempts = 3

    while(login_attempts > 0):
        username = input("enter username: ")
        password = input("enter password: ")
        if username == stored_username and password == stored_password:
            print("Welcome")
            break
        elif username != stored_username:
            print("User not found !!")
            break
        else:
            login_attempts -=1
            print(f"Wrong password. {login_attempts} attempts remaining.")
                
        if login_attempts == 0:
            print("Account Locked!!")

login()


