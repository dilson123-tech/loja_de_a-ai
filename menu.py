def mostrar_cardapio():
    print("=== Cardápio de Açaí ===")
    print("Tamanhos disponíveis:")
    print("1 - Pequeno (R$5,00)")
    print("2 - Médio (R$8,00)")
    print("3 - Grande (R$12,00)")
    print("\nSabores disponíveis:")
    print("a - Morango")
    print("b - Uva")
    print("c - Cupuaçu")
    print("=======================")

def pedir_opcao(mensagem, opcoes_validas):
    while True:
        escolha = input(mensagem).lower()
        if escolha in opcoes_validas:
            return escolha
        else:
            print("Opção inválida. Tente novamente.")
