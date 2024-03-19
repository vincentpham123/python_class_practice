from smaple_class import PartyAnimal

test = PartyAnimal(100)

class Rave(PartyAnimal):

    def __init__(self,dj, size=1):
        self.dj = dj
        super().__init__(size)
    
    def dance(self):
        self.party()
        print(self.dj, self.x)

new_rave = Rave('Jay-Z')
print(new_rave.x)
new_rave.party()
new_rave.dance()