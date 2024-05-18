from colorama import Fore, Back, Style
from os import system

def mensaje_bienvenida():
    print(f"{Back.GREEN}                             {Style.BRIGHT}{Back.LIGHTRED_EX}{Fore.BLUE}  BIENVENIDO  {Back.BLUE}                             {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
    print(f"{Back.GREEN}  {Style.RESET_ALL}  En este juego puedes adivinar un número que propone la maquina o  {Back.BLUE}  {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}   puedes hacer que la maquina adivine un número que tu propongas.  {Back.BLUE}  {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
    print(f"{Back.GREEN}                                    {Back.BLUE}                                    {Style.RESET_ALL}\n"*1,end="")

def mensaje_seleccion_modo_juego():
    print(f"{Back.GREEN}                             {Style.BRIGHT}{Back.LIGHTRED_EX}{Fore.BLUE}  SELECCIONA  {Back.BLUE}                             {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
    print(f"{Back.GREEN}  {Style.RESET_ALL}  Ingresa [1] para adivinar un número o ingresa [2] para que la     {Back.BLUE}  {Style.RESET_ALL}") 
    print(f"{Back.GREEN}  {Style.RESET_ALL}             maquina adivine un numero que tu propongas.            {Back.BLUE}  {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                            Para salir [0]                          {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
    print(f"{Back.GREEN}                                    {Back.BLUE}                                    {Style.RESET_ALL}\n"*1,end="")
    print(f"{Fore.RED}{Style.BRIGHT}                                -->{Back.RED}{Style.RESET_ALL}",end="")

def mensaje_error_seleccion():
    print(f"{Back.GREEN}                             {Style.BRIGHT}{Back.LIGHTRED_EX}{Fore.BLUE}     ERROR    {Back.BLUE}                             {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                    SELECCIONA UNA OPCIÓN VALIDA                    {Back.BLUE}  {Style.RESET_ALL}") 

def limpiar_pantalla():
    system("cls")

def mensaje_user_dificultad():
    print(f"{Back.GREEN}                             {Style.BRIGHT}{Back.LIGHTRED_EX}{Fore.BLUE}  DIFICULTAD  {Back.BLUE}                             {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
    print(f"{Back.GREEN}  {Style.RESET_ALL}  Elige modo de dificultad:                                         {Back.BLUE}  {Style.RESET_ALL}") 
    print(f"{Back.GREEN}  {Style.RESET_ALL}  [F] Para facil (10 intentos)                                      {Back.BLUE}  {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}  [N] Para normal (8 Intentos)                                      {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
    print(f"{Back.GREEN}  {Style.RESET_ALL}  [D] Para dificil (6 Intentos)                                     {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
    print(f"{Back.GREEN}                                    {Back.BLUE}                                    {Style.RESET_ALL}\n"*1,end="")
    print(f"{Fore.RED}{Style.BRIGHT}                                -->{Back.RED}{Style.RESET_ALL}",end="")

def mensaje_inicio_user(intentos):
    if intentos>9:
        print(f"{Back.GREEN}                             {Style.BRIGHT}{Back.LIGHTRED_EX}{Fore.BLUE}  ADIVINADOR  {Back.BLUE}                             {Style.RESET_ALL}")
        print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
        print(f"{Back.GREEN}  {Style.RESET_ALL}                    Te quedan {intentos} para adivinar                      {Back.BLUE}  {Style.RESET_ALL}") 
        print(f"{Back.GREEN}  {Style.RESET_ALL}                   Los numeros van del 1 al 500                     {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
        print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
        print(f"{Back.GREEN}                                    {Back.BLUE}                                    {Style.RESET_ALL}\n"*1,end="")
        print(f"{Fore.RED}{Style.BRIGHT}                                -->{Back.RED}{Style.RESET_ALL}",end="")
    else:
        print(f"{Back.GREEN}                             {Style.BRIGHT}{Back.LIGHTRED_EX}{Fore.BLUE}  ADIVINADOR  {Back.BLUE}                             {Style.RESET_ALL}")
        print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
        print(f"{Back.GREEN}  {Style.RESET_ALL}                    Te quedan {intentos} para adivinar                       {Back.BLUE}  {Style.RESET_ALL}") 
        print(f"{Back.GREEN}  {Style.RESET_ALL}                   Los numeros van del 1 al 500                     {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
        print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
        print(f"{Back.GREEN}                                    {Back.BLUE}                                    {Style.RESET_ALL}\n"*1,end="")
        print(f"{Fore.RED}{Style.BRIGHT}                                -->{Back.RED}{Style.RESET_ALL}",end="")

def mensaje_pista_user(p):
    if p==0:
        print(f"{Back.GREEN}                             {Style.BRIGHT}{Back.LIGHTRED_EX}{Fore.BLUE}     MAYOR    {Back.BLUE}                             {Style.RESET_ALL}")
        print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
        print(f"{Back.GREEN}  {Style.RESET_ALL}                    El número secreto esta más abajo                {Back.BLUE}  {Style.RESET_ALL}") 
        print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
    elif p==1:
        print(f"{Back.GREEN}                             {Style.BRIGHT}{Back.LIGHTRED_EX}{Fore.BLUE}     MENOR    {Back.BLUE}                             {Style.RESET_ALL}")
        print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
        print(f"{Back.GREEN}  {Style.RESET_ALL}                    El número secreto esta más arriba               {Back.BLUE}  {Style.RESET_ALL}") 
        print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")

def mensaje_ganar_perder_user(juego):
    if juego["ganado"]:
        print(f"{Back.GREEN}                             {Style.BRIGHT}{Back.LIGHTRED_EX}{Fore.BLUE}   GANASTE    {Back.BLUE}                             {Style.RESET_ALL}")
        print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
        print(f"{Back.GREEN}  {Style.RESET_ALL}                        FELICIDADES, GANASTE                        {Back.BLUE}  {Style.RESET_ALL}") 
        print(f"{Back.GREEN}  {Style.RESET_ALL}                  EFECTIVAMENTE EL NUMERO ERA {str(juego["num"]).zfill(3)}                   {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
        print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
    else:
        print(f"{Back.GREEN}                             {Style.BRIGHT}{Back.LIGHTRED_EX}{Fore.BLUE}   PERDISTE   {Back.BLUE}                             {Style.RESET_ALL}")
        print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
        print(f"{Back.GREEN}  {Style.RESET_ALL}                           JAJAJA TE GANE                           {Back.BLUE}  {Style.RESET_ALL}") 
        print(f"{Back.GREEN}  {Style.RESET_ALL}                     EL NUMERO SECRETO ERA {str(juego["num"]).zfill(3)}                      {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
        print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")

def mensaje_inicio_maquina():
    print(f"{Back.GREEN}                             {Style.BRIGHT}{Back.LIGHTRED_EX}{Fore.BLUE}  ADIVINADOR  {Back.BLUE}                             {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
    print(f"{Back.GREEN}  {Style.RESET_ALL}             Intetare adivinar un número que tu elijas              {Back.BLUE}  {Style.RESET_ALL}") 
    print(f"{Back.GREEN}  {Style.RESET_ALL}             Cuando indique un número tu debes indicar:             {Back.BLUE}  {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}         [>] Si el numero que quieres que adivine es mayor          {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
    print(f"{Back.GREEN}  {Style.RESET_ALL}         [<] Si el numero que quieres que adivine es menor          {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
    print(f"{Back.GREEN}  {Style.RESET_ALL}         [=] Si acerte el número que querias que adivinara          {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")

def mensaje_min_maquina():
    print(f"{Back.GREEN}                             {Style.BRIGHT}{Back.LIGHTRED_EX}{Fore.BLUE}    MINIMO    {Back.BLUE}                             {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
    print(f"{Back.GREEN}  {Style.RESET_ALL}               Dime el número minimo del rango a adivinar           {Back.BLUE}  {Style.RESET_ALL}") 
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
    print(f"{Back.GREEN}                                    {Back.BLUE}                                    {Style.RESET_ALL}\n"*1,end="")
    print(f"{Fore.RED}{Style.BRIGHT}                                -->{Back.RED}{Style.RESET_ALL}",end="")

def mensaje_max_maquina():
    print(f"{Back.GREEN}                             {Style.BRIGHT}{Back.LIGHTRED_EX}{Fore.BLUE}    MAXIMO    {Back.BLUE}                             {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
    print(f"{Back.GREEN}  {Style.RESET_ALL}               Dime el número maximo del rango a adivinar           {Back.BLUE}  {Style.RESET_ALL}") 
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
    print(f"{Back.GREEN}                                    {Back.BLUE}                                    {Style.RESET_ALL}\n"*1,end="")
    print(f"{Fore.RED}{Style.BRIGHT}                                -->{Back.RED}{Style.RESET_ALL}",end="")

def mensaje_error_rango():
    print(f"{Back.GREEN}                             {Style.BRIGHT}{Back.LIGHTRED_EX}{Fore.BLUE}     ERROR    {Back.BLUE}                             {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                       EL RANGO ES MUY CORTO                        {Back.BLUE}  {Style.RESET_ALL}") 

def mensaje_trampa():
    print(f"{Back.GREEN}                             {Style.BRIGHT}{Back.LIGHTRED_EX}{Fore.BLUE}    TRAMPA    {Back.BLUE}                             {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
    print(f"{Back.GREEN}  {Style.RESET_ALL}                      ESTAS HACIENDO TRAMPA!!                       {Back.BLUE}  {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                  POR ESO NO PODRAS SEGUIR JUGANDO                  {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
    print(f"{Back.GREEN}                                    {Back.BLUE}                                    {Style.RESET_ALL}\n"*1,end="")

def mensaje_ganar_maquina():
    print(f"{Back.GREEN}                             {Style.BRIGHT}{Back.LIGHTRED_EX}{Fore.BLUE}    GANE!!    {Back.BLUE}                             {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
    print(f"{Back.GREEN}  {Style.RESET_ALL}                    HE LOGRADO ADIVINAR TU NUMERO                   {Back.BLUE}  {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}             INTENTA HACERLO MÁS DIFICIL LA PROXIMA VEZ             {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
    print(f"{Back.GREEN}                                    {Back.BLUE}                                    {Style.RESET_ALL}\n"*1,end="")

def mensaje_perder_maquina():
    print(f"{Back.GREEN}                             {Style.BRIGHT}{Back.LIGHTRED_EX}{Fore.BLUE}    PERDI!    {Back.BLUE}                             {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
    print(f"{Back.GREEN}  {Style.RESET_ALL}                      NO HE LOGRADO ADIVINAR TU NUMERO              {Back.BLUE}  {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}               ESTA VEZ ME GANASTE, LO HARE MEJOR EN LA PROXIMA     {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
    print(f"{Back.GREEN}                                    {Back.BLUE}                                    {Style.RESET_ALL}\n"*1,end="")

def mensaje_intento_adivinar_maquina(intento,num):
    print(f"{Back.GREEN}                             {Style.BRIGHT}{Back.LIGHTRED_EX}{Fore.BLUE}  ADIVINADOR  {Back.BLUE}                             {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
    print(f"{Back.GREEN}  {Style.RESET_ALL}                             Intento {str(intento).zfill(2)}                             {Back.BLUE}  {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                          Tu numero es {str(num).zfill(3)}                          {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
    print(f"{Back.GREEN}                                    {Back.BLUE}                                    {Style.RESET_ALL}\n"*1,end="")
    print(f"{Fore.RED}{Style.BRIGHT}                                -->{Back.RED}{Style.RESET_ALL}",end="")

def mensaje_seguir_jugando():
    print(f"{Back.GREEN}                             {Style.BRIGHT}{Back.LIGHTRED_EX}{Fore.BLUE}  SELECCIONA  {Back.BLUE}                             {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="") 
    print(f"{Back.GREEN}  {Style.RESET_ALL}                        ¿Desea seguir jugando?                      {Back.BLUE}  {Style.RESET_ALL}") 
    print(f"{Back.GREEN}  {Style.RESET_ALL}     Presiona [0] para salir o presiona [1] para jugar otra vez     {Back.BLUE}  {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
    print(f"{Back.GREEN}                                    {Back.BLUE}                                    {Style.RESET_ALL}\n"*1,end="")
    print(f"{Fore.RED}{Style.BRIGHT}                                -->{Back.RED}{Style.RESET_ALL}",end="")

def mensaje_despedida():
    print(f"{Back.GREEN}                             {Style.BRIGHT}{Back.LIGHTRED_EX}{Fore.BLUE}     ADIOS    {Back.BLUE}                             {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                         Gracias por jugar                          {Back.BLUE}  {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                     Juego hecho por LiquuidSoft                    {Back.BLUE}  {Style.RESET_ALL}")
    print(f"{Back.GREEN}  {Style.RESET_ALL}                                                                    {Back.BLUE}  {Style.RESET_ALL}\n"*1,end="")
    print(f"{Back.GREEN}                                    {Back.BLUE}                                    {Style.RESET_ALL}\n"*1,end="")

