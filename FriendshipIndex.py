"""This function calcuate two users' friendship index
It receives two user name and return their friendship index
For the algorithm, please refer to the report

Written by Yunfei LIU Nov 13, 2020"""

def FriendshipIndex(user1,user2):
    #This function receives a user name and return the post list
    def UserInfo(userName):
        user = open('user.txt')
        userInfoList = []
        for userInfo in user:
            userInfoList.append(userInfo.strip())
        nameList = []
        postList = []
        for userInfo in userInfoList:
            name,password,birthday,phoneNumber,friend,post = map(str,userInfo.split(','))
            nameList.append(name)
            postList.append(post)
        try:
            userIndex = nameList.index(userName)
        except ValueError:
            return []
        userPostList = postList[userIndex].split(';')
        return userPostList
    
    #This function receives a user's post and return the resource list
    def UserQuoteList(postList):
        quoteList = []
        for post in postList:
            try:
                postData = open('post/' + post + '.txt', encoding='UTF-8')
            except IOError:
                continue
            line1 = postData.readline()
            line2 = postData.readline()
            line3 = postData.readline()
            quotation = line3.strip()
            postData.close()
            quoteList.append(quotation)
        return quoteList

    user1Quote = UserQuoteList(UserInfo(user1))
    user2Quote = UserQuoteList(UserInfo(user2))
    if len(user1Quote) == 0 or len(user2Quote) == 0:
        return 0
    user1Friendship = 0
    user2Friendship = 0
    for resource in user1Quote:
        for post in UserInfo(user2):
            if resource == post:
                user1Friendship += 1
    for resource in user2Quote:
        for post in UserInfo(user1):
            if resource == post:
                user2Friendship += 1
    if user1Friendship < user2Friendship:
        eachOtherQuote = user1Friendship
    else:
        eachOtherQuote = user2Friendship
    friendshipIndex = (((eachOtherQuote/len(user1Quote))**2)+((eachOtherQuote/len(user2Quote))**2))**0.5
    return "{:.3f}".format(friendshipIndex)

print(FriendshipIndex('CHANTaiman','Bob'))