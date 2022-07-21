# Funcion que recibe como parametro otra funcion, le añade cosas, y retorna una funcion diferente

def decorator(func):
    def wrapper():
        print("This is added to my original function")
        func()
    return wrapper


def uppercase(func):
    def wrapper(text):
        return func(text).upper()
    return wrapper


@uppercase
def greets(name):
    return f"Hola {name}!"

# greets = decorator(greets)


print(greets("David"))
