import os; os.system('cls')
import csv

def criar_dicionario_estudantes(arquivo_csv, chave_id, nome):
    dicionario = {}
    with open(arquivo_csv, "rt", encoding="utf-8") as arquivo_de_estudantes:
        leitor_de_arquivo = csv.reader(arquivo_de_estudantes)
        next(leitor_de_arquivo)

        for linha in leitor_de_arquivo:
            id_studente = linha[chave_id]
            dicionario[id_studente] = linha[nome]

    return dicionario

def main():
    INDICE_ID = 0
    INDICE_NOME = 1

    d_estudante = criar_dicionario_estudantes('estudantes.csv', INDICE_ID, INDICE_NOME)

    id = input("Por favor, informe qual o ID do estudante que você deseja saber o nome:")
    id = id.replace("-", "")

    if id in d_estudante:
        print(f"O nome do aluno é {d_estudante[id]}")
    elif not id.isdigit():
        print("Número de identificação inválido.")
    elif len(id) < 9:
        print("Número de identificação inválido: dígitos insuficientes.")
    elif len(id) > 9:
        print("Número de identificação inválido: ultrapassa o limite de digitos.")
    else:
        print("Estudante inexistente.")

if __name__ == '__main__':
    main()