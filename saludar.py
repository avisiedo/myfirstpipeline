import random


def saludo1():
    return "Hola"


def saludo2():
    return "Buenos días"


def saludo3():
    return "Hola, ¿Qué tal?"


def saludo4():
    return "¿Como te encuentras hoy?"


saludo = random.randint(0, 3)

if saludo == 0:
    print(saludo1())
elif saludo == 1:
    print(saludo2())
elif saludo == 2:
    print(saludo3())
elif saludo == 3:
    print(saludo4())
else:
    print("Adios")
