#Richie Marier

class customer(object):  # creating customer class

    def __init__(self, custFirstName, custLastName, custGender, custAge, custMarital):  # initializes variables
        self.custFirstName = custFirstName
        self.custLastName = custLastName
        self.custGender = custGender
        self.custAge = custAge
        self.custMarital = custMarital

    def getFirstName(self):  # defines getFirstName method
        return self.custFirstName

    def getLastName(self):  # defines getLastName method
        return self.custLastName

    def getGender(self):  # defines getGender method
        return self.custGender

    def getAge(self):  # defines getAge method
        return self.custAge

    def getMaritalStatus(self):  # defines getMaritalStatus method
        return self.custMarital
