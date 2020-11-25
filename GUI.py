
def GUI():
    import tkinter as tk
    mainWindow = tk.Tk()
    mainWindow.title("Users And Posts Management System")
    mainWindow.geometry("600x400")

    welInfo = tk.Label(mainWindow,text = "Welcome to use this system", font = ('Arial',24))
    welInfo.pack()

    crInfo = tk.Label(mainWindow,text = "Copyright 2020 Muyuan LI, Owen Chan, Yunfei LIU.\nAll rights reserved.",font = ('Arial',10))
    crInfo.pack()

    def GetUserName():
        user = open('user.txt')
        userInfoList = []
        for userInfo in user:
            userInfoList.append(userInfo.strip())
        nameList = []
        for userInfo in userInfoList:
            name,password,birthday,phoneNumber,friend,post = map(str,userInfo.split(','))
            nameList.append(name)
        return nameList

    GUI.nameList = GetUserName()
    
    import os
    postFileList = os.listdir("post")
    GUI.postList = []
    for postFile in postFileList:
        try:
            readFile = open("post/"+postFile,encoding = 'UTF-8')
        except IOError:
            print("Cannot open the file")
            return []
        fileTitle = readFile.readline()
        GUI.postList.append(fileTitle.strip())
    
    def AdvancedScreen():
        advWindow = tk.Tk()
        advWindow.title("Advanced Functions")
        advWindow.geometry("600x400")

        advLabel = tk.Label(advWindow,text = 'Advanced Functions', font = ('Arial',16)).pack()

        frame = tk.Frame(advWindow)
        frame.pack()
        frame_l = tk.Frame(frame)
        frame_l.pack(side = 'left')
        frame_r = tk.Frame(frame)
        frame_r.pack(side = 'right')

        def GUIUserImpactIndex():
            uIndex = tk.Tk()
            uIndex.title('User Impact Index')
            uIndex.geometry("600x400")
            titleLabel = tk.Label(uIndex,text = 'User Impact Index', font = ('Arial',16)).pack()

            frame = tk.Frame(uIndex)
            frame.pack()
            frame_l = tk.Frame(frame)
            frame_l.pack(side = 'left')
            frame_r = tk.Frame(frame)
            frame_r.pack(side = 'right')

            leftLabel = tk.Label(frame_l,text = 'Names',width = 15).pack()
            rightLabel = tk.Label(frame_r, text = 'Impact Index',width = 15).pack()

            nameBox = tk.Listbox(uIndex,width = 30, height = 15)
            impactList = []
            for item in GUI.nameList:
                impactList.append(UserImpactIndex(item))
            count = 0
            for i in GUI.nameList:
                nameBox.insert('end',i+'          '+str(impactList[count]))
                count += 1

            nameBox.pack()
            uIndex.mainloop()

        def GUIPostImpactIndex():
            pIndex = tk.Tk()
            pIndex.title('Post Impact Index')
            pIndex.geometry("600x400")
            titleLabel = tk.Label(pIndex,text = 'Post Impact Index', font = ('Arial',16)).pack()

            frame = tk.Frame(pIndex)
            frame.pack()
            frame_l = tk.Frame(frame)
            frame_l.pack(side = 'left')
            frame_r = tk.Frame(frame)
            frame_r.pack(side = 'right')

            leftLabel = tk.Label(frame_l,text = 'Titles',width = 15).pack()
            rightLabel = tk.Label(frame_r, text = 'Impact Index', width = 15).pack()

            impactList = []
            for item in GUI.postList:
                impactList.append(PostImpactIndex(item))

            postBox = tk.Listbox(pIndex,width = 30,height = 15)
            count = 0
            for i in GUI.postList:
                postBox.insert('end',i+'          '+str(impactList[count]))
                count += 1

            postBox.pack()
            pIndex.mainloop()
            
        def GUIFriendshipIndex():
            fIndex = tk.Tk()
            fIndex.title('Friendship Index')
            fIndex.geometry("600x400")
            titleLabel = tk.Label(fIndex,text = 'Friendship Index', font = ('Arial',16)).pack()

            leftFrame = tk.Frame(fIndex)
            middleFrame = tk.Frame(fIndex)
            leftFrame.pack(side = 'left')
            middleFrame.pack()
            
            leftLabel = tk.Label(leftFrame,text = 'Users', font = ('Arial',12)).pack()
            GUIFriendshipIndex.leftBox = tk.Listbox(leftFrame,height = 15)
            for item in GUI.nameList:
                GUIFriendshipIndex.leftBox.insert('end',item)
            GUIFriendshipIndex.leftBox.pack()

            var1 = tk.StringVar(fIndex)
            var2 = tk.StringVar(fIndex)
            indexVar = tk.StringVar(fIndex)
            emptyLabel = tk.Label(middleFrame,text = ' ',font = ('Arial',16),height=2).pack()
            user1Label = tk.Label(middleFrame,text = "User 1",font = ('Arial',12)).pack()
            user1Entry = tk.Entry(middleFrame,show = None,textvariable = var1).pack()
            user2Label = tk.Label(middleFrame,text = "User 2",font = ('Arial',12)).pack()
            user2Entry = tk.Entry(middleFrame,show = None,textvariable = var2).pack()

            def GetVar():
               indexNumber = FriendshipIndex(var1.get(),var2.get())
               indexVar.set(indexNumber)

            checkButton = tk.Button(middleFrame,text = "Check",command = GetVar,height=2,width=10,font = ('Arial',16),bg = 'light grey').pack()
            emptyLabel2 = tk.Label(middleFrame,text = ' ',font = ('Arial',16),height=2).pack()
            hintLabel = tk.Label(middleFrame,text = "The friendship index of user 1 and user 2 is",font = ('Arial',12)).pack()
            numEntry = tk.Entry(middleFrame, textvariable=indexVar).pack()
            fIndex.mainloop()

        def GUIQuotationIndex():
            qIndex = tk.Tk()
            qIndex.title('Quotation Index')
            qIndex.geometry("600x400")
            titleLabel = tk.Label(qIndex,text = 'Quotation Index', font = ('Arial',16)).pack()

            leftFrame = tk.Frame(qIndex)
            middleFrame = tk.Frame(qIndex)
            leftFrame.pack(side = 'left')
            middleFrame.pack()
            
            leftLabel = tk.Label(leftFrame,text = 'Users', font = ('Arial',12)).pack()
            GUIFriendshipIndex.leftBox = tk.Listbox(leftFrame,height = 15)
            for item in GUI.nameList:
                GUIFriendshipIndex.leftBox.insert('end',item)
            GUIFriendshipIndex.leftBox.pack()

            var1 = tk.StringVar(qIndex)
            var2 = tk.StringVar(qIndex)
            indexVar = tk.StringVar(qIndex)
            emptyLabel = tk.Label(middleFrame,text = ' ',font = ('Arial',16),height=2).pack()
            user1Label = tk.Label(middleFrame,text = "User 1",font = ('Arial',12)).pack()
            user1Entry = tk.Entry(middleFrame,show = None,textvariable = var1).pack()
            user2Label = tk.Label(middleFrame,text = "User 2",font = ('Arial',12)).pack()
            user2Entry = tk.Entry(middleFrame,show = None,textvariable = var2).pack()

            def GetVar():
               indexNumber = QuotationIndex(var1.get(),var2.get())
               indexVar.set(indexNumber)

            checkButton = tk.Button(middleFrame,text = "Check",command = GetVar,height=2,width=10,font = ('Arial',16),bg = 'light grey').pack()
            emptyLabel2 = tk.Label(middleFrame,text = ' ',font = ('Arial',16),height=2).pack()
            hintLabel = tk.Label(middleFrame,text = "The quotation index of user 1 and user 2 is",font = ('Arial',12)).pack()
            numEntry = tk.Entry(middleFrame, textvariable=indexVar).pack()
            qIndex.mainloop()

        def GUIFindKOL():
            kol = tk.Tk()
            kol.title('Find KOL')
            kol.geometry("600x400")
            titleLabel = tk.Label(kol,text = 'Find KOL', font = ('Arial',16)).pack()
            emptyLabel1 = tk.Label(kol,text = ' ', font = ('Arial',16),height = 2).pack()

            leftFrame = tk.Frame(kol)
            middleFrame = tk.Frame(kol)
            rightFrame = tk.Frame(kol)
            leftFrame.pack(side = 'left')
            middleFrame.pack()
            rightFrame.pack(side = 'right')
            
            leftLabel = tk.Label(leftFrame,text = 'Users', font = ('Arial',12)).pack()
            GUIFindKOL.leftBox = tk.Listbox(leftFrame,height = 15)
            for item in GUI.nameList:
                GUIFindKOL.leftBox.insert('end',item)
            GUIFindKOL.leftBox.pack()

            rightLabel = tk.Label(rightFrame,text = 'KOL', font = ('Arial',12)).pack()
            GUIFindKOL.rightBox = tk.Listbox(rightFrame,height = 15)
            GUIFindKOL.rightBox.pack()

            number = tk.Label(kol,text = "Your selection:")
            GUIFindKOL.percentNumber = 0
            def selection(num):
                number.config(text = "Your selection:"+ num)
                GUIFindKOL.percentNumber = num
            percentage = tk.Scale(kol, label='Percentage of KOL', from_=0, to=100, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=20, resolution=0.1,command = selection).pack()
            number.pack()

            var = tk.StringVar(kol)
            
            impact = tk.Label(kol,text = "Your selection:")
            GUIFindKOL.impactNumber = 0
            def selection(num):
                impact.config(text = "Your selection:"+ num)
                GUIFindKOL.impactNumber = num
            miniImpact = tk.Scale(kol, label='Minimum impact index', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=2, resolution=0.01,command = selection).pack()
            impact.pack()

            def addKOL():
                GUIFindKOL.rightBox.delete(0,'end')
                kolList = KOL(GUIFindKOL.impactNumber,GUIFindKOL.percentNumber)
                for item in kolList:
                    GUIFindKOL.rightBox.insert('end', item)

            emptyLabel2 = tk.Label(kol,text = ' ', font = ('Arial',16),height = 1).pack()
            findButton = tk.Button(kol, text = "Find KOL",command = addKOL,font = ('Arial',16),height = 2,width = 20,bg = 'light grey').pack()



            kol.mainloop()

        func1 = tk.Button(frame_l,text = "User Impact Index", font = ("Arial",12),width = 20, height = 2,bg = 'light grey',command = GUIUserImpactIndex).pack()
        func2 = tk.Button(frame_l,text = "Post Impact Index", font = ("Arial",12),width = 20, height = 2,bg = 'light grey',command = GUIPostImpactIndex).pack()
        func3 = tk.Button(frame_r,text = "Friendship Index", font = ("Arial",12),width = 20, height = 2,bg = 'light grey',command = GUIFriendshipIndex).pack()
        func4 = tk.Button(frame_r,text = "Quotation Index", font = ("Arial",12),width = 20, height = 2,bg = 'light grey',command = GUIQuotationIndex).pack()
        func5 = tk.Button(advWindow,text = "Find KOL", font = ("Arial",12),width = 20, height = 2,bg = 'light grey',command = GUIFindKOL).pack()
        advWindow.mainloop()

    def BasicScreen():
        basWindow = tk.Tk()
        basWindow.title("Basic Functions")
        basWindow.geometry("600x400")

        basLabel = tk.Label(basWindow,text = 'Basic Functions', font = ('Arial',16)).pack()

        frame = tk.Frame(basWindow)
        frame.pack()
        frame_l = tk.Frame(frame)
        frame_l.pack(side = 'left')
        frame_r = tk.Frame(frame)
        frame_r.pack(side = 'right')

        def GUIAnchor():
            return 0
        def GUIDirectReport():
            dR = tk.Tk()
            dR.title('Direct Report')
            dR.geometry("600x400")
            titleLabel = tk.Label(dR,text = 'Direct Report', font = ('Arial',16)).pack()
            emptyLabel = tk.Label(dR,text = ' ', font = ('Arial',16),height = 5)
            hintLabel = tk.Label(dR, text = 'Enter Post Title',font = ('Arial',12))
            
            leftFrame = tk.Frame(dR)
            middleFrame = tk.Frame(dR)
            rightFrame = tk.Frame(dR)
            leftFrame.pack(side = 'left')
            middleFrame.pack()
            rightFrame.pack(side = 'right')
            
            leftLabel = tk.Label(leftFrame,text = 'Post', font = ('Arial',12)).pack()
            GUIDirectReport.leftBox = tk.Listbox(leftFrame,height = 15)
            for item in GUI.postList:
                GUIDirectReport.leftBox.insert('end',item)
            GUIDirectReport.leftBox.pack()

            var = tk.StringVar(dR)
            GUIDirectReport.choice = ''
            def getReport():
                var.set(GUI.postList[GUIDirectReport.leftBox.curselection()[0]])
                GUIDirectReport.choice = GUI.postList[GUIDirectReport.leftBox.curselection()[0]]
                printReport()

            emptyLabel.pack()
            hintLabel.pack()
            reportEntry = tk.Entry(dR,show=None,textvariable=var).pack()
            reportButton = tk.Button(dR,text="Find Direct Report",command = getReport,font = ('Arial',16),height = 2,width=20,bg = 'light grey').pack(side = 'bottom')

            rightLabel = tk.Label(rightFrame,text = 'Direct Report', font = ('Arial',12)).pack()
            GUIDirectReport.rightBox = tk.Listbox(rightFrame,height = 15)

            def printReport():
                reportList = DirectReport(GUIDirectReport.choice)
                GUIDirectReport.rightBox.delete(0,'end')
                for item in reportList:
                    GUIDirectReport.rightBox.insert('end',item)

            
            GUIDirectReport.rightBox.pack()
            dR.mainloop()

        def GUIGetA():
            return 0
        def GUIGetU():
            return 0
        def GUIIsDirectSource():
            isDirectSource = tk.Tk()
            isDirectSource.title('Is Direct Source?')
            isDirectSource.geometry("600x400")
            titleLabel = tk.Label(isDirectSource,text = 'Is Direct Source?', font = ('Arial',16)).pack()

            leftFrame = tk.Frame(isDirectSource)
            middleFrame = tk.Frame(isDirectSource)
            leftFrame.pack(side = 'left')
            middleFrame.pack()
            
            leftLabel = tk.Label(leftFrame,text = 'Post', font = ('Arial',12)).pack()
            isDirectSource.leftBox = tk.Listbox(leftFrame,height = 15)
            for item in GUI.postList:
                isDirectSource.leftBox.insert('end',item)
            isDirectSource.leftBox.pack()

            var1 = tk.StringVar(isDirectSource)
            var2 = tk.StringVar(isDirectSource)
            indexVar = tk.StringVar(isDirectSource)
            emptyLabel = tk.Label(middleFrame,text = ' ',font = ('Arial',16),height=2).pack()
            user1Label = tk.Label(middleFrame,text = "Enter Source",font = ('Arial',12)).pack()
            user1Entry = tk.Entry(middleFrame,show = None,textvariable = var1).pack()
            user2Label = tk.Label(middleFrame,text = "Enter Report",font = ('Arial',12)).pack()
            user2Entry = tk.Entry(middleFrame,show = None,textvariable = var2).pack()

            def GetVar():
               indexNumber = IsDirectSource(var1.get(),var2.get())
               if indexNumber == True:
                   indexVar.set("Yes")
               elif indexNumber == False:
                   indexVar.set("No")

            checkButton = tk.Button(middleFrame,text = "Check",command = GetVar,height=2,width=10,font = ('Arial',16),bg = 'light grey').pack()
            emptyLabel2 = tk.Label(middleFrame,text = ' ',font = ('Arial',16),height=2).pack()
            hintLabel = tk.Label(middleFrame,text = "Is Direct Source?",font = ('Arial',12)).pack()
            numEntry = tk.Entry(middleFrame, textvariable=indexVar).pack()
            isDirectSource.mainloop()

        def GUIIsSource():
            isSource = tk.Tk()
            isSource.title('Is Source?')
            isSource.geometry("600x400")
            titleLabel = tk.Label(isSource,text = 'Is Source?', font = ('Arial',16)).pack()

            leftFrame = tk.Frame(isSource)
            middleFrame = tk.Frame(isSource)
            leftFrame.pack(side = 'left')
            middleFrame.pack()
            
            leftLabel = tk.Label(leftFrame,text = 'Post', font = ('Arial',12)).pack()
            isSource.leftBox = tk.Listbox(leftFrame,height = 15)
            for item in GUI.postList:
                isSource.leftBox.insert('end',item)
            isSource.leftBox.pack()

            var1 = tk.StringVar(isSource)
            var2 = tk.StringVar(isSource)
            indexVar = tk.StringVar(isSource)
            emptyLabel = tk.Label(middleFrame,text = ' ',font = ('Arial',16),height=2).pack()
            user1Label = tk.Label(middleFrame,text = "Enter Source",font = ('Arial',12)).pack()
            user1Entry = tk.Entry(middleFrame,show = None,textvariable = var1).pack()
            user2Label = tk.Label(middleFrame,text = "Enter Report",font = ('Arial',12)).pack()
            user2Entry = tk.Entry(middleFrame,show = None,textvariable = var2).pack()

            def GetVar():
               indexNumber = IsSource(var1.get(),var2.get())
               if indexNumber == True:
                   indexVar.set("Yes")
               elif indexNumber == False:
                   indexVar.set("No")

            checkButton = tk.Button(middleFrame,text = "Check",command = GetVar,height=2,width=10,font = ('Arial',16),bg = 'light grey').pack()
            emptyLabel2 = tk.Label(middleFrame,text = ' ',font = ('Arial',16),height=2).pack()
            hintLabel = tk.Label(middleFrame,text = "Is Source?",font = ('Arial',12)).pack()
            numEntry = tk.Entry(middleFrame, textvariable=indexVar).pack()
            isSource.mainloop()

        def GUIIsFriend():
            isFriend = tk.Tk()
            isFriend.title('Is Friend?')
            isFriend.geometry("600x400")
            titleLabel = tk.Label(isFriend,text = 'Is Friend?', font = ('Arial',16)).pack()

            leftFrame = tk.Frame(isFriend)
            middleFrame = tk.Frame(isFriend)
            leftFrame.pack(side = 'left')
            middleFrame.pack()
            
            leftLabel = tk.Label(leftFrame,text = 'Users', font = ('Arial',12)).pack()
            GUIIsFriend.leftBox = tk.Listbox(leftFrame,height = 15)
            for item in GUI.nameList:
                GUIIsFriend.leftBox.insert('end',item)
            GUIIsFriend.leftBox.pack()

            var1 = tk.StringVar(isFriend)
            var2 = tk.StringVar(isFriend)
            indexVar = tk.StringVar(isFriend)
            emptyLabel = tk.Label(middleFrame,text = ' ',font = ('Arial',16),height=2).pack()
            user1Label = tk.Label(middleFrame,text = "Enter User 1",font = ('Arial',12)).pack()
            user1Entry = tk.Entry(middleFrame,show = None,textvariable = var1).pack()
            user2Label = tk.Label(middleFrame,text = "Enter User 2",font = ('Arial',12)).pack()
            user2Entry = tk.Entry(middleFrame,show = None,textvariable = var2).pack()

            def GetVar():
               indexNumber = IsFriend(var1.get(),var2.get())
               if indexNumber == True:
                   indexVar.set("Yes")
               elif indexNumber == False:
                   indexVar.set("No")

            checkButton = tk.Button(middleFrame,text = "Check",command = GetVar,height=2,width=10,font = ('Arial',16),bg = 'light grey').pack()
            emptyLabel2 = tk.Label(middleFrame,text = ' ',font = ('Arial',16),height=2).pack()
            hintLabel = tk.Label(middleFrame,text = "user 1 and user 2 are friends?",font = ('Arial',12)).pack()
            numEntry = tk.Entry(middleFrame, textvariable=indexVar).pack()
            isFriend.mainloop()

        def GUINicePrintU():
            def EditNicePrintU(userName):
                user = open('user.txt')
                userInfoList = []
                for userInfo in user:
                    userInfoList.append(userInfo.strip())
                nameList = []
                passwordList = []
                birthdayList = []
                phoneNumberList = []
                friendList = []
                postList = []
                for userInfo in userInfoList:
                    name,password,birthday,phoneNumber,friend,post = map(str,userInfo.split(','))
                    nameList.append(name)
                    passwordList.append(password)
                    birthdayList.append(birthday)
                    phoneNumberList.append(phoneNumber)
                    friendList.append(friend)
                    postList.append(post)
                index = -1
                name = ''
                password = ''
                birthday = ''
                phoneNumber = ''
                friendNameList = []
                postTitleList = []
                for alluser in nameList:
                    index += 1
                    if alluser == userName:
                        name = nameList[index]
                        password = passwordList[index]
                        birthday = birthdayList[index]
                        phoneNumber = phoneNumberList[index]
                        friendNameList = friendList[index].split(';')
                        postTitleList = postList[index].split(';')
                        
                user.close()
                return [name,password,birthday,phoneNumber,friendNameList,postTitleList]

            NPU = tk.Tk()
            NPU.title('Nice Print User')
            NPU.geometry("600x400")
            titleLabel = tk.Label(NPU,text = 'Nice Print User', font = ('Arial',16)).pack()

            leftFrame = tk.Frame(NPU)
            middleFrame = tk.Frame(NPU)
            rightFrame = tk.Frame(NPU)
            leftFrame.pack(side = 'left')
            middleFrame.pack()
            rightFrame.pack(side = 'right')
            middleLeft = tk.Frame(middleFrame)
            middleRight = tk.Frame(middleFrame)
            middleLeft.pack(side = 'left')
            middleRight.pack(side = 'right')
            middleBottom = tk.Frame(NPU)
            middleBottom.pack()
            
            leftLabel = tk.Label(leftFrame,text = 'Choose User', font = ('Arial',12)).pack()
            GUINicePrintU.leftBox = tk.Listbox(leftFrame,height = 15)
            for item in GUI.nameList:
                GUINicePrintU.leftBox.insert('end',item)
            GUINicePrintU.leftBox.pack()

            nameVar = tk.StringVar(NPU)
            passVar = tk.StringVar(NPU)
            phoneVar = tk.StringVar(NPU)
            birthdayVar = tk.StringVar(NPU)

            nameLabel = tk.Label(middleLeft,text = 'User Name').pack()
            nameEntry = tk.Entry(middleRight,show = None,textvariable = nameVar).pack()
            emptyLabel1 = tk.Label(middleLeft,text = '').pack()
            emptyLabel2 = tk.Label(middleRight,text = '').pack()
            passLabel = tk.Label(middleLeft,text = 'Password').pack()
            passEntry = tk.Entry(middleRight,show = None,textvariable = passVar).pack()
            birthdayLabel = tk.Label(middleLeft, text = 'Birthday').pack()
            birthdayEntry = tk.Entry(middleRight, show = None, textvariable = birthdayVar).pack()
            phoneLabel = tk.Label(middleLeft, text = 'Phone').pack()
            phoneEntry = tk.Entry(middleRight, show = None, textvariable = phoneVar).pack()
            friendLabel = tk.Label(middleLeft, text = 'Friend').pack()
            GUINicePrintU.friendBox = tk.Listbox(middleLeft,height = 7)
            GUINicePrintU.friendBox.pack()
            postLabel = tk.Label(middleRight, text = 'Post').pack()
            GUINicePrintU.postBox = tk.Listbox(middleRight, height = 7)
            GUINicePrintU.postBox.pack()

            def GetData():
                nameVar.set(GUI.nameList[GUINicePrintU.leftBox.curselection()[0]])
                userName = GUI.nameList[GUINicePrintU.leftBox.curselection()[0]]
                userData = EditNicePrintU(userName)
                passVar.set(userData[1])
                phoneVar.set(userData[3])
                birthdayVar.set(userData[2])
                GUINicePrintU.friendBox.delete(0,'end')
                for item in userData[4]:
                    GUINicePrintU.friendBox.insert('end',item)
                GUINicePrintU.postBox.delete(0,'end')
                for post in userData[5]:
                    GUINicePrintU.postBox.insert('end',post)

            printButton = tk.Button(middleBottom,text = 'Print User',command = GetData,font = ("Arial",16), width = 20, height = 2, bg = 'light grey').pack()

            NPU.mainloop()

        def GUINicePrintA():
            def EditNicePrintA(postName):
                try:
                    post = open('post/'+str(postName)+'.txt',encoding = 'UTF-8')
                except IOError:
                    return ['','','',['']]
                titleString = post.readline()
                title = titleString.strip()
                authorString = post.readline()
                author = authorString.strip()
                quoteString = post.readline()
                quote = quoteString.strip()
                content = []
                for contentLine in post:
                    content.append(contentLine)
                post.close()
                return [title,author,quote,content]

            NPA = tk.Tk()
            NPA.title('Nice Print Article')
            NPA.geometry("600x400")
            titleLabel = tk.Label(NPA,text = 'Nice Print Aritcle', font = ('Arial',16)).pack()

            leftFrame = tk.Frame(NPA)
            middleFrame = tk.Frame(NPA)
            rightFrame = tk.Frame(NPA)
            leftFrame.pack(side = 'left')
            middleFrame.pack()
            rightFrame.pack(side = 'right')
            middleLeft = tk.Frame(middleFrame)
            middleRight = tk.Frame(middleFrame)
            middleLeft.pack(side = 'left')
            middleRight.pack(side = 'right')
            middleBottom = tk.Frame(NPA)
            middleBottom.pack()
            middleDown = tk.Frame(middleFrame)
            
            leftLabel = tk.Label(leftFrame,text = 'Choose Post', font = ('Arial',12)).pack()
            GUINicePrintA.leftBox = tk.Listbox(leftFrame,height = 15)
            for item in GUI.postList:
                GUINicePrintA.leftBox.insert('end',item)
            GUINicePrintA.leftBox.pack()

            titleVar = tk.StringVar(NPA)
            authorVar = tk.StringVar(NPA)
            quoteVar = tk.StringVar(NPA)
            contentVar = tk.StringVar(NPA)

            emptyLebel3 = tk.Label(middleLeft,text='',font = ('Arial',6)).pack()
            titleLabel = tk.Label(middleLeft,text = 'Post Title').pack()
            titleEntry = tk.Entry(middleRight,show = None,textvariable = titleVar).pack()
            emptyLabel1 = tk.Label(middleLeft,text = '').pack()
            emptyLabel2 = tk.Label(middleRight,text = '').pack()
            authorLabel = tk.Label(middleLeft,text = 'Author').pack()
            authorEntry = tk.Entry(middleRight,show = None,textvariable = authorVar).pack()
            quoteLabel = tk.Label(middleLeft, text = 'Quotation').pack()
            quoteEntry = tk.Entry(middleRight, show = None, textvariable = quoteVar).pack()
            
            contentLabel = tk.Label(middleLeft, text = 'Content').pack()
            GUINicePrintA.contentText = tk.Text(middleBottom,height = 7)
            GUINicePrintA.contentText.pack()

            def GetData():
                titleVar.set(GUI.postList[GUINicePrintA.leftBox.curselection()[0]])
                postName = GUI.postList[GUINicePrintA.leftBox.curselection()[0]]
                userData = EditNicePrintA(postName)
                authorVar.set(userData[1])
                quoteVar.set(userData[2])
                GUINicePrintA.contentText.delete('1.0','end')
                for item in userData[3]:
                    GUINicePrintA.contentText.insert('end',item)

            printButton = tk.Button(middleBottom,text = 'Print Post',command = GetData,font = ("Arial",16), width = 20, height = 2, bg = 'light grey').pack()

            NPA.mainloop()
        def GUIReport():
            R = tk.Tk()
            R.title('Report')
            R.geometry("600x400")
            titleLabel = tk.Label(R,text = 'Report', font = ('Arial',16)).pack()
            emptyLabel = tk.Label(R,text = ' ', font = ('Arial',16),height = 5)
            hintLabel = tk.Label(R, text = 'Post Title',font = ('Arial',12))
            
            leftFrame = tk.Frame(R)
            middleFrame = tk.Frame(R)
            rightFrame = tk.Frame(R)
            leftFrame.pack(side = 'left')
            middleFrame.pack()
            rightFrame.pack(side = 'right')
            
            leftLabel = tk.Label(leftFrame,text = 'Choose Post', font = ('Arial',12)).pack()
            GUIReport.leftBox = tk.Listbox(leftFrame,height = 15)
            for item in GUI.postList:
                GUIReport.leftBox.insert('end',item)
            GUIReport.leftBox.pack()
           

            var = tk.StringVar(R)
            GUIReport.choice = ''
            def getReport():
                var.set(GUI.postList[GUIReport.leftBox.curselection()[0]])
                GUIReport.choice = GUI.postList[GUIReport.leftBox.curselection()[0]]
                printReport()

            emptyLabel.pack()
            hintLabel.pack()
            reportEntry = tk.Entry(R,show=None,textvariable=var).pack()
            reportButton = tk.Button(R,text="Find Report",command = getReport,font = ('Arial',16),height = 2,width=20,bg = 'light grey').pack(side = 'bottom')

            rightLabel = tk.Label(rightFrame,text = 'Report', font = ('Arial',12)).pack()
            GUIReport.rightBox = tk.Listbox(rightFrame,height = 15)

            def printReport():
                reportList = Report(GUIReport.choice)
                GUIReport.rightBox.delete(0,'end')
                for item in reportList:
                    GUIReport.rightBox.insert('end',item)

            
            GUIReport.rightBox.pack()
            R.mainloop()
        
        func1 = tk.Button(frame_l,text = "Anchor", font = ("Arial",12),width = 20, height = 2,bg = 'light grey',command = GUIAnchor).pack()
        func2 = tk.Button(frame_l,text = "Direct Report", font = ("Arial",12),width = 20, height = 2,bg = 'light grey',command = GUIDirectReport).pack()
        func3 = tk.Button(frame_l,text = "GetA", font = ("Arial",12),width = 20, height = 2,bg = 'light grey',command = GUIGetA).pack()
        func4 = tk.Button(frame_l,text = "GetU", font = ("Arial",12),width = 20, height = 2,bg = 'light grey',command = GUIGetU).pack()
        func5 = tk.Button(frame_l,text = "Is Direct Source", font = ("Arial",12),width = 20, height = 2,bg = 'light grey',command = GUIIsDirectSource).pack()
        func6 = tk.Button(frame_r,text = "Is Source", font = ("Arial",12),width = 20, height = 2,bg = 'light grey',command = GUIIsSource).pack()
        func7 = tk.Button(frame_r,text = "Is Friend", font = ("Arial",12),width = 20, height = 2,bg = 'light grey',command = GUIIsFriend).pack()
        func8 = tk.Button(frame_r,text = "Nice Print U", font = ("Arial",12),width = 20, height = 2,bg = 'light grey',command = GUINicePrintU).pack()
        func9 = tk.Button(frame_r,text = "Nice Print A", font = ("Arial",12),width = 20, height = 2,bg = 'light grey',command = GUINicePrintA).pack()
        func10 = tk.Button(frame_r,text = "Report", font = ("Arial",12),width = 20, height = 2,bg = 'light grey',command = GUIReport).pack()
        basWindow.mainloop()

    advButton = tk.Button(mainWindow,text = "Advanced Function", font = ("Arial",16),width = 20, height = 2,bg = 'light gray', command = AdvancedScreen)
    advButton.pack(side='bottom')

    basButton = tk.Button(mainWindow,text = "Basic Function", font = ("Arial",16),width = 20, height = 2,bg = 'light gray', command = BasicScreen)
    basButton.pack(side='bottom')
    


    mainWindow.mainloop()

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

