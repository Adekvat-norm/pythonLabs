class Car:
    def __init__(self, model, color, speed, engineStatus):
        self.__model=model;
        self.__color=color;
        self.__speed=speed;
        self.__engineStatus=engineStatus;
    @property
    def model(self):
        return self.__model;
    @model.setter
    def model(self, mod):
        self.__model=mod;
    @property
    def color(self):
        return self.__color;
    @color.setter
    def color(self, col):
        self.__color=col;
    @property
    def engineStatus(self):
        return self.__engineStatus;
    @engineStatus.setter
    def engineStatus(self, engStatus):
        self.__engineStatus=engStatus;
        if engStatus == True:
            print('Двигатель запущен')
        elif engStatus == False:
            print('Двигатель остановлен')
    @property
    def speed(self):
        return self.__speed;
    @speed.setter
    def speed(self, sp):
        self.__speed=sp;
    def BoostSpeed(self, value):
        if self.engineStatus==True:
            self.speed +=value;
            print(f"Вы повысили скорость на {value} теперь ваша скорость равна: {self.speed}")
            return self.speed;
        elif self.engineStatus==False:
            print('Вы не можете повысить скорость с отключённым двигателем');
    def DeboostSpeed(self, value):
        if self.engineStatus==True:
            self.speed -=value;
            print(f"Вы сбавили скорость на {value} теперь ваша скорость равна: {self.speed}")
        elif self.engineStatus==False:
            print('Нельзя замедлятся с выключенным двигателем...');

class SportCar(Car):
    def __init__(self, model, color, speed, engineStatus, maxSpeed):
        super().__init__(model, color, speed, engineStatus);
        self.__maxSpeed=maxSpeed;
    @property
    def maxSpeed(self):
        return self.__maxSpeed;
    @maxSpeed.setter
    def maxSpeed(self, mSp):
        self.__maxSpeed=mSp;
    def BoostSpeed(self, value):
        if self.engineStatus==True:
            self.speed += value;
            if(self.speed<self.maxSpeed):
                print(f"Вы повысили скорость на {value} теперь ваша скорость равна: {self.speed}, а максимальная: {self.maxSpeed}")
            elif(self.speed>self.maxSpeed):
                self.speed-=value;
                print('Вы не можете превысить максимальную скорость...')

class Truck(Car):
    def __init__(self, model, color, speed, engineStatus, loadCapacity):
        super().__init__(model, color, speed, engineStatus);
        self.__loadCapacity=loadCapacity;
    @property
    def loadCapacity(self):
        return self.__loadCapacity;
    @loadCapacity.setter
    def loadCapacity(self, lC):
        self.__loadCapacity=lC;

car = Car('bmw', 'black', 100, True);
sportCar = SportCar('porsh', 'red', 150, True, 250);
truck = Truck('Kamaz', 'brown', 70, True, 1000)
car.BoostSpeed(5);
car.DeboostSpeed(15);
sportCar.BoostSpeed(120);
print(f"{car.model}, {car.color}, {car.speed}, {car.engineStatus}")
print(f"{sportCar.model}, {sportCar.color}, {sportCar.speed}, {sportCar.engineStatus}, {sportCar.maxSpeed}")
print(f"{truck.model}, {truck.color}, {truck.speed}, {truck.engineStatus}, {truck.loadCapacity}")

