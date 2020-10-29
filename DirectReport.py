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

print(DirectReport("testfather"))