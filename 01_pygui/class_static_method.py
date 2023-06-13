
class Vhicle:

    @classmethod # decorator
    def class_method(self):
        print("this is vhicle class method")

    @staticmethod # decorator
    def static_method():
        print("this is vhicle static method")

class Car(Vhicle):

    @classmethod # decorator
    def class_method(self):
        print("this is car class method")

Vhicle.class_method()
Car.class_method()

Vhicle.static_method()
Car.static_method()
