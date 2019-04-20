from models.Particula import Particula
import libraries.userInput as userInput
import libraries.filesHandle as filesHandle
import particulasPSO
import os

def main(NUM_EXECUCOES: int, NUMERO_ITERACOES: int, NUMERO_PARTICULAS: int) -> int :
    # Cria as particulas instanciando o objeto Particula e retorna uma lista de particulas
    particulas: list = particulasPSO.criarParticulas(NUMERO_PARTICULAS)
    
    # Pega uma lista de partículas gbest para cada iteração inserida pelo usuário, onde se baseia
    # no cálculo de aptidão assim como o melhor pbest de todas as partículas
    lstGBests: list = particulasPSO.getGbestsPorIteracao(particulas, NUMERO_ITERACOES)

    # Imprimindo a lista de gBests para cada iteração
    particulasPSO.printGBests(lstGBests)

    # Escrevendo as informações no arquivo de saída
    filesHandle.writeGBestData(lstGBests, "execucao_{0}.txt".format(NUM_EXECUCOES), NUMERO_ITERACOES)

    return 0

if __name__ == '__main__' :
    # O usuário insere o número de execuções do algoritmo, partículas da população e iterações fornecidas pelo usuário
    NUM_EXECUCOES: int = userInput.qntExecucoesAlgoritmo()
    NUMERO_PARTICULAS: int = userInput.qntParticulas()
    NUMERO_ITERACOES: int = userInput.qntIteracoesPorParticula()

    for execucao in range(1, NUM_EXECUCOES + 1) :
        main(execucao, NUMERO_ITERACOES, NUMERO_PARTICULAS)