class vehicle():
  def __init__(self,type):
    self.type = type

class automobile(vehicle):
  def __init__(self,type):
    super().__init__(type)
    self.year = ""
    self.make = ""
    self.model = ""
    self.doors = ""
    self.roof = ""

  def user_input(self):
    self.year = input("Enter the year:")
    self.make = input("Enter the make:")
    self.model = input("Enter the model:")
    self.doors = input("Enter the doors:")
    self.roof = input("Enter the roof:")

  def display_values(self):
    print("\n")
    print(f"Vehicle type:{self.type}")
    print(f"Year:{self.year}")
    print(f"Make:{self.make}")
    print(f"Model:{self.model}")
    print(f"Number of doors:{self.doors}")
    print(f"Type of rRoof:{self.roof}")

vehicle_type = input("Enter the type:")

def vehicle_info():
  car = automobile(vehicle_type)
  car.user_input()
  car.display_values()

vehicle_info()