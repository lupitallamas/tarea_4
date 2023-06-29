"""Escribe un script que imprima si un string dado por el usuario contiene números o no."""
sigue = "S"
dato=""
while sigue in ["S","s"]:
    dato=input("Dato: ")
    
    if dato.isalpha():
        print("\t \t .......tu dato:",dato, "'NO' contiene números")
    else:
        print("\t \t ....tu dato: ",dato,"contiene números")
        
    sigue =input("\n \n \t \t Deses ingresar mas nombres s/n: ")
