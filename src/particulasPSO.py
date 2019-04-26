# -*- coding: utf-8 -*-

"""
    Lida com a lógica de geração das partículas e cálculos do algoritmo usando
    a classe Particula
"""

from models.Particula import Particula
from operator import attrgetter

# Lógica que recebe o número de partículas e as cria de forma aleatória
def criarParticulas(numParticulas: int) -> list :
    particulas: list = []
    numParticulasGeradas: int = 0

    # Gerando as particulas de forma aleatória
    while numParticulasGeradas < numParticulas :
        particulas.append(Particula())
        numParticulasGeradas += 1

    return particulas

# Retorna uma lista de gBests a partir das particulas e a quantidade de iterações passadas como argumento
def getGbestsPorIteracao(particulas: list, numIteracoes: int) -> list :
    contadorIteracoes: int = 0
    lstGbests: list = []

    while (contadorIteracoes < numIteracoes) :
        lstPbests: list = []

        # Iterando sobre cada partícula da população atualizando sua aptidão pelo cálcula de schaffer e o seu pBest
        for i in range(len(particulas)) :
            particula: Particula = particulas[i]
            
            # Faz as atualizações necessárias de cada partícula em cada iteração
            particula.atualizarAptidao()
            particula.atualizarPbest()

            # Guarda as partículas pBests para depois pegar o melhor pbest de todos que no caso é o gBest
            lstPbests.append(particula.pbest)

        # Pega o melhor pBest de todos os pBests e faz uma shallow copy da sua instância atual, para ficar com o seu histórico de informações
        gBestCorrente: dict = getGBest(lstPbests)

        # Adiciona na lista de gBests a cópia do obj do melhor pBest referente a iteração corrente
        lstGbests.append(gBestCorrente)
        
        # Cálculo de ponderação da velocidade por iteração
        w: float = __calculoReducaoLinearPonderacaoInercia(contadorIteracoes+1, numIteracoes)
		
        # Iterando novamente sobre os indivíduos da população, porém atualizando velocidade e posição de acordo com o gBest encontrado
        for i in range(len(particulas)) :
            particula: Particula = particulas[i]
            particula.atualizarVelocidade(gBestCorrente, w)
            particula.atualizarPosicao()
			
        contadorIteracoes += 1
        
    return lstGbests

# Pega a partícula com melhor pBest, ou seja, o gBest
def getGBest(pBests: list) -> dict :
    return min(pBests, key=lambda x:x['aptidao'])

# Printa as partículas gBest de forma organizada e alinhada
def printGBests(lstGBests: list) -> None :
    print('\n')
    for dic in lstGBests :
        espacamento = " " * (50 - len(str(dic['posicao'])))
        print("Posição: {0}{1}Aptidão: {2}".format(dic['posicao'], espacamento, dic['aptidao']))
    print('\n')
    return

# Lógica que recebe uma lista de Gbest e retorna a média.
def calculaMediaGbest(lstGbests: list) -> float:
    somatorio: float = sum(item['aptidao'] for item in lstGbests)
    numElementos: int = len(lstGbests)

    return somatorio / numElementos

# Lógica do Desvio padrão calculado em cima do Gbest.
def calculaDesvioPadraoGbest(lstGbests: list, mediaAritmetica: float = None) -> float :
    mediaAritmetica = calculaMediaGbest(lstGbests) if (mediaAritmetica == None) else mediaAritmetica
    somatorio: float = sum((item['aptidao'] - mediaAritmetica)**2 for item in lstGbests)
    numElementos: int = len(lstGbests)

    return (somatorio / numElementos)**0.5

# Calcula a a ponderação para cada iteração no cálculo da velocidade
def __calculoReducaoLinearPonderacaoInercia(iteracaoCorrente: int, iteracaoMax: int) :
	wmax: float = 0.9
	wmin: float = 0.4
	w: float = wmax - iteracaoCorrente * ((wmax - wmin)/iteracaoMax)
	
	return w 
	
	
# Para testes do módulo
if __name__ == '__main__' :
    particulas: list = criarParticulas(20)
    particulasGBest: list = getGbestsPorIteracao(particulas, 100)
    printGBests(particulasGBest)
    
