locations = []
class Location:
    def __init__(self, name, num_units, unit_cap):
        self.name = name
        self.num_units = num_units
        self.unit_cap = unit_cap

def getLocations():
    
    num_locations = input("How many housing options (i.e. buildings): ")

    housing_location = []
    for i in range(num_locations):
        location_name = raw_input("What is the name of location " + str(i+1) + ": ")
        housing_location.append(location_name)

    for j in range(num_locations):
        number_units = input("How many units does " + housing_location[j] + " have (i.e. rooms): ")
        unit_capacity = input("What is the capacity of units at " + housing_location[j] + ": ")
        locations.append(Location(housing_location[j], number_units, unit_capacity))

    return locations
 
