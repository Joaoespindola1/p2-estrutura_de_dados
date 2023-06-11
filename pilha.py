from copy import deepcopy
from typing import Iterator

class Stack_Pilha():
    def __init__(self) -> None:
        self.dados: list[any] = []  # self.dados significa o início
        self.inicio = 0

    def append(self, item: any) -> None:
        self.dados.append(item)

    def pop(self) -> any:
        return self.dados.pop()  # Tirando um elemento da pilha
    
    def peek(self) -> any:
        if not self.dados:
            return []
        return self.dados[-1]  # Retornando o último elemento da lista
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.dados})'  # Para fazer a função print

    def __iter__(self) -> Iterator[any]:  # Trabalhando com o import, retornando a própria classe
        self.inicio = len(self.dados)
        return self

    def __next__(self) -> any:
        if self.inicio == 0:
            raise StopIteration  # Trabalhando junto com o for, fazendo o -1
        self.inicio -= 1
        return self.dados[self.inicio]  # Caso passe para voltar, tratamento de erro

    def __bool__(self):
        return bool(self.dados)  # Sempre que a lista não tiver valores, retornará falso

if __name__ == "__main__":
    stack = Stack_Pilha()

    stack.append('A')
    stack.append('B')
    stack.append('C')

    for pilhas in stack:
        print(pilhas)

    pilha_copia = deepcopy(stack)
    print('\n while: ')
    while pilha_copia:
        print(pilha_copia.pop())