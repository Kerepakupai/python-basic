def main():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'firstname': 'David', 'lastname': 'Fuentes'}
    
    super_list = [
        {'firstname': 'David', 'lastname': 'Fuentes'},
        {'firstname': 'Mariela', 'lastname': 'Villalba'},
        {'firstname': 'Vilma', 'lastname': 'Zambrano'},
        {'firstname': 'Esperanza', 'lastname': 'Barrios'},
        {'firstname': 'David', 'lastname': 'Enrrique'}
    ]
    
    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-1, -2, 0, 1, 2],
        'foating_nums': [1.1, 4.5, 6.43]
    }
    
    for key, value in super_dict.items():
        print(f'{key} :: {value}')
        
    for item in super_list:
        print(item)

    square_list = []
    for num in range(1, 101):
        square_list.append(num**2)

    print(square_list)



if __name__ == '__main__':
    main()
    
        
