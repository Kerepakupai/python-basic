def is_prime(number: int):
    count = 0
    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            count += 1
            
    if count == 0 and number != 1:
        return True
    else:
        return False


def main():
    number = int(input("Ingrese un numero: "))
    if is_prime(number):
        print("Is Prime")
    else:
        print("Not Prime")             
        
      
if __name__ == "__main__":
    main()
