class Metodos():
     
    #Metodo para agregar al final
    def agregar(lis,tam):
        i=0
        while(i<tam):
            print("Ingrese el [",i,"] valor de la lista")
            lis.append(int(input("numero: ")))
            i=i+1
    
    def agregar_final(lis):  
        print("Ingrese el valor de la lista")
        lis.append(int(input("numero: ")))
        
            
    def impresion(lis):
        print(lis)
        
    def vaciar(lis):
        lis.clear()
        print(lis)
        
    def unir_lista(lis):
        lis2 = []
        j = int(input("Ingrese el tamaño de la lista:"))
        i=0
        while(i<j):
            print("Ingrese el [",i,"] valor de la lista")
            lis2.append(int(input("numero: ")))
            i=i+1    
        lis.extend(lis2)
        print(lis)
        
    def contar_veces(lis):
        bus = int(input("Ingrese el item a buscar: "))
        print("Cantidad de veces que se repite en la lista: ",lis.count(bus))
        print(lis)
        
    def buscar_index(lis):
        bus = int(input("Ingrese el item a buscar:"))
        print("Indice: ",lis.index(bus))
        print(lis)
        
    def insertar(lis):
        lis.insert(int(input("Ingrese la posicion a insertar:")),int(input("Ingrese el valor a ingresar:")))
        print(lis)
    
    def extraer(lis):
        l = int(input("Ingrese la posicion a extraer:"))
        print("Elemento extraido: ", lis.pop(l))
        print(lis)
        
    def eliminar(lis):
        bus = int(input("Ingrese el valor a elminar: "))
        lis.remove(bus)
        
    def reversa(lis):
        lis.reverse()
        print(lis)
        
    def ordenar(lis):
        print("¿En que orden desea (A) Ascendente (D) Desendente?")
        if(input("Ingrese una opcion: ")=="A"):
            lis.sort()
            print(lis)
        else:
            lis.sort(reverse = True)
            print(lis)
        
    