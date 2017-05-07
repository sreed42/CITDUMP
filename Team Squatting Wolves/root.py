from salesperson import *
from vehicle import *
from purchaseOrder import *
from customer import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import getpass


root = Tk()

##########################################################################################################
#Erick
#PURCHASE ORDER
def PO():
    pOrder = Tk()

    heading = Label(pOrder,text="Please fill out the following information"+"\n"+"regarding the purchase order:"+"\n")
    heading.grid(row=0,columnspan=3)

    #Choose Employee
    empLbl = Label(pOrder,text="Employee who made \n the sale:")
    empLbl.grid(row=1,column=0)
    empChoose = ttk.Combobox(pOrder, state = 'readonly')
    empChoose['values']=('Rick James','Jenny TuTone','Craig Michaels')
    empChoose.grid(row=1,column=1)

    #Empty Space
    empty = Label(pOrder,text="")
    empty.grid(row=2)

    #Choose Vehicle
    vLbl = Label(pOrder,text="ID of vehicle \n that was sold:")
    vLbl.grid(row=3,column=0)
    vChoose = ttk.Combobox(pOrder, state = 'readonly')
    vChoose['values']=('Vehicle 101','Vehicle 102','Vehicle 103','Vehicle 104','Vehicle 201','Vehicle 202','Vehicle 203','Vehicle 204','Vehicle 301','Vehicle 302')
    vChoose.grid(row=3,column=1)

    #Empty Space
    empty1 = Label(pOrder,text="")
    empty1.grid(row=4)

    #Customer Information
    custLbl = Label(pOrder,text="Customer Information:")
    custLbl.grid(row=5,column=0)

    #Empty Space
    empty2 = Label(pOrder,text="")
    empty2.grid(row=6)

    custFNameLbl = Label(pOrder,text="First Name:")
    custFNameLbl.grid(row=7,column=0)
    custFNameEntry = Entry(pOrder)
    custFNameEntry.grid(row=7,column=1)

    #Empty Space
    empty3 = Label(pOrder,text="")
    empty3.grid(row=8)

    custLNameLbl = Label(pOrder,text="Last Name:")
    custLNameLbl.grid(row=9,column=0)
    custLNameEntry = Entry(pOrder)
    custLNameEntry.grid(row=9,column=1)

    #Empty Space
    empty4 = Label(pOrder,text="")
    empty4.grid(row=10)

    custGendLbl = Label(pOrder,text="Gender:")
    custGendLbl.grid(row=11,column=0)
    custGendList = ttk.Combobox(pOrder, state = 'readonly')
    custGendList['values']=('Male','Female','Other')
    custGendList.grid(row=11,column=1)

    #Empty Space
    empty5 = Label(pOrder,text="")
    empty5.grid(row=12)

    custAgeLbl = Label(pOrder,text="Age:")
    custAgeLbl.grid(row=13,column=0)
    custAgeEntry = Entry(pOrder)
    custAgeEntry.grid(row=13,column=1)

    #Empty Space
    empty6 = Label(pOrder,text="")
    empty6.grid(row=14)

    custMarLbl = Label(pOrder,text="Marital Status:")
    custMarLbl.grid(row=15,column=0)
    custMarList = ttk.Combobox(pOrder, state = 'readonly')
    custMarList['values']=('Single','Married','Other')
    custMarList.grid(row=15,column=1)

    #Empty Space
    empty7 = Label(pOrder,text="")
    empty7.grid(row=16)

    #Button Functions
    def closeForm():
        pOrder.destroy()

    def finishPurOrder():
        # Salesperson Declaration
        employee = salesperson('','','','','')

        if empChoose.get() == 'Rick James':
            employee = salesperson("Rick James", 213, "Compact Cars", "Male", 48)
        elif empChoose.get() == 'Jenny TuTone':
            employee = salesperson("Jenny TuTone", 8675309, "Diesel Trucks", "Female", 15)
        elif empChoose.get() == 'Craig Michaels':
            employee = salesperson("Craig Michaels", 656, "Motorcycles", "Male", 25)

        # Vehicle Declaration
        car = vehicle('','','','','','')

        if vChoose.get() == 'Vehicle 101':
            car = vehicle(101, "White", "Sedan", "New", 2017, 22999)
        elif vChoose.get() == 'Vehicle 102':
            car = vehicle(102, "Yellow", "Coupe", "Used", 2007, 20197)
        elif vChoose.get() == 'Vehicle 103':
            car = vehicle(103, "Black", "Sedan", "Used", 2009, 15999)
        elif vChoose.get() == 'Vehicle 104':
            car = vehicle(104, "Green", "Coupe", "New", 2016, 25199)
        elif vChoose.get() == 'Vehicle 201':
            car = vehicle(201, "Silver", "Crew Cab", "New", 2017, 32999)
        elif vChoose.get() == 'Vehicle 202':
            car = vehicle(202, "Brown", "Regular Cab", "Used", 2011, 25999)
        elif vChoose.get() == 'Vehicle 203':
            car = vehicle(203, "Red", "Crew Cab", "Used", 2013, 26999)
        elif vChoose.get() == 'Vehicle 204':
            car = vehicle(204, "Blue", "Regular Cab", "New", 2017, 30999)
        elif vChoose.get() == 'Vehicle 301':
            car = vehicle(301, "Black", "Sport", "New", 2017, 19999)
        elif vChoose.get() == 'Vehicle 302':
            car = vehicle(302, "White", "Sport", "Used", 2012, 15987)

        # Customer Information Declaration
        custFirstName = custFNameEntry.get()
        custLastName = custLNameEntry.get()
        custGender = ""
        custAge = custAgeEntry.get()
        custMarital = ""

        if custGendList.get() == 'Male':
            custGender = "Male"
        elif custGendList.get() == 'Female':
            custGender = "Female"
        elif custGendList.get() == 'Other':
            custGender = "Other"

        if custMarList.get() == 'Single':
            custMarital = "Single"
        elif custMarList.get() == 'Married':
            custMarital = "Married"
        elif custMarList.get() == 'Other':
            custMarital = "Other"

        purchasingCust = customer(custFirstName, custLastName, custAge, custGender, custMarital)

        # Purchase Order Declaration
        purchaseOrderUp = purchaseOrder()
        purchaseOrderUp.insertCarInfo(car.getID(), car.getColor(), car.getType(), car.getCondition(), car.getPrice(),car.getYear())
        purchaseOrderUp.insertCustInfo(purchasingCust.getFirstName(), purchasingCust.getLastName(),purchasingCust.getGender(), purchasingCust.getAge(),purchasingCust.getMaritalStatus())
        purchaseOrderUp.insertEmpInfo(employee.getName(), employee.getID(), employee.getSpecial(), employee.getGender(),employee.getAge())

        username = getpass.getuser()


        text_file = open("C:/Users/" + str(username) + "/Desktop/Purchase Order.txt","w")
        text_file.write(str(purchaseOrderUp.printEmployeeInfo()) + "\n" + str(purchaseOrderUp.printVehicleInfo()) + "\n" + str(purchaseOrderUp.printCustomerInfo()))
        text_file.close()

        messagebox.showinfo("Congrats!", "Your purchase order can be found on your desktop.")
        pOrder.destroy()

