# -*- coding: utf-8 -*-

"""
    Classe que representa a partícula do enxame de partículas
"""

from random import randrange

class Particulas:

    def __init__(self, x1x2, v1v2):
        self.x1x2 = x1x2
        self.v1v2 = v1v2
        self.pbest = self.schafferFunction(x1x2)

    # Getters e Setters da classe
    def getParticula(self):
        return self.x1x2

    def getVelocidade(self):
        return self.v1v2

    def getPbest(self):
        return self.pbest

    #Atualiza a velocidade da atual partícula.
    def atualizarVelocidade(self,gbest):
        q1 = 0.5            #constante q1.
        q2 = 0.8            #constante q2.
        x1 = randrange(0,1) # rand¹ da formula.
        x2 = randrange(0,1) # rand² da formula.

        v0 = self.v1v2[0] + q1 * x1 * (self.pbest[0] - self.x1x2[0]) +  q2*x2(gbest[0] - self.x1x2[0])
        v1 = self.v1v2[1] + q1 * x1 * (self.pbest[1] - self.x1x2[1]) +  q2*x2(gbest[1] - self.x1x2[1])
        
        #verificando melhores velocidades.
        if(self.v1v2[0] > v0):
            self.v1v2[0] = v0
        if(self.v1v2[1]< v1):
            self.v1v2[1] = v1

        return self

    #Atualização da posição de acordo com a nova velocidade.
    def atualizarPosicao(self):
        self.x1x2[0] = self.v1v2[0]+self.x1x2[0]
        self.x1x2[1] = self.v1v2[1] + self.x1x2[1]
        return self

    def schafferFunction(self, particula):
        x = ((((particula[0])** 2 + (particula[1])**2) ** 2) ** 0.5)
        y = (1 + 0.001 * (particula[0]**2 + particula[1]**2))**2
        fx = 0, 5 + (x / y)
        return fx

    def geraAleatorio(dominioX1, dominioX2):
        x1 = randrange(dominioX1[0], dominioX1[1])
        x2 = randrange(dominioX2[0], dominioX2[1])
        return (x1, x2)

    def verificaParticula(dominio, particula):
        verify = 1
        if (particula[0] > dominio[0] or particula[1] > dominio[1]) :
            verify = 0
        return verify