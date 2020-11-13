"""This function calcuate two users' quotation index
It receives two user name and return their quotation index
For the algorithm, please refer to the report

Written by Yunfei LIU Nov 13, 2020"""

def QuotationIndex(user1,user2):
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
            return 0
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
    user1Quotation = 0
    user2Quotation = 0
    for resource in user1Quote:
        for post in UserInfo(user2):
            if resource == post:
                user1Quotation += 1
    for resource in user2Quote:
        for post in UserInfo(user1):
            if resource == post:
                user2Quotation += 1
    quotationIndex = (((user1Quotation/len(user1Quote))**2)+((user2Quotation/len(user2Quote))**2))**0.5
    return "{:.3f}".format(quotationIndex)

print(QuotationIndex('Bob','CHANTaiman'))
