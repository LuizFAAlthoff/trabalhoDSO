class Galpao:
    def __init__(self, posicao, espaco: float, cpf: str, preco: float):
        self.__posicao = posicao
        self.__espaco = espaco
        self.__cpf = cpf
        self.__preco = preco

    @property
    def posicao(self):
        return self.__posicao

    @property
    def espaco(self):
        return self.__espaco

    @property
    def cpf(self):
        return self.__cpf

    @property
    def preco(self):
        return self.__preco

    @espaco.setter
    def espaco(self, espaco):
        if isinstance(espaco, float):
            self.__espaco = espaco

    @preco.setter
    def preco(self, preco):
        if isinstance(preco, float):
            self.__preco = preco
