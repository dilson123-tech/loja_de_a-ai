from menu import mostrar_cardapio, pedir_opcao
from calculo import calcular_preco

def main():
    mostrar_cardapio()
    tamanho = pedir_opcao("Escolha o tamanho (1, 2 ou 3): ", ['1','2','3'])
    sabor = pedir_opcao("Escolha o sabor (a, b ou c): ", ['a','b','c'])
    
    while True:
        try:
            quantidade = int(input("Quantos açaís deseja? "))
            if quantidade > 0:
                break
            else:
                print("Digite um número maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    preco_total = calcular_preco(tamanho, quantidade)

    sabores_dict = {'a': 'Morango', 'b': 'Uva', 'c': 'Cupuaçu'}
    tamanhos_dict = {'1': 'Pequeno', '2': 'Médio', '3': 'Grande'}

    print("\n=== Resumo do Pedido ===")
    print(f"Tamanho: {tamanhos_dict[tamanho]}")
    print(f"Sabor: {sabores_dict[sabor]}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço total: R${preco_total:.2f}")

if __name__ == "__main__":
    main()
