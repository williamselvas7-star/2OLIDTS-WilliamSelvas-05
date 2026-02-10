#Declara una lista de cadenas
aves=["Loros gris", "Paloma de diaente","Cóctel"]
print("Los valores de las lista antes de insetar")
#Itera sobre la lista para imprimir los valores 
for ave in aves:
    print (ave, end=" ")

print("\n")

#Agrega tres valores al final de la lista utilizando el método append()
aves.append("Mayna")
aves.append("Periquitos")
aves.append("Cacatúa")
print("Los valores de la lista después de insertar: ")
#Itera sobre la lista para imprimir los valores 
for ave in aves:
    print(ave, end=" ")

print("\n")


