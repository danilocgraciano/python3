class CalculadorImpostos:

    def realiza_calculo(self, orcamento, imposto):
        valor = imposto.calcular(orcamento)
        print(valor)