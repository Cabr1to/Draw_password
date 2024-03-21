# A maioria das pessoas iniciam suas senhas nos numeros ( 1 - 44%| 3 - 15%| 7 - 14%,
#                                                         2 - 9%| 4 - 6%| 5 - 4%| 9 - 4%| 8 - 3%| 6 - 2%)
# As sequencias iniciais mais utilizadas sao ( 123 | 147 | 159)
# Trigramas ( 123 | 147 | 789 | 369 | 478 | 236 | 698 | 321 | 741 | 258 | 987 | 145 | 569 | 896 | 357 | 456 | 963 | 125 | 214 | 159)
import re

# Dicionário com as probabilidades
probabilidades = {
    '1': 0.44,
    '3': 0.15,
    '7': 0.14,
    '2': 0.09,
    '4': 0.06,
    '5': 0.04,
    '9': 0.04,
    '8': 0.03,
    '6': 0.02
}

# Lista dos trigramas mais comuns
trigramas_comuns = ['123', '124', '125', '126', '147', '142', '145', '148',
                    '152', '153', '156', '159', '158', '157', '154']

def calc_score(sequencia):
    score = 0
    if sequencia[0] in probabilidades:
        score += probabilidades[sequencia[0]]
    for trigram in trigramas_comuns:
        if sequencia.startswith(trigram):
            score += 1
    return score

# Função que organiza as senhas de acordo com as probabilidades
def organizar_senhas(senhas):
    return sorted(senhas, key=lambda x: calc_score(x), reverse=True)

def main():

    # Lê as senhas do arquivo de entrada
    with open('at-most-9-connected-dots.txt', 'r') as file:
        senhas = [line.strip() for line in file]

    # Organizar as senhas de acordo com as probabilidades
    senhas_organizadas = organizar_senhas(senhas)

    # Escreve as senhas em um arquivo .txt
    with open('senhas_organizadas.txt', 'w') as file:
        for senha in senhas_organizadas:
            file.write(senha + '\n')

    print("Senhas organizadas foram salvas no arquivo senhas_organizadas.txt.")

if __name__ == "__main__":
    main()
