print("Bem-vindo à calculadora de IMC!")
print("Aqui você poderá nos dizer seu peso e sua altura e nós lhe diremos seu Índice de Massa Corporal!")

peso = float(input("Digite seu peso em KG: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / altura**2

if imc < 18.5:
    print("Você está abaixo do peso.")
    print(f"Seu IMC é: {imc:.2f}")
elif 18.5 <= imc < 25.9:
    print("Você está com um peso normal.")
    print(f"Seu IMC é: {imc:.2f}")
elif 25 <= imc < 29.9:
    print("Você está com sobrepeso.")
    print(f"Seu IMC é: {imc:.2f}")
elif 30 <= imc < 39.9:
    print("Você está com obesidade.")
    print(f"Seu IMC é: {imc:.2f}")
else:
    print("Você está com obesidade grave.")
    print(f"Seu IMC é: {imc:.2f}")