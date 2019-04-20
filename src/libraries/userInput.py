# -*- coding: utf-8 -*-

"""
    Responsável por lidar com a entrada de dados do usuário especificamente para as partículas PSO
"""

# Determina o número de indivíduos da população que é fornecida pela entrada do usuário
def qntParticulas() -> int :
    while (True) :
        numParticulasInput: str = input("Insira o número de partículas da população a ser estudada: ")

        if (__tryParseIntPositive(numParticulasInput)) :
            return int(numParticulasInput)

# Pega o número de iterações que é o critério de parada do algoritmo e é fornecida pelo usuário
def qntIteracoesPorParticula() -> int :
    while (True) :
        numInteracoesInput: str = input("Insira o número de iterações de cada partícula na população: ")

        if (__tryParseIntPositive(numInteracoesInput)) :
            return int(numInteracoesInput)

# Checa se a string passa é possível de converter para um inteiro positivo
def __tryParseIntPositive(strInt: str) -> bool :
    if (not strInt.isdigit() or int(strInt) < 0) :
        print("Favor digite um valor inteiro válido e positivo!")
        return False

    return True