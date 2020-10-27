"""This function is used to verify friendship
It receives 2 user names and return a boolean
If the users are in each other's friend list, return True
If not, return False

Written by Yunfei LIU
Edit log:
Oct 27, 2020 created
"""
def IsFriend(userName1,userName2):
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
    try:
        index1 = nameList.index(userName1)
        index2 = nameList.index(userName2)
    except ValueError:
        print("\nUser not found\n")
        user.close()
        return False
    if friendList[index1] == ' ' or friendList[index2] == ' ':
        user.close()
        return False
    friendNameList1 = friendList[index1].split(';')
    friendNameList2 = friendList[index2].split(';')
    for friendName1 in friendNameList1:
        if friendName1 == userName2:
            for friendName2 in friendNameList2:
                if friendName2 == userName1:
                    user.close()
                    return True
    user.close()
    return False

