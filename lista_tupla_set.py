#Pregunta al usuario varios nombre
#El usuario debe de especificar cuando quiere terminar de ingresar nombres
#print en lista, tupla y set
sigue = "S"
lista_nombre=[]


while sigue =="s" or sigue =="S":
    nombre=input("Dame un Nombre: ")
    lista_nombre.append(nombre)
    sigue =input("\t \t Deses ingresar mas nombres s/n: ")
tupla_nombre=tuple(lista_nombre)
set_nombre = set(lista_nombre)
print("\n \n Esta es una  Lista :",lista_nombre) 
print("\n Esta es un Set: ", set_nombre)
print("\n \t Esta es una tupla:",tupla_nombre, "\n \n")
#for tupla in tupla_nombre:  
#    print(tupla)
