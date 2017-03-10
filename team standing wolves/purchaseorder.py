#Richie Marier

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
