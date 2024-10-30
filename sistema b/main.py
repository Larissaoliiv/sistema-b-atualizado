from abc import ABCMeta, abstractmethod, abstractproperty

from datetime import datetime 

class cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self,conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)    

class pessoa_fisica (cliente):
      def __init__(self, nome, data_nascimento, cpf, endereco):
          super().__init__(endereco)
          self.nome = nome 
          self.data_nascimento = data_nascimento
          self.cpf = cpf

class conta:
    def __init__(self, numero, cliente):
          self._saldo = 0
          self._numero = numero
          self._agencia = "0001"
          self._cliente = cliente
          self._historico = historico()
          
    @classmethod
    def nova_conta(cls, cliente, numero):
         return cls(numero, cliente)
    @property 
    def saldo(self):
        return self._saldo
    @property
    def numero(self):
         return self._numero
    @property
    def agencia(self):
        return self._agencia
    @property
    def cliente(Self):
        return Self._cliente 
    @property
    def historico(Self):
        return Self._historico

    def sacar(Self, valor):
        saldo = Self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print ("Operação falhou! Você não tem saldo suficiente.")

        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        
        else:
            print("Operação falhou! O valor informado é inválido.")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print ("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False
        
        return True 
 
     
    class conta_corrente(conta):
        def __init__(self, numero, cliente, limite=500, limite_saques=3):
          super().__init__(numero, cliente)
          self.limite = limite
          self.limite_saques = limite_saques
        
        def sacar(self, valor):
            numero_saques = len(
                [ transacao for transacao in self.historico.
                  transacoes if transacao["tipo"] == "Saque".
                  __name__ 
                ]
                  
                 )
            excedeu_limite = valor > self.limite
            excedeu_saques = numero_saques > self
            limite_saques = limite_saques

            if excedeu_limite:
                print("Operação falhou! O valor do saque excedeu o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedidos")
            else: 
                return super().sacar(valor)    
            
            return False
        
        def __str__(self):
            return f"""
                  Agência: {self.agencia}
                  C/C: {self.numero}
                  Titular: {self.cliente.nome}
                """

    class historico:
        def __init__(self):
             self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
        
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime
                ("%d-%m-%Y  %H:%M:%s"),
            }
        ) 

    class transacao(ABC):
        @property
        @abstractproperty
        def valor(Self):
            pass

        @abstractclassmethod
        def registrar(self, conta):
            pass

    class saque(transacao):
        def __init__(self, valor):
            self._valor = valor
        @property
        def valor(self):
            return self._valor

        def registrar(self, conta):
            sucesso_transacao = conta.sacar(self.valor)  

            if sucesso_transacao:
                conta.historico.adicionar_transacao(self)  
             
    class deposito(transacao):
        def __init__(self, valor):
             self._valor = valor

        @property
        def valor(self):
             return self._valor
 
        def registrar(self, conta):
            sucesso_transacao = conta.depositar(self.valor)  

            if sucesso_transacao:
                conta.historico.adicionar_transacao(self) 