import random

messages = ("Hola", "Hola! Que tal?", "Buenos dias")

def saludar() -> str:
    return random.choice(messages)

if __name__ == "__main__":
    msg = saludar()
    print("%s" %(msg))

