#Calcula cuantas veces se repite un nombre en una lista de nombres determinada
#por el usuario



       
lista_nombre=[]


while sigue =="s" or sigue =="S":
    nombre=input("Dame un Nombre: ")
    lista_nombre.append(nombre)
    sigue =input("\t \t Deses ingresar mas nombres s/n: ")

sigue ="S"
while sigue =="s" or sigue =="S":
    print("\n tu lista de nombres:",lista_nombre)
    nombre_buscar=input("Dame el nombre a Buscar y contar ")
    contador=lista_nombre.count(nombre_buscar)   
    if contador > 0 :
        print("El nombre: ",nombre_buscar," se repite: ", contador, " veces")
    else: 
        print("El nombre",nombre_buscar, "NO se encuentra \")
    sigue =input("\t \t Deses ingresar mas nombres s/n: ")    
