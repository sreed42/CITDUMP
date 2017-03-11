# Richie and Jared

#Jared
class salesperson(object):  # creating salesperson class

    def __init__(self, name, idnum, gender, age):
        self.name = name
        self.idnum = idnum
        self.gender = gender
        self.age = age

    def getname(self):
        return self.name

    def getID(self):
        return self.idnum

    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age

#Jared
class customer(object):  # creating customer class

    def __init__(self, custFirstName, custLastName, custGender, custAge, custMarital):
        self.custFirstName = custFirstName
        self.custLastName = custLastName
        self.custGender = custGender
        self.custAge = custAge
        self.custMarital = custMarital

    def getFirstName(self):
        return self.custFirstName

    def getLastName(self):
        return self.custLastName

    def getGender(self):
        return self.custGender

    def getAge(self):
        return self.custAge

    def getMaritalStatus(self):
        return self.custMarital

#Richie
class vehicle(object):  # creating vehicle class

    def __init__(self, id, color, type, condition, year, price):
        self.id = id
        self.color = color
        self.type = type
        self.condition = condition
        self.year = year
        self.price = price

    def getID(self):
        return self.id

    def getColor(self):
        return self.color

    def getType(self):
        return self.type

    def getCondition(self):
        return self.condition

    def getYear(self):
        return self.year

    def getPrice(self):
        return self.price

#Richie
class purchaseOrder(object):  # creating purchaseOrder class

    def insertEmpInfo(self, empName, empID, empGender, empAge):  # defines insertEmpInfo method
        self.empName = empName
        self.empID = empID
        self.empGender = empGender
        self.empAge = empAge

    def insertCustInfo(self, custFname, custLname, custgender, custMarital, custAge):  # defines insertCustInfo method
        self.custFname = custFname
        self.custLname = custLname
        self.custgender = custgender
        self.custMarital = custMarital
        self.custAge = custAge

    def insertCarInfo(self, carID, carColor, carType, carCondition, carYear, carPrice):  # defines insertVehicleInfo method
        self.carID = carID
        self.carColor = carColor
        self.carType = carType
        self.carCondition = carCondition
        self.carYear = carYear
        self.carPrice = carPrice


    def printEmployeeInfo(self):  # defines printEmployeeInfo method
        print("Salesperson Info:\n"
              "Name: " + str(self.empName), "\n"
              "ID: " + str(self.empID), "\n"
              "Gender: " + str(self.empGender), "\n"
              "Age: " + str(self.empAge), "\n")

    def printCustomerInfo(self):  # defines printCustomerInfo method
        print("Customer Info:\n"
              "First Name: " + str(self.custFname), "\n"
              "Last Name: " + str(self.custLname), "\n"
              "Gender: " + str(self.custgender), "\n"
              "Marital Status: " + str(self.custMarital),"\n"
              "Age: " + str(self.custAge), "\n")

    def printVehicleInfo(self):  # defines printVehicleInfo method
        print("Vehicle Information:\n"
              "ID: " + str(self.carID), "\n"
              "Color: " + str(self.carColor), "\n"
              "Type: " + str(self.carType), "\n"
              "Condition: " + str(self.carCondition), "\n"
              "Price: " + str(self.carPrice), "\n"
              "Year: " + str(self.carYear), "\n")

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

