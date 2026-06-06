# Melhoria adicionada:
# O programa imprime um cupom de desconto no final do recibo
# para um dos produtos comprados pelo cliente.

import csv
from datetime import datetime


def ler_dicionario(filename, indice_coluna_chave):
    """Lê um arquivo CSV e retorna um dicionário."""

    dicionario = {}

    with open(filename, "rt") as arquivo:
        leitor = csv.reader(arquivo)

        next(leitor)

        for linha in leitor:
            chave = linha[indice_coluna_chave]
            dicionario[chave] = linha

    return dicionario


def main():
    try:
        produtos = ler_dicionario("produtos.csv", 0)

        print("Empório Inkom")
        print()

        numero_itens = 0
        subtotal = 0

        with open("pedido.csv", "rt") as pedido:
            leitor = csv.reader(pedido)

            next(leitor)

            for linha in leitor:
                num_prod = linha[0]
                quantidade = int(linha[1])

                infos_produto = produtos[num_prod]

                nome_produto = infos_produto[1]
                cupom = nome_produto
                preco = float(infos_produto[2])

                print(f"{nome_produto}: {quantidade} @ {preco:.2f}")

                numero_itens += quantidade
                subtotal += quantidade * preco

        imposto = subtotal * 0.06
        total = subtotal + imposto

        print()
        print(f"Número de itens: {numero_itens}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Imposto sobre vendas: {imposto:.2f}")
        print(f"Total: {total:.2f}")
        print()
        print("Obrigado por comprar no Empório Inkom.")

        data_atual = datetime.now()
        print(data_atual.strftime("%d/%m/%Y %H:%M"))

        print()
        print("===== CUPOM DE DESCONTO =====")
        print(f"Ganhe 10% de desconto na próxima compra de {cupom}!")
        print("Obrigado pela preferência!")

    except FileNotFoundError as erro:
        print("Erro: arquivo não encontrado")
        print(erro)

    except PermissionError as erro:
        print("Erro: permissão negada")
        print(erro)

    except KeyError as erro:
        print("Erro: produto desconhecido no arquivo pedido.csv")
        print(erro)


if __name__ == "__main__":
    main()