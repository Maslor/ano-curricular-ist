################################################################################
#Formula de Calculo -> AC = min( int( ECTS + 24)/60+1; numero de anos do curso)#
################################################################################

import unittest

### Functions ###

def calculaCreditosNecessariosParaProximoAno(creditosFeitos, nroAnosCurso):
	creditosExtra = 0.5
	concluido = False
	proximoAnoCurricular = calculaAnoCurricularCorrente(creditosFeitos, nroAnosCurso) + 1
	if proximoAnoCurricular > nroAnosCurso:
		print "Frequentas o ultimo ano curricular do curso."
		return 0
	while concluido == False:
		tentativa = calculaAnoCurricularCorrente(creditosFeitos + creditosExtra, nroAnosCurso)
		if tentativa >= proximoAnoCurricular:
			concluido = True
		else:
			creditosExtra = creditosExtra + 0.5
	return creditosExtra

def calculaAnoCurricularCorrente(creditosFeitos, nroAnosCurso):
	anoCurricular = min((creditosFeitos + 24) // 60 + 1, nroAnosCurso)
	return anoCurricular

### Interface ###

anosCurso = input('Quantos anos tem o curso? ')
if anosCurso > 10:
	raise ValueError("O curso nao pode ter mais de 10 anos.")
if anosCurso < 1:
	raise ValueError("O curso nao pode ter menos de 1 ano.")
creditos = input('Quantos creditos tens aprovados? ')
print ('O teu ano curricular -> ' + str(calculaAnoCurricularCorrente(creditos, anosCurso)))
print ('Faltam-te ' + str(calculaCreditosNecessariosParaProximoAno(creditos, anosCurso)) + ' creditos para passar de ano.')

### Tests ###

class TesteCalculoAnoCurricular(unittest.TestCase):
	def test1Ano(self):
		self.assertEqual(calculaAnoCurricularCorrente(10,3), 1)
	def test2Ano(self):
		self.assertEqual(calculaAnoCurricularCorrente(36,3), 2)
	def test3Ano(self):
		self.assertEqual(calculaAnoCurricularCorrente(96,3), 3)
	def testCreditosPara2Ano(self):
		self.assertEqual(calculaCreditosNecessariosParaProximoAno(30,3), 6.0)
	def testCreditosPara3Ano(self):
		self.assertEqual(calculaCreditosNecessariosParaProximoAno(64,3), 32.0)
	def testFinalista(self):
		self.assertEqual(calculaCreditosNecessariosParaProximoAno(96,3), 0.0)

if __name__ == '__main__':
    unittest.main()