# program
a = 1
while a == 1:  # program while loop
    b = 1
    while b == 1:  # if statement while loop
        print("\nWhat would you like to do?\n"
              "1. Look up employee info.\n"
              "2. Look up car info.\n"
              "3. Create Purchase Order\n"
              "4. exit")  # choices
        choice2 = input()
        try:
            choice2 = int(choice2)  # checking input
            b = 0
        except ValueError:
            print("Please enter a number 1 through 4.")
    if choice2 == 1:  # looking up employee info
        saleschoice = 1
        while saleschoice == 1:  # while for employee input
            salesinput = input("\nWhich Employee would you like to see?\n"
                  "1. " + Employee1.name + "\n"
                  "2. " + Employee2.name + "\n"
                  "3. " + Employee3.name + "\n")  # employee choices
            try:
                salesinput = int(salesinput)  # checking input
            except ValueError:
                pass
            if salesinput == 1:
                print("\nInformation: \nEmployee Name: "
                      + Employee1.name + "\nEmployee ID: "
                      + Employee1.idnum + "\nEmployee Gender: "
                      + Employee1.gender + "\nEmployee Age: "
                      + Employee1.age + "\n")
                saleschoice = 0
            elif salesinput == 2:
                print("\nInformation: \nEmployee Name: "
                      + Employee2.name + "\nEmployee ID: "
                      + Employee2.idnum + "\nEmployee Gender: "
                      + Employee2.gender + "\nEmployee Age: "
                      + Employee2.age + "\n")
                saleschoice = 0
            elif salesinput == 3:
                print("\nInformation: \nEmployee Name: "
                      + Employee3.name + "\nEmployee ID: "
                      + Employee3.idnum + "\nEmployee Gender: "
                      + Employee3.gender + "\nEmployee Age: "
                      + Employee3.age + "\n")
                saleschoice = 0
            else:
                print("\nPlease enter a number between 1 and 3")
    elif choice2 == 2:  # looking up car info
        carchoice = 1
        while carchoice == 1:
            carinput = input("\nWhich vehicle's information would you like to see?\n"
                             "1. " + Car1.id + "\n"
                             "2. " + Car2.id + "\n"
                             "3. " + Car3.id + "\n"
                             "4. " + Car4.id + "\n"
                             "5. " + Car5.id + "\n"
                             "6. " + Car6.id + "\n"
                             "7. " + Car7.id + "\n")  # car choices
            try:
                carinput = int(carinput)  # checking input
            except ValueError:
                pass
            if carinput == 1:
                print("\nInformation: \nCar: "
                      + Car1.id + "\nColor: "
                      + Car1.color + "\nType: "
                      + Car1.type + "\nCondition: "
                      + Car1.condition + "\nYear: "
                      + Car1.year + "\nPrice: "
                      + Car1.price + "\n")
                carchoice = 0
            elif carinput == 2:
                print("\nInformation: \nCar: "
                      + Car2.id + "\nColor: "
                      + Car2.color + "\nType: "
                      + Car2.type + "\nCondition: "
                      + Car2.condition + "\nYear: "
                      + Car2.year + "\nPrice: "
                      + Car2.price + "\n")
                carchoice = 0
            elif carinput == 3:
                print("\nInformation: \nCar: "
                      + Car3.id + "\nColor: "
                      + Car3.color + "\nType: "
                      + Car3.type + "\nCondition: "
                      + Car3.condition + "\nYear: "
                      + Car3.year + "\nPrice: "
                      + Car3.price + "\n")
                carchoice = 0
            elif carinput == 4:
                print("\nInformation: \nCar: "
                      + Car4.id + "\nColor: "
                      + Car4.color + "\nType: "
                      + Car4.type + "\nCondition: "
                      + Car4.condition + "\nYear: "
                      + Car4.year + "\nPrice: "
                      + Car4.price + "\n")
                carchoice = 0
            elif carinput == 5:
                print("\nInformation: \nCar: "
                      + Car5.id + "\nColor: "
                      + Car5.color + "\nType: "
                      + Car5.type + "\nCondition: "
                      + Car5.condition + "\nYear: "
                      + Car5.year + "\nPrice: "
                      + Car5.price + "\n")
                carchoice = 0
            elif carinput == 6:
                print("\nInformation: \nCar: "
                      + Car6.id + "\nColor: "
                      + Car6.color + "\nType: "
                      + Car6.type + "\nCondition: "
                      + Car6.condition + "\nYear: "
                      + Car6.year + "\nPrice: "
                      + Car6.price + "\n")
                carchoice = 0
            elif carinput == 7:
                print("\nInformation: \nCar: "
                      + Car7.id + "\nColor: "
                      + Car7.color + "\nType: "
                      + Car7.type + "\nCondition: "
                      + Car7.condition + "\nYear: "
                      + Car7.year + "\nPrice: "
                      + Car7.price + "\n")
                carchoice = 0
            else:
                print("Please enter a number between 1 and 7")
    elif choice2 == 3:  # creating purchase order
        customerFirstName = input("Customer's first name: ")
        customerLastName = input("Customer's last name: ")

        agechoice = 1
        while agechoice == 1:  # while loop for age input
            customerAge = input("Customer's Age: ")
            try:
                customerAge = int(customerAge)  # checking input
                agechoice = 0
            except ValueError:
                print("Please use a number.")

        genderchoice = 1
        while genderchoice == 1:  # while loop for gender input
            customerGender = input("Customer's Gender: ")
            if customerGender in ['male','m']:
                customerGender = 'male'
                genderchoice = 0
            elif customerGender in ['female', 'f']:
                customerGender = 'female'
                genderchoice = 0
            else:
                print("Please enter the correct input (male, m, female, f)")
        maritalchoice = 1
        while maritalchoice == 1:  # while loop for marital status input
            customerMarital = input("Customer's Marital Status (Married, Single, n/a): ")
            if customerMarital in ['married','Married','m','M']:
                customerMarital = "Married"
                maritalchoice = 0
            elif customerMarital in ['single', 'Single', 's', 'S']:
                customerMarital = "Single"
                maritalchoice = 0
            elif customerMarital in ['n/a','N/a','n/A','N/A']:
                customerMarital = "N/A"
                maritalchoice = 0
            else:
                print("Please enter a valid marital status. (Married, Single, or n/a)")

        newCustomer = customer(customerFirstName, customerLastName, customerAge, customerGender, customerMarital)
        purchaseorder=purchaseOrder()
        purchaseorder.insertCustInfo(newCustomer.custFirstName, newCustomer.custLastName, newCustomer.custAge,
                                     newCustomer.custGender, newCustomer.custMarital)

        employeechoice = 1
        while employeechoice == 1:  # while loop for employee input
            employeeinput = input("\nWhich employee did you see?\n"
                                  "1. " + Employee1.name + "\n"
                                  "2. " + Employee2.name + "\n"
                                  "3. " + Employee3.name + "\n")
            try:
                employeeinput = int(employeeinput)  # checking input
            except ValueError:
                pass
            if employeeinput == 1:
                purchaseorder.insertEmpInfo(Employee1.name, Employee1.idnum, Employee1.gender, Employee1.age)
                employeechoice = 0
            elif employeeinput == 2:
                purchaseorder.insertEmpInfo(Employee2.name, Employee2.idnum, Employee2.gender, Employee2.age)
                employeechoice = 0
            elif employeeinput == 3:
                purchaseorder.insertEmpInfo(Employee3.name, Employee3.idnum, Employee3.gender, Employee3.age)
                employeechoice = 0
            else:
                print("Please pick a number between 1 and 3.")

        vehiclechoice = 1
        while vehiclechoice == 1:  # while loop for vehicle input
            vehicleinput = input("\nWhich car did you look at?\n"
                                 "1. " + Car1.id + "\n"
                                 "2. " + Car2.id + "\n"
                                 "3. " + Car3.id + "\n"
                                 "4. " + Car4.id + "\n"
                                 "5. " + Car5.id + "\n"
                                 "6. " + Car6.id + "\n"
                                 "7. " + Car7.id + "\n")
            try:
                vehicleinput = int(vehicleinput)  # checking input
            except ValueError:
                pass
            if vehicleinput == 1:
                purchaseorder.insertCarInfo(Car1.id, Car1.color, Car1.type, Car1.condition, Car1.year, Car1.price)
                vehiclechoice = 0
            elif vehicleinput == 2:
                purchaseorder.insertCarInfo(Car2.id, Car2.color, Car2.type, Car2.condition, Car2.year, Car2.price)
                vehiclechoice = 0
            elif vehicleinput == 3:
                purchaseorder.insertCarInfo(Car3.id, Car3.color, Car3.type, Car3.condition, Car3.year, Car3.price)
                vehiclechoice = 0
            elif vehicleinput == 4:
                purchaseorder.insertCarInfo(Car4.id, Car4.color, Car4.type, Car4.condition, Car4.year, Car4.price)
                vehiclechoice = 0
            elif vehicleinput == 5:
                purchaseorder.insertCarInfo(Car5.id, Car5.color, Car5.type, Car5.condition, Car5.year, Car5.price)
                vehiclechoice = 0
            elif vehicleinput == 6:
                purchaseorder.insertCarInfo(Car6.id, Car6.color, Car6.type, Car6.condition, Car6.year, Car6.price)
                vehiclechoice = 0
            elif vehicleinput == 7:
                purchaseorder.insertCarInfo(Car7.id, Car7.color, Car7.type, Car7.condition, Car7.year, Car7.price)
                vehiclechoice = 0
            else:
                print("Please enter a valid number between 1 and 7.")

        print("\nPurchase Order:\n")
        purchaseorder.printCustomerInfo()  # printing customer info
        purchaseorder.printEmployeeInfo()  # printing employee info
        purchaseorder.printVehicleInfo()  # printing vehicle info
        input("Press Enter to Continue\n")
    elif choice2 == 4:  # exiting program
        a = 0
    else:
        print("Please enter a valid number between 1 and 4.")
