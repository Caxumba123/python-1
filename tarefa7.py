par = 0

for i in range(10):
    numero = int(input(f"Digite o {i+1}º numero: "))

    if numero % 2 == 0:
        par += 1
print(f"Você digitou {par} numeros pares.")
