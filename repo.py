class Repo():
  def __init__(self, phones):
    self.cart = []
    self.phones = phones

# searches phones
  def find_phone(self, item):
    phone = self.phones[item -1]
    self.cart.append(phone)

  def set_plan(self, plan):
    self.plan = plan

  def calc_bill(self):
    self.price = 0
    for f in self.cart:
      self.price += f.calc_price()
    total = self.price + self.plan
    return total
