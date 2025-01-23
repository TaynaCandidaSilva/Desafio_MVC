from abc import ABC, abstractmethod


class Cliente(ABC):
    @abstractmethod
    def sacar_dinheiro(self, pessoa_fisica, valor):
        pass

    @abstractmethod
    def realizar_extrato(self, pessoa_fisica):
        pass
