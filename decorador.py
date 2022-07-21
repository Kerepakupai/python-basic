from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f"Take {str(time_elapsed.total_seconds())} seconds")
    return wrapper()


@execution_time
def random_func():
    for _ in range(10000000):
        pass


@execution_time
def sum_two_numbers(a: int, b: int) -> int:
    return a + b


@execution_time
def saludo(name):
    print(f"Hola {name}")


random_func()
sum_two_numbers(5, 5)
saludo(name="David")
