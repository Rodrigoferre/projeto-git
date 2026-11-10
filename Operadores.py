pontos = 7
vitorias = 2
saldo_gols = 4

if pontos > 5:
    print("A selecao possui mais de 5 pontos")
else:
    print("A selecao nao possui mais de 5 pontos")
if vitorias == 3:
    print("A selecao possui 3 vitorias")
else:
    print ("A selecao nao possui 3 vitorias")
if saldo_gols >= 0:
    print ("Saldo maior")
else:
    print ("Saldo menor")
if pontos > 5 and saldo_gols > 0:
    print ("Pontos e saldo bom")
else:
    print ("Precisa melhorar")
if vitorias == 3 or pontos > 6:
    print("Sim")
else:
    print("Nao")