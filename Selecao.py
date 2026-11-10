# Programa para armazenar informações sobre uma seleção

nomeselecao = input("Nome da seleção: ")
qtdtitulos = int(input("Quantidade de títulos: "))
posranking = int(input("Posição no ranking: "))
resposta = input("Está classificada para a Copa? (sim/não): ").strip().lower()

classificacopa = resposta == "sim"

print()
print("--- Informações da seleção ---")
print(f"Nome: {nomeselecao}")
print(f"Títulos: {qtdtitulos}")
print(f"Posição no ranking: {posranking}")

if classificacopa:
    print("Classificada para a Copa: Sim")
else:
    print("Classificada para a Copa: Não")
