class Renter(object):
  renter_list ={}

  def __init__(self,name,apartment_number, building_number):
    self.name = name
    self.apartment_number = apartment_number
    self.building_number = building_number
    Renter.renter_list[self.name] = self

