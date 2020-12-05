""" This function is used to check whether a post is an anchor.
A file of  post data will be read into the function, it returns the article K,
if it is the anchor of article A, i.e. K is an anchor and A directly/indirectly quote K 

Written by Owen CHAN  15 Nov, 2020 
Edited by Yunfei LIU Dec 5, 2020"""

def Anchor(reportPost):
    def GetSource(report):
        try:
            postData = open( 'post/' +  report + '.txt' , encoding = 'UTF-8')
        except IOError :   
            print('Fail to open the file\n')
            return 'Fail'
        line1 = postData.readline()   
        line2 = postData.readline()
        line3 = postData.readline()
        quote = line3.strip()
        postData.close()
        return  quote

    report = reportPost
    while True:
        source = GetSource(report)
        if source == 'null':
            return report
        if source == 'Fail':
            return ''
        report = source

