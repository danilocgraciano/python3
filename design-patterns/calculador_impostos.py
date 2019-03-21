class CalculadorImpostos:

    def realiza_calculo(self, orcamento):
        icms_calculado = orcamento.valor * 0.1
        print(icms_calculado)