"""This function calcuate two users' friendship index
It receives two user name and return their friendship index
For the algorithm, please refer to the report

Written by Yunfei LIU Nov 13, 2020"""

def FriendshipIndex(user1,user2):
    #This function receives a user name and return the post list
    def UserInfo(userName):
        user = open('user.txt')
        userInfoList = []
        for userInfo in user:
            userInfoList.append(userInfo.strip())
        nameList = []
        postList = []
        for userInfo in userInfoList:
            name,password,birthday,phoneNumber,friend,post = map(str,userInfo.split(','))
            nameList.append(name)
            postList.append(post)
        try:
            userIndex = nameList.index(userName)
        except ValueError:
            return []
        userPostList = postList[userIndex].split(';')
        return userPostList
    
    #This function receives a user's post and return the resource list
    def UserQuoteList(postList):
        quoteList = []
        for post in postList:
            try:
                postData = open('post/' + post + '.txt', encoding='UTF-8')
            except IOError:
                continue
            line1 = postData.readline()
            line2 = postData.readline()
            line3 = postData.readline()
            quotation = line3.strip()
            postData.close()
            quoteList.append(quotation)
        return quoteList

    user1Quote = UserQuoteList(UserInfo(user1))
    user2Quote = UserQuoteList(UserInfo(user2))
    if len(user1Quote) == 0 or len(user2Quote) == 0:
        return 0
    user1Friendship = 0
    user2Friendship = 0
    for resource in user1Quote:
        for post in UserInfo(user2):
            if resource == post:
                user1Friendship += 1
    for resource in user2Quote:
        for post in UserInfo(user1):
            if resource == post:
                user2Friendship += 1
    if user1Friendship < user2Friendship:
        eachOtherQuote = user1Friendship
    else:
        eachOtherQuote = user2Friendship
    friendshipIndex = (((eachOtherQuote/len(user1Quote))**2)+((eachOtherQuote/len(user2Quote))**2))**0.5
    return "{:.3f}".format(friendshipIndex)

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
            quote = str(input("Please enter the quotation. Or enter 'null' if no quotation: "))       
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

