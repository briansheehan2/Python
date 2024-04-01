from tkinter import*

def Close():#Close Event
    frmOrder.destroy() #Remove form from memory and close application
def Reset():#Reset Form Event
    entCustName.delete(0,END)#Clear Entry Widget
    lblCustCopy["text"]=""#Set Label Test Property to an empty string
    entCustName.focus()#Set Cursor Position
def Process():
    strCustName=entCustName.get()
    lblCustCopy["text"]="Thank You "+strCustName

frmOrder=Tk()

frmOrder.configure(width=800,height=600,bg="sky blue")
frmOrder.title("Delicious Coffee - By Brian Sheehan")

lblCoName=Label(text="Delicious Coffee Order Form",font="Arial 16 bold",bg="sky blue",fg="navy")
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

Size=StringVar()#Variable for Radiobuttons

lblSize=Label(text="Choose Size",font="Arial 16 bold",bg="sky blue",fg="navy")
lblSize.place(x=10,y=150)
radSize=Radiobutton(variable=Size,text="Small",value="small",fg="blue",font="Arial 14 bold",bg="sky blue")
radSize.place(x=20,y=200)
radSize=Radiobutton(variable=Size,text="Medium",value="medium",fg="blue",font="Arial 14 bold",bg="sky blue")
radSize.place(x=20,y=250)
radSize=Radiobutton(variable=Size,text="Large",value="large",fg="blue",font="Arial 14 bold",bg="sky blue")
radSize.place(x=20,y=300)
Size.set("medium")

addAmericano=IntVar()
addEspresso=IntVar()
addMocha=IntVar()
addLatte=IntVar()

lblFlavor=Label(text="Flavor",font="Arial 16 bold",bg="sky blue",fg="navy")
lblFlavor.place(x=230,y=150)
chkAmericano=Checkbutton(variable=addAmericano,text="Americano",font="Arial 14",fg="blue",bg="sky blue")
chkAmericano.place(x=230,y=200)
chkEspresso=Checkbutton(variable=addEspresso,text="Espresso",font="Arial 14",fg="blue",bg="sky blue")
chkEspresso.place(x=230,y=240)
chkMocha=Checkbutton(variable=addMocha,text="Mocha",font="Arial 14",fg="blue",bg="sky blue")
chkMocha.place(x=230,y=280)
chkLatte=Checkbutton(variable=addLatte,text="Latte",font="Arial 14",fg="blue",bg="sky blue")
chkLatte.place(x=230,y=320)


addMilk=IntVar()#Variable for Checkbutton
addCream=IntVar()
addSugar=IntVar()
addWhiskey=IntVar()
addCinnamon=IntVar()
addPepperment=IntVar()

lblIngredients=Label(text="Add Ingrediants",font="Arial 16 bold",bg="sky blue",fg="navy")
lblIngredients.place(x=460,y=150)
chkMilk=Checkbutton(variable=addMilk,text="Milk",font="Arial 14",fg="blue",bg="sky blue")
chkMilk.place(x=460,y=200)
chkMilk=Checkbutton(variable=addCream,text="Creamer",font="Arial 14",fg="blue",bg="sky blue")
chkMilk.place(x=460,y=240)
chkMilk=Checkbutton(variable=addSugar,text="Sugar",font="Arial 14",fg="blue",bg="sky blue")
chkMilk.place(x=460,y=280)
chkMilk=Checkbutton(variable=addWhiskey,text="Whiskey",font="Arial 14",fg="blue",bg="sky blue")
chkMilk.place(x=570,y=200)
chkMilk=Checkbutton(variable=addCinnamon,text="Cinnamon",font="Arial 14",fg="blue",bg="sky blue")
chkMilk.place(x=570,y=240)
chkMilk=Checkbutton(variable=addPepperment,text="Pepperment",font="Arial 14",fg="blue",bg="sky blue")
chkMilk.place(x=570,y=280)


frmOrder.mainloop()
    
