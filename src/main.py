from models.Particula import Particula
import libraries.userInput as userInput
import particulasPSO, filesHandle
import os

EXECUCAO_FILE_NAME: str = "execucao_{0}.txt"

# A main é executada baseada nos parâmetro do usuário e retorna a lista de melhores gBests daquela execuçã
def main(NUM_EXECUCAO: int, NUMERO_ITERACOES: int, NUMERO_PARTICULAS: int) -> list :
    # Cria as particulas instanciando o objeto Particula e retorna uma lista de particulas
    particulas: list = particulasPSO.criarParticulas(NUMERO_PARTICULAS)
    
    # Pega uma lista de partículas gbest para cada iteração inserida pelo usuário, onde se baseia
    # no cálculo de aptidão assim como o melhor pbest de todas as partículas
    lstGBests: list = particulasPSO.getGbestsPorIteracao(particulas, NUMERO_ITERACOES)

    # Imprimindo a lista de gBests para cada iteração
    #particulasPSO.printGBests(lstGBests)

    # Escrevendo as informações no arquivo de saída
    filesHandle.writeGBestData(lstGBests, EXECUCAO_FILE_NAME.format(NUM_EXECUCAO), NUMERO_ITERACOES)

    return lstGBests

if __name__ == '__main__' :
    # O usuário insere o número de execuções do algoritmo, partículas da população e iterações fornecidas pelo usuário
    NUM_EXECUCOES: int = userInput.qntExecucoesAlgoritmo()
    NUMERO_PARTICULAS: int = userInput.qntParticulas()
    NUMERO_ITERACOES: int = userInput.qntIteracoesPorParticula()
    lstGBests: list = []
    dicGBestsPorArquivos: dict = {}

    # Deleta todos os arquivos do diretório daquele número de iterações caso ele exista
    filesHandle.deleteAllFilesGBest(NUMERO_ITERACOES)

    for execucao in range(1, NUM_EXECUCOES + 1) :
        lstGBests = main(execucao, NUMERO_ITERACOES, NUMERO_PARTICULAS)
        
        # Armazena em um dicionário como chave o nome do arquivo e valor o resultado da aptidão
        dicGBestsPorArquivos[EXECUCAO_FILE_NAME.format(execucao)] = particulasPSO.getGBest(lstGBests)['aptidao']

    # Pega o nome do arquivo com menor valor de aptidão dentre todos eles e o renomeia com o novo nome
    lowestValueFileName: str = min(dicGBestsPorArquivos, key=dicGBestsPorArquivos.get)
    filesHandle.renameBestGBestFile(lowestValueFileName, lowestValueFileName[:lowestValueFileName.index(".")] + "_melhor_gbest.txt", NUMERO_ITERACOES)
    
    


    