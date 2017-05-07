#Kyle
class vehicle:
    ID = 0
    Color = ''
    Type = ''
    Condition = ''
    Year = ''
    Price = 0

    def __init__(self, ID, Color, Type, Condition, Year, Price):
        self.ID = ID
        self.Color = Color
        self.Type = Type
        self.Condition = Condition
        self.Year = Year
        self.Price = Price

    def getID(self):
        return self.ID

    def getColor(self):
        return self.Color

    def getType(self):
        return self.Type

    def getCondition(self):
        return self.Condition

    def getYear(self):
        return self.Year

    def getPrice(self):
        return self.Price
