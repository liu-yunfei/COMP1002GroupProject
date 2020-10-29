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

