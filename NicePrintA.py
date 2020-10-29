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


