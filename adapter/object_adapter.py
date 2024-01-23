class CelsiusTemperature:
    def getCTemperature(self):
        pass

class FahrenheitTemperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def getTemperature(self):
        return self.temperature
    
class FahrenheitToCelsiusAdapter(CelsiusTemperature):
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    def getCTemperature(self):
        return (self.fahrenheit.getTemperature() - 32) * 5 / 9
    
if __name__ == '__main__':
    f = FahrenheitTemperature(100)
    c = FahrenheitToCelsiusAdapter(f)
    print("The temperature is", c.getCTemperature(), "degrees Celsius.")