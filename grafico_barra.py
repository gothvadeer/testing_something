import matplotlib.pyplot as grafico

votos_lula = 57259504
votos_bolsonaro = 51072345

candidatos = ['Lula', 'Bolsonaro']
votos = [votos_lula, votos_bolsonaro]

grafico.ylabel('Votos')
grafico.xlabel('Candidato')

grafico.bar(candidatos, votos, color=['green', 'red'], label='Votos')

for i in range(len(candidatos)):
    grafico.text(candidatos[i], votos[i], f'{votos[i]/sum(votos)*100:.2f}%', ha='center', va='bottom')

grafico.show()
