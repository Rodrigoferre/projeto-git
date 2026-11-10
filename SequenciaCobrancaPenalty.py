gols = 0

for cobranca in range (5):
        resposta = input("Resultado da cobrança: (gol ou perdeu): ").strip().lower()
        while resposta != "gol" and resposta != "perdeu":
            print("Opção não reconhecida.")
            resposta = input("Resultado da cobrança: gol ou perdeu? ").strip().lower()

        
        if resposta == "gol":
            gols += 1
        
if gols in (4,5):
     print ("Ótimo desempenho nos pênaltis!")
elif gols in (2,3):
     print ("Desempenho regular nos pênaltis.")
else:
     print ("Desempenho ruim nos pênaltis.")

print(f"Total de gols marcados?: {gols}")
