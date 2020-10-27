"""This function is used to check direct source
it receives two post titles and return True if article A is a direct source of B, and False otherwise.

Written by Yunfei LIU
Edit log:
Oct 27, 2020 created"""
def IsDirectSource(post1,post2):
    try:
        postData1 = open('post/'+post1+'.txt')
        postData2 = open('post/'+post2+'.txt')
    except IOError:
        print('Fail to open the file\n')
        return False
    title1 = postData1.readline()
    author1 = postData1.readline()
    quotation