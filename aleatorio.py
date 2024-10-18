import random

numero = random.randint(1,10)
intentoa = 0

while True:
    valor = int (input("ingrese su numero : "))
    if valor == numero:
         print("Has acertado y ganado")
         break
    else:
         print("has fallado")
         intentoa+=1
    if intentoa >5:
        print("Game Over")
        break