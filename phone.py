# Phone Model
class Phone():
  def __init__(self, name, price):
    self.name = name
    self.price = price

  """
   We divide by 24 because that is the installment term of T-Mobile Phones
   We add 8 cents because for whatever reason an extra 8 cents is charged over
   the course of 24 months
  """
  def calc_price(self):
    price = self.price
    return round((price + .08) / 24, 2)




