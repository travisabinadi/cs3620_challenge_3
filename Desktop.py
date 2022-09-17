from Computer import Computer


class Desktop(Computer):
    def __init__(self, weight, memory, cpu, graphics_card):
        super().__init__(weight, memory, cpu)
        self.graphics_card = graphics_card

    def getspecs(self):
        return [self.weight, self.memory, self.cpu, self.graphics_card]

    def displayspecs(self):
        print("DESKTOP")
        print(f"Weight: {self.weight}")
        print(f"Display: {self.memory}")
        print(f"CPU: {self.cpu}")
        print(f"Battery: {self.graphics_card}")
