from math import pi

def main():
    nome_lata = "#1 Piquinique" 
    raio = 6.83
    altura = 10.16

    print("inicia o programa")
    volume = calcular_volume(raio, altura)
    print(f"Volume da lata {nome_lata} = {volume}")

    area = calcular_superficie(raio, altura)
    print(f"Área da lata f{nome_lata} = {area}")

    eficiencia =calcular_eficiencia(volume, area)
    print(f"A eficiência da lata {nome_lata} = {eficiencia}")

def calcular_volume(p_raio, p_altura):
    print("Calcula Volume")
    volume = pi * p_raio ** 2 * p_altura
    return volume

def calcular_superficie(p_raio, p_altura):
    print("Calcula Superfície")
    area = 2 * pi * p_raio * (p_raio + p_altura)
    return area


def calcular_eficiencia():
    print("Calcula Eficiência")

main()
