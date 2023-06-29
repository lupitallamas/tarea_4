""" Escribe un script que convierta una cantidad de segundos dada por el 
usuario a horas, minutos y segundos."""

dato =""
horas=0
seconds=0
hora={}

while dato.isdigit() == False:        
        dato = input("Dame la cantidad de segundo: ")
seconds=int(dato)

if seconds > 59:
    minutes=seconds // 60
    seconds=seconds % 60     
    if minutes > 59:
        horas= minutes // 60
        minutes = minutes % 60
    else:
        hora =  0          
   


hora["hora"] = horas
hora["minutos"] =minutes 
hora["segundos"] =seconds

print("\n" ,hora)

print("\t \t Hora:",hora["hora"],":",hora["minutos"],":",hora["segundos"],"\n \n")