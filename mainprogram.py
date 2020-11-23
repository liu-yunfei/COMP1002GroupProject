"""This function is used to return the direct report
it receives a post title and return a list of direct report, return an empty list when no report

Written by Yunfei LIU
Edit log:
Oct 29, 2020 created"""
def DirectReport(anchor):
    import os
    postFileList = os.listdir("post")
    reportList = []
    for postFile in postFileList:
        try:
            readFile = open("post/"+postFile,encoding = 'UTF-8')
        except IOError:
            print("Cannot open the file")
            return []
        fileTitle = readFile.readline()
        title = fileTitle.strip()
        fileAuthor = readFile.readline()
        fileQuote = readFile.readline()
        report = fileQuote.strip()
        if report == anchor:
            if ord(title[0])==65279:
                reportList.append(title[1:])
            else:
                reportList.append(title)
        readFile.close()
    return reportList

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

"""This function is used to add post to post folder
No receiving and return True when finished.

Written by Yunfei LIU
Edit log:
Oct 27, 2020 created"""
def GetA():
    #This function is used to add post from keyboard
    #No receiving and return True when write successfully and False in other situation
    def GetFromKeyboard():
        title = str(input("\nPlease enter the title: "))
        try:
            existFile = open('post/'+title+'.txt','r',encoding= 'UTF-8')
        except IOError:
            author = str(input("Please enter the author: "))
            quote = str(input("Please enter the quotation. Or enter 'null' if no quotation: "))       
            print("Please enter the content, end with EOF(just type Ctrl+D or Ctrl+Z or Ctrl+C)\n")
            content=[]
            while True:
                try:
                    content.append(input()+'\n')
                except:
                    break
            print("Check your title, author and quote:\n")
            print("Title:%s\nAuthor:%s\nQuote:%s\n " %(title,author,quote))
            commandChar = str(input("Please check the format carefully and enter [Y/y] to confirm, others to cancel: "))
            if commandChar == 'Y' or commandChar == 'y':
                try:
                    writeFile = open('post/'+title+'.txt','w',encoding = 'UTF-8')
                except IOError:
                    print("Failed to create the file\n")
                    return False
                writeFile.write('%s\n%s\n%s\n' % (title,author,quote))
                for line in content:
                    writeFile.write('%s' % line)
                writeFile.close()
                print("\nWrite Successfully\n")
                return True
            else:
                print("\nCanceled")
                return False
        print("The title already exist, change a new one\n")
        return False
 
    #This function is used to add post from file
    #No receiving and return True when successfully write and return False in other situation
    def GetFromFile():
        filePath = str(input("Please input the full path and name of the file: "))
        try:
            open(filePath)
            fileData = open(filePath,encoding = 'UTF-8')
        except IOError:
            print("\nCannot found the file\n")
            return False
        else:
            titleString = fileData.readline()
            title = titleString.strip()
            authorString = fileData.readline()
            author = authorString.strip()
            quoteString = fileData.readline()
            quote = quoteString.strip()
            content = []
            for line in fileData:
                content.append(line)
            print("File found\n Check the information:\nTitle:%s\nAuthor:%s\nQuote:%s\n" % (title,author,quote))
            commandChar = str(input("Enter [C/c] to print the content, others to cancel printing: "))
            if commandChar == 'C' or commandChar == 'c':
                for line in content:
                    print(line)
            commandChar = str(input("\nPlease check all the information carefully and enter [Y/y] to confirm, others to cancel: "))
            if commandChar == 'Y' or commandChar == 'y':
                try:
                    writeFile = open('post/'+title+'.txt','w',encoding = 'UTF-8')
                except IOError:
                    print("Failed to create the file\n")
                    return False
                writeFile.write('%s\n%s\n%s\n' % (title,author,quote))
                for line in content:
                    writeFile.write('%s' % line)
                writeFile.close()
                print("\nWrite Successfully\n")
                return True
            else:
                print("\nCanceled")
                return False

    print("\nWelcome to the add post mode\n")
    while True:
        commandChar = str(input("Type [N/n] to get new account by keyboard, type [F/f] to get new by file, type [E/e] to exit: "))
        if commandChar == 'n' or commandChar == 'N':
            GetFromKeyboard()
        if commandChar == 'F' or commandChar == 'f':
            GetFromFile()
        if commandChar == 'E' or commandChar == 'e':
            return True

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

"""This function is used to check direct source
it receives two post titles and return True if article A is a direct source of B, and False otherwise.

Written by Yunfei LIU
Edit log:
Oct 27, 2020 created"""
def IsDirectSource(post1,post2):
    try:
        postData2 = open('post/'+post2+'.txt',encoding = 'UTF-8')
    except IOError:
        print('Fail to open the file\n')
        return False
    line1 = postData2.readline()
    line2 = postData2.readline()
    line3 = postData2.readline()
    quotation2 = line3.strip()
    if quotation2 == post1:
        postData2.close()
        return True
    postData2.close()
    return False

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

"""This function is used to check whether the given sourcepost is the source of a report.
It receives sourcepost and reportpost titles and return True when sourcepost is source of reportpost
return False otherwise.

Written by Muyuan LI Oct 30, 2020
Edited by Yunfei LIU Oct 31, 2020"""

