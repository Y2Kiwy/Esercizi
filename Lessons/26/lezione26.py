from abc import ABC, abstractmethod

class CodificatoreMessaggio(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def codifica(self, testoInChiaro: str) -> str:
        pass


class DecodificatoreMessaggio(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def decodifica(self, testoCodificato: str) -> str:
        pass

import string

class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, chiave: int) -> None:
        super().__init__()
        self.chiave: int = chiave

    def _sposta_carattere(self, c: str, chiave: int) -> str:
        """Restituisce un carattere spostato di self.chiave volte"""
        if c.isalpha():
            maiuscolo = c.isupper()
            alfabeto = string.ascii_lowercase
            indice = (string.ascii_lowercase.index(c.lower()) + chiave) % 26
            nuovo_c = alfabeto[indice]

            return nuovo_c.upper() if maiuscolo else nuovo_c
        
        else:
            return c
    
    def codifica(self, testoInChiaro: str) -> str:
        """Codifica la stringa usando un metodo a scorrimento"""
        testCifrato: str = ''
        for c in testoInChiaro:
            nuovo_c: str = self._sposta_carattere(c, self.chiave)
            testCifrato += nuovo_c

        return testCifrato
    
    def decodifica(self, testoCodificato: str) -> str:
        """Decodifica la stringa usando un metodo a scorrimento inverso"""
        testCifrato: str = ''
        for c in testoCodificato:
            nuovo_c: str = self._sposta_carattere(c, -self.chiave)
            testCifrato += nuovo_c

        return testCifrato
    
class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, n: int) -> None:
        super().__init__()
        self.n: int = n

    def codifica(self, testoInChiaro: str) -> str:
        """Codifica la stringa usando un metodo a combinazione"""
        pass

    def decodifica(self, testoCodificato: str) -> str:
        """Decodifica la stringa usando un metodo a combinazione inverso"""
        pass
