import interfaz
from random import randrange

def selección_dificultad():
    while True:
        interfaz.mensaje_user_dificultad()
        try:
            d = input()
            if d.upper() == "F" or d.upper() == "N" or d.upper() == "D":
                interfaz.limpiar_pantalla()
                return d
            else:
                interfaz.limpiar_pantalla()
                interfaz.mensaje_error_seleccion()
        except:
            interfaz.limpiar_pantalla()
            interfaz.mensaje_error_seleccion()

def num_user(juego):
    while True:
        try:
            num_user = int(input())
            if num_user<1 or num_user>500:
                raise ValueError
            
            interfaz.limpiar_pantalla()
            return num_user
        except:
            interfaz.limpiar_pantalla()
            interfaz.mensaje_error_seleccion()
            interfaz.mensaje_inicio_user(juego["intent"])

def iniciar_juego(dificultad):
    if dificultad.upper()=="F":
        intentos = 10
    elif dificultad.upper()=="N":
        intentos = 8
    else:
        intentos = 6

    numero_secreto = randrange(1,500)
    juego = {
        "intent":intentos,
        "num":numero_secreto,
        "ganado": False,
        "dif": dificultad.upper()
    }
    return juego

def verificar_entrada(n,j):
    if n==j["num"]:
        j["ganado"]=True
        return 2
    elif n>j["num"]:
        return 0
    elif n<j["num"]:
        return 1

def juego_user():
    juego = iniciar_juego(selección_dificultad())
    while juego["intent"]!=0:

        if juego["ganado"]:
            break

        interfaz.mensaje_inicio_user(juego["intent"])
        num = num_user(juego)
        pista = verificar_entrada(num,juego)

        if juego["ganado"]:
            break

        juego["intent"] -= 1
        if juego["intent"]!=0:
            interfaz.mensaje_pista_user(pista)
        
    interfaz.mensaje_ganar_perder_user(juego)


    

