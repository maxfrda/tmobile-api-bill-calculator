from tmo_api import TmoData

class Controller():
  def __init__(self, view, repo):
    self.view = view
    self.repo = repo

  def get_lines(self):
    self.lines = self.view.welcome()

  def get_phones(self):
    for i in range(self.lines):
      self.view.show_count(self.lines, self.repo.cart)
      choice = self.view.show_phones(self.repo.phones)
      self.repo.find_phone(choice)

  def get_plan(self):
    TmoData.get_names(self.lines)
    choice = self.view.choose_plan()
    price = TmoData.get_price(choice)
    self.repo.set_plan(price)

  def get_bill(self):
    total = self.repo.calc_bill()
    self.view.show_bill(total)
