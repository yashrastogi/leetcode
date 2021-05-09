class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.bigc = big
        self.medc = medium
        self.smoc = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.bigc > 0:
                self.bigc -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.medc > 0:
                self.medc -= 1
                return True
            else:
                return False
        elif carType == 3:
            if self.smoc > 0:
                self.smoc -= 1
                return True
            else:
                return False
        
            
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)