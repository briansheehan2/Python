from tkinter import*

def Close():#Close Event
    frmOrder.destroy() #Remove form from memory and close application
def Reset():#Reset Form Event
    entCustName.delete(0,END)#Clear Entry Widget
    lblCustCopy["text"]=""#Set Label Test Property to an empty string
    entCustName.focus()#Set Cursor Position
def Process():
    strCustName=entCustName.get()
    lblCustCopy["text"]=strCustName

frmOrder=Tk()

frmOrder.configure(width=800,height=600,bg="sky blue")
frmOrder.title("Best Pizza Ever Order Form")

lblCoName=Label(text="Best Pizza Ever",font="Arial 16 bold",bg="sky blue",fg="navy")
lblCoName.place(x=300,y=10)

lblCustName=Label(text="Customer Name: ",font="Arial 14",bg="sky blue",fg="navy")
lblCustName.place(x=100,y=50)

entCustName=Entry(font="Arial 14",bg="white",fg="navy",width=30)
entCustName.place(x=260,y=50)

lblCustCopy=Label(text="",font="Arial 14",bg="sky blue",fg="red")
lblCustCopy.place(x=260,y=100)

btnClose=Button(text="Close",font="Arial 14",bg="sky blue",fg="navy",width=8,command=Close)
btnClose.place(x=650,y=500)

btnReset=Button(text="Reset",font="Arial 14",bg="sky blue",fg="navy",width=8,command=Reset)
btnReset.place(x=550,y=500)

btnProcess=Button(text="Process",font="Arial 14",bg="sky blue",fg="navy",width=8,command=Process)
btnProcess.place(x=450,y=500)

entCustName.focus()#Set Cursor Position

frmOrder.mainloop()
    
