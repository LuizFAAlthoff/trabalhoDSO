from boto import NullHandler


class Usuario:
    def __init__(self, email: str, senha: str):
        self.__email == email
        self.__senha == senha
        self.__nome == None
        self.__fone == None
        self.__cpf == None
        self.__posicao == None
        self.__propostas == []
        self.__acordos == []

    @property
    def email(self):
        return self.__email

    @property
    def senha(self):
        return self.__senha

    @property
    def nome(self):
        return self.__nome

    @property
    def fone(self):
        return self.__fone

    @property
    def cpf(self):
        return self.__cpf

    @property
    def posicao(self):
        return self.__posicao

    @email.setter
    def email(self, email):
        if isinstance(email, str):
            self.__email = email

    @senha.setter
    def senha(self, senha):
        if isinstance(senha, str):
            self.__senha = senha

    @fone.setter
    def fone(self, fone):
        if isinstance(fone, str):
            self.__fone = fone

    @posicao.setter
    def posicao(self, posicao):
        if isinstance(posicao, str):
            self.__posicao = posicao

    def mostrar_propostas(self):
        return self.__propostas

    def mostrar_acordos(self):
        return self.__acordos
    
