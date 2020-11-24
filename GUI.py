def GUI():
    import tkinter as tk
    mainWindow = tk.Tk()
    mainWindow.title("Users And Posts Management System")
    mainWindow.geometry("600x400")

    welInfo = tk.Label(mainWindow,text = "Welcome to use this system", font = ('Arial',24))
    welInfo.pack()

    crInfo = tk.Label(mainWindow,text = "Copyright 2020 Muyuan LI, Owen Chan, Yunfei LIU.\nAll rights reserved.",font = ('Arial',10))
    crInfo.pack()
    
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
            return 0
        def GUIPostImpactIndex():
            return 0
        def GUIFriendshipIndex():
            return 0
        def GUIQuotationIndex():
            return 0
        def GUIFindKOL():
            return 0

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
            return 0
        def GUIGetA():
            return 0
        def GUIGetU():
            return 0
        def GUIIsDirectSource():
            return 0
        def GUIIsSource():
            return 0
        def GUIIsFriend():
            return 0
        def GUINicePrintU():
            return 0
        def GUINicePrintA():
            return 0
        def GUIReport():
            return 0
        
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

GUI()
