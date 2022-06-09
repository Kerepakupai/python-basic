# [element for element in iterable if condition]

# def main():
#     squares = []
#     for num in range(1, 101):
#         if num % 3 != 0:
#             squares.append(num**2)

#     print(squares)

def main():
    squares = [num**2 for num in range(1, 101) if num % 3 != 0]
    # print(squares)
    
    for_multiply = [num for num in range(1, 100000) if num % 36 == 0]
    print(for_multiply)


if __name__ == '__main__':
    main()
