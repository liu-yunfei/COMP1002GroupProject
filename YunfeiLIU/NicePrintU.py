def NicePrintU(userName):
    user = open('user.txt')
    userInfoList = []
    for userInfo in user:
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
    index = -1
    for alluser in nameList:
        index += 1
        if alluser == userName:
            print("\nUser Found\n")
            print("Username:",nameList[index])
            print("Password:",passwordList[index])
            print("Birthday:",birthdayList[index])
            print("Phone number:",phoneNumberList[index])
            print("\nfriends:")
            if friendList[index] != ' ':
                friendNameList = friendList[index].split(';')
                for friendName in friendNameList:
                    print(friendName)
            print("\nPosts:")
            if postList[index] != ' ':
                postTitleList = postList[index].split(';')
                for postTitle in postTitleList:
                    print(postTitle)
            return True
    print("Cannot find a user named",userName,'\n')
    return False