"""This function is used to add users into user.txt
No receiving and return True when finished.

Written by Yunfei LIU
Edit log:
Oct 24, 2020 created"""
def GetU():
    #This function is used to add user from keyboard
    #No receiving and return True when write successfully and False in other situation
    def GetFromKeyboard():
        userName = str(input("\nPlease enter the user name: "))
        password = str(input("Please enter the password: "))
        birthday = str(input("Please enter the birthday or enter ' ' if no birthday: "))
        phoneNumber = str(input("Please enter the phone number or enter ' ' if no phone number: "))
        friend = str(input("Please enter friends, separate with ';' and also end with ';': "))
        post = str(input("Please enter posts, no space, separate with ';' and also end with ';': "))
        print("\nCheck your input:\n")
        print("username:%s\npassword:%s\nbirthday:%s\nphone number:%s\nfriend:%s\nposts:%s\n" %(userName,password,birthday,phoneNumber,friend,post))
        commandChar = str(input("Please check the format carefully and enter [Y/y] to confirm, others to cancel: "))
        if commandChar == 'Y' or commandChar == 'y':
            writeFile = open('user.txt','a')
            writeFile.write('%s,%s,%s,%s,%s,%s\n' % (userName,password,birthday,phoneNumber,friend,post))
            writeFile.close()
            print("\nWrite Successfully")
            return True
        else:
            print("\nCanceled")
            return False

    #This function is used to add user from file
    #No receiving and return True when successfully write and return False in other situation
    def GetFromFile():
        filePath = str(input("Please input the full path and name of the file: "))
        try:
            open(filePath)
            fileData = open(filePath)
        except IOError:
            print("\nCannot found the file\n")
            return False
        else:
            userInfoList = []
            for userInfo in fileData:
                userInfoList.append(userInfo.strip())
            nameList = []
            passwordList = []
            birthdayList = []
            phoneNumberList = []
            friendList = []
            postList = []
            for userInfo in userInfoList:
                 name,password,birthday,phoneNumber,friend,post = map(str,userInfo.split(','))
                 nameList.append(name)
                 passwordList.append(password)
                 birthdayList.append(birthday)
                 phoneNumberList.append(phoneNumber)
                 friendList.append(friend)
                 postList.append(post)
            print("\nFile read\nThe following are users: ")
            for i in nameList:
                print(i)
            commandChar = str(input("Please check it carefully and enter [Y/y] to confirm, others to cancel: "))
            if commandChar == 'Y' or commandChar == 'y':
                writeFile = open('user.txt','a')
                for userInfo in userInfoList:
                    name,password,birthday,phoneNumber,friend,post = map(str,userInfo.split(','))
                    writeFile.write('%s,%s,%s,%s,%s,%s\n' % (name,password,birthday,phoneNumber,friend,post))
                writeFile.close()
                print("\nWrite Successfully\n")
                return True
            else:
                print("\nCanceled\n")
                return False


    print("\nWelcome to the add user mode\n")
    while True:
        commandChar = str(input("Type [N/n] to get new account by keyboard, type [F/f] to get new by file, type [E/e] to exit: "))
        if commandChar == 'n' or commandChar == 'N':
            GetFromKeyboard()
        if commandChar == 'F' or commandChar == 'f':
            GetFromFile()
        if commandChar == 'E' or commandChar == 'e':
            return True

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

