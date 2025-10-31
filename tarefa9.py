som= 0

num = int(input("Digite um número (0 para encerrar): "))

while num != 0:
    som += num
    num = int(input("Digite outro número (0 para encerrar): "))

print(f"A soma de todos os números digitados é: {som}")
