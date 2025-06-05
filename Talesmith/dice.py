import random

def rolar_d20():
    print("\nOs Dados serão rolados, Boa sorte!")
    resultado = random.randint(1, 20)
    print("O Resultado dos dados é:")
    print(resultado)
    return resultado
