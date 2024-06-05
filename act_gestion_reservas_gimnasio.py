import csv 
import msvcrt 
import os 

usuarios = {}
clases = [ 
    ("Levantamiento de pesas","Lunes y Martes de 8:30 a 10:00 AM",15),
    ("Corsfit","Miercoles y Jueves de 8:30 a 10:00 AM",10),
    ("Nutrición para ganar peso","Viernes y Sabado de 8:30 a 10:00 AM",20)
]

while True: 
    print("<< presione para continuar >>")
    msvcrt.getch()
    os.system("cls")

    print(""" 
    \033[35mSISTEMA RESERVAS DE CLASES 
    ------------------------------------\033[0m
    1) Registrar nuevo usuario
    2) Reservar clase
    3) Mostrar clases disponibles 
    4) Mostrar reservas de usuarios 
    0) Salir
    """)
    opcion = input("Seleccione : ")

    if opcion=="0":
        break
    elif opcion=="1":
        print("\033[33mRegistrar usuario\033[0m")
        id = input("Ingrese ID único : ")
        if len(id)>=3:
            nombre = input("ingrese nombre : ")
            if len(nombre)>=5:
                usuarios[id] = (nombre)
            else: 
                print("\033[31mFaltan caracteres\033[0m")
        else: 
            print("\033[31mID no válido\033[0m")
    elif opcion=="2":
        print("\033[33mReservar clase\033[0m")
    elif opcion=="3":
        print("\033[33mMostrar clases disponibles\033[0m")
    elif opcion=="4":
        print("\033[33mReservas de usuarios\033[0m")
    else:
        print("\033[31mSeleccion inválida\033[0m")