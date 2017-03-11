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