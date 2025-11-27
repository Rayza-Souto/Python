class Cliente:
    def __init__ (self, n, fone):
        # a palavra __init__ é um método construtor e o self representa as características do objeto
        # todo metodo tem que ter o self como primeiro parâmetro
        self._nome = n
        self._telefone = fone
        #pass
        # a palavra pass é usada para criar uma classe vazia

        #metodo get
    def get_nome(self):
        return self._nome
    
        #metodo set
    def set_nome(self, saldo):
        if(saldo<0):
            print("O saldo não pode ser negativo")
        else:
            self._saldo = saldo