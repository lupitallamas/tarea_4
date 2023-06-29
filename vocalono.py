"""Escribe un script que determine si una letra es vocal o no"""


sigue = "S"


while sigue =="s" or sigue =="S":
    letra=input("Dame una  letra: ")
    if len(letra) > 0:
        letra = letra[0]
        if letra in ["a","A","e","E","i","o","O","u","U"]:
            print("tu letra ", letra,"es una vocal")
        else:
            print("Tu letra no es vocal")
    sigue =input("\t \t Deses ingresar mas nombres s/n: ")