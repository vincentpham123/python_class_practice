class PartyAnimal:

    def __init__(self, size = 1):
        # initialize
        self.x = size

    def party(self):
        self.x = self.x + 1 
        print('party guests: ', self.x)
    def __del__(self):
        print('party is done')

if __name__ == "__main__":
    # This block will only execute if the script is run directly, not when imported
    test = PartyAnimal(10)
    test.party()

