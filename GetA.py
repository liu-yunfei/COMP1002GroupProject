"""This function is used to add post to post folder
No receiving and return True when finished.

Written by Yunfei LIU
Edit log:
Oct 27, 2020 created"""
def GetA():
    #This function is used to add post from keyboard
    #No receiving and return True when write successfully and False in other situation
    def GetFromKeyboard():
        title = str(input("\nPlease enter the title: "))
        try:
            existFile = open('post/'+title+'.txt','r',encoding= 'UTF-8')
        except IOError:
            author = str(input("Please enter the author: "))
            quote = str(input("Please enter the quotation, separate with ';' and also end with ';'\nOr enter 'null' if no quotation: "))       
            print("Please enter the content, end with EOF(just type Ctrl+D or Ctrl+Z or Ctrl+C)\n")
            content=[]
            while True:
                try:
                    content.append(input()+'\n')
                except:
                    break
            print("Check your title, author and quote:\n")
            print("Title:%s\nAuthor:%s\nQuote:%s\n " %(title,author,quote))
            commandChar = str(input("Please check the format carefully and enter [Y/y] to confirm, others to cancel: "))
            if commandChar == 'Y' or commandChar == 'y':
                try:
                    writeFile = open('post/'+title+'.txt','w',encoding = 'UTF-8')
                except IOError:
                    print("Failed to create the file\n")
                    return False
                writeFile.write('%s\n%s\n%s\n' % (title,author,quote))
                for line in content:
                    writeFile.write('%s' % line)
                writeFile.close()
                print("\nWrite Successfully\n")
                return True
            else:
                print("\nCanceled")
                return False
        print("The title already exist, change a new one\n")
        return False
 
    #This function is used to add post from file
    #No receiving and return True when successfully write and return False in other situation
    def GetFromFile():
        filePath = str(input("Please input the full path and name of the file: "))
        try:
            open(filePath)
            fileData = open(filePath,encoding = 'UTF-8')
        except IOError:
            print("\nCannot found the file\n")
            return False
        else:
            titleString = fileData.readline()
            title = titleString.strip()
            authorString = fileData.readline()
            author = authorString.strip()
            quoteString = fileData.readline()
            quote = quoteString.strip()
            content = []
            for line in fileData:
                content.append(line)
            print("File found\n Check the information:\nTitle:%s\nAuthor:%s\nQuote:%s\n" % (title,author,quote))
            commandChar = str(input("Enter [C/c] to print the content, others to cancel printing: "))
            if commandChar == 'C' or commandChar == 'c':
                for line in content:
                    print(line)
            commandChar = str(input("\nPlease check all the information carefully and enter [Y/y] to confirm, others to cancel: "))
            if commandChar == 'Y' or commandChar == 'y':
                try:
                    writeFile = open('post/'+title+'.txt','w',encoding = 'UTF-8')
                except IOError:
                    print("Failed to create the file\n")
                    return False
                writeFile.write('%s\n%s\n%s\n' % (title,author,quote))
                for line in content:
                    writeFile.write('%s' % line)
                writeFile.close()
                print("\nWrite Successfully\n")
                return True
            else:
                print("\nCanceled")
                return False

    print("\nWelcome to the add post mode\n")
    while True:
        commandChar = str(input("Type [N/n] to get new account by keyboard, type [F/f] to get new by file, type [E/e] to exit: "))
        if commandChar == 'n' or commandChar == 'N':
            GetFromKeyboard()
        if commandChar == 'F' or commandChar == 'f':
            GetFromFile()
        if commandChar == 'E' or commandChar == 'e':
            return True
