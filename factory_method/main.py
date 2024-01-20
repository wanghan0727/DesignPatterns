from abc import ABC, abstractmethod

#所有具體車型產品的主接口
class Car(ABC):

    @abstractmethod
    def startEngine(self):
        pass

    @abstractmethod
    def turnOffEngine(self):
        pass

#具體產品Ａ
class ModelA(Car):
    def startEngine(self):
        print("modelA start Engine")
        return True
    
    def turnOffEngine(self):
        print("modelA turnOffEngine")

#具體產品B
class ModelB(Car):
    def startEngine(self):
        print("modelB start Engine")
        return True
    
    def turnOffEngine(self):
        print("modelB turnOffEngine")

#工廠接口
class CarFactory(ABC):
    @abstractmethod
    def makeCar(self):
        pass

#具體工廠A
class ModelAFactory(CarFactory):
    def makeCar(self):
        modelA = ModelA()
        if modelA.startEngine() == True:
            modelA.turnOffEngine
            return modelA
        else:
            return None
        
#具體工廠B        
class ModelBFactory(CarFactory):
    def makeCar(self):
        modelB = ModelB()
        if modelB.startEngine() == True:
            modelB.turnOffEngine
            return modelB
        else:
            return None
        

class CarStorage:

    carStorage = [None] * 10

    def importCars(self):
        factoryA = ModelAFactory()
        factoryB = ModelBFactory()
        for i in range(5):
            self.carStorage[i] = factoryA.makeCar()
        for i in range(5, 10):
            self.carStorage[i] = factoryB.makeCar()

storage = CarStorage()
storage.importCars()