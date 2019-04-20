# -*- coding: utf-8 -*-

"""
    Lida com a lógica de leitura e escrita de arquivos especificamente para o
    algoritmo PSO
"""

import os

# Variável global que armazena o local/diretório onde é guardado os arquivos
storeFilesPath: str = os.path.dirname(os.path.abspath(__file__)) + "/../files"

def writeGBestData(lstGbests: list, filename: str, numero_iteracoes: int) -> None :
    try :
        directoryStorage: str = "{0}/{1}_iteracoes/".format(storeFilesPath, numero_iteracoes)

        # Cria o diretório onde armazena a partir da quantidade de iterações
        if not os.path.exists(directoryStorage):
            os.makedirs(directoryStorage)

        with open(directoryStorage + filename, "w") as outfile :
            separador: str = ';'
            iteracao: int = 1

            cabecalho: tuple = ("Iteração", "Posição X1", "Posição X2", "Aptidão(fp)")
            outfile.write(separador.join(cabecalho) + '\n')
            for dicData in lstGbests :
                outfile.write("%d;%.16f;%.16f;%.16f\n" %(iteracao, dicData["posicao"][0], dicData["posicao"][1], dicData["aptidao"]))
                iteracao += 1
    except IOError :
        raise Exception("Não foi possível abrir o arquivo")