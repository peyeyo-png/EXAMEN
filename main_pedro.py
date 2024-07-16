from functions import *





while True:
    clear()
    mm("Asignar sueldos aleatorios", "Clasificar sueldos", "Ver estadisticas", "Reporte de sueldos", "Salir del programa")
    user = input("Ingresa una opción: ")

    if user == "5":
        clear()
        print("Finalizando...")
        print("Desarrollado por Diego Sandoval \nRut: 22... quitado por privacidad, esta en la entrega del AVA.")
        break

    if user == "1":
        asignar_sueldos_aleatorios()
        wait(0)

    if user == "2":
        clasificar_sueldos()
        wait(6)
    if user == "3":
        mm("Sueldo mas alto", "Sueldo mas bajo", "Promedio de sueldos", "Media geometrica")
        op = input("Ingresa una opción: ")
        ver_estadisticas(op)
        wait(3)
