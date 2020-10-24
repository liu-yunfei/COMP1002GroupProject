"""This function is used to add users into user.txt
No receiving and return True when finished.

Written by Yunfei LIU
Edit log:
Oct 24, 2020 created"""
def GetU():
    #This function is used to add user from keyboard
    #No receiving and return True when write successfully and False in other situation
    def GetFromKeyboard():
        userName = str(input("\nPlease enter the user name: "))
        password = str(input("Please enter the password: "))
        birthday = str(input("Please enter the birthday or enter ' ' if no birthday: "))
        phoneNumber = str(input("Please enter the phone number or enter ' ' if no phone number: "))
        friend = str(input("Please enter friends, separate with ';' and also end with ';': "))
        post = str(input("Please enter posts, no space, separate with ';' and also end with ';': "))
        print("\nCheck your input:\n")
        print("username:%s\npassword:%s\nbirthday:%s\nphone number:%s\nfriend:%s\nposts:%s\n" %(userName,password,birthday,phoneNumber,friend,post))
        commandChar = str(input("Please check the format carefully and enter [Y/y] to confirm, others to cancel: "))
        if commandChar == 'Y' or commandChar == 'y':
            writeFile = open('user.txt','a')
            writeFile.write('%s,%s,%s,%s,%s,%s\n' % (userName,password,birthday,phoneNumber,friend,post))
            writeFile.close()
            print("\nWrite Successfully")
            return True
        else:
            print("\nCanceled")
            return False

    #This function is used to add user from file
    #No receiving and return True when successfully write and return False in other situation
    def GetFromFile():
        filePath = str(input("Please input the full path and name of the file: "))
        try:
            open(filePath)
            fileData = open(filePath)
        except IOError:
            print("\nCannot found the file\n")
            return False
        else:
            userInfoList = []
            for userInfo in fileData:
                userInfoList.append(userInfo.strip())
            nameList = []
            passwordList = []
            birthdayList = []
            phoneNumberList = []
            friendList = []
            postList = []
            for userInfo in userInfoList:
                 name,password,birthday,phoneNumber,friend,post = map(str,userInfo.split(','))
                 nameList.append(name)
                 passwordList.append(password)
                 birthdayList.append(birthday)
                 phoneNumberList.append(phoneNumber)
                 friendList.append(friend)
                 postList.append(post)
            print("\nFile read\nThe following are users: ")
            for i in nameList:
                print(i)
            commandChar = str(input("Please check it carefully and enter [Y/y] to confirm, others to cancel: "))
            if commandChar == 'Y' or commandChar == 'y':
                writeFile = open('user.txt','a')
                for userInfo in userInfoList:
                    name,password,birthday,phoneNumber,friend,post = map(str,userInfo.split(','))
                    writeFile.write('%s,%s,%s,%s,%s,%s\n' % (name,password,birthday,phoneNumber,friend,post))
                writeFile.close()
                print("\nWrite Successfully\n")
                return True
            else:
                print("\nCanceled\n")
                return False


    print("\nWelcome to the add user mode\n")
    while True:
        commandChar = str(input("Type [N/n] to get new account by keyboard, type [F/f] to get new by file, type [E/e] to exit: "))
        if commandChar == 'n' or commandChar == 'N':
            GetFromKeyboard()
        if commandChar == 'F' or commandChar == 'f':
            GetFromFile()
        if commandChar == 'E' or commandChar == 'e':
            return True

