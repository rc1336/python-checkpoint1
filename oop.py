# #1: Define a Vehicle class with the following properties and methods:
# - `vehicle_type`
# - `wheel_count`
# - `name`
# - `cost`
# - `colors`
# - `vehicle_brand`
# - `mpg`, a 'dict', with the following properties:
#     - `city`
#     - `highway`
#     - `combined`


class Vehicle:
    def __init__(self, dict):
        vehicle_type = dict['vehicle_type']
        wheel_count = dict['wheel_count']
        name = dict['name']
        cost = dict['cost']
        colors = dict['colors']
        vehicle_brand = dict['vehicle_brand']
        mpg = dict['mpg']


dict = {
    "city": "city",
    "highway": "highway",
    "combined": "combined"
}

# - `get_vehicle_type` should return the `vehicle_type`


def get_vehicle_type(self):
    print(f'the vehicle type is: {self.vehicle_type}')

    # - `get_vehicle_brand` should return the classes `vehicle_brand`


def get_vehicle_brand(self):
    return vehicle_brand

    # - `get_vehicle_drive` if the `wheel_count` for that class is "no wheels!" then
    #     it should return "no wheels send it back to the shop" otherwise it should
    #     return "I have "  + self.wheel_count  + " wheel drive"


def get_vehicle_drive(self):
    if wheel_count == "no wheels!":
        return "no wheels send it back to the shop."
    else:
        f'I have {self.wheel_count} wheel drive'

    # Your Vehicle class should take one argument (a `dict`) with the above
    # attributes. Define the properties on the class from the dict that is passed in.

    # #2: Create a Motorcycle class that inherits from the Vehicle class and has the


class Motorcycle(Vehicle):
    pass
    # following properties and methods:
    # - property: `wheel_count` defaults to "no wheels!"
    # - method: `pop_wheelie` if `wheel_count` is not equal to 2 then it should be False,
    #       otherwise return "......pop!"

    # #3: Define a Car class that inherits from the vehicle class with the following attributes and methods:
    # - property: `wheel_count` defaults to 4
    # - method: `can_drive` that should return 'Vrrooooom Vroooom'


class Car(Vehicle):
    pass

    # #4: Define a Truck class that inherits from the vehicle class with the following attributes and methods:
    # - property: `wheel_count` defaults to "no wheels!"
    # - method: `rev_engine` that should return 'revvvvvreeeev'


class Truck(Vehicle):
    pass
    # Commit when you finish working on these questions!
