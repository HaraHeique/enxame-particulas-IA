# -*- coding: utf-8 -*-

"""
    Lida com a lógica de geração das partículas e cálculos do algoritmo usando
    a classe Particula
"""

from src.models.Particula import Particula

# Lógica que recebe o número de partículas e as cria de forma aleatória
def criarParticulas(numParticulas: int) -> list :
    particulas: list = []

    # Gerando as particulas de forma aleatória
    for posParticula in range(numParticulas) :
        particulas.append(Particula())

    return particulas