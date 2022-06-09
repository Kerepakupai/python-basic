DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def main():
    # desarrolladores python
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    print(f'all_python_devs: {all_python_devs}')
    
    all_python_devs = list(filter(lambda worker: worker['language'] == 'python', DATA))
    all_python_devs = list(map(lambda worker: worker['name'], all_python_devs))
    print(f'all_python_devs: {all_python_devs}')
    
    
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    print(f'all_platzi_workers: {all_platzi_workers}')
    
    all_platzi_workers = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    all_platzi_workers = list(map(lambda worker: worker['name'], all_platzi_workers))
    print(f'all_platzi_workers: {all_platzi_workers}')


    
    adults = list(filter(lambda worker: worker['age'] >= 18, DATA))
    adults_names = list(map(lambda worker: worker['name'], adults))
    print(f'adults: {adults_names}')

    adults = [worker['name'] for worker in DATA if worker['age'] >= 18]
    print(f'adults: {adults}')

    # python 3.9 
    # old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))
    old_people = list(map(lambda worker: {**worker, **{'old': worker['age'] > 70}}, DATA))
    
    old_people_2 = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]
    
    print(old_people == old_people_2)



if __name__ == '__main__':
    main()
