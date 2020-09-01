class Router():
  def __init__(self, controller):
    self.controller = controller


  def run(self):
      self.controller.get_lines()
      self.controller.get_phones()
      self.controller.get_plan()
      self.controller.get_bill()

