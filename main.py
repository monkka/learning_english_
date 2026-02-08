import random

# Banco de dados com 50 palavras essenciais para turistas
# Formato: [Inglês, Português]
vocabulario = [
    ["Hello", "Ola"], ["Good morning", "Bom dia"], ["Good night", "Boa noite"],
    ["Please", "Por favor"], ["Thank you", "Obrigado"], ["Excuse me", "Com licenca"],
    ["Sorry", "Desculpe"], ["Yes", "Sim"], ["No", "Nao"], ["Help", "Ajuda"],
    ["Water", "Agua"], ["Food", "Comida"], ["Bread", "Pao"], ["Coffee", "Cafe"],
    ["Milk", "Leite"], ["Beer", "Cerveja"], ["Wine", "Vinho"], ["Bill", "Conta"],
    ["Hotel", "Hotel"], ["Room", "Quarto"], ["Bathroom", "Banheiro"], ["Toilet", "Privada"],
    ["Airport", "Aeroporto"], ["Taxi", "Taxi"], ["Bus", "Onibus"], ["Train", "Trem"],
    ["Ticket", "Bilhete"], ["Street", "Rua"], ["Store", "Loja"], ["Market", "Mercado"],
    ["Money", "Dinheiro"], ["Bank", "Banco"], ["Beach", "Praia"], ["City", "Cidade"],
    ["Left", "Esquerda"], ["Right", "Direita"], ["Straight", "Direto"], ["Near", "Perto"],
    ["Far", "Longe"], ["Now", "Agora"], ["Today", "Hoje"], ["Tomorrow", "Amanha"],
    ["Time", "Hora"], ["Open", "Aberto"], ["Closed", "Fechado"], ["Price", "Preco"],
    ["Cheap", "Barato"], ["Expensive", "Caro"], ["Friend", "Amigo"], ["Police", "Policia"]
]

# Separando as listas para manter a estrutura do seu código original
eng_words = [item[0] for item in vocabulario]
pt_words = [item[1] for item in vocabulario]
score = 0

print("--- SISTEMA DE APRENDIZADO DE INGLÊS ---")
mode = input("Selecione: 0 (Adicionar) ou 1 (Treinamento): ")

while mode not in ['0', '1']:
    mode = input("Invalido! Escolha 0 ou 1: ")

if mode == "1":
    print("\nTraduza as palavras! (10 rodadas)")
    
    for i in range(10):
        # Sorteia um número entre 0 e o total de palavras que temos
        indice = random.randint(0, len(eng_words) - 1)
        
        pergunta = eng_words[indice]
        resposta_correta = pt_words[indice].lower()
        
        tentativa = input(f"{i+1}. Como traduzir '{pergunta}'? ").lower()
        
        if tentativa == resposta_correta:
            print("Muito bem! ✨")
            score += 1
        else:
            print(f"Errado. A resposta era: {pt_words[indice]}")

    print(f"\nTreino finalizado! Pontuacao: {score}/10")

else:
    print("\n--- ADICIONAR NOVA PALAVRA ---")
    nova_pt = input("Palavra em Português: ")
    nova_en = input("Tradução em Inglês: ")

    if nova_pt and nova_en:
        pt_words.append(nova_pt)
        eng_words.append(nova_en)
        print(f"'{nova_en}' adicionada com sucesso!")
