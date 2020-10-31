"""This function is used to check whether the given sourcepost is the source of a report.

Written by Muyuan LI"""


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


def IsSource(sourcePost, reportPost):
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
        print(source,report)
        if report == source:
            return True
        if report == 'null':
            return False
        report = DirectSource(report)
    return False

