Size=StringVar() #variable for radio buttons

#radiobuttons
radSize=Radiobutton(variable=Size,text="Small",value="small",fg="blue",font="Arial 14 bold")
radSize.place(x=20,y=20)
radSize=Radiobutton(variable=Size,text="Medium",value="medium",fg="blue",font="Arial 14 bold")
radSize.place(x=20,y=60)
radSize=Radiobutton(variable=Size,text="Large",value="large",fg="blue",font="Arial 14 bold")
radSize.place(x=20,y=100)

Size.set("medium")#set default size to medium
