def is_palindromo(cadena: str):
  _cadena = cadena.replace(" ", "").lower()
  if _cadena == _cadena[::-1]:
    return True
  else:
    return False 


def run():
  cadena = input("Ingrese palabra: ")

  if is_palindromo(cadena):
    print("👍 " + cadena + " es palindromo")
  else:
    print("👎 " + cadena + " no es palindromo")


if __name__ == "__main__":
  run()