#Kyle    
    #Buttons
    finishBut = Button(pOrder,text="Complete",command = lambda: finishPurOrder())
    finishBut.grid(row=17,column=0)

    closeBut = Button(pOrder,text="Close",command = closeForm)
    closeBut.grid(row=17,column=1)

    #Empty Space
    empty8 = Label(pOrder,text="")
    empty8.grid(row=18)

    pOrder.mainloop()
    #END PURCHASE ORDER
    ######################################################################################################################

def EI():
    def Emp1():
        messagebox.showinfo("Employee Information",
                            "Name: Rick James\nId#: 213\nSpecialty: Compact Cars\nGender: Male\nAge: 48")
    def Emp2():
        messagebox.showinfo("Employee Information",
                            "Name: Jenny TuTone\nId#: 8675309\nSpecialty: Diesel Trucks\nGender: Female\nAge: 15")
    def Emp3():
        messagebox.showinfo("Employee Information",
                            "Name: Craig Michaels\nId#: 656\nSpecialty: Motorcycles\nGender: Male\nAge: 25")

    def Exit():
        eInfo.destroy()
        # messagebox.showinfo("Close", "Goodbye")

    eInfo = Tk()

    label = Label(eInfo, text="Employees \n Choose an Employee for more information")
    label.grid(padx=50, pady=20)

    Q = Button(eInfo, text="Rick James", command=Emp1)
    Q.grid(padx=2, pady=2)

    R = Button(eInfo, text="Jenny Tutone", command=Emp2)
    R.grid(padx=2, pady=2)

    S = Button(eInfo, text="Craig Michaels", command=Emp3)
    S.grid(padx=2, pady=2)

    T = Button(eInfo, text="Close", command=Exit)
    T.grid(padx=2, pady=20)

