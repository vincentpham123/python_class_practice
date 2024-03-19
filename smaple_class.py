class PartyAnimal:

    def __init__(self, size = 1):
        # initialize
        self.x = size

    def party(self):
        self.x = self.x + 1 
        print('party guests: ', self.x)
    def __del__(self):
        print('party is done')

instance_party = PartyAnimal(100)
instance_party.party()
instance_party.party()
instance_party.party()
instance_party.party()
instance_party.__del__()
instance_party.party()
