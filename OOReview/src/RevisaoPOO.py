from datetime import datetime


class Pessoa:
    def __init__(self: object, nome: str):
        self.__nome = nome
        self.__nascimento: datetime.now()

    def __str__(self: object) -> str:
        return self.__nome

    def __repr__(self: object) -> str:
        return self.__nome


class Carro:
    def __init__(self: object, is_sedan: bool = False) -> None:
        self.__is_sedan = is_sedan
        self.__velocidade = 0
        self.__motorista = None

    def __str__(self: object) -> str:
        if self.__motorista:
            return f'Carro do(a) {self.__motorista.__nome}'
        return 'Carro sem motorista'

    def dirigir(self: object, motorista: Pessoa) -> None:
        self.motorista = motorista
        self.acelerar(1)

    def acelerar(self: object, velocidade: int) -> None:
        self.__velocidade += velocidade

    def parar(self: object):
        self.velocidade = 0


p1 = Pessoa('Angelina')
fusca = Carro()

fusca.dirigir(p1)
fusca.acelerar(50)

print(fusca.__dict__)


from typing import List, Tuple

class Curso:

    def __init__(self: object, nome: str = 'Curso Padrão', carga_horaria: int = 45):
        self.__nome = nome
        self.__carga_horaria = carga_horaria


curso1: Curso = Curso()
curso2: Curso = Curso(nome='Padrões de Projetos em Python')
curso3: Curso = Curso(nome='Orquestração de Containers com Kubernetes', carga_horaria=23)

print(curso1.__dict__)
print(curso2.__dict__)
print(curso3.__dict__)


nome: str = 'Geek University'
tupla: Tuple = (1, 2, 3, 4, 5)
lista: List = [1, 2, 3, 4, 5]


print(nome[:4], tupla[:4], lista[:4])


class Pessoa:

    def __init__(self: object, nome: str):
        self.__nome = nome

    def andar(self: object):
        print('Estou andando...')


class Aluno(Pessoa):

    def __init__(self: object, nome: str, matricula: str):
        super().__init__(nome)
        self.__matricula = matricula



felicity = Aluno('Felicity', 12345)

felicity.andar()


def gerar_fibonacci(qtd: int):
    if qtd <= 0:
        print('A quantidade deve ser maior que 0')
    else:
        print(f'A sequência Fibonacci para {qtd} termo(s) é: ')
        contador: int = 0
        aux1: int = 0
        aux2: int = 1
        while contador < qtd:
            print(aux1)
            proximo = aux1 + aux2
            aux1 = aux2
            aux2 = proximo
            contador += 1


gerar_fibonacci(7)


class Motor:

    def ligar(self: object):
        print('Motor ligado...')

class Pneu:

    def enxer(self: object):
        print('Pneu cheio...')


class Carro:

    def __init__(self: object, modelo: str):
        self.__modelo = modelo
        self.__motor = Motor()
        self.__pneu1 = Pneu()
        self.__pneu2 = Pneu()
        self.__pneu3 = Pneu()
        self.__pneu4 = Pneu()


fusca = Carro('Fusca')
fusca._Carro__motor.ligar()
