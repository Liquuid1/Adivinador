import interfaz
from math import log

def validar_min():
    while True:
        interfaz.mensaje_min_maquina()
        try:
            aux = int(input())
            if aux<0 or aux>32000:
                raise ValueError
            return aux
        except:
            interfaz.limpiar_pantalla()
            interfaz.mensaje_error_seleccion()


def validar_max(min):
    interfaz.limpiar_pantalla
    while True:
        interfaz.mensaje_max_maquina()
        try:
            aux = int(input())
            if aux<0 or aux>32000:
                raise ValueError
            if log(aux-min,2)<=2:
                raise IndexError
            return aux
        except IndexError:
            interfaz.limpiar_pantalla()
            interfaz.mensaje_error_rango()
        except:
            interfaz.limpiar_pantalla()
            interfaz.mensaje_error_seleccion()

def validar_op_user(intentos,num):
    interfaz.limpiar_pantalla()
    while True:
        interfaz.mensaje_intento_adivinar_maquina(intentos,num)
        aux = input()
        if aux==">" or aux=="<" or aux=="=":
            return aux
        else:
            interfaz.limpiar_pantalla()
            interfaz.mensaje_error_seleccion()





def juego_maquina():
    interfaz.mensaje_inicio_maquina()
    min = validar_min()
    maxi = validar_max(min)
    interfaz.limpiar_pantalla()
    intentos = round(log(maxi-min,2))

    while intentos!=0:
        interfaz.limpiar_pantalla()
        num_pos = (maxi-min)//2+min
        res = validar_op_user(intentos,num_pos)

        if res == ">":
            min = num_pos+1
        elif res == "<":
            maxi = num_pos-1
        elif res == "=":
            interfaz.limpiar_pantalla()
            interfaz.mensaje_ganar_maquina()
            break

        if min>maxi or maxi<min:
            interfaz.limpiar_pantalla()
            interfaz.mensaje_trampa()
            break
        
        intentos -= 1

    if intentos==0:
        interfaz.limpiar_pantalla()
        interfaz.mensaje_perder_maquina()
    