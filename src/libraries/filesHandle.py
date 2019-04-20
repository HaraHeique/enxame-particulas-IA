# -*- coding: utf-8 -*-

"""
    Lida com a lógica de leitura e escrita de arquivos especificamente para o
    algoritmo PSO
"""
from src import particulasPSO
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


#Lógica para pegar o melhor Gbest.
def getMelhorGbest(lstGbest: list , nInteracoes: int) -> list:
    menor = 10000
    count = 0

    #Percorre a lista de gbests e pega o melhor.
    for dic in lstGbest:
        if(dic["aptidao"] < menor):
            menor = dic["aptidao"]
            iTxt = count #Armazena em qual arquivo ele foi encontrado.
        count +=1
    #
    nomeArq = 'execucao_'+ str(iTxt)+'.txt'
    path = "./files/"+str(nInteracoes)+"_iteracoes/"

    #Percorre o arquivo aberto até o final.
    # Escreve no final a média e o desvio padrão.
    with (open(path+nomeArq,'a'))as arq:
        arq.write("Média:" + str(particulasPSO.calculaMediaGbest(lstGbest)) + "\n")
        arq.write("Desvio Padrão:" + str(particulasPSO.calculaDesvioPadrao(lstGbest, len(lstGbest))) + "\n")
        arq.write('\n')
        arq.close()


    #Renomeia o arquivo para o melhor de todos.
    novoNome = "execucao_"+str(iTxt)+"_melhor_gbest.txt"
    for nomeArq in os.listdir(path):
        os.rename(path+nomeArq,path+novoNome)
        print("Arquivo modificado.")
    return