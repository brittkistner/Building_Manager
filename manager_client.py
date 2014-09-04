import sys
from apartments import Apartment
from building import Building
from renters import Renter


user = raw_input("What's your username? ")

print "\nHello %s.\n" % (user)

def print_menu(): #prints terminal menu
  while True:
    to_do = raw_input("What do you want to do?\n--Add (N)ew building\n--Review the (B)uilding information\n--add new (A)partment\n--(L)ook up apartment information\n--add new (R)enter\n--check apartment (O)ccupancy\n--(Q)uit\n ").lower()
    if to_do == 'n': #adds new building
      number = int(raw_input("\nWhat is the building number? "))
      address = raw_input("\nWhat is the building address? ")
      doorman = raw_input("\nDoes the building have a doorman? (T) or (F)") #work on, convert to boolean
      number_units = int(raw_input("\nHow many units does the building have?"))

      building = Building(number,address,number_units, doorman)

      print "\nBuilding Number: %s Added\n" % (building.building_number)
    elif to_do == 'b': #asks for building information
      building_number = int(raw_input("\nWhich building number do you want information on? "))
      building = Building.building_list[building_number]
      building_info = raw_input("\nWhat do you want to look up?\n--(A)ddress\n--(D)oorman\n--(N)umber of Units?\n ").lower()

      if building_info == 'a':
        print building.address
      elif building_info == 'd':
        print building.doorman
      elif building_info == 'n':
        print building.number_units
      else:
        print "\nSorry I could not understand\n"
    elif to_do == 'a': #adds new apartment
      building_number = int(raw_input("What is the building number? "))
      building = Building.building_list[building_number]

      unit_number = int(raw_input("What is the unit number? "))
      rent = int(raw_input("What is the rent per month? "))
      square_footage = int(raw_input("What is the square_footage? "))
      bathrooms = int(raw_input("Number of bathrooms? "))


      apartment = building.add_apartment(unit_number, rent, square_footage, bathrooms)

      print "\nApartment Number: %s added to building number %s\n" % (apartment.unit_number,building)

    elif to_do == 'l': #requests apartment information
      building_number = int(raw_input("Which building number is the apartment located in? "))
      unit_number = int(raw_input("Which apartment number? "))

      print "unit number %s" %(unit_number)

      building = Building.building_list[building_number]
      apartment = building.apartment_dict[unit_number]

      apt_info = raw_input("What do you want to look up?\n--(R)ent\n--(S)quare footage\n--(N)umber of bathrooms\n--Ren(T)er\n--(O)ccupied? ").lower()

      if apt_info == 'r':
        print apartment.rent
      elif apt_info == 's':
        print apartment.square_footage
      elif apt_info == 'n':
        print apartment.number_bathrooms
      elif apt_info == 't':
        print apartment.renter
      elif apt_info == 'o':
        print apartment.occupied
      else:
        print "\nSorry I could not understand\n"
        #finish loop here

    elif to_do =='r': #adds renter
      building_number = int(raw_input("Which building number is the renter located in? "))
      building = Building.building_list[building_number]

      unit_number = int(raw_input("Which apartment number? "))

      apartment = building.apartment_dict[unit_number]

      name = raw_input("What is the renter's name? ")

      renter = apartment.add_renter(name)

      print "\nRenter: %s, added to building number: %s and unit number %s\n" % (renter.name, renter.building_number, renter.apartment_number)
    elif to_do == 'o': #checks apartment occupancy
      building_number = int(raw_input("Which building number is the apartment located in? "))
      unit_number = int(raw_input("Which apartment number? "))

      building = Building.building_list[building_number]
      apartment = building.apartment_dict[unit_number]

      result = apartment.check_occupied()
      if True:
        print "\nOCCUPIED\n"
      else:
        print "\nUNOCCUPIED\n"
    elif to_do == 'q': #quits the program
        print "\nThanks for using Manager Client!\n"
        return False
    else:
        print "\nSorry, I don't understand what you want.\n"

print_menu()


