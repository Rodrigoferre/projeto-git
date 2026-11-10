posicaojogador = input("Informe a posição do jogador: ")

match posicaojogador:
    case "Goleiro":
        print ("Jogador que pode usar as mãos")
    case "Defesa":
        print ("Jogador que evita os gols")
    case "Meio":
        print ("Jogador que cria as jogadas")
    case "Ataque":
        print ("Jogador que faz gols")
    case _:
        print("Posição inválida")


resposta = "Sim"

while resposta == "Sim":
    print("Treino iniciado!")
    print("Deseja realizar outro treino?")
    if resposta != "Sim":
        print("Treino encerrado!")