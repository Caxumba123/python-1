nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)

if media > 7:
    print("Você está aprovado.")
elif media < 4:
    print("Você está reprovado.")
else:
    print("Você está de recuperação.")