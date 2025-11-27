class Main:
    pass

print("Testando o projeto")

from Cliente import Cliente

from Conta import Conta

c1= Cliente("João", "114444-5555")
conta=Conta(c1._nome, 1234, 0)

conta.deposito(500)
conta.saque(200)
conta.extrato()