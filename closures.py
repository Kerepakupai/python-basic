# Hola 3 -> HolaHolaHola
# David 2 -> DavidDavid

def make_repeater_of(n):
    # nested function
    def repeater(string):
        assert type(string) == str, "Only can used string"
        # reference to a superior var
        return string * n
    # return a function
    return repeater


def make_division_by(n):
    """This closure returns a function that returns the division of an x number by n"""
    # nested function
    def division(x):
        # remember a superior var
        return x / n
    # return a function
    return division


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola"))

    repeat_10 = make_repeater_of(10)
    print(repeat_10("David"))

    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_5 = make_division_by(5)
    print(division_by_5(100))

    division_by_18 = make_division_by(18)
    print(division_by_18(54))


if __name__ == '__main__':
    run()
