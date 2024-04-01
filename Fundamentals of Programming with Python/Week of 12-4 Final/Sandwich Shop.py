from tkinter import*
import random
import math

fltTax=0.0
fltSize=0.0
fltPrice=0.0
fltMNTax=0.1
fltTax=0.0
fltCurrency=0.0
fltAddOns=0.0
fltSubTotal=0.0
fltTotal=0.0

def Close():#Close Event
    frmSandwich.destroy() #Remove form from memory and close application
def Reset():#Reset Form Event
    entCustName.delete(0,END)#Clear Entry Widget
    lblCustCopy["text"]=""#Set Label Test Property to an empty string
    lblCustPay["text"]=""
    entCustName.focus()#Set Cursor Position
    lbxPay.selection_set(0)
def Process():
    strCustName=entCustName.get()
    strPaymentMethod=lbxPay.get(lbxPay.curselection())
    lblCustCopy["text"]="Thank You "+strCustName
    lblCustPay["text"]="Processed Payment : "+strPaymentMethod
    if Size.get()=="small":
        fltSize=5.00
    elif Size.get()=="medium":
        fltSize=10.00
    elif Size.get()=="large":
        fltSize=15.00
    else:
        fltSize=0.00

    fltAddOns=(addTurkey.get()+addChicken.get()+addSteak.get()+addCheese.get()+addOnion.get()+addPepper.get())*1.00

    fltCurrency="{:.2f}".format(fltSize)
    lblSizeCost["text"]="Size Cost = $"+str(fltCurrency)


    fltCurrency="{:.2f}".format(fltAddOns)
    lblAddOns["text"]="Meats and Veggies = $"+str(fltCurrency)

    fltPrice=fltSize+fltAddOns
    fltCurrency="{:.2f}".format(fltPrice)
    lblPrice["text"]="Price/Sandwich = $"+str(fltCurrency)

    fltTax=fltPrice*fltMNTax
    fltCurrency="{:.2f}".format(fltTax)
    lblMNTax["text"]="MN Tax 10% = $"+str(fltCurrency)
    
    fltSubTotal=fltPrice+fltTax
    fltCurrency="{:.2f}".format(fltSubTotal)
    lblTotal["text"]="Sandwich Total = $"+str(fltCurrency)
    
    

    

frmSandwich=Tk()

frmSandwich.configure(width=800,height=600,bg="magenta")
frmSandwich.title("Incredible Sandwiches - By Brian Sheehan")

lblCoName=Label(text="Incredible Sandwiches Order Form",font="Arial 20 bold",bg="magenta",fg="cyan")
lblCoName.place(x=200,y=10)

lblCustName=Label(text="Customer Name: ",font="Arial 14",bg="magenta",fg="cyan")
lblCustName.place(x=100,y=50)

lblOrderNumber=Label(text="Order # ",font="Arial 14 bold",bg="magenta",fg="cyan")
lblOrderNumber.place(x=20,y=370)
intRandom=random.randint(1000,2000)
lblRandom=Label(text=str(intRandom),font="Arial 14 bold",bg="magenta",fg="cyan")
lblRandom.place(x=70,y=370)

lblSizeCost=Label(text="Size Cost",font="Arial 14 bold",bg="magenta",fg="cyan")
lblSizeCost.place(x=20,y=390)

lblAddOns=Label(text="Meats and Veggies",font="Arial 14 bold",bg="magenta",fg="cyan")
lblAddOns.place(x=20,y=410)

lblPrice=Label(text="Price/Sandwich",font="Arial 14 bold",bg="magenta",fg="cyan")
lblPrice.place(x=20,y=430)

lblMNTax=Label(text="MN Tax 10%",font="Arial 14 bold",bg="magenta",fg="cyan")
lblMNTax.place(x=20,y=450)

lblTotal=Label(text="Total Cost",font="Arial 14 bold",bg="magenta",fg="cyan")
lblTotal.place(x=20,y=470)

entCustName=Entry(font="Arial 14",bg="white",fg="black",width=30)
entCustName.place(x=260,y=50)

lblCustCopy=Label(text="",font="Arial 14",bg="magenta",fg="yellow")
lblCustCopy.place(x=20,y=330)

lblCustPay=Label(text="",font="Arial 14",bg="magenta",fg="yellow")
lblCustPay.place(x=20,y=350)

btnClose=Button(text="Close",font="Arial 14",bg="sky blue",fg="navy",width=8,command=Close)
btnClose.place(x=650,y=500)

btnReset=Button(text="Reset",font="Arial 14",bg="sky blue",fg="navy",width=8,command=Reset)
btnReset.place(x=550,y=500)

btnProcess=Button(text="Process",font="Arial 14",bg="sky blue",fg="navy",width=8,command=Process)
btnProcess.place(x=450,y=500)

entCustName.focus()#Set Cursor Position

Size=StringVar()#Variable for Radiobuttons

lblSize=Label(text="Choose Size",font="Arial 16 bold",bg="magenta",fg="cyan")
lblSize.place(x=10,y=150)
radSize=Radiobutton(variable=Size,text="Small",value="small",fg="black",font="Arial 14 bold",bg="magenta")
radSize.place(x=20,y=200)
radSize=Radiobutton(variable=Size,text="Medium",value="medium",fg="black",font="Arial 14 bold",bg="magenta")
radSize.place(x=20,y=250)
radSize=Radiobutton(variable=Size,text="Large",value="large",fg="black",font="Arial 14 bold",bg="magenta")
radSize.place(x=20,y=300)
Size.set("small")

addTurkey=IntVar()#Variable for Checkbutton
addChicken=IntVar()
addSteak=IntVar()
addCheese=IntVar()
addOnion=IntVar()
addPepper=IntVar()

lblMeats=Label(text="Meats",font="Arial 16 bold",bg="magenta",fg="cyan")
lblMeats.place(x=230,y=150)
chkTurkey=Checkbutton(variable=addTurkey,text="Turkey",font="Arial 14",bg="magenta",fg="black")
chkTurkey.place(x=230,y=200)
chkChicken=Checkbutton(variable=addChicken,text="Chicken",font="Arial 14",bg="magenta",fg="black")
chkChicken.place(x=230,y=240)
chkSteak=Checkbutton(variable=addSteak,text="Steak",font="Arial 14",bg="magenta",fg="black")
chkSteak.place(x=230,y=280)

lblVeggies=Label(text="Veggies",font="Arial 16 bold",bg="magenta",fg="cyan")
lblVeggies.place(x=340,y=150)
chkCheese=Checkbutton(variable=addCheese,text="Cheese",font="Arial 14",bg="magenta",fg="black")
chkCheese.place(x=340,y=200)
chkOnion=Checkbutton(variable=addOnion,text="Onion",font="Arial 14",bg="magenta",fg="black")
chkOnion.place(x=340,y=240)
chkPepper=Checkbutton(variable=addPepper,text="Pepper",font="Arial 14",bg="magenta",fg="black")
chkPepper.place(x=340,y=280)

lblPay=Label(text="Payment",font="Arial 16 bold",bg="magenta",fg="cyan")
lblPay.place(x=530,y=150)
lbxPay=Listbox(fg="black",font="Arial 14")
lbxPay.place(x=530,y=200)
lbxPay.insert(0,"Cash")
lbxPay.insert(1,"Check")
lbxPay.insert(2,"Visa")
lbxPay.insert(3,"Mastercard")
lbxPay.insert(4,"American Express")
lbxPay.selection_set(0)



frmSandwich.mainloop()
    
