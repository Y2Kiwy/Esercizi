class Pagamento:
    def __init__(self) -> None:
        self.__importo: float = 0

    def setImporto(self, importo: float) -> None:
        self.__importo = importo

    def getImporto(self) -> float:
        return self.__importo
    
    def dettagliPagamento(self) -> None:
        print(f"Importo del pagamento: €{self.__importo:.2f}")

class PagamentoContanti(Pagamento):
    def __init__(self) -> None:
        super().__init__()

    def dettagliPagamento(self) -> None:
        print(f"Importo del pagamento in contanti: €{self.getImporto():.2f}")
        self.inPezziDa()

    def inPezziDa(self):
        importo = self.getImporto()

        pezzi = {
            500: "banconota/e da 500 euro",
            200: "banconota/e da 200 euro",
            100: "banconota/e da 100 euro",
            50: "banconota/e da 50 euro",
            20: "banconota/e da 20 euro",
            10: "banconota/e da 10 euro",
            5: "banconota/e da 5 euro",
            2: "moneta/e da 2 euro",
            1: "moneta/e da 1 euro",
            0.50: "moneta/e da 50 centesimi",
            0.20: "moneta/e da 20 centesimi",
            0.10: "moneta/e da 10 centesimi",
            0.05: "moneta/e da 5 centesimi",
            0.01: "moneta/e da 1 centesimo"
        }

        print(f"{self.getImporto()} da pagare in contanti con:")

        for valore, descrizione in pezzi.items():
            quantita = int(importo // valore)
            if quantita > 0:
                print(f"{quantita} {descrizione}")
                importo = round(importo - quantita * valore, 2)

class PagamentoCartaDiCredito (Pagamento):
    def __init__(self, nome_titolare: str, data_scadenza: str, numero_carta: int) -> None:
        super().__init__()
        self.nome_titolare: str = nome_titolare
        self.data_scadenza: str = data_scadenza
        self.numero_carta: int = numero_carta


    def dettagliPagamento(self) -> None:
        print(f"Pagamento di: €{self.getImporto():.2f} effettuato con la carta di credito")
        print(f"Nome sulla carta: {self.nome_titolare}")
        print(f"Data di scadenza: {self.data_scadenza}")
        print(f"Numero della carta: {self.numero_carta}")

if __name__ == "__main__":

    print()

    contanti1: PagamentoContanti = PagamentoContanti()
    contanti1.setImporto(150.00)
    contanti1.dettagliPagamento()

    print()

    contanti2: PagamentoContanti = PagamentoContanti()
    contanti2.setImporto(95.25)
    contanti2.dettagliPagamento()

    print()

    carta1: PagamentoCartaDiCredito = PagamentoCartaDiCredito("Mario Rossi", "Mario Rossi", 1234567890123456)
    carta1.setImporto(200.00)
    carta1.dettagliPagamento()

    print()

    carta2: PagamentoCartaDiCredito = PagamentoCartaDiCredito("Luigi Bianchi", "01/25", 6543210987654321)
    carta2.setImporto(500.00)
    carta2.dettagliPagamento()