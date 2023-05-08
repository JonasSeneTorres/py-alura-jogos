import adivinhacao
import forca

def selecionar_jogo():
    jogo_selecionado = False
    jogo_adivinhacao = "1"
    jogo_forca = "2"

    print("*********************************")
    print("******* Escolha seu jogo ********")
    print("*********************************\n")

    while ( not jogo_selecionado):
        print("Selecione um jogo: \n(1) adivinhacao, (2) forca")
        jogo = input("Qual jogo: ")

        if (jogo == jogo_adivinhacao):
            adivinhacao.jogar()
        elif (jogo == jogo_forca):
            forca.jogar()
        else:
            continue
        jogo_selecionado = True

if __name__ == "__main__":
    selecionar_jogo()