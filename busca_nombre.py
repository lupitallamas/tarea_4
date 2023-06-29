


sigue = "S"
lista_nombre=[]


sigue ="s"
while sigue =="s" or sigue =="S":
    nombre=input("Dame un Nombre: ")
    lista_nombre.append(nombre)
    sigue =input("\t \t Deses ingresar mas nombres s/n: ")
sigue = "s"
while sigue =="s" or sigue =="S":
    print("\n tu lista de nombres:",lista_nombre)
    nombre_buscar=input("Dame el nombre a Buscar ")
    contador=lista_nombre.count(nombre_buscar)   
    if contador > 0 :
        print("El nombre: ",nombre_buscar," si se encuentra en la lista")
    else: 
        print("El nombre: ",nombre_buscar," NO se encuentra en la lista")
    sigue =input("\t \t Deses ingresar mas nombres s/n: ")