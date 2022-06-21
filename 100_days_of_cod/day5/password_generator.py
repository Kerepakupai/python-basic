import random

# random.choice : Choose a random item from a list 
# random.shuffle: Randonly order a list

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the Password Generator!')
nr_letters = int(input('How many letters would you like in your password\n'))
nr_symbols = int(input('How many symbols would you like in your password\n'))
nr_numbers = int(input('How many number would you like in your passqords\n'))

password = []
random_letters = []
random_numbers = []
random_symbols = []
r = ''

for i in range(0, nr_letters):
    random_letters.append(letters[random.randint(0, len(letters)-1)])
    
for i in range(0, nr_symbols):
    random_symbols.append(symbols[random.randint(0, len(symbols)-1)])
    
for i in range(0, nr_numbers):
    random_numbers.append(numbers[random.randint(0, len(numbers)-1)])
    

password = random_letters + random_numbers + random_symbols
for i in range(0, len(password)):
    r += password.pop(random.randint(0, len(password)-1))   

print(r)
