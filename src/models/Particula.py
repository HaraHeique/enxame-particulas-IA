# -*- coding: utf-8 -*-

"""
    Classe que representa a partícula do enxame de partículas
"""

from random import randrange, uniform
from math import sin

class Particula :

    def __init__(self, posicao: list = None, velocidade: list = None, dominioX1: tuple = None, dominioX2: tuple = None, dominioVelocidade: tuple = None) :
        self._dominioX1: tuple = dominioX1 if dominioX1 != None else (-100, 100)
        self._dominioX2: tuple = dominioX2 if dominioX2 != None else (-100, 100)
        self._dominioVelocidade: tuple = dominioVelocidade if dominioVelocidade != None else (-15, 15)
        self._posicao: list = posicao if dominioX1 != None else self.__geraParticulaAleatorio()
        self._velocidade: list = velocidade if velocidade != None else [-self._dominioX1[1] * 0.15, self._dominioX2[1] * 0.15]
        self._aptidao: float = self.__schafferFunction()
        self._pbest: dict = { "posicao": self._posicao[:], "aptidao": self._aptidao }

    @property
    def posicao(self) -> list :
        return self._posicao

    @property
    def velocidade(self) -> list :
        return self._velocidade

    @property
    def pbest(self) -> dict :
        return self._pbest

    @property
    def aptidao(self) -> float :
        return self._aptidao

    # Atualiza a velocidade da atual partícula.
    def atualizarVelocidade(self, gbest: dict) :
        Q1: float = 0.5            # constante q1.
        Q2: float = 0.8            # constante q2.
        x1: float = uniform(0,1) # rand¹ da formula.
        x2: float = uniform(0,1) # rand² da formula.

        # Atualiza as velocidades
        # v1: float = self._velocidade[0] + Q1 * x1 * (self._pbest._posicao[0] - self._posicao[0]) +  Q2 * uniform(0, gbest._posicao[0] - self._posicao[0])
        # v2: float = self._velocidade[1] + Q1 * x1 * (self._pbest._posicao[1] - self._posicao[1]) +   Q2 * uniform(0, gbest._posicao[1] - self._posicao[1])
        v1: float = self._velocidade[0] + Q1 * x1 * (self._pbest["posicao"][0] - self._posicao[0]) + Q2 * x2 * (gbest["posicao"][0] - self._posicao[0])
        v2: float = self._velocidade[1] + Q1 * x1 * (self._pbest["posicao"][1] - self._posicao[1]) + Q2 * x2 * (gbest["posicao"][1] - self._posicao[1])
        
        # Atualiza a velocidade caso ela passa do limite implicado no domínio
        self._velocidade[0] = self.__atualizaVelocidadeNoLimite(v1)
        self._velocidade[1] = self.__atualizaVelocidadeNoLimite(v2)

        return self

    # Atualização da posição de acordo com a nova velocidade.
    def atualizarPosicao(self) :
        x1: float = self._velocidade[0] + self._posicao[0]
        x2: float = self._velocidade[1] + self._posicao[1]

        # Atualiza a posição caso ela passa do limite implicado no domínio caso contrário fica com mesmo valor
        self._posicao[0] = self.__atualizaPosicaoX1NoLimite(x1)
        self._posicao[1] = self.__atualizaPosicaoX2NoLimite(x2)

        return self

    # Atualização da aptidão a partir do cálculo de Schaffer
    def atualizarAptidao(self) :
        fp: float = self.__schafferFunction()
        self._aptidao = fp

        return self

    # Atualização do pbest a partir do valor de aptidão
    def atualizarPbest(self) :
        if (self._aptidao < self.pbest["aptidao"]) :
            self._pbest["posicao"] = self._posicao[:]
            self._pbest["aptidao"] = self._aptidao

        return self

    # Realiza o cálculo de Scaffer para saber a aptidão da partícula
    def __schafferFunction(self) -> float :
        x: float = (sin(((self._posicao[0]**2) + (self._posicao[1]**2))**0.5)**2) - 0.5
        y: float = (1 + (0.001 * ((self._posicao[0]**2) + (self._posicao[1]**2))))**2
        fp: float = 0.5 + (x / y)
        
        return fp

    # Gera a partícula de forma aleatória a partir do domínio
    def __geraParticulaAleatorio(self) -> list:
        x1: float = randrange(self._dominioX1[0], self._dominioX1[1] + 1)
        x2: float = randrange(self._dominioX2[0], self._dominioX2[1] + 1)
        particula: list = [x1, x2]

        return particula

    # Atualiza a velocidade caso esteja fora do limite do domínio definido
    def __atualizaVelocidadeNoLimite(self, valor: float) :
        if (valor < self._dominioVelocidade[0]) :
            return self._dominioVelocidade[0]
        elif (valor > self._dominioVelocidade[1]) :
            return self._dominioVelocidade[1]
        
        return valor
    
    # Atualização da posição X1 caso esteja fora do limite do domínio definido
    def __atualizaPosicaoX1NoLimite(self, valorPos: float) -> float :
        # OBS.: Tem que atualizar a velocidade também para zero caso ocorra quebra de limites
        if (valorPos < self._dominioX1[0]) :
            self._velocidade[0] = 0
            return self._dominioX1[0]

        elif (valorPos > self._dominioX1[1]) :
            self._velocidade[0] = 0
            return self._dominioX1[1]
        
        return valorPos

    # Atualização da posição X2 caso esteja fora do limite do domínio definido
    def __atualizaPosicaoX2NoLimite(self, valorPos: float) -> float :
        # OBS.: Tem que atualizar a velocidade também para zero caso ocorra quebra de limites
        if (valorPos < self._dominioX2[0]) :
            self._velocidade[1] = 0
            return self._dominioX2[0]
        elif (valorPos > self._dominioX2[1]) :
            self._velocidade[1] = 0
            return self._dominioX2[1]
        
        return valorPos
        
