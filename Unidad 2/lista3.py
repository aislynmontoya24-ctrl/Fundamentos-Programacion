#Van a crear una lista vacia con su nombre y van agregar 5 elementos con input: (nombre , lugar de residencia , edad , carrera)
#Se crea lista llamada lista_nombre
lista_vacia = []

print("Lista")
dato1 = input(" Agrega tu nombre: ")
lista_vacia.append(dato1)

#Agregar producto 
dato2 = input("Agrega tu lugar de residencia: ")
lista_vacia.append(dato2)

dato3 = input("Agrega tu edad: ")
lista_vacia.append(dato3)

dato4 = input("Agrega tu carrera: ")
lista_vacia.append(dato4)

dato5 = input("Agrega tu preparatoria: ")
lista_vacia.append(dato5)

print("\n📌 Tu lista es:")
for dato in lista_vacia:
    print(f"- {dato}")
    
print("\n✅ ¡Lista creada con éxito!")
#https://www.webfx.com/tools/emoji-cheat-sheet/  