"""This function is used to verify friendship
It receives 2 user names and return a boolean
If the users are in each other's friend list, return True
If not, return False

Written by Yunfei LIU
Edit log:
Oct 27, 2020 created
"""
def IsFriend(userName1,userName2):
    user = open('user.txt')
    userInfoList = []
    for userInfo in user:
        userInfoList.append(userInfo.strip())
    nameList = []
    passwordList = []
    birthdayList = []
    phoneNumberList = []
    friendList = []
    postList = []
    for userInfo in userInfoList:
        name,password,birthday,phoneNumber,friend,post = map(str,userInfo.split(','))
        nameList.append(name)
        passwordList.append(password)
        birthdayList.append(birthday)
        phoneNumberList.append(phoneNumber)
        friendList.append(friend)
        postList.append(post)
    try:
        index1 = nameList.index(userName1)
        index2 = nameList.index(userName2)
    except ValueError:
        print("\nUser not found\n")
        user.close()
        return False
    if friendList[index1] == ' ' or friendList[index2] == ' ':
        user.close()
        return False
    friendNameList1 = friendList[index1].split(';')
    friendNameList2 = friendList[index2].split(';')
    for friendName1 in friendNameList1:
        if friendName1 == userName2:
            for friendName2 in friendNameList2:
                if friendName2 == userName1:
                    user.close()
                    return True
    user.close()
    return False

