import random

def jogar():
    tracejado = "*********************************"
    numero_secreto = random.randrange(1, 101)

    dificuldade_selecionada = False
    total_de_tentativas = 0
    pontos = 1000
    acertouONumero = False

    print(tracejado, "\nBem vindo ao jogo de adivinhação!\n", tracejado, "\n")

    while not dificuldade_selecionada:
        print("Selecione o nível de dificuldade: \n(1) Fácil, (2) Médio, (3) Difícil")
        nivel = input("Defina o nível: ")
        dificuldade_selecionada = True

        if (nivel == "1"):
            total_de_tentativas = 20
        elif (nivel == "2"):
            total_de_tentativas = 10
        elif (nivel == "3"):
            total_de_tentativas = 5
        else:
            print("Dificuldade selecionada não válida...\n")
            dificuldade_selecionada = False
            continue
        print(tracejado, "\n")


    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        palpite = int(input("Digite o seu número: "))

        palpite_invalido = 0 >= palpite or palpite > 100
        acertou_numero_secreto = palpite == numero_secreto
        errou_para_cima = palpite > numero_secreto
        errou_para_baixo = palpite < numero_secreto

        if (palpite_invalido):
            print("Você deve digitar um numero entre 1 e 100")
            palpite = 100
            continue
        elif (acertou_numero_secreto):
            print("Você acertou!")
            acertouONumero = True
            break
        elif (errou_para_cima):
            print("Você errou! o numero escolhido é maior do que número secreto!\n", tracejado, "\n")
        elif (errou_para_baixo):
            print("Você errou! o numero escolhido é menor do que número secreto!\n", tracejado, "\n")
        pontos = pontos - abs(palpite)

    print("\n", tracejado)
    if (not acertouONumero):
        pontos = 0
        print("    O numero secreto era: {}".format(numero_secreto))
    print("    Fim de jogo    {} pontos \n".format(pontos), tracejado)

if __name__ == "__main__":
    jogar()