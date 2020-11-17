""" This function is used to check whether a post is an anchor.
A file of  post data will be read into the function, it returns the article K,
if it is the anchor of article A, i.e. K is an anchor and A directly/indirectly quote K 

Written by Owen CHAN  15 Nov, 2020 """

def Anchor(reportPost):

        try:
            postData = open( 'post/' +  reportPost + '.txt' , encoding = 'UTF-8')
        except IOError :   
            print('Fail to open the file\n')
            return 'Fail'

        line1 = postData.readline()   
        line2 = postData.readline()
        line3 = postData.readline()
        quote = line3.strip()
        postData.close()

        if quote = 'null' :
            print(reportPost, 'does not quote any other post.')
            return False
        else:
            try:
                postData = open('post/' + quote + '.txt',  encoding = 'UTF-8')
            except IOError :
                print('Fail to open to quoted file\n')
                return 'Fail'
            line1 = postData.readline()   
            line2 = postData.readline()
            line3 = postData.readline()
            quote2 = line3.strip()

        if  quote2 = 'null' :
            print(quote2, 'is an anchor of ', reportPost)
            return True
        
