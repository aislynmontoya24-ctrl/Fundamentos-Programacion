#Declaramos las variables que vamos a necesitar 
edades = {
    "Brayan": 25,
    "Luis": 30,
    "Jose": 22,
}
#Imprimimos las variables
print("Edad de Luis:", edades["Luis"]) 
#Madamos llamar las variables   
edades["Brayan"] = 28
print("\nDespués de añadir a Pedro:")
print(edades)                               

edades["Luis"] = 26
print("\nDespués de actualizar la edad de Luis:")
print(edades)                              

del edades["Jose"]
print("\nDespués de eliminar a José:")
print(edades)                               

print("\nRecorriendo el diccionario:")
#Utilizamos el for y print para declarar las variables en orden
for nombre, edad in edades.items():         
     print(f"{nombre} tiene {edad} años")