def IsSource(sourcePost, reportPost):
    def DirectSource(post):
        try:
            postData = open('post/' + post + '.txt', encoding='UTF-8')
        except IOError:
            print('Fail to open the file\n')
            return 'Fail'
        line1 = postData.readline()
        line2 = postData.readline()
        line3 = postData.readline()
        quotation = line3.strip()
        postData.close()
        return quotation
    #This part is used to ensure the file names are valid
    try:
        fin1 = open('post/' + sourcePost + '.txt', encoding='UTF-8')
        fin2 = open('post/' + reportPost + '.txt', encoding='UTF-8')
        fin1.close()
        fin2.close()
    except IOError:
        print("Fail to open the file")
        return False

    source = sourcePost
    report = reportPost
    if sourcePost == DirectSource(reportPost):
        return True
    while (report != 'null'):
        if report == source:
            return True
        if report == 'null':
            return False
        report = DirectSource(report)
    return False

"""This function is used to print a post
it receives a post title and return True while post found and printed successfully, return False when name not found

Written by Yunfei LIU
Edit log:
Oct 27, 2020 created"""
def NicePrintA(postName):
    try:
        post = open('post/'+str(postName)+'.txt',encoding = 'UTF-8')
    except IOError:
        print("\nFile not found\n")
        return False
    titleString = post.readline()
    title = titleString.strip()
    authorString = post.readline()
    author = authorString.strip()
    quoteString = post.readline()
    quote = quoteString.strip()
    content = []
    for contentLine in post:
        content.append(contentLine)
    print("\nFile found\n")
    print("Title: "+title[1:])
    print("Author: "+author)
    print("Quote: "+quote)
    print("The following are the content: \n")
    for contentLine in content:
        print(contentLine)
    post.close()
    return True


"""This function is used to print a user's profile
it receives a user's name and return True while name found, return False when name not found

Written by Yunfei LIU
Edit log:
Oct 24, 2020 created"""
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
            user.close()
            return True
    print("Cannot find a user named",userName,'\n')
    user.close()
    return False

"""This function calcate the impact index of a post
It receives a post name and return a impact index float
For the algorithm please watch the report

Written by Yunfei LIU Nov 11, 2020
"""
def PostImpactIndex(anchor):
    #This function is as same as DirectReport(anchor)
    countDict = dict()
    PostImpactIndex.countDict = {}
    def DirectReport(anchor):
        import os
        postFileList = os.listdir("post")
        reportList = []
        for postFile in postFileList:
            try:
                readFile = open("post/"+postFile,encoding = 'UTF-8')
            except IOError:
                print("Cannot open the file")
                return []
            fileTitle = readFile.readline()
            title = fileTitle.strip()
            fileAuthor = readFile.readline()
            fileQuote = readFile.readline()
            report = fileQuote.strip()
            if report == anchor:
                if ord(title[0])==65279:
                    reportList.append(title[1:])
                    if title[1:] not in countDict:
                        PostImpactIndex.countDict[title[1:]] = 1
                    else: 
                        PostImpactIndex.countDict[title[1:]] += 1
                else:
                    reportList.append(title)
                    if title not in countDict:
                        PostImpactIndex.countDict[title] = 1
                    else: 
                        PostImpactIndex.countDict[title] += 1
            readFile.close()
        return reportList

    #This function is used to check the list have something except empty
    def CheckList(list):
        count = 0
        for item in list:
            if item != []:
                count += 1
        if count != 0:
            return True
        else:
            return False

    if DirectReport(anchor) == []:
        return 0
    reportList = DirectReport(anchor)
    anchorList = DirectReport(anchor)
    tempList = anchorList
    count = 2
    for dictKey in PostImpactIndex.countDict:
        PostImpactIndex.countDict[dictKey] += 1
    for anchorItem in anchorList:
        if not CheckList(anchorList):
            break
        reportList.extend(DirectReport(anchorItem))
        tempList.extend(DirectReport(anchorItem))
        if DirectReport(anchorItem) != []:
            count += 1
            for dictKey in PostImpactIndex.countDict:
                PostImpactIndex.countDict[dictKey] += 1
    anchorList = tempList
    impactIndex = 0
    for dictKey in PostImpactIndex.countDict:
        PostImpactIndex.countDict[dictKey] = count+1-PostImpactIndex.countDict[dictKey]
        impactIndex += (0.5)**(PostImpactIndex.countDict[dictKey]-1)
    return "{:.3f}".format(impactIndex)

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

