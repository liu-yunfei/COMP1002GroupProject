"""
This is a generater which can generate user file and post data
"""
def main():
    username = open("peoplename.txt",encoding = 'UTF-8')
    usernameList = []
    for line in username:
        usernameList.append(line.strip())
    word = open("word.txt",encoding = 'UTF-8')
    wordList = []
    for line in word:
        wordList.append(line.strip())
    username.close()
    word.close()
    
    import random,string
    
    def EightDigits():
        list = []
        for i in range(8):
            list.append(str(random.randint(0,9)))
        return ''.join(list)
    
    def Birthday():
        date = str(random.randint(1,28))
        if len(date) < 2:
            date = '0' + date
        month = str(random.randint(1,12))
        if len(month) < 2:
            month = '0' + month
        return date+'/'+month+'/'+str(random.randint(1970,2010))

    def Password():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    userInfo = []
    for i in range(10):
        userInfo.append('username' + str(i) + ',' + usernameList[random.randint(0,1000)] + ',' + usernameList[random.randint(0,1000)] +',' + str(Password()) +','+Birthday()+','+EightDigits() + ',')
   
    for j in range(20):
        user1 = random.randint(0,9)
        user2 = random.randint(0,9)
        if user1 != user2:
            userInfo[user1] = userInfo[user1] + userInfo[user2][:userInfo[user2].find(',')] + ';'
            userInfo[user2] = userInfo[user2] + userInfo[user1][:userInfo[user1].find(',')] + ';' 
    
    postList = []
    for k in range(10):
        userInfo[k] += ','
        postList.append([])
        for m in range(random.randint(2,4)):
            title = wordList[random.randint(0,3000)]
            postList[k].append(userInfo[k][:userInfo[k].find(',')] + title + str(m))
    
    for n in range(10):
        for item in postList[n]:
            write = open('post/' + item + '.txt','w', encoding='UTF-8')
            write.write(item+'\n')
            write.write(userInfo[n][:userInfo[n].find(',')]+'\n')
            quoteUser = random.randint(0,9)
            if quoteUser != n and random.randint(0,9) != 0:
                write.write(random.choice(postList[quoteUser])+'\n')
            else:
                write.write('null\n')
            for p in range(50):
                write.write(wordList[random.randint(0,3000)]+' ')
            write.write('\n')
            write.close()
            userInfo[n] += item + ';'
       
    writeUser = open('user.txt','w',encoding = 'UTF-8')
    for line in userInfo:
        writeUser.write(line+'\n')
    writeUser.close()
    

main()