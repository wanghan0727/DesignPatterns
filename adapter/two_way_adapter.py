class CelsiusTemperature:
    def get_temperature(self):
        pass

class FahrenheitTemperature:
    def get_temperature(self):
        return self.temperature
    
class Celsius(CelsiusTemperature):
    def __init__(self, temperature):
        self.temperature = temperature
    
    def get_temperature(self):
        return self.temperature
    
class Fahrenheit(FahrenheitTemperature):
    def __init__(self, temperature):
        self.temperature = temperature
    
    def get_temperature(self):
        return self.temperature
    
class TwoWayAdapter(CelsiusTemperature, FahrenheitTemperature):
    def __init__(self, celsius=None, fahrenheit=None):
        if celsius:
            self.celsius = celsius
            self.fahrenheit = Fahrenheit(celsius.get_temperature() * 9 / 5 + 32)

        else:
            self.fahrenheit = fahrenheit
            self.celsius = Celsius((fahrenheit.get_temperature() - 32) * 5 / 9)

    def get_celsius_temperature(self):
        return self.celsius.get_temperature()
    
    def get_fahrenheit_temperature(self):
        return self.fahrenheit.get_temperature()
    

celsius = Celsius(25)
fahrenheit = Fahrenheit(77)

adapter1 = TwoWayAdapter(celsius)
adapter2 = TwoWayAdapter(fahrenheit)

print("Celsius temperature:", adapter1.get_celsius_temperature())
print("Fahrenheit temperature:", adapter1.get_fahrenheit_temperature())

print("Celsius temperature:", adapter2.get_celsius_temperature())
print("Fahrenheit temperature:", adapter2.get_fahrenheit_temperature())