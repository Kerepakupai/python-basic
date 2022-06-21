import random as rnd


def main():
    rnd_number = rnd.randint(1, 100)
    print("🎲Adivina el Número🎲\n")
    
    while True:
        option = int(input("Elige un número del 1 al 100: "))
        if option < rnd_number:
            print("Intenta con un número más grande\n")
            continue
        elif option > rnd_number:
            print("Intenta con un número más pequeño\n") 
            continue
        else:
            print("👌Ganaste!")
            break


if __name__ == "__main__":
    main()
