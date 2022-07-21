def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]


if __name__ == '__main__':
    # mypy palindromo_con_tipado.py --check-untyped-defs
    # string_input = input("Enter a sentence: ")
    print(is_palindrome(10000))


