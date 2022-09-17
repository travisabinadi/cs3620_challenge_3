class Computer:
    def __init__(self, weight, memory, cpu):
        self.weight = weight
        self.memory = memory
        self.cpu = cpu

    def getspecs(self):
        return [self.weight, self.memory, self.cpu]

    def displayspecs(self):
        print("COMPUTER")
        print(f"Weight: {self.weight}")
        print(f"Display: {self.memory}")
        print(f"CPU: {self.cpu}")
