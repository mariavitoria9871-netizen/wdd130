# Copyright 2020, Brigham Young University-Idaho. Todos os direitos reservados.

"""
Este programa solicita ao usuário:
1) o nome de um arquivo de texto
2) o  número de uma linha
e imprime o texto dessa linha do arquivo.
"""
def main():
    try:
        # Solicita ao usuário o nome de um arquivo.
        nome_arquivo = input("Digite o nome do arquivo de texto: ")

        # Lê o arquivo de texto especificado pelo usuário em uma lista.
        linhas_texto = ler_lista(nome_arquivo)

        # Solicita ao usuário o  número de uma linha.
        num_linha = int(input("Digite o número da linha: "))

        # Obtém a linha solicitada pelo usuário a partir da lista.
        linha = linhas_texto[num_linha - 1]

        # Imprime a linha solicitada.
        print()
        print(linha)

    except FileNotFoundError as erro_arquivo_nao_encontrado:
        # Esse código será executado se o usuário informar o nome de um arquivo que não existe.
        print()
        print(type(erro_arquivo_nao_encontrado).__name__, erro_arquivo_nao_encontrado, sep=": ")
        print(f"O arquivo {nome_arquivo} não existe.")
        print("Execute o programa novamente e digite o nome de um arquivo existente.")

    except PermissionError as erro_permissao:
        # Esse código será executado se o usuário informar um arquivo que ele não tem permissão para ler.
        print()
        print(type(erro_permissao).__name__, erro_permissao, sep=": ")
        print(f"Você não tem permissão para ler {nome_arquivo}.")
        print("Execute o programa novamente e digite o nome de um arquivo que possa ser lido.")

    except ValueError as erro_valor:
        # Esse código será executado se o usuário digitar o número de uma linha que não seja inteiro.
        print()
        print(type(erro_valor).__name__, erro_valor, sep=": ")
        print("Você digitou um número inválido para a linha.")
        print("Execute o programa novamente e digite um número inteiro para o número da linha.")

    except IndexError as erro_indice:
        # Esse código será executado se o usuário digitar um número válido, mas maior que o total de linhas.
        print()
        print(type(erro_indice).__name__, erro_indice, sep=": ")
        total_linhas = len(linhas_texto)
        if num_linha < 0:
            print(f"{num_linha} é um número negativo.")
        else:
            print(f"{num_linha} é maior que o número de linhas em {nome_arquivo}.")
            print(f"Há apenas {total_linhas} linhas em {nome_arquivo}.")
        print(f"Execute o programa novamente e digite um número de linha entre 1 e {total_linhas}.")

    except Exception as excecao:
        # Esse código será executado se ocorrer algum outro tipo de exceção.
        print()
        print(type(excecao).__name__, excecao, sep=": ")


def ler_lista(nome_arquivo):
    """Lê o conteúdo de um arquivo de texto para uma lista
    e retorna a lista contendo as linhas de texto.

    Parâmetro nome_arquivo: nome do arquivo de texto a ser lido
    Retorno: lista de strings
    """
    # Cria uma lista vazia chamada linhas_texto.
    linhas_texto = []

# Abra o arquivo de texto para leitura e armazena uma referência
# ao arquivo aberto em uma variável chamada arquivo_texto.
    with open(nome_arquivo, "rt", encoding="utf-8") as arquivo_texto:

        # Lê o conteúdo do arquivo uma linha por vez.
        for linha in arquivo_texto:

            # Remove espaços em branco do início e do fim da linha caso existam.
            linha_limpa = linha.strip()

            # Adiciona a linha de texto limpa no final da lista.
            linhas_texto.append(linha_limpa)

    # Retorna a lista com as linhas de texto.
    return linhas_texto


# Se este arquivo for executado diretamente:
# > python solucao_professor.py
# então chama a função main(). Caso seja importado, não executa.
if __name__ == "__main__":
    main()
