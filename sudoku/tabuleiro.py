import random

class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [
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

    def mostrar(self):
        for i, linha in enumerate(self.tabuleiro):
            if i % 3 == 0 and i != 0:
                print("------+------+------")
            for j, numero in enumerate(linha):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(numero if numero != 0 else ".", end=" ")
            print()

    def checa_vitoria(self):
        return all(0 not in linha for linha in self.tabuleiro)

    def checa_linha(self, numero, linha):
        if numero in self.tabuleiro[linha]:
            return True
        return False

    def checa_colunas(self, numero, coluna):
        for linha in self.tabuleiro:
            if linha[coluna] == numero:
                return True
        return False
    
    def checa_quadrante(self, numero, linha, coluna):   
        linha_inicio = (linha//3)*3
        coluna_inicio = (coluna//3)*3

        for linha in range(linha_inicio, linha_inicio+3):
            for coluna in range(coluna_inicio, coluna_inicio+3):
                if self.tabuleiro[linha][coluna] == numero:
                    return True
        return False
   
    def aleatorizar_numeros(self):
        qt_nums = 40
        while qt_nums > 0:
            linha = random.randint(0,8)
            coluna = random.randint(0,8)
            numero_aleatorio = random.randint(1,9)
            if not self.checa_quadrante(numero_aleatorio, linha, coluna) and not self.checa_linha(numero_aleatorio, linha) and not self.checa_colunas(numero_aleatorio, coluna):
                self.tabuleiro[linha][coluna] = numero_aleatorio
                qt_nums -= 1