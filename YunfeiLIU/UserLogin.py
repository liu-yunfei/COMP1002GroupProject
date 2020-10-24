"""This function is used for user login
it use userdata.txt in the same folder to check the login
if the user do not have an account, it will register one
it returns username while the user log in successfully

Written by Yunfei LIU
Edit log:
created Oct 24, 2020
"""
def UserLogin():

    #This function is used to check if the user name exists
    #If exist, return True, If not exist, return false
    def CheckUserName(name):
        userData = open('userdata.txt')
        for info in userData:
            userInfo = info.strip()
            userName,password = map(str,userInfo.split(','))
            if userName == name:
                userData.close()
                return True
        return False
    
    #This function is used to check password, receives the userpassword and the real password
    #If password is right, return true. If password is wrong, return false
    def CheckPassword(userName,userPassword):
        userData = open('userdata.txt')
        for info in userData:
            userInfo = info.strip()
            name,password = map(str,userInfo.split(','))
            if userPassword == password and userName == name:
                userData.close()
                return True
        return False

    #This function is used to sign up
    #It write the username and password into userdata.txt
    def SignUp():
        print('\n\nWelcome to sign up mode\n')
        userName = str(input("Enter your user name: "))
        while True:
            password = str(input("Enter your password: "))
            repeatPassword = str(input("Please repeat your password: "))
            if password == repeatPassword:
                break
            print("\nTwo input are different")
        fileWrite = open('userdata.txt','a')
        fileWrite.write(userName+','+password+'\n')
        fileWrite.close()
        print("Your user name is "+userName+" and password is "+password)
        print("Successfully Registered\n")
    
    import sys
    while True:
        userName = str(input("Please input your username: "))
        if CheckUserName(userName) == False:
            print("\nNo account")
            commandChar = str(input("Type R/r to register or Type exit to exit: "))
            if commandChar == 'R' or commandChar == 'r':
                SignUp()
            elif commandChar == "exit":
                sys.exit(0)
            else:
                print("Wrong command\n")
        print("\nCurrently user name: "+userName)
        print("If it is not your user name, just press enter to reset")
        password = str(input("Please input your password: "))
        if CheckPassword(userName,password):
            return userName
        else:
            print("Wrong Password \n")


