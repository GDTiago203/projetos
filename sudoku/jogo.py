import os
from tabuleiro import Tabuleiro
class Jogo:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.tabuleiro.aleatorizar_numeros()

    def menu(self):
        print("Bem vindo ao Sudoku do Tiago :):):):):):)")
        while True:
            print("1 Jogar           2 Regras            3 Sair")
            opcao = input("O que deseja fazer? (digite 1, 2 ou 3 e aperte enter): ")
            if opcao == "1":
                os.system("cls")
                self.jogar()

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

    def jogar(self):
         while True:
            self.tabuleiro.mostrar()
            linha = int(input("Insira o número da linha que se deseja alterar: "))-1
            coluna = int(input("Insira o número da coluna que se deseja alterar: "))-1
            if 0 <= coluna <= 8 and 0 <= linha <= 8:
                numero = int(input("Insira o número que se deseja ser insirido: "))
                while True:
                    if self.tabuleiro.checa_linha(numero, linha):
                        os.system("cls")
                        print("Esse número já está na linha designada por favor insira outro número")
                        break
                    elif self.tabuleiro.checa_colunas(numero, coluna):
                        os.system("cls")
                        print("Esse número já está na coluna designada por favor insira outro número")
                        break
                    elif self.tabuleiro.checa_quadrante(numero, linha, coluna):
                        os.system("cls")
                        print("Esse número já está no quadrante designado por favor insira outro número")
                        break
                    elif 1 <= numero <= 9:
                        os.system("cls")
                        self.tabuleiro.tabuleiro[linha][coluna] = numero
                        break
                    else:
                        os.system("cls")
                        print("Erro! Insira um número valido (entre 1 e 9)")
                        break

                if self.tabuleiro.checa_vitoria():
                    self.tabuleiro.mostrar()
                    print("Parábens! Você completou o sudoku do Tiago :):):):)")
                    break
            
            else:
                os.system("cls")
                print("Erro! Por favor insira um número valido (entre 1 e 9)")

if __name__ == "__main__":
    jogo = Jogo()
    jogo.menu()