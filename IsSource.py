"""This function is used to check whether the given sourcepost is the source of a report.

Written by Muyuan LI"""


def IsDirectSource(post1, post2):
    try:
        postData2 = open('post/' + post2 + '.txt', encoding='UTF-8')
    except IOError:
        print('Fail to open the file\n')
        return False
    line1 = postData2.readline()
    line2 = postData2.readline()
    line3 = postData2.readline()
    quotation2 = line3.strip()
    if quotation2 == post1:
        postData2.close()
        return quotation2
    postData2.close()
    return False


def isSource(sourcePost, reportPost):
    if sourcePost == IsDirectSource(sourcePost, reportPost):
        return True
    while IsDirectSource(sourcePost, reportPost) != False:
        if sourcePost == source:
            return True
            sourcePost = IsDirectSource(sourcePost, reportPost)
    return False

print(isSource("testchildchild2","textroot"))