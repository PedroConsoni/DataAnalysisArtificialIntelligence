import random

pedraPapelTesoura = ["Pedra", "Papel", "Tesoura"]

escolhaDoAdversario = random.choice(pedraPapelTesoura)

escolhaDoUsuario = input("Escolha entre Pedra, Papel e Tesoura: ").capitalize()

print("Você escolheu: ", escolhaDoUsuario)
print("Seu adversário escolheu: ", escolhaDoAdversario)

if escolhaDoUsuario == "Pedra" and escolhaDoAdversario == "Pedra":
    print("Empate!")
elif escolhaDoUsuario == "Pedra" and escolhaDoAdversario == "Tesoura":
    print("Você ganhou!")
elif escolhaDoUsuario == "Pedra" and escolhaDoAdversario == "Papel":
    print("Você perdeu!")
elif escolhaDoUsuario == "Papel" and escolhaDoAdversario == "Papel":
    print("Empate!")
elif escolhaDoUsuario == "Papel" and escolhaDoAdversario == "Pedra":
    print("Você ganhou!")
elif escolhaDoUsuario == "Papel" and escolhaDoAdversario == "Tesoura":
    print("Você perdeu!")
elif escolhaDoUsuario == "Tesoura" and escolhaDoAdversario == "Tesoura":
    print("Empate!")
elif escolhaDoUsuario == "Tesoura" and escolhaDoAdversario == "Papel":
    print("Você ganhou!")
elif escolhaDoUsuario == "Tesoura" and escolhaDoAdversario == "Pedra":
    print("Você perdeu!")
else:
    print("Você digitou uma opção inválida.")