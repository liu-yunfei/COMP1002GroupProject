"""This function calcuate a user's impact index
It receives a user name and return this user's impact index
For the algorithm, please refer to the report

Written by Yunfei LIU Nov 11, 2020"""
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
    if anchorList == []:
        return 0
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
    impactIndex = math.log(impactSum,math.e)
    return "{:.3f}".format(impactIndex)

