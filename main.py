from Listas import Metodos

salir = True

milist = []
tam = int(input("Ingrese el tamaño de la lista:"))

Metodos.agregar(milist,tam)

while salir:
    print ("++++++++++++++++++++ Menu ++++++++++++++++++++"
           "\n1.-Agregar al final de la lista"
           "\n2.-Mostrar lista"
           "\n3.-Unir lista a otra"           
           "\n4.-Contar la cantidad de veces que aparecer un item"
           "\n5.-Buscar un item por nombre y devolver indice"
           "\n6.-Agregar un item en un indice especifico"
           "\n7.-Extrar un elemento(Borra de la lista el elemento)"
           "\n8.-Borrar un item en especifico"
           "\n9.-Dar vuelta a la lista"
           "\n10.-Ordernar Lista"
           "\n11.-Vaciar lista"
           "\n12.-Prueba"
           "\n0.-Salir")
    opc = int(input("Ingrese una opcion:"))
    if(opc == 0):
        salir = False
    else:
        if(opc == 1):
            Metodos.agregar_final(milist)
            tam += 1
        if(opc == 2):
            Metodos.impresion(milist)
        if(opc == 3):
            Metodos.unir_lista(milist)
        if(opc == 4):
            Metodos.contar_veces(milist)
        if(opc == 5):
            Metodos.buscar_index(milist)
        if(opc == 6):
            Metodos.insertar(milist)
        if(opc == 7):
            Metodos.extraer(milist)
        if(opc == 8):
            Metodos.eliminar(milist) 
        if(opc == 9):
            Metodos.reversa(milist) 
        if(opc == 10):
            Metodos.ordenar(milist)
        if(opc == 11):
            Metodos.vaciar(milist)   
        if opc == 12:
            Metodos.Prueba(milist)  
        
    