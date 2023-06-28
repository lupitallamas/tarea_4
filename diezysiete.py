#Calcula la diferencia entre un número dato y el 17 imprimir el resultado
#Si el número > 17 imprimir el doble de la diferencia
#Valida solo que sea un entero

dato ="ver"
numero = 0

while dato.isdigit() == False: 
    dato = input("Dame un Número: ") 
           
numero=int(dato)   
numero= numero - 17
if numero > 17:
    print("Es el doble de la diferencia:",numero*2)
else:
    print ("La diferencia es:", numero)

