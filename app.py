# This runs the application
from phone_data import phones
from tmo_api import TmoData

class Run():
  def __init__(self, phones):
    self.phones = phones
    self.cart = []


  def menu(self):
    print 'Welcome to the T-Mobile Bill Calculator!'
    print ' '
    print '          -----------            '
    print 'How many phone lines do you need?'
    self.lines = input()
    self.menu_two()

  def menu_two(self):
      self.choose_phone()
      self.choose_plan()
      self.calc_bill()

  # we run this method until user selects all phones
  def choose_phone(self):
    for i in range(self.lines):
      print ' '
      print '%s/%s selected' % (len(self.cart), self.lines)
      print 'Which Phone would you like to add?'
      i = 1
      for f in self.phones:
        print "%s. %s($%s)" % (i, f.name, f.price)
        i += 1
      choice = input()
      self.find_phone(choice)

  # searches phones
  def find_phone(self, item):
    phone = self.phones[item -1]
    self.cart.append(phone)

  # gets data from our API, which is inside of global TmoData object
  def choose_plan(self):
    print 'Select your plan'
    TmoData.get_names(self.lines)
    choice = input()
    self.plan_cost = TmoData.get_price(choice)

  #adds plan price to price of each phone and prints result
  def calc_bill(self):
    self.price = 0
    for f in self.cart:
      self.price += f.calc_price()
    total = self.price + self.plan_cost
    print  "Your bill is $%s per month" % (total)

# gets phones from phone data file
app = Run(phones())

# runs the app
app.menu()