def VI():
    def Choice1():
        messagebox.showinfo("Vehicle Information",
                            "Id#: 101\nColor: White\nType: Sedan\nCondition: New\nYear: 2017\nPrice: $22,999")

    def Choice2():
        messagebox.showinfo("Vehicle Information",
                            "ID#: 102\nColor: Yellow\nType: Coupe\nCondition: Used\nYear: 2007\nPrice: $20,197")

    def Choice3():
        messagebox.showinfo("Vehicle Information",
                            "ID#: 103\nColor: Black\nType: Sedan\nCondition: Used\nYear: 2009\nPrice: $15,999")

    def Choice4():
        messagebox.showinfo("Vehicle Information",
                            "ID#: 104\nColor: Green\nType: Coupe\nCondition: New\nYear: 2016\nPrice: $25,199")

    def Choice5():
        messagebox.showinfo("Vehicle Information",
                            "ID#: 201\nColor: Silver\nCab: Crew\nCondition: New\nYear: 2017\nPrice: $32,999")

    def Choice6():
        messagebox.showinfo("Vehicle Information",
                            "ID#: 202\nColor: Brown\nCab: Regular\nCondition: Used\nYear: 2011\nPrice: $25,999")

    def Choice7():
        messagebox.showinfo("Vehicle Information",
                            "ID#: 203\nColor: Red\nCab: Crew\nCondition: Used\nYear: 2013\nPrice: $26,999")

    def Choice8():
        messagebox.showinfo("Vehicle Information",
                            "ID#: 204\nColor: Blue\nCab: Regular\nCondition: New\nYear: 2017\nPrice: $30,999")

    def Choice9():
        messagebox.showinfo("Vehicle Information",
                            "ID#: 301\nColor: Black\nType: Sport\nCondition: New\nYear: 2017\nPrice: $19,999")

    def Choice10():
        messagebox.showinfo("Vehicle Information",
                            "ID#: 302\nColor: White\nType: Sport\nCondition: Used\nYear: 2012\nPrice: $15,987")

    def Close():
        vInfo.destroy()
        #messagebox.showinfo("Close", "Goodbye")

    vInfo = Tk()

    label = Label(vInfo, text="Vehicles \n Choose a Vehicle for more information")
    label.grid(padx=50, pady=20)

    A = Button(vInfo, text="ID# 101", command=Choice1)
    A.grid(padx=2, pady=2)

    B = Button(vInfo, text="ID# 102", command=Choice2)
    B.grid(padx=2, pady=2)

    C = Button(vInfo, text="ID# 103", command=Choice3)
    C.grid(padx=2, pady=2)

    D = Button(vInfo, text="ID# 104", command=Choice4)
    D.grid(padx=2, pady=2)

    E = Button(vInfo, text="ID# 201", command=Choice5)
    E.grid(padx=2, pady=2)

    F = Button(vInfo, text="ID# 202", command=Choice6)
    F.grid(padx=2, pady=2)

    G = Button(vInfo, text="ID# 203", command=Choice7)
    G.grid(padx=2, pady=2)

    H = Button(vInfo, text="ID# 204", command=Choice8)
    H.grid(padx=2, pady=2)

    I = Button(vInfo, text="ID# 301", command=Choice9)
    I.grid(padx=2, pady=2)

    J = Button(vInfo, text="ID# 302", command=Choice10)
    J.grid(padx=2, pady=2)

    K = Button(vInfo, text="Close", command=Close)
    K.grid(padx=2, pady=20)



def Leave():
    messagebox.showinfo("Close", "Good Bye")
    quit()

rootFrame = Frame(root)
rootFrame.grid()

label = Label(rootFrame, text = "Welcome to our Dealership \n Choose button 1 - 4 for more information")
label.grid(padx = 100, pady = 50)

Z = Button(rootFrame, text = "Purchase Order", command = PO)
Z.grid(padx = 2, pady = 2)

Y = Button(rootFrame, text = "Employee Information", command = EI)
Y.grid(padx = 2, pady = 2)

X = Button(rootFrame, text = "Car Information", command = VI)
X.grid(padx = 2, pady = 2)

W = Button(rootFrame, text = "Close", command = Leave)
W.grid(padx = 2, pady = 15)

root.mainloop()