"""This function is used to check whether the given sourcepost is the source of a report.
It receives sourcepost and reportpost titles and return True when sourcepost is source of reportpost
return False otherwise.

Written by Muyuan LI Oct 30, 2020
Edited by Yunfei LIU Oct 31, 2020"""

def IsSource(sourcePost, reportPost):
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
        if report == source:
            return True
        if report == 'null':
            return False
        report = DirectSource(report)
    return False

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


"""This function is used to print a user's profile
it receives a user's name and return True while name found, return False when name not found

Written by Yunfei LIU
Edit log:
Oct 24, 2020 created"""
def NicePrintU(userName):
    user = open('user.txt')
    userInfoList = []
    for userInfo in user:
        userInfoList.append(userInfo.strip())
    nameList = []
    passwordList = []
    birthdayList = []
    phoneNumberList = []
    friendList = []
    postList = []
    for userInfo in userInfoList:
        name,password,birthday,phoneNumber,friend,post = map(str,userInfo.split(','))
        nameList.append(name)
        passwordList.append(password)
        birthdayList.append(birthday)
        phoneNumberList.append(phoneNumber)
        friendList.append(friend)
        postList.append(post)
    index = -1
    for alluser in nameList:
        index += 1
        if alluser == userName:
            print("\nUser Found\n")
            print("Username:",nameList[index])
            print("Password:",passwordList[index])
            print("Birthday:",birthdayList[index])
            print("Phone number:",phoneNumberList[index])
            print("\nfriends:")
            if friendList[index] != ' ':
                friendNameList = friendList[index].split(';')
                for friendName in friendNameList:
                    print(friendName)
            print("\nPosts:")
            if postList[index] != ' ':
                postTitleList = postList[index].split(';')
                for postTitle in postTitleList:
                    print(postTitle)
            user.close()
            return True
    print("Cannot find a user named",userName,'\n')
    user.close()
    return False

