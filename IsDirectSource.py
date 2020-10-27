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

