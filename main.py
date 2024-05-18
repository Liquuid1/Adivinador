import adivina_maquina
import adivina_user
import interfaz

def seguir_jugando():
    while True:
        interfaz.mensaje_seguir_jugando()
        try:
            opcion = int(input())
            if opcion<0 or opcion>1:
                raise ValueError
        except:
            interfaz.limpiar_pantalla()
            interfaz.mensaje_error_seleccion()
        else:
            return opcion
        

running = True
interfaz.limpiar_pantalla()

while running:
    interfaz.mensaje_bienvenida()
    while True:
        interfaz.mensaje_seleccion_modo_juego()
        try:
            opcion = int(input())
            break
        except:
            interfaz.limpiar_pantalla()
            interfaz.mensaje_error_seleccion()

    if opcion == 0:
        interfaz.limpiar_pantalla()
        running = False
    elif opcion == 1:
        interfaz.limpiar_pantalla()
        adivina_user.juego_user()

        if seguir_jugando()==0:
            running = False
        else:
            interfaz.limpiar_pantalla()
        
    elif opcion == 2:
        interfaz.limpiar_pantalla()
        adivina_maquina.juego_maquina()

        if seguir_jugando()==0:
            running = False
    else:
        interfaz.limpiar_pantalla()
        interfaz.mensaje_error_seleccion()

interfaz.limpiar_pantalla()
interfaz.mensaje_despedida()
input()
