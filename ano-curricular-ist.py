################################################################################
#Formula de Calculo -> AC = min( int( ECTS + 24)/60+1; numero de anos do curso)#
################################################################################

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
creditos = input('Quantos creditos tens aprovados? ')
print ('O teu ano curricular -> ' + str(calculaAnoCurricularCorrente(creditos, anosCurso)))
print ('Faltam-te ' + str(calculaCreditosNecessariosParaProximoAno(creditos, anosCurso)) + ' creditos para passar de ano.')






