num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
num3 = int(input("Digite outro numero: "))

if num1 > num2 and num1 > num3:
    print("O primeiro numero é maior")
elif num2 > num1 and num2 > num3:
    print("O segundo numero é maior")
else:
    print("O ultimo numero é maior")