"""This function calcate the impact index of a post
It receives a post name and return a impact index float
For the algorithm please watch the report

Written by Yunfei LIU Nov 11, 2020
"""
def PostImpactIndex(anchor):
    #This function is as same as DirectReport(anchor)
    countDict = dict()
    PostImpactIndex.countDict = {}
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
                    if title[1:] not in countDict:
                        PostImpactIndex.countDict[title[1:]] = 1
                    else: 
                        PostImpactIndex.countDict[title[1:]] += 1
                else:
                    reportList.append(title)
                    if title not in countDict:
                        PostImpactIndex.countDict[title] = 1
                    else: 
                        PostImpactIndex.countDict[title] += 1
            readFile.close()
        return reportList

    #This function is used to check the list have something except empty
    def CheckList(list):
        count = 0
        for item in list:
            if item != []:
                count += 1
        if count != 0:
            return True
        else:
            return False

    if DirectReport(anchor) == []:
        return 0
    reportList = DirectReport(anchor)
    anchorList = DirectReport(anchor)
    tempList = anchorList
    count = 2
    for dictKey in PostImpactIndex.countDict:
        PostImpactIndex.countDict[dictKey] += 1
    for anchorItem in anchorList:
        if not CheckList(anchorList):
            break
        reportList.extend(DirectReport(anchorItem))
        tempList.extend(DirectReport(anchorItem))
        if DirectReport(anchorItem) != []:
            count += 1
            for dictKey in PostImpactIndex.countDict:
                PostImpactIndex.countDict[dictKey] += 1
    anchorList = tempList
    impactIndex = 0
    for dictKey in PostImpactIndex.countDict:
        PostImpactIndex.countDict[dictKey] = count+1-PostImpactIndex.countDict[dictKey]
        impactIndex += (0.5)**(PostImpactIndex.countDict[dictKey]-1)
    return "{:.3f}".format(impactIndex)

