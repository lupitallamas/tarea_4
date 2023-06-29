"""Escribe un script que le pida al usuario un número mínimo y un número máximo de un rango 
    de números.
    El script debe imprimir cuales de ellos son divisibles entre 3"""
    
dato ="ver"
numeros = {}
numero=0
contador=1
print("\t \t \t ------------Dame  número entre 0 al 100-------------")
      
while contador < 3:
    dato=""
    if contador ==1:
        num_letra="--Dame tu mínimo: "
    else:
        num_letra="--Dame tu maximo: " 
        
    while dato.isdigit() == False:        
        dato = input(num_letra)
    numero=int(dato)
      
            
    if numero >= 0 and numero < 101 :        
        if contador == 1:
            if numero < 100:
                numeros["minimo"]=numero
                contador = contador + 1
            else:
                print("\t \t.....El mínimo no puede ser el rango Máximo")
        else:
            if numeros["minimo"] < numero:
                numeros["maximo"]=numero
                contador =contador + 1
                #print("contador: ",contador)
            else:
                print("\t \t.....El número maximo debe ser mayor al Mínimo")   
    else:
        print("El número no esta en el rango permitido")
print("\n \t \t ",numeros)        
for key, value in numeros.items():
    #print("\n \t ",numeros)
    #print(key)
    #print(value)
    if value % 3 == 0:
        print("\n \t \t El número ", key,": ",value, " es divisible entre 3")
    else:
        print("\t \t El número ", key,": ",value, " NO es divisible entre 3")