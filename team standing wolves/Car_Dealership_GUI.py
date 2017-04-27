from tkinter import *
from tkinter import messagebox

class salesperson(object):  # creating salesperson class

    def __init__(self, name, idnum, gender, empage):
        self.name = name
        self.idnum = idnum
        self.gender = gender
        self.empage = empage


class vehicle(object):  # creating vehicle class

    def __init__(self, id, color, type, condition, year, price):
        self.id = id
        self.color = color
        self.type = type
        self.condition = condition
        self.year = year
        self.price = price

# Employees
Employee1 = salesperson("Henry Ford", "6161903", "m", "114")  # variables for salesperson object
Employee2 = salesperson("Enzo Ferrari", "2181898", "m", "119")
Employee3 = salesperson("Bruce Mclaren", "8301937", "m", "32")

# Cars
Car1 = vehicle("Ford Fusion", "Red", "Sedan", "New", "2017", "22610")  # variables for vehicle object
Car2 = vehicle("Ford Mustang", "White", "Coupe", "New", "2017", "25185")
Car3 = vehicle("Ford Escape", "Black", "SUV", "New", "2017", "23750")
Car4 = vehicle("Ferrari California T", "Red", "Convertible", "New", "2016", "206473")
Car5 = vehicle("Ferrari 488 Spider", "Blue", "Convertible", "New", "2016", "272700")
Car6 = vehicle("McLaren 650S", "Grey", "Coupe", "New", "2016", "349500")
Car7 = vehicle("McLaren 675LT", "White", "Coupe", "New", "2016", "349500")

#========================================idk if the above is right ====================

