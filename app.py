class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def moves(self):
        print('moves along...')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


class Airplane(Vehicle):
    def moves(self):
        print('Flies along...')

class Truck(Vehicle):
    def moves(self):
        print('Rumbles along...')

class GolfCart(Vehicle):
    pass

cessina = Airplane('Cessna', 'Skyhawk')
mack = Truck('Mack', 'Pinnacle')

cessina.get_make_model()
mack.get_make_model()