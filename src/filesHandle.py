# -*- coding: utf-8 -*-

"""
    Lida com a lógica de leitura e escrita de arquivos especificamente para o
    algoritmo PSO
"""

import os
import shutil
import particulasPSO

# Variável global que armazena o local/diretório onde é guardado os arquivos
STORE_FILES_PATH: str = os.path.dirname(os.path.abspath(__file__)) + "/files"

def writeGBestData(lstGbests: list, filename: str, numero_iteracoes: int) -> None :
    try :
        directoryStorage: str = "{0}/{1}_iteracoes/".format(STORE_FILES_PATH, numero_iteracoes)

        # Cria o diretório onde armazena a partir da quantidade de iterações
        if not os.path.exists(directoryStorage) :
            os.makedirs(directoryStorage)

        with open(directoryStorage + filename, "w") as outfile :
            separador: str = ';'
            iteracao: int = 1

            # Escrevendo informações referente aos resultados de cada iteração
            cabecalho: tuple = ("Iteração", "Posição X1", "Posição X2", "Aptidão(fp)")
            outfile.write(separador.join(cabecalho) + '\n')
            for dicData in lstGbests :
                outfile.write("%d;%.16f;%.16f;%.16f\n" %(iteracao, dicData['posicao'][0], dicData['posicao'][1], dicData['aptidao']))
                iteracao += 1

            # Escrevendo o melhor gBest de todos os gBests escritos no arquivo
            bestGbestOfAll: dict = particulasPSO.getGBest(lstGbests)
            outfile.write("\nMelhor gBest:\n")
            outfile.write("Iteração: %d; Posição X1: %.16f; Posição X2: %.16f; Aptidão(fp): %.16f\n" %(lstGbests.index(bestGbestOfAll) + 1, bestGbestOfAll['posicao'][0], bestGbestOfAll['posicao'][1], bestGbestOfAll['aptidao']))

            # Escrevendo por final a média e desvio padrão da aptidão
            mediaGBests: float = particulasPSO.calculaMediaGbest(lstGbests)
            outfile.write("\nMédia(fp): %.16f\n" %(mediaGBests))
            outfile.write("Desvio Padrão(fp): %.16f\n" %(particulasPSO.calculaDesvioPadraoGbest(lstGbests, mediaGBests)))
    except IOError :
        raise Exception("Não foi possível abrir o arquivo.")

# Renomeia o arquivo de resultados passando a partir do número de iterações para pegar a sua pasta
def renameBestGBestFile(oldFileName: str, newFileName: str, numero_iteracoes: int) -> None :
    # Reescrevendo o arquivo no diretório onde se encontra todos os arquivos
    oldFileName = "{0}/{1}_iteracoes/{2}".format(STORE_FILES_PATH, numero_iteracoes, oldFileName)
    newFileName = "{0}/{1}_iteracoes/{2}".format(STORE_FILES_PATH, numero_iteracoes, newFileName)

    try :
        os.rename(oldFileName, newFileName)
    except IOError :
        raise Exception("Não foi possível renomear o arquivo. Provavelmente ele não existe.")

# Deleta todos os arquivo de uma determina pasta baseado no número de iterações
def deleteAllFilesGBest(numero_iteracoes: int) -> None :
    try :
        directoryDeleteFiles: str = "{0}/{1}_iteracoes/".format(STORE_FILES_PATH, numero_iteracoes)
        if (os.path.exists(directoryDeleteFiles)) :
            shutil.rmtree(directoryDeleteFiles)
    except IOError :
        raise Exception("Não foi possível apagar os arquivos. Provavelmente não existe a pasta.")