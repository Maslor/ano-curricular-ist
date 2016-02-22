#AC = min( int( ECTS + 24)/60+1; numero de anos do curso)

anosCurso = input('Quantos anos tem o curso? ')
creditosInput = input('Quantos creditos tens aprovados? ')

anoCurricular = min((creditosInput + 24)//60+1, anosCurso)

print ('O teu ano curricular -> ' + str(anoCurricular))

creditosExtra=0.5
concluded = False
proxAnoCurricular = anoCurricular + 1
while not concluded:
	tentativa = min((creditosInput + creditosExtra + 24)//60+1, anosCurso)
	if tentativa >= proxAnoCurricular:
		concluded = True
	else:
		creditosExtra = creditosExtra + 0.5

print ('Faltam-te ' + str(creditosExtra) + ' para passar de ano.')