"""This function calcuate two users' quotation index
It receives two user name and return their quotation index
For the algorithm, please refer to the report

Written by Yunfei LIU Nov 13, 2020"""

def QuotationIndex(user1,user2):
    #This function receives a user name and return the post list
    def UserInfo(userName):
        user = open('user.txt')
        userInfoList = []
        for userInfo in user:
            userInfoList.append(userInfo.strip())
        nameList = []
        postList = []
        for userInfo in userInfoList:
            name,password,birthday,phoneNumber,friend,post = map(str,userInfo.split(','))
            nameList.append(name)
            postList.append(post)
        try:
            userIndex = nameList.index(userName)
        except ValueError:
            return []
        userPostList = postList[userIndex].split(';')
        return userPostList
    
    #This function receives a user's post and return the resource list
    def UserQuoteList(postList):
        quoteList = []
        for post in postList:
            try:
                postData = open('post/' + post + '.txt', encoding='UTF-8')
            except IOError:
                return []
            line1 = postData.readline()
            line2 = postData.readline()
            line3 = postData.readline()
            quotation = line3.strip()
            postData.close()
            quoteList.append(quotation)
        return quoteList

    user1Quote = UserQuoteList(UserInfo(user1))
    user2Quote = UserQuoteList(UserInfo(user2))
    if len(user1Quote) == 0 or len(user2Quote) == 0:
        return 0
    user1Quotation = 0
    user2Quotation = 0
    for resource in user1Quote:
        for post in UserInfo(user2):
            if resource == post:
                user1Quotation += 1
    for resource in user2Quote:
        for post in UserInfo(user1):
            if resource == post:
                user2Quotation += 1
    quotationIndex = (((user1Quotation/len(user1Quote))**2)+((user2Quotation/len(user2Quote))**2))**0.5
    return "{:.3f}".format(quotationIndex)

"""This function is used to find direct and indirect posts
it receives a post title and return a list of direct and indirect reports, return an empty list when no report

Written by Yunfei LIU
Edit log:
Oct 29, 2020 created"""
def Report(anchor):
    #This function is as same as DirectReport(anchor)
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

    #This function is used to check the list have something except empty
    def CheckList(list):
        count = 0
        for item in list:
            if item != []:
                count += 1
        if count != 0:
            return True
        else:
            return False

    if DirectReport(anchor) == []:
        return []
    reportList = DirectReport(anchor)
    anchorList = DirectReport(anchor)
    if anchorList == []:
        return []
    tempList = anchorList
    for anchorItem in anchorList:
        if not CheckList(anchorList):
            break
        reportList.extend(DirectReport(anchorItem))
        tempList.extend(DirectReport(anchorItem))
    anchorList = tempList
    return reportList

