class Property():
    def __init__(self, description="I am a property"):
        self.description = description

    def createProperty(self):
        self.property_name = input('What is the name of the property that you would like to add?')
        self.income = float(input('What is the income for this property?'))
        self.expenses = float(input('What are the expenses for this property?'))
        self.initial_investment = float(input('What is the initial investment for this property?'))
        self.roi = (self.income - self.expenses) / self.initial_investment * 100

        print(self.property_name, 'has been added to your portfolio.')
        print('Here is your ROI on', self.property_name, ' : ', self.roi)

class User():
    def __init__(self, username):
        self.username = username
        self.portfolio = {}

    def createUser(self):
        self.username = input('Please choose a username for yourself.')
        return self.username

    def addProperty(self):
        myProperty = Property()
        myProperty.createProperty()
        self.portfolio[myProperty.property_name] = myProperty
        print('This Property has been added to your portfolio', self.portfolio)

    def selectProperty(self):
        print('Here is your current portfolio:', self.portfolio)
        response = input('Type in the name of the property you would like to view.')
        print('Here is the roi of the property you have selected:',self.portfolio[response].roi)

    def delProperty(self, theProperty):
        del self.portfolio[theProperty]
    
    # def switch(self):
    #     self.username = input("Please select a user: ", Run.usersList)

def run():
    running = True
    myUser = User('Patrick')
    while running == True:
        response = input('What would you like to do? [1] Add property, [2] View property, [3] Modify property, or [4] quit.')
        if response == '1':
            myUser.addProperty()
        elif response == '2':
            myUser.selectProperty()
        elif response == '3':
            propertyChoice = input('What property would you like to modify?')
            print(f'Deleting {propertyChoice} from your portfolio.')
            myUser.delProperty(propertyChoice)
            myUser.addProperty()
            print(f'{propertyChoice} was successfully modified.')
        elif response == '4':
            running = False
            break
run()