import os

menu = """💱 Bienvenido al conversor de monedas 💱
(1) Pesos Colombianos
(2) Pesos Argentinos
(3) Pesos Mexicanos
(4) Pesos Chilenos

Elige una opción: """

os.system('clear')

opcion = input(menu)

if opcion == '1':
  moneda = "pesos colombianos"
  valor_dolar = 4099.60
elif opcion == '2':
  moneda = "pesos argentinos"
  valor_dolar = 117.43
elif opcion == '3':
  moneda = "pesos mexicanos"
  valor_dolar = 20.11
elif opcion == '4':
  moneda = "pesos chilenos"
  valor_dolar = 860.40
else:
  print("Ingrese una opción valida")
  exit(0)


cantidad = int(input("Ingrese cantidad de " + moneda + " que desea convertir: "))
dolares = round(cantidad / valor_dolar, 2)

print(str(cantidad) + " " + moneda + " son " + str(dolares) + ' dolares')