"""This function calcuate a user's impact index
It receives a user name and return this user's impact index
For the algorithm, please refer to the report

Written by Yunfei LIU Nov 11, 2020"""
def UserImpactIndex(userName):
    user = open('user.txt')
    userInfoList = []
    for userInfo in user:
        userInfoList.append(userInfo.strip())
    nameList = []
    postList = []
    for userInfo in userInfoList:
        name,password,birthday,phoneNumber,friend,post = map(str,userInfo.split(','))
        nameList.append(name)
        postList.append(post)
    try:
        userIndex = nameList.index(userName)
    except ValueError:
        return 0
    userPostList = postList[userIndex].split(';')
    impactSum = 0
    for title in userPostList:
        impactSum += float(PostImpactIndex(title))
    import math
    impactIndex = math.log(impactSum+1,math.e)
    return "{:.3f}".format(impactIndex)

"""This function is used for finding KOL
It receives a mininum impact index and a percentage of KOLs
It returns a list of KOL names and their impact index

Written by Yunfei LIU  Nov 24,2020"""
def KOL(miniIndex,percentage):
    percentage = float(percentage)
    if percentage >100 or percentage < 0:
        return []
    user = open('user.txt')
    userInfoList = []
    for userInfo in user:
        userInfoList.append(userInfo.strip())
    nameList = []
    for userInfo in userInfoList:
        name,password,birthday,phoneNumber,friend,post = map(str,userInfo.split(','))
        nameList.append(name)
    impactList = []
    for i in nameList:
        impactList.append([i,UserImpactIndex(i)])
    kolNumber = int((len(nameList)*percentage/100)//1)

    def Verify(list):
        return list[1]

    impactList.sort(key=Verify)
    impactList.reverse()
    kolList = []
    for i in range(kolNumber):
        if float(impactList[i][1]) >= float(miniIndex):
            kolList.append(impactList[i])
    return kolList

"""This function is main function in terminal.
It receives void and return 0 when no error

Written by Yunfei LIU  Nov 23, 2020"""
def main():
    print("Copyright 2020 Mu Yuan LI, Owen CHAN, Yun Fei LIU\nAll rights reserved.\n\n")
    while True:
        modeChar = str(input("Enter 'C' for command line mode, 'G' for GUI (Not developed yet), 'E' for exit: "))
        if modeChar == 'E':
            return 0
        if modeChar == 'G':
            GUI()
            return 0
            return 0
        if modeChar == 'C':
            while True:
                funcChar = str(input("\nEnter 'A' for advanced functions, 'B' for basic functions, 'R' for return to previous menu: "))
                if funcChar == 'R':
                    break
                if funcChar == 'A':
                    print("\n1.UserImpactIndex\n2.PostImpactIndex\n3.FriendshipIndex\n4.QuotationIndex\n5.FindKOL\n")
                    choiceChar = str(input("Please enter numbers to use functions, other to return: "))
                    if choiceChar == '1':
                        userName = str(input("\nEnter the user name: "))
                        print("The impact index for %s is %s\n" %(userName,UserImpactIndex(userName)))
                    elif choiceChar == '2':
                        post = str(input("\nEnter the post title: "))
                        print("The impact index for %s is %s\n" %(post,PostImpactIndex(post)))
                    elif choiceChar == '3':
                        userName1 = str(input("\nEnter user name 1: "))
                        userName2 = str(input("\nEnter user name 2: "))
                        print("\nThe friendship index between %s and %s is %s" %(userName1,userName2,FriendshipIndex(userName1,userName2)))
                    elif choiceChar == '4':
                        userName1 = str(input("\nEnter user name 1: "))
                        userName2 = str(input("\nEnter user name 2: "))
                        print("\nThe quotation index between %s and %s is %s" %(userName1,userName2,QuotationIndex(userName1,userName2)))
                    elif choiceChar == '5':
                        miniIndex = float(input("Please enter the minimum index of KOL: "))
                        percentage = float(input("Please enter the percentage of KOL: "))
                        print("\nThe KOL list\n")
                        for i in KOL(miniIndex,percentage):
                            print("Name:%s\nImpact Index:%s\n" %(i[0],i[1]))

                if funcChar == 'B':
                    print("1.Anchor\n2.DirectReport\n3.GetA\n4.GetU\n5.IsDirectSource\n6.IsSource\n7.IsFriend\n8.NicePrintA\n9.NicePrintU\n10.Report\n")
                    choiceChar = str(input("Please enter numbers to use functions, other to return: "))
                    if choiceChar == '1':
                        continue
                    elif choiceChar == '2':
                        post = str(input("\nEnter the post title: "))
                        reportList = DirectReport(post)
                        print("Direct report of post '%s'"% post)
                        for item in reportList:
                            print(item)
                    elif choiceChar == '3':
                        GetA()
                    elif choiceChar == '4':
                        GetU()
                    elif choiceChar == '5':
                        post1 = str(input("\nEnter source title: "))
                        post2 = str(input("\nEnter report title: "))
                        print("%s is the direct source of %s ? "%(post1,post2),end='')
                        print(IsDirectSource(post1,post2))
                    elif choiceChar == '6':
                        post1 = str(input("\nEnter source title: "))
                        post2 = str(input("\nEnter report title: "))
                        print("%s is the source of %s ? "%(post1,post2),end='')
                        print(IsSource(post1,post2))
                    elif choiceChar == '7':
                        userName1 = str(input("\nEnter user name 1: "))
                        userName2 = str(input("\nEnter user name 2: "))
                        print("%s and %s are friends? "%(userName1,userName2),end = '')
                        print(IsFriend(userName1,userName2))
                    elif choiceChar == '8':
                        post = str(input("\nEnter the post title: "))
                        NicePrintA(post)
                    elif choiceChar == '9':
                        userName = str(input("\nEnter the user name: "))
                        NicePrintU(userName)
                    elif choiceChar == '10':
                        post = str(input("\nEnter the post title: "))
                        reportList = Report(post)
                        print("Report of post '%s'"% post)
                        for item in reportList:
                            print(item)


GUI()     
