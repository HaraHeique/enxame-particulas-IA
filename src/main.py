from models.Particula import Particula
import libraries.userInput as userInput
import particulasPSO
import os

def main() -> int :
    # Pega o número de partículas da população e iterações fornecidas pelo usuário
    NUMERO_PARTICULAS: int = userInput.qntParticulas()
    NUMERO_ITERACOES: int = userInput.qntIteracoesPorParticula()
    
    # Cria as particulas instanciando o objeto Particula e retorna uma lista de particulas
    particulas: list = particulasPSO.criarParticulas(NUMERO_PARTICULAS)
    
    # Pega uma lista de partículas gbest para cada iteração inserida pelo usuário, onde se baseia
    # no cálculo de aptidão assim como o melhor pbest de todas as partículas
    lstGBests: list = particulasPSO.getGbestsPorIteracao(particulas, NUMERO_ITERACOES)

    # Imprimindo a lista de gBests para cada iteração
    particulasPSO.printGBests(lstGBests)

    return 0

if __name__ == '__main__' :
    main()