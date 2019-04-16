# -*- coding: utf-8 -*-

"""
    Classe que representa a partícula do enxame de partículas
"""

from random import randrange

class Particula:

    def __init__(self, posicao: list = None, velocidade: list = None, dominioX1: tuple = None, dominioX2: tuple = None):
        self.dominioX1 = dominioX1 if dominioX1 != None else (-100, 100)
        self.dominioX2 = dominioX2 if dominioX2 != None else (-100, 100)
        self.posicao = posicao if dominioX1 != None else self.geraParticulaAleatorio(self.dominioX1, self.dominioX2)
        self.velocidade = velocidade if velocidade != None else (-self.dominioX1[1]*0.15, self.dominioX2[1]*0.15)
        self.pbest = self.posicao

    # Getters e Setters da classe
    def getParticula(self) -> list:
        return self.posicao

    def getVelocidade(self) -> list:
        return self.velocidade

    def getPbest(self) -> list:
        return self.pbest

    #Atualiza a velocidade da atual partícula.
    def atualizarVelocidade(self, gbest: list) -> list:
        q1 = 0.5            #constante q1.
        q2 = 0.8            #constante q2.
        x1 = randrange(0,1) # rand¹ da formula.
        x2 = randrange(0,1) # rand² da formula.

        v0 = self.velocidade[0] + q1 * x1 * (self.pbest[0] - self.posicao[0]) +  q2*x2(gbest[0] - self.posicao[0])
        v1 = self.velocidade[1] + q1 * x1 * (self.pbest[1] - self.posicao[1]) +  q2*x2(gbest[1] - self.posicao[1])
        
        #verificando melhores velocidades.
        if(self.velocidade[0] > v0):
            self.velocidade[0] = v0
        if(self.velocidade[1] < v1):
            self.velocidade[1] = v1

        return self

    #Atualização da posição de acordo com a nova velocidade.
    def atualizarPosicao(self):
        self.posicao[0] = self.velocidade[0] + self.posicao[0]
        self.posicao[1] = self.velocidade[1] + self.posicao[1]

        return self

    def schafferFunction(self, particula):
        x = ((((particula[0])** 2 + (particula[1])**2) ** 2) ** 0.5)
        y = (1 + 0.001 * (particula[0]**2 + particula[1]**2))**2
        fx = 0, 5 + (x / y)
        
        return fx

    def geraParticulaAleatorio(self, dominioX1, dominioX2):
        x1 = randrange(self.dominioX1[0], self.dominioX1[1])
        x2 = randrange(self.dominioX2[0], self.dominioX2[1])
        particula = (x1, x2)

        return particula

    def verificaParticula(self, dominio, particula):
        verify = 1
        if (particula[0] > self.dominioX1[0] or particula[1] > self.dominioX2[1]) :
            verify = 0

        return verify