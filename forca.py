import random


def jogar():
    enforcou = False
    acertou = False
    contador_erros: int = 0
    num_maximo_erro = 7

    imprime_mensagem_abertura()
    palavra_secreta = selecionar_palavra_secreta()
    letras_acertadas = inicializar_letras_acertadas(palavra_secreta)

    while not enforcou and not acertou:
        chute = solicitar_palpite()

        if chute in palavra_secreta:
            letras_acertadas = tratar_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            contador_erros += 1
            tentativas_restantes = num_maximo_erro - contador_erros
            imprime_mensagem_err_chute(tentativas_restantes)

        enforcou = contador_erros == num_maximo_erro
        acertou = "_" not in letras_acertadas

        imprime_mensagem_rodada(enforcou, acertou, palavra_secreta, letras_acertadas)

    imprime_mensagem_fim()


def imprime_mensagem_abertura():
    print("*********************************")
    print("*******  Jogo de Forca   ********")
    print("*********************************\n")

def imprime_mensagem_fim():
    print("\n*********************************")
    print("           Fim de jogo")
    print("*********************************\n")

def imprime_mensagem_err_chute(tentativas_restantes):
    # print("a letra '{}' não existe na palavra secreta".format(chute))
    #
    # if tentativas_restantes > 0:
    #     print("Resta(m) {} tentativa(s)".format(tentativas_restantes))
    print("  _______     ", tentativas_restantes)
    print(" |/      |    ")

    if(tentativas_restantes == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas_restantes == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas_restantes == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas_restantes == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas_restantes == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas_restantes == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas_restantes == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
def imprime_mensagem_rodada(enforcou, acertou, palavra_secreta, letras_acertadas):
    print("\n", letras_acertadas)

    if enforcou:
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
    if acertou:
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
def selecionar_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    lista_palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        lista_palavras.append(linha)

    arquivo.close()

    indice_aleatorio = random.randrange(0, len(lista_palavras))
    return lista_palavras[indice_aleatorio]

def inicializar_letras_acertadas(palavra):
    palavra = ["_" for letra in palavra]
    print("A palavra a ser descoberta é: {}".format(palavra))
    return palavra

def solicitar_palpite():
    return input("Qual letra? ").strip().upper()

def tratar_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra.upper()
        index += 1
    return letras_acertadas

if __name__ == "__main__":
    jogar()
