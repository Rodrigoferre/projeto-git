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