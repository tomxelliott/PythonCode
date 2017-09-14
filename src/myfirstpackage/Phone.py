class Phone:
  "This class provides basic functionality to track details of our phones..."
  new = True
  
  def __init__(self, number, model):
    self.number = number
    self.model = model
    self.new = False
  
  def set_number(num):
    self.number = num
