#suma tres numeros si son iguales imprimir la suma *3

contador= 0
suma=0
numeros=[]
while contador < 3:
    dato=""
    while dato.isnumeric() == False: 
      dato = input("Dame un Número: ")
      
    numeros.append(int(dato))
    contador +=1
for i in range(0,3):
    suma = suma+numeros[i]
        
iguales =numeros.count(numeros[0])
if iguales == 3:
     print("la suma por 3:",suma*3)    
else:
    print("Suma sencilla: ", suma)
    
   