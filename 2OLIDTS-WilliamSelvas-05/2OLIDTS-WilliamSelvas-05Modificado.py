def pop_arreglo_aves(arreglo):
   for i in range(0,4,1):
     arreglo.pop()

   print("Los valores de la lista después de eliminar son: \n")
   for i in arreglo:
        print(i, end=", ")
   print("\n")
   return arreglo


def push_arreglo_aves(arreglo):
    arreglo.append("Guacamaya")
    arreglo.append("Periquitos Australianos")
    arreglo.append("Cacatúa")
    print("Los valores de la lista despues de insertar son:\n")
    for i in arreglo:
        print(i, end=", ")
    print("\n")
    return arreglo

def arreglo_aves(arreglo_original):
    print("Los valores de la lista original son:")
    for a in arreglo_original:
        print(a, end=", ")
    print("\n")


def main():
    aves = ["Loro gris", "Paloma de Diamante", "Loro verde"]
    nuevo_aves = []
    nuevo_aves_dos = []
    arreglo_aves(aves)
    nuevo_aves=push_arreglo_aves(aves)
    nuevo_aves=pop_arreglo_aves(nuevo_aves)
    arreglo_aves(nuevo_aves_dos)
if __name__ == "__main__":
    main()