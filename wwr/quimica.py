try:
    from formula import interpretar_formula
except ImportError:
    def interpretar_formula(formula):
        resultado = []
        i = 0

        while i < len(formula):
            simbolo = formula[i]
            i += 1

            if i < len(formula) and formula[i].islower():
                simbolo += formula[i]
                i += 1

            quantidade = ""
            while i < len(formula) and formula[i].isdigit():
                quantidade += formula[i]
                i += 1

            if quantidade == "":
                quantidade = 1
            else:
                quantidade = int(quantidade)

            resultado.append([simbolo, quantidade])

        return resultado


def criar_tabela_periodica():
    dic_da_tabela_periodica = {
        "H": ["Hidrogênio", 1.00794],
        "He": ["Hélio", 4.002602],
        "Li": ["Lítio", 6.941],
        "Be": ["Berílio", 9.012182],
        "B": ["Boro", 10.811],
        "C": ["Carbono", 12.0107],
        "N": ["Nitrogênio", 14.0067],
        "O": ["Oxigênio", 15.9994],
        "F": ["Flúor", 18.9984032],
        "Ne": ["Néon", 20.1797],
        "Na": ["Sódio", 22.98976928],
        "Mg": ["Magnésio", 24.305],
        "Al": ["Alumínio", 26.9815386],
        "Si": ["Silício", 28.0855],
        "P": ["Fósforo", 30.973762],
        "S": ["Enxofre", 32.065],
        "Cl": ["Cloro", 35.453],
        "Ar": ["Argônio", 39.948],
        "K": ["Potássio", 39.0983],
        "Ca": ["Cálcio", 40.078],
        "Sc": ["Escândio", 44.955912],
        "Ti": ["Titânio", 47.867],
        "V": ["Vanádio", 50.9415],
        "Cr": ["Cromo", 51.9961],
        "Mn": ["Manganês", 54.938045],
        "Fe": ["Ferro", 55.845],
        "Co": ["Cobalto", 58.933195],
        "Ni": ["Níquel", 58.6934],
        "Cu": ["Cobre", 63.546],
        "Zn": ["Zinco", 65.38],
        "Ga": ["Gálio", 69.723],
        "Ge": ["Germânio", 72.64],
        "As": ["Arsênico", 74.9216],
        "Se": ["Selênio", 78.96],
        "Br": ["Bromo", 79.904],
        "Kr": ["Criptônio", 83.798],
        "Rb": ["Rubídio", 85.4678],
        "Sr": ["Estrôncio", 87.62],
        "Y": ["Ítrio", 88.90585],
        "Zr": ["Zircônio", 91.224],
        "Nb": ["Nióbio", 92.90638],
        "Mo": ["Molibdênio", 95.96],
        "Tc": ["Tecnécio", 98],
        "Ru": ["Rutênio", 101.07],
        "Rh": ["Ródio", 102.9055],
        "Pd": ["Paládio", 106.42],
        "Ag": ["Prata", 107.8682],
        "Cd": ["Cádmio", 112.411],
        "In": ["Índio", 114.818],
        "Sn": ["Estanho", 118.71],
        "Sb": ["Antimônio", 121.76],
        "Te": ["Telúrio", 127.6],
        "I": ["Iodo", 126.90447],
        "Xe": ["Xenônio", 131.293],
        "Cs": ["Césio", 132.9054519],
        "Ba": ["Bário", 137.327],
        "La": ["Lantânio", 138.90547],
        "Ce": ["Cério", 140.116],
        "Pr": ["Praseodímio", 140.90765],
        "Nd": ["Neodímio", 144.242],
        "Pm": ["Promécio", 145],
        "Sm": ["Samário", 150.36],
        "Eu": ["Európio", 151.964],
        "Gd": ["Gadolínio", 157.25],
        "Tb": ["Térbio", 158.92535],
        "Dy": ["Disprósio", 162.5],
        "Ho": ["Hólmio", 164.93032],
        "Er": ["Érbio", 167.259],
        "Tm": ["Túlio", 168.93421],
        "Yb": ["Itérbio", 173.054],
        "Lu": ["Lutécio", 174.9668],
        "Hf": ["Háfnio", 178.49],
        "Ta": ["Tântalo", 180.94788],
        "W": ["Tungstênio", 183.84],
        "Re": ["Rênio", 186.207],
        "Os": ["Ósmio", 190.23],
        "Ir": ["Irídio", 192.217],
        "Pt": ["Platina", 195.084],
        "Au": ["Ouro", 196.966569],
        "Hg": ["Mercúrio", 200.59],
        "Tl": ["Tálio", 204.3833],
        "Pb": ["Chumbo", 207.2],
        "Bi": ["Bismuto", 208.9804],
        "Po": ["Polônio", 209],
        "At": ["Ástato", 210],
        "Rn": ["Radônio", 222],
        "Fr": ["Frâncio", 223],
        "Ra": ["Rádio", 226],
        "Ac": ["Actínio", 227],
        "Th": ["Tório", 232.03806],
        "Pa": ["Protactínio", 231.03588],
        "U": ["Urânio", 238.02891],
        "Np": ["Neptúnio", 237],
        "Pu": ["Plutônio", 244]
    }

    return dic_da_tabela_periodica


def calcular_massa_molar(lista_quantidade_simbolos, dic_da_tabela_periodica):
    massa_total = 0

    for item in lista_quantidade_simbolos:
        simbolo = item[0]
        quantidade = item[1]
        massa_atomica = dic_da_tabela_periodica[simbolo][1]
        massa_total += massa_atomica * quantidade

    return massa_total


def main():
    formula = input("Insira a fórmula molecular da amostra: ")
    massa_amostra = float(input("Insira a massa em gramas da amostra: "))

    dic_da_tabela_periodica = criar_tabela_periodica()
    lista_quantidade_simbolos = interpretar_formula(formula)

    massa_molar = calcular_massa_molar(
        lista_quantidade_simbolos,
        dic_da_tabela_periodica
    )

    numero_mols = massa_amostra / massa_molar

    print(f"{massa_molar} gramas/mol")
    print(f"{numero_mols:.5f} mols")


if __name__ == "__main__":
    main()