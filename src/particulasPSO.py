# -*- coding: utf-8 -*-

"""
    Lida com a lógica de geração das partículas e cálculos do algoritmo usando
    a classe Particula
"""

from models.Particula import Particula

# Lógica que recebe o número de partículas e as cria de forma aleatória
def criarParticulas(numParticulas: int) -> list :
    particulas: list = []
    numParticulasGeradas: int = 0

    # Gerando as particulas de forma aleatória
    while numParticulasGeradas < numParticulas :
        particulas.append(Particula())
        numParticulasGeradas += 1

    return particulas

# if __name__ == '__main__':
    