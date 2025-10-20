class Auto:
    def __init__(self, marca, velocidad_maxima):
        self.__marca = marca  #asignar un valor
        self.__velocidad_maxima = velocidad_maxima #guardar el valor
        self.__velocidad_actual = 0 #establecer la velocidad

    # obtiene velocidad
    def get_velocidad_actual(self):
        return self.__velocidad_actual

    # método para acelerar
    def acelerar(self, aumento):
        if self.__velocidad_actual + aumento > self.__velocidad_maxima:
            self.__velocidad_actual = self.__velocidad_maxima
        else:
            self.__velocidad_actual += aumento

    # método para frenar
    def frenar(self, reduccion):
        if self.__velocidad_actual - reduccion < 0:
            self.__velocidad_actual = 0
        else:
            self.__velocidad_actual -= reduccion

print("TOYOTA")
auto1 = Auto("Toyota", 180)

auto1.acelerar(50)
print("Velocidad actual:", auto1.get_velocidad_actual(), "km/h")

auto1.acelerar(200)
print("Velocidad actual:", auto1.get_velocidad_actual(), "km/h")

auto1.frenar(100)
print("Velocidad actual:", auto1.get_velocidad_actual(), "km/h")

print("MERCEDES")

auto2 = Auto("Mercedes", 180)

auto2.acelerar(200)
print("Velocidad actual:", auto2.get_velocidad_actual(), "km/h")

auto2.acelerar(250)
print("Velocidad actual:", auto2.get_velocidad_actual(), "km/h")

auto2.frenar(100)
print("Velocidad actual:", auto2.get_velocidad_actual(), "km/h")

#Encapsulamiento 

#_marca = variables privadas
#_marca = variables que se pueden llamar llamando primero a la clase o funcion 
#_marca = variables  publicas