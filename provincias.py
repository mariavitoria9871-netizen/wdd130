def main():

    # Cria uma lista vazia
    provincias = []

    # Abre o arquivo para leitura
    with open("provincias.txt", "rt", encoding="utf-8") as arquivo:

        # Lê cada linha do arquivo
        for linha in arquivo:

            # Remove espaços e quebra de linha
            linha_limpa = linha.strip()

            # Adiciona na lista
            provincias.append(linha_limpa)

    # Remove o primeiro elemento
    provincias.pop(0)

    # Remove o último elemento
    provincias.pop()

    # Substitui "AB" por "Alberta"
    for i in range(len(provincias)):
        if provincias[i] == "AB":
            provincias[i] = "Alberta"

    # Exibe a lista
    print(provincias)

    # Conta quantas vezes Alberta aparece
    quantidade = provincias.count("Alberta")

    # Exibe o resultado
    print(f"Alberta aparece {quantidade} vezes na lista modificada.")


# Inicia o programa
if __name__ == "__main__":
    main()