"""This function is used to find direct and indirect posts
it receives a post title and return a list of direct and indirect reports, return an empty list when no report

Written by Yunfei LIU
Edit log:
Oct 29, 2020 created"""
def Report(anchor):
    #This function is as same as DirectReport(anchor)
    def DirectReport(anchor):
        import os
        postFileList = os.listdir("post")
        reportList = []
        for postFile in postFileList:
            try:
                readFile = open("post/"+postFile,encoding = 'UTF-8')
            except IOError:
                print("Cannot open the file")
                return []
            fileTitle = readFile.readline()
            title = fileTitle.strip()
            fileAuthor = readFile.readline()
            fileQuote = readFile.readline()
            report = fileQuote.strip()
            if report == anchor:
                if ord(title[0])==65279:
                    reportList.append(title[1:])
                else:
                    reportList.append(title)
            readFile.close()
        return reportList

    #This function is used to check the list have something except empty
    def CheckList(list):
        count = 0
        for item in list:
            if item != []:
                count += 1
        if count != 0:
            return True
        else:
            return False

    if DirectReport(anchor) == []:
        return []
    reportList = DirectReport(anchor)
    anchorList = DirectReport(anchor)
    if anchorList == []:
        return []
    tempList = anchorList
    for anchorItem in anchorList:
        if not CheckList(anchorList):
            break
        reportList.extend(DirectReport(anchorItem))
        tempList.extend(DirectReport(anchorItem))
    anchorList = tempList
    return reportList

"""This function calcuate a user's impact index
It receives a user name and return this user's impact index
For the algorithm, please refer to the report

Written by Yunfei LIU Nov 11, 2020"""
def UserImpactIndex(userName):
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
    impactSum = 0
    for title in userPostList:
        impactSum += float(PostImpactIndex(title))
    import math
    impactIndex = math.log(impactSum+1,math.e)
    return "{:.3f}".format(impactIndex)


"""This function is main function in terminal.
It receives void and return 0 when no error

Written by Yunfei LIU  Nov23, 2020"""
def main():
    print("Copyright 2020 Mu Yuan LI, Owen CHAN, Yun Fei LIU\nAll rights reserved.\n\n")
    while True:
        modeChar = str(input("Enter 'C' for command line mode, 'G' for GUI (Not developed yet), 'E' for exit: "))
        if modeChar == 'E':
            return 0
        if modeChar == 'G':
            print('Not developed yet!')
            return 0
        if modeChar == 'C':
            while True:
                funcChar = str(input("\nEnter 'A' for advanced functions, 'B' for basic functions, 'R' for return to previous menu: "))
                if funcChar == 'R':
                    break
                if funcChar == 'A':
                    print("\n1.UserImpactIndex\n2.PostImpactIndex\n3.FriendshipIndex\n4.QuotationIndex\n")
                    choiceChar = str(input("Please enter numbers to use functions, other to return: "))
                    if choiceChar == '1':
                        userName = str(input("\nEnter the user name: "))
                        print("The impact index for %s is %s\n" %(userName,UserImpactIndex(userName)))
                    elif choiceChar == '2':
                        post = str(input("\nEnter the post title: "))
                        print("The impact index for %s is %s\n" %(post,PostImpactIndex(post)))
                    elif choiceChar == '3':
                        userName1 = str(input("\nEnter user name 1: "))
                        userName2 = str(input("\nEnter user name 2: "))
                        print("\nThe friendship index between %s and %s is %s" %(userName1,userName2,FriendshipIndex(userName1,userName2)))
                    elif choiceChar == '4':
                        userName1 = str(input("\nEnter user name 1: "))
                        userName2 = str(input("\nEnter user name 2: "))
                        print("\nThe quotation index between %s and %s is %s" %(userName1,userName2,QuotationIndex(userName1,userName2)))
                if funcChar == 'B':
                    print("1.Anchor\n2.DirectReport\n3.GetA\n4.GetU\n5.IsDirectSource\n6.IsSource\n7.IsFriend\n8.NicePrintA\n9.NicePrintU\n10.Report\n")
                    choiceChar = str(input("Please enter numbers to use functions, other to return: "))
                    if choiceChar == '1':
                        continue
                    elif choiceChar == '2':
                        post = str(input("\nEnter the post title: "))
                        reportList = DirectReport(post)
                        print("Direct report of post '%s'"% post)
                        for item in reportList:
                            print(item)
                    elif choiceChar == '3':
                        GetA()
                    elif choiceChar == '4':
                        GetU()
                    elif choiceChar == '5':
                        post1 = str(input("\nEnter source title: "))
                        post2 = str(input("\nEnter report title: "))
                        print("%s is the direct source of %s ? "%(post1,post2),end='')
                        print(IsDirectSource(post1,post2))
                    elif choiceChar == '6':
                        post1 = str(input("\nEnter source title: "))
                        post2 = str(input("\nEnter report title: "))
                        print("%s is the source of %s ? "%(post1,post2),end='')
                        print(IsSource(post1,post2))
                    elif choiceChar == '7':
                        userName1 = str(input("\nEnter user name 1: "))
                        userName2 = str(input("\nEnter user name 2: "))
                        print("%s and %s are friends? "%(userName1,userName2),end = '')
                        print(IsFriend(userName1,userName2))
                    elif choiceChar == '8':
                        post = str(input("\nEnter the post title: "))
                        NicePrintA(post)
                    elif choiceChar == '9':
                        userName = str(input("\nEnter the user name: "))
                        NicePrintU(userName)
                    elif choiceChar == '10':
                        post = str(input("\nEnter the post title: "))
                        reportList = Report(post)
                        print("Report of post '%s'"% post)
                        for item in reportList:
                            print(item)

main()


        