import random, os
def mostrar(numeros):
    for i, linha in enumerate(numeros):
        if i % 3 == 0 and i != 0:
            print("------+------+------")
        for j, numero in enumerate(linha):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(numero if numero != 0 else ".", end=" ")
        print()

def checa_vitoria(tabela):
    return all(0 not in linha for linha in tabela)

def checa_linha(tabela, numero, linha):
    if numero in tabela[linha]:
        return True
    return False

def checa_colunas(tabela, coluna, numero):
    for linha in tabela:
        if linha[coluna] == numero:
            return True
    return False
    
def checa_quadrante(tabela, numero,linha,coluna):   
    linha_inicio = (linha//3)*3
    coluna_inicio = (coluna//3)*3

    for linha in range(linha_inicio, linha_inicio+3):
        for coluna in range(coluna_inicio, coluna_inicio+3):
            if tabela[linha][coluna] == numero:
                return True
    return False
   
tabela = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]

qt_nums = 40
while qt_nums > 0:
    linha = random.randint(0,8)
    coluna = random.randint(0,8)
    numero_aleatorio = random.randint(1,9)
    if not checa_quadrante(tabela, numero_aleatorio, linha, coluna) and not checa_linha(tabela, numero_aleatorio, linha) and not checa_colunas(tabela, coluna, numero_aleatorio):
        tabela[linha][coluna] = numero_aleatorio
        qt_nums -= 1

print("Bem vindo ao Sudoku do Tiago :):):):):):)")
while True:
    print("1 Jogar           2 Regras            3 Sair")
    opcao = input("O que deseja fazer? (digite 1, 2 ou 3 e aperte enter): ")
    if opcao == "1":
        os.system("cls")
        while True:
            mostrar(tabela)
            linha = int(input("Insira o número da linha que se deseja alterar: "))-1
            coluna = int(input("Insira o número da coluna que se deseja alterar: "))-1

            if 0 <= coluna <= 8 and 0 <= linha <= 8:
                numero = int(input("Insira o número que se deseja ser insirido: "))
                while True:
                    if checa_linha(tabela, numero, linha):
                        os.system("cls")
                        print("Esse número já está na linha designada por favor insira outro número")
                        break
                    elif checa_colunas(tabela, coluna, numero):
                        os.system("cls")
                        print("Esse número já está na coluna designada por favor insira outro número")
                        break
                    elif checa_quadrante(tabela, numero, linha, coluna):
                        os.system("cls")
                        print("Esse número já está no quadrante designado por favor insira outro número")
                        break
                    elif 1 <= numero <= 9:
                        os.system("cls")
                        tabela[linha][coluna] = numero
                        break
                    else:
                        os.system("cls")
                        print("Erro! Insira um número valido (entre 1 e 9)")
                        break
            elif checa_vitoria(tabela):
                mostrar(tabela)
                print("Parábens! Você completou o sudoku do Tiago :):):):)")
                break
            
            else:
                os.system("cls")
                print("Erro! Por favor insira um número valido (entre 1 e 9)")
            
    elif opcao == "2":
        os.system("cls")
        print("O Sudoku é um jogo de lógica com um tabuleiro 9x9 dividido em 9 blocos 3x3. O objetivo é preencher cada linha, coluna e bloco com os números de 1 a 9, sem repetição. Cada número deve aparecer apenas uma vez em cada linha, coluna e bloco. ")
        print("Tabuleiro: O jogo é jogado em uma grade 9x9, dividida em 9 blocos 3x3. ")
        print("Números: Use apenas os números de 1 a 9. ")
        print("Linhas: Cada linha horizontal deve conter todos os números de 1 a 9, sem repetições. ")
        print("Colunas: Cada coluna vertical deve conter todos os números de 1 a 9, sem repetições. ")
        print("Blocos: Cada um dos nove blocos 3x3 deve conter todos os números de 1 a 9, sem repetições. ")
        print("Resolução: O jogo é resolvido quando todas as células estão preenchidas corretamente, seguindo as regras de cada linha, coluna e bloco. ")

    elif opcao == "3":
        break
    
    else:
        os.system("cls")
        print("Por favor insira um número valido (Entre 1, 2 ou 3)")
          