
import random


personas = [
    {
        "nombre": "Juan Perez",
        "sueldo": 0
    },
    {
        "nombre": "María García",
        "sueldo": 0
    },
    {
        "nombre": "Carlos López",
        "sueldo": 0
    },
    {
        "nombre": "Ana Martínez",
        "sueldo": 0
    },
    {
        "nombre": "Pedro Rodríguez",
        "sueldo": 0
    },
    {
        "nombre": "Laura Hernández",
        "sueldo": 0
    },
    {
        "nombre": "Miguel Sánchez",
        "sueldo": 0
    },
    {
        "nombre": "Isabel Gómez",
        "sueldo": 0
    },
    {
        "nombre": "Francisco Díaz",
        "sueldo": 0
    },
    {
        "nombre": "Elena Fernández",
        "sueldo": 0
    }

]

def clear():
    return os.system('cls')

def wait(s):
    return time.sleep(s)

def mm(*args):
    for i, option in enumerate(args, start=1):
        print(f'{i}.- {option}')


# Class

def asignar_sueldos_aleatorios():
    for s in personas:
        sueldo_random = random.randint(250000, 3000000)
        sueldo = s["sueldo"]
        nombre = s["nombre"]

        s["sueldo"] = sueldo_random
    print(f'Se han generado {len(personas)} saldos aleatorios exitosamente.')
    print(personas)



def clasificar_sueldos():
    menor_800k = []
    entre_800k_y_2m = []
    superior_2m = []

    for persona in personas:
        sueldo = persona["sueldo"]
        nombre = persona["nombre"]
        if sueldo < 800000:
            menor_800k.append(persona)
        elif sueldo > 800000 and sueldo < 2000000:
            entre_800k_y_2m.append(persona)
        elif sueldo > 2000000:
            superior_2m.append(persona)
    print()
    print(f"Sueldos menores a $800.000. TOTAL: {len(menor_800k)}")
    print(f"Nombre\t\tSueldo")
    for persona in menor_800k:
        nombre = persona["nombre"]
        sueldo = persona["sueldo"]
        print(f"{nombre}\t${sueldo}")
    print()
    print(f"Sueldos entre $800.000 y 2.000.000. TOTAL: {len(entre_800k_y_2m)}")
    print(f"Nombre\t\tSueldo")
    for persona in entre_800k_y_2m:
        nombre = persona["nombre"]
        sueldo = persona["sueldo"]
        print(f"{nombre}\t${sueldo}")
    print()
    print(f"Sueldos mayores a 2.000.000. TOTAL: {len(superior_2m)}")
    print(f"Nombre\t\tSueldo")
    for persona in superior_2m:
        nombre = persona["nombre"]
        sueldo = persona["sueldo"]
        print(f"{nombre}\t${sueldo}")


def ver_estadisticas(opcion):
    if opcion == "1":
        ord = []
        ordenados = sorted(personas, key= lambda x: x["sueldo"],)
        print("Nombre Empleado\t\tSueldo")
        for a in ordenados:
            nombre = a["nombre"]
            sueldo = a["sueldo"]

            ord.append({"nombre": nombre, "sueldo": sueldo})

        usr = ord[1]
        nombre = usr["nombre"]
        sueldo = usr["sueldo"]
        print(f"{nombre}\t\t{sueldo}")
    if opcion == "2":
        ord = []
        ordenados = sorted(personas, key= lambda x: x["sueldo"], reverse=True)
        print("Nombre Empleado\t\tSueldo")
        for a in ordenados:
            nombre = a["nombre"]
            sueldo = a["sueldo"]

            ord.append({"nombre": nombre, "sueldo": sueldo})

        usr = ord[1]
        nombre = usr["nombre"]
        sueldo = usr["sueldo"]
        print(f"{nombre}\t\t{sueldo}")

    if opcion == "3":
        total = 0
        for persona in personas:
            sueldo = persona["sueldo"]
            total += sueldo
        
        print(f"El sueldo promedio es de: ${total/10} pesos.")
    
    if opcion == "4":
        total = 1
        for persona in personas:
            sueldo = persona["sueldo"]
            total *= sueldo
        print(f"El promedio geometrico es de ${total**(1/10)}")
            



 
    

