def main():
    # Cria e exibe a lista de frutas
    lista_de_frutas = ["pêra", "banana", "maçã", "manga"]
    print(f"original: {lista_de_frutas}")

    # Inverte a lista
    lista_de_frutas.reverse()
    print(f"invertida: {lista_de_frutas}")

    # Adiciona laranja
    lista_de_frutas.append("laranja")
    print(f"anexação de laranja ao final: {lista_de_frutas}")

    # Insere cereja antes de maçã
    indice = lista_de_frutas.index("maçã")
    lista_de_frutas.insert(indice, "cereja")
    print(f"inserção de cereja: {lista_de_frutas}")

    # Remove banana
    lista_de_frutas.remove("banana")
    print(f"remoção de banana: {lista_de_frutas}")

    # Remove o último elemento (laranja)
    removida = lista_de_frutas.pop()
    print(f"remoção de {removida}: {lista_de_frutas}")

    # Ordena a lista
    lista_de_frutas.sort()
    print(f"ordenada: {lista_de_frutas}")

    # Limpa a lista
    lista_de_frutas.clear()
    print(f"vazia: {lista_de_frutas}")


if __name__ == "__main__":
    main()