class CarDealership(Frame):
    def __init__(self, root):
        Frame.__init__(self,root)
        #self.grid()
        self.Layout()
        self.options()
        #self.purchaseOrder()
    def Layout(self):
        self.root = root
        root.title("Car Dealership")
        root.geometry("800x800+0+0")

        self.Title=Frame(root, width = 1600, height = 50,bg = "blue",relief = SUNKEN)
        self.Title.grid(sticky=N)

        self.Options = Frame(root, width=500, height=600, bg="powder blue", relief=SUNKEN)
        self.Options.grid(sticky=W)

        self.Right = Frame(root, width=800, height=1000)
        self.Right.grid(sticky=E)

        self.FinalFrame = Frame(root,bg="red")
        self.FinalFrame.grid(sticky=N)

        self.lblTitle = Label(self.Title, font=('arial',50, 'bold'),text="Car Dealership")
        self.lblTitle.grid(row=0,column=0)

    def options(self):
        self.lblOptions=Label(self.Options, text="What would you like to do?")
        self.lblOptions.grid()
        self.btn1 = Button(self.Options, text="1. Create Purchase Order",command=self.purchaseOrder)
        self.btn2 = Button(self.Options, text="2. Car Info",command=self.carInfo)
        self.btn3 = Button(self.Options, text="3. Employee Info",command=self.empInfo)
        self.btn4 = Button(self.Options, text="4. Exit", command=quit)
        self.btn1.grid(row=2, column=0,sticky=W)
        self.btn2.grid(row=3, column=0,sticky=W)
        self.btn3.grid(row=4, column=0,sticky=W)
        self.btn4.grid(row=5, column=0,sticky=W)

    def empInfo(self):
        self.Options.destroy()
        self.empnumber=StringVar()
        Label(self.Right, text = "EMPLOYEE INFO", font=(30)).grid()
        Label(self.Right, text = "What employee's info would you like to see?").grid(row=1,column=0)
        text=Text(self.Right, height=3)
        text.insert(INSERT,"1. Henry Ford"
                           "\n2. Enzo Ferrari"
                           "\n3. Bruce McLaren")
        text.grid(row=2,column=0)
        Entry(self.Right, textvariable=self.empnumber).grid(row=3,column=0)
        Button(self.Right, text="SUBMIT", command=self.displayEmpl).grid(row=4, column=0)

    def displayEmpl(self):
        text=Text(self.FinalFrame)
        self.empnumber.get()
        if self.empnumber.get()in["Henry","henry","1"]:
            text.insert(INSERT,"\n\nSalesperson Info:\n"
                "Name: " + str(Employee1.name)+ "\n"
                "ID: " + str(Employee1.idnum)+ "\n"
                "Gender: " + str(Employee1.gender)+ "\n"
                "Age: " + str(Employee1.empage)+ "\n")
        elif self.empnumber.get() in ["Enzo","enzo","2"]:
            text.insert(INSERT,"\n\nInformation: \nEmployee Name: "
                + Employee2.name + "\nEmployee ID: "
                + Employee2.idnum + "\nEmployee Gender: "
                + Employee2.gender + "\nEmployee Age: "
                + Employee2.empage + "\n")
        elif self.empnumber.get() in ["Bruce","bruce","3"]:
            text.insert(INSERT,"\n\nInformation: \nEmployee Name: "
                + Employee3.name + "\nEmployee ID: "
                + Employee3.idnum + "\nEmployee Gender: "
                + Employee3.gender + "\nEmployee Age: "
                + Employee3.empage + "\n")
        else:
            messagebox.showwarning("Error","Please enter a correct employee name")
            self.FinalFrame.destroy()
            self.Title.destroy()
            self.Right.destroy()
            CarDealership(root)
        text.grid(row=0, column=0)
    def carInfo(self):
        self.Options.destroy()
        self.carnumber=StringVar()
        Label(self.Right, text="CAR INFO",font=(30)).grid()
        Label(self.Right, text="What car would you like to see?(Enter 1 - 7)").grid(row=1,column=0)
        text=Text(self.Right, height = 7)
        text.insert(INSERT,"1. Ford Fusion"
                           "\n2. Ford Mustang"
                           "\n3. Ford Escape"
                           "\n4. Ferrari California T"
                           "\n5. Ferrari 488 Spider"
                           "\n6. McLaren 650S"
                           "\n7. McLaren 675LT")
        text.grid(row=2,column=0)
        Entry(self.Right, textvariable=self.carnumber).grid(row=3,column=0)
        Button(self.Right, text="SUBMIT",command=self.displayCar).grid(row=4, column=0)

    def displayCar(self):
        text=Text(self.FinalFrame)
        self.carnumber.get()
        if self.carnumber.get() == "1":
            text.insert(INSERT, "\nVehicle Information:\n"
                        "Car: " + Car1.id + "\n"
                        "Color: " + Car1.color + "\n"
                        "Type: " + Car1.type + "\n"
                        "Condition: " + Car1.condition + "\n"
                        "Price: " + Car1.price + "\n"
                        "Year: " + Car1.year + "\n")
        elif self.carnumber.get() == "2":
            text.insert(INSERT, "\nInformation: \nCar: "
                        + Car2.id + "\nColor: "
                        + Car2.color + "\nType: "
                        + Car2.type + "\nCondition: "
                        + Car2.condition + "\nYear: "
                        + Car2.year + "\nPrice: "
                        + Car2.price + "\n")
        elif self.carnumber.get() == "3":
            text.insert(INSERT, "\nInformation: \nCar: "
                        + Car3.id + "\nColor: "
                        + Car3.color + "\nType: "
                        + Car3.type + "\nCondition: "
                        + Car3.condition + "\nYear: "
                        + Car3.year + "\nPrice: "
                        + Car3.price + "\n")
        elif self.carnumber.get() == "4":
            text.insert(INSERT, "\nInformation: \nCar: "
                        + Car4.id + "\nColor: "
                        + Car4.color + "\nType: "
                        + Car4.type + "\nCondition: "
                        + Car4.condition + "\nYear: "
                        + Car4.year + "\nPrice: "
                        + Car4.price + "\n")
        elif self.carnumber.get() == "5":
            text.insert(INSERT, "\nInformation: \nCar: "
                        + Car5.id + "\nColor: "
                        + Car5.color + "\nType: "
                        + Car5.type + "\nCondition: "
                        + Car5.condition + "\nYear: "
                        + Car5.year + "\nPrice: "
                        + Car5.price + "\n")
        elif self.carnumber.get() == "6":
            text.insert(INSERT, "\nInformation: \nCar: "
                        + Car6.id + "\nColor: "
                        + Car6.color + "\nType: "
                        + Car6.type + "\nCondition: "
                        + Car6.condition + "\nYear: "
                        + Car6.year + "\nPrice: "
                        + Car6.price + "\n")
        elif self.carnumber.get() == "7":
            text.insert(INSERT, "\nInformation: \nCar: "
                        + Car7.id + "\nColor: "
                        + Car7.color + "\nType: "
                        + Car7.type + "\nCondition: "
                        + Car7.condition + "\nYear: "
                        + Car7.year + "\nPrice: "
                        + Car7.price + "\n")
        else:
            messagebox.showwarning("Error", "Please enter a number between 1 and 7")
            self.FinalFrame.destroy()
            self.Title.destroy()
            self.Right.destroy()
            CarDealership(root)
        text.grid(row=0, column=0)

    def purchaseOrder(self):
        self.Options.destroy()

        # PURCHASE ORDER

        self.Fname = StringVar()
        self.Lname = StringVar()
        self.Age = StringVar()
        self.Gender = StringVar()
        self.MS = StringVar()
        self.Empl = StringVar()
        self.Car = StringVar()

        Label(self.Right, text="PURCHASE ORDER", font=(30)).grid(row=0, column=0)
        Label(self.Right, text="Customer First Name: ").grid(row=1, column=0)
        Label(self.Right, text="Customer Last Name: ").grid(row=2, column=0)
        Label(self.Right, text="Customer Age: ").grid(row=3, column=0)
        Label(self.Right, text="Customer Gender: ").grid(row=4, column=0)
        Entry(self.Right, textvariable =self.Fname).grid(row=1, column=1)
        Entry(self.Right, textvariable =self.Lname).grid(row=2, column=1)
        Entry(self.Right, textvariable =self.Age).grid(row=3, column=1)
        Entry(self.Right, textvariable =self.Gender).grid(row=4, column=1)
        Label(self.Right, text="Married, Single, N/A").grid(row=5, column=0)
        Entry(self.Right, textvariable=self.MS).grid(row=5, column=1)
        Label(self.Right, text="Which Employee did you see? ").grid(row=7, column=1)
        Label(self.Right, text="Henry\nEnzo\nBruce").grid(row=8, column=1)
        Entry(self.Right,textvariable=self.Empl).grid(row=9, column=1)
        Label(self.Right, text="What car did you look at?\n1. Ford Fusion\n2. Ford Mustang\n"
                                    "3. Ford Escape\n4. Ferrari California T\n5. Ferrari 488 Spider\n"
                                    "6. McLaren 650S\n7. McLaren 675LT").grid(row=10, column=1)
        Entry(self.Right, textvariable=self.Car).grid(row=11, column=1)
        Button(self.Right, text="SUBMIT",command=self.displayPO).grid(row=12, column=1)

    def displayPO(self):
        self.Right.destroy()

        text=Text(self.FinalFrame, height=20)
        text.insert(INSERT,"Customer First Name: ")
        text.insert(INSERT, self.Fname.get())
        text.insert(INSERT,"\nCustomer Last Name: ")
        text.insert(INSERT, self.Lname.get())
        text.insert(INSERT,"\nCustomer Age: ")
        text.insert(INSERT, self.Age.get())
        text.insert(INSERT,"\nCustomer Gender: ")
        text.insert(INSERT, self.Gender.get())
        text.insert(INSERT,"\nCustomer Marital Status: ")
        text.insert(INSERT, self.MS.get())
        self.Empl.get()
        if self.Empl.get()in["Henry","henry","1"]:
            text.insert(INSERT,"\n\nSalesperson Info:\n"
                "Name: " + str(Employee1.name)+ "\n"
                "ID: " + str(Employee1.idnum)+ "\n"
                "Gender: " + str(Employee1.gender)+ "\n"
                "Age: " + str(Employee1.empage)+ "\n")
        elif self.Empl.get() in ["Enzo","enzo","2"]:
            text.insert(INSERT,"\n\nInformation: \nEmployee Name: "
                + Employee2.name + "\nEmployee ID: "
                + Employee2.idnum + "\nEmployee Gender: "
                + Employee2.gender + "\nEmployee Age: "
                + Employee2.empage + "\n")
        elif self.Empl.get()  in ["Bruce","bruce","3"]:
            text.insert(INSERT,"\n\nInformation: \nEmployee Name: "
                + Employee3.name + "\nEmployee ID: "
                + Employee3.idnum + "\nEmployee Gender: "
                + Employee3.gender + "\nEmployee Age: "
                + Employee3.empage + "\n")
        else:
            messagebox.showwarning("Error","Please enter a correct employee name")
            self.FinalFrame.destroy()
            self.Title.destroy()
            CarDealership(root)
        self.Car.get()
        if self.Car.get()=="1":
            text.insert(INSERT,"\nVehicle Information:\n"
                "Car: " + Car1.id+ "\n"
                "Color: " + Car1.color+"\n"
                "Type: " + Car1.type+ "\n"
                "Condition: " + Car1.condition+ "\n"
                "Price: " + Car1.price+ "\n"
                "Year: " + Car1.year+ "\n")
        elif self.Car.get() == "2":
            text.insert(INSERT,"\nInformation: \nCar: "
                + Car2.id+ "\nColor: "
                + Car2.color + "\nType: "
                + Car2.type + "\nCondition: "
                + Car2.condition + "\nYear: "
                + Car2.year + "\nPrice: "
                + Car2.price + "\n")
        elif self.Car.get() == "3":
            text.insert(INSERT,"\nInformation: \nCar: "
                + Car3.id + "\nColor: "
                + Car3.color + "\nType: "
                + Car3.type + "\nCondition: "
                + Car3.condition + "\nYear: "
                + Car3.year + "\nPrice: "
                + Car3.price + "\n")
        elif self.Car.get() == "4":
            text.insert(INSERT,"\nInformation: \nCar: "
                + Car4.id + "\nColor: "
                + Car4.color + "\nType: "
                + Car4.type + "\nCondition: "
                + Car4.condition + "\nYear: "
                + Car4.year + "\nPrice: "
                + Car4.price + "\n")
        elif self.Car.get() == "5":
            text.insert(INSERT,"\nInformation: \nCar: "
                + Car5.id + "\nColor: "
                + Car5.color + "\nType: "
                + Car5.type + "\nCondition: "
                + Car5.condition + "\nYear: "
                + Car5.year + "\nPrice: "
                + Car5.price + "\n")
        elif self.Car.get() == "6":
            text.insert(INSERT,"\nInformation: \nCar: "
                + Car6.id + "\nColor: "
                + Car6.color + "\nType: "
                + Car6.type + "\nCondition: "
                + Car6.condition + "\nYear: "
                + Car6.year + "\nPrice: "
                + Car6.price + "\n")
        elif self.Car.get() == "7":
            text.insert(INSERT,"\nInformation: \nCar: "
                + Car7.id + "\nColor: "
                + Car7.color + "\nType: "
                + Car7.type + "\nCondition: "
                + Car7.condition + "\nYear: "
                + Car7.year + "\nPrice: "
                + Car7.price + "\n")
        else:
            messagebox.showwarning("Error","Please enter a number between 1 and 7")
            self.FinalFrame.destroy()
            self.Title.destroy()
            CarDealership(root)
        text.grid(row=0,column=0)


root=Tk()
gui=CarDealership(root)
root.mainloop()