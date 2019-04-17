from models.Particula import Particula
# import libraries.userInput as userInput
import particulasPSO
import os

def main() :
    
    # Declarando as variáveis
    NUMERO_PARTICULAS: int = 20
    particulas: list = particulasPSO.criarParticulas(NUMERO_PARTICULAS)
    print(particulas)

    return 0


if __name__ == '__main__':
    main()
