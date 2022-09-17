from Computer import Computer


class Laptop(Computer):
    def __init__(self, weight, memory, cpu, battery):
        super().__init__(weight, memory, cpu)
        self.battery = battery

    def getspecs(self):
        return [self.weight, self.memory, self.cpu, self.battery]

    def displayspecs(self):
        print("LAPTOP")
        print(f"Weight: {self.weight}")
        print(f"Display: {self.memory}")
        print(f"CPU: {self.cpu}")
        print(f"Battery: {self.battery}")