from restaurants import Restaurant as R

class IceCreamStand(R):
    def __init__(self,flavours):
        self.flavours = []

    def flavour_type(self):
        print(f"/n{self.flavours}/n")

ice_cream = IceCreamStand('chacolate','vainila','straberry')

ice_cream.flavour_type()