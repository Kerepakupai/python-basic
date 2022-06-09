# { key: value for value in iterable if condition }

def main():
    # cubes = {}
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         cubes[i] = i**3
                
    # print(cubes)
    
    my_dict = {num: num**3 for num in range(1, 101) if num %3 != 0}
    # print(my_dict)
    
    my_dict2 = {num: num**0.5 for num in range(1, 1001)}
    print(my_dict2)


if __name__ == '__main__':
    main()
