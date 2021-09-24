class Car:
    def __init__(self,year,make):
        self.__year = year
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brakes(self):
        self.__speed -= 5

    def get_spood(self):
        return self.__speed
        
