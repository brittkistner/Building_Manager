from apartments import Apartment

class Building(object):
  building_list = {}

  def __init__(self,building_number, address,number_units, doorman = False):
    self.building_number = int(building_number) #think about incrementing building number
    self.address = address
    self.doorman = doorman
    self.number_units = int(number_units)
    self.apartment_dict = {} #one to many relationship think about appending to list from building
    Building.building_list[self.building_number] = self

  def __repr__(self):
    return '%s' % (self.address)

  def add_apartment(self, unit_number, rent, square_footage, number_bathrooms,renter=None, occupied=False): #creates a new apartment instance and adds to the apartment_dict
    new_apt = Apartment(self.building_number, unit_number, rent, square_footage, number_bathrooms,renter, occupied)
    self.apartment_dict[new_apt.unit_number] = new_apt
    return new_apt


##TESTS####

# print Building.building_list
# new_building = Building(1,2,3)

# print Building.building_list
# print Building.building_list[1]

# print new_building.apartment_dict

# new_building.add_apartment(0,1,200,1)

# print new_building.apartment_dict
# apt = new_building.apartment_dict[0]
# apt.unit_number
# apt.add_renter('suzie')

# print apt.renter
# print apt.occupied




