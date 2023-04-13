"""
Descrição:
Devemos desenvolver uma aplicação onde ao ser inicializada solicite ao usuárioescolheronível de
dificuldade do jogo e após isso gera e apresenta, de forma aletaória, umcálculoparaquepossamos
informar o resultado.
Iremos limitar as operações em somar, diminuir e multiplicar.
Se o usuário acertar a resposta, somará 1 ponto ao seu score.
Acertando ou errando, ele poderá ou não continuar o jogo.

"""
import random

def dif1():
    resp_usuario = 0
    resp_certa = 0
    n = random.sample(range(10), k=2)
    tipo_operacao = random.randrange(0,10)
    print(tipo_operacao)
    # teste de vaidação
    if tipo_operacao>=0 and tipo_operacao<=3: #Soma
        resp_certa = n[0]+n[1]
        resp_usuario = int(f"Qual o resultado de {n[0]} + {n[1]}? ")
        try:
            if resp_usuario == resp_certa:
                print("Você acertou!")
            else:
                print("Errou!!")
        except:
            print("Algo deu errado! Tente novamente")

class Jogo:
    def __init__(self):
        self.__resp_usuario = 0
        self.__resp_certa = 0
        self.__tipo_op = 0
        self.__valores = []
        self.__pontos = 0

    @property
    def resp_usuario(self):
        return self.__resp_usuario

    @property
    def resp_certa(self):
        return self.__resp_certa

    @property
    def tipo_op(self):
        return self.__tipo_op

    @property
    def valores(self):
        return self.__valores

    @property
    def pontos(self):
        return self.__pontos

    @resp_usuario.setter
    def resp_usuario(self, novo_dado):
        self.__resp_usuario = novo_dado

    @resp_certa.setter
    def resp_certa(self, novo_dado):
        self.__resp_certa = novo_dado

    @tipo_op.setter
    def tipo_op(self, novo_dado):
        self.__tipo_op = novo_dado

    @valores.setter
    def valores(self, novo_dado):
        self.__valores = novo_dado

    @pontos.setter
    def pontos(self, novo_dado):
        self.__pontos = novo_dado


    # Dificuldade 1
    def dif1(self):
        self.__valores = random.sample(range(10), k=2)
        self.__tipo_op = random.randrange(0, 10)
        # teste de vaidação
        print(self.__tipo_op)

        if self.__tipo_op >= 0 and self.__tipo_op <= 3:  # Soma
            self.__resp_certa = self.valores[0] + self.__valores[1]
            self.__resp_usuario = int(input(f"Qual o resultado de {self.__valores[0]} + {self.__valores[1]} ? "))
            try:
                if self.__resp_usuario == self.__resp_certa:
                    print("Você acertou!")
                    self.__pontos+=1
                else:
                    print("Errou!!")
            except:
                print("Algo deu errado! Tente novamente")

        elif self.__tipo_op >= 4 and self.__tipo_op <= 6: #subtração
            self.__resp_certa = self.valores[0] - self.__valores[1]
            self.__resp_usuario = int(input(f"Qual o resultado de {self.__valores[0]} - {self.__valores[1]} ? "))
            try:
                if self.__resp_usuario == self.__resp_certa:
                    print("Você acertou!")
                    self.__pontos += 1
                else:
                    print("Errou!!")
            except:
                print("Algo deu errado! Tente novamente")

        elif self.__tipo_op >= 7 and self.__tipo_op <= 9: #Multiplicação
            self.__resp_certa = self.valores[0] * self.__valores[1]
            self.__resp_usuario = int(input(f"Qual o resultado de {self.__valores[0]} * {self.__valores[1]} ? "))
            try:
                if self.__resp_usuario == self.__resp_certa:
                    print("Você acertou!")
                    self.__pontos += 1
                else:
                    print("Errou!!")
            except:
                print("Algo deu errado! Tente novamente")
     # |--------------------------||----------------------|

     # Dificuldade 2
    def dif2(self):
        self.__valores = random.sample(range(50), k=2)
        self.__tipo_op = random.randrange(0, 10)
        # teste de vaidação
        print(self.__tipo_op)

        if self.__tipo_op >= 0 and self.__tipo_op <= 3:  # Soma
            self.__resp_certa = self.valores[0] + self.__valores[1]
            self.__resp_usuario = int(input(f"Qual o resultado de {self.__valores[0]} + {self.__valores[1]} ? "))
            try:
                if self.__resp_usuario == self.__resp_certa:
                    print("Você acertou!")
                    self.__pontos += 1
                else:
                    print("Errou!!")
            except:
                print("Algo deu errado! Tente novamente")

        elif self.__tipo_op >= 4 and self.__tipo_op <= 6:  # subtração
            self.__resp_certa = self.valores[0] - self.__valores[1]
            self.__resp_usuario = int(input(f"Qual o resultado de {self.__valores[0]} - {self.__valores[1]} ? "))
            try:
                if self.__resp_usuario == self.__resp_certa:
                    print("Você acertou!")
                    self.__pontos += 1
                else:
                    print("Errou!!")
            except:
                print("Algo deu errado! Tente novamente")

        elif self.__tipo_op >= 7 and self.__tipo_op <= 9:  # Multiplicação
            self.__resp_certa = self.valores[0] * self.__valores[1]
            self.__resp_usuario = int(input(f"Qual o resultado de {self.__valores[0]} * {self.__valores[1]} ? "))
            try:
                if self.__resp_usuario == self.__resp_certa:
                    print("Você acertou!")
                    self.__pontos += 1
                else:
                    print("Errou!!")
            except:
                print("Algo deu errado! Tente novamente")

     # Dificuldade 3
    def dif3(self):
        self.__valores = random.sample(range(100), k=2)
        self.__tipo_op = random.randrange(0, 10)
        # teste de vaidação
        print(self.__tipo_op)

        if self.__tipo_op >= 0 and self.__tipo_op <= 3:  # Soma
            self.__resp_certa = self.valores[0] + self.__valores[1]
            self.__resp_usuario = int(input(f"Qual o resultado de {self.__valores[0]} + {self.__valores[1]} ? "))
            try:
                if self.__resp_usuario == self.__resp_certa:
                    print("Você acertou!")
                    self.__pontos += 1
                else:
                    print("Errou!!")
            except:
                print("Algo deu errado! Tente novamente")

        elif self.__tipo_op >= 4 and self.__tipo_op <= 6:  # subtração
            self.__resp_certa = self.valores[0] - self.__valores[1]
            self.__resp_usuario = int(input(f"Qual o resultado de {self.__valores[0]} - {self.__valores[1]} ? "))
            try:
                if self.__resp_usuario == self.__resp_certa:
                    print("Você acertou!")
                    self.__pontos += 1
                else:
                    print("Errou!!")
            except:
                print("Algo deu errado! Tente novamente")

        elif self.__tipo_op >= 7 and self.__tipo_op <= 9:  # Multiplicação
            self.__resp_certa = self.valores[0] * self.__valores[1]
            self.__resp_usuario = int(input(f"Qual o resultado de {self.__valores[0]} * {self.__valores[1]} ? "))
            try:
                if self.__resp_usuario == self.__resp_certa:
                    print("Você acertou!")
                    self.__pontos += 1
                else:
                    print("Errou!!")
            except:
                print("Algo deu errado! Tente novamente")

    def mostra_pontos(self):
        print(f"Os pontos atuais foram de {self.__pontos}")


# Menu de inicio
print("Bem vindo ao jogo matemático!")
saida = 0

usuario = Jogo()

while saida !=5:
    try:
        saida =int(input("---Faça sua escolha de jogo---\n 1 - nível facil \n 2 - Nível médio \n 3 - nível difícil \n 4- Verificar pontos \n 5 - saida\n"))
        if saida ==1:# Facil
            usuario.dif1()

        elif saida ==2:#Medio
            usuario.dif2()

        elif saida ==3:# Dificil
            usuario.dif3()

        elif saida ==4:#verifica pontos
            usuario.mostra_pontos()

        elif saida ==5:#saida
            saida = 5
            print(f"Que pena que acabou!Seus pontos foram {usuario.pontos}")

    except:
        print("Escolha inválida!, tente novamente")