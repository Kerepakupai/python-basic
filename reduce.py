from functools import reduce

numbers = []
with open('./archivos/numbers.txt', 'r', encoding='utf-8') as f:
    for line in f:
        numbers.append(int(line))

print(numbers)


total = reduce(lambda x, y: x + y, numbers)
avg = round(total/len(numbers)) 
print(avg)
