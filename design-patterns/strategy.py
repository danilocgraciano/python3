from orcamento import Orcamento
from calculador_impostos import CalculadorImpostos
from impostos import ICMS, ISS

orcamento = Orcamento(500);
calculadorImpostos = CalculadorImpostos()
calculadorImpostos.realiza_calculo(orcamento, ICMS())
calculadorImpostos.realiza_calculo(orcamento, ISS())
