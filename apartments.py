from renters import *

class Apartment(object):
  def __init__(self,building_number, unit_number, rent, square_footage, number_bathrooms,renter=None, occupied = False):
    self.building_number = int(building_number)
    self.unit_number = int(unit_number)
    self.rent = int(rent)
    self.square_footage = int(square_footage)
    self.number_bathrooms = int(number_bathrooms)
    self.renter = renter
    self.occupied = occupied

  def __repr__(self):
    return '%s' % (self.unit_number)


  def check_occupied(self): #checks whether an apartment is occupied by a renter
    if self.occupied == True:
      return True
    else:
      return False

  def change_ocupancy(self): #changes the occupancy of an apartment
    if self.occupied == False:
      self.occupied = True
    else:
      self.occupied = False

  def add_renter(self,name): #creates a new renter instance, first checks if occupied and if not will change the occupancy of the apt
    statement = self.check_occupied()
    if statement == True:
      return #apartment is full
    else:
      renter = Renter(name,self.unit_number, self.building_number)
      name = renter.name
      self.renter = name
      self.change_ocupancy()
      return renter


##Tests##
# new_apt = Apartment(1,2,3,200,1)
# print new_apt.renter
# print new_apt.occupied
# print new_apt.check_occupied()
# new_apt.add_renter('suzie')
# print new_apt.renter
# print new_apt.occupied


