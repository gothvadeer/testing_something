import matplotlib.pyplot as grafico
import numpy as np

homens = [181, 498, 938, 848, 484, 884]
mulheres = [948, 929, 944, 101, 339, 988]

eixo1 = np.arange(len(homens))
eixo2 = [dist + 0.25 for dist in eixo1]

grafico.bar(eixo1, homens, width=0.25, label='Homens', color='blue')
grafico.bar(eixo2, mulheres, width=0.25, label='Mulheres', color='pink')

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
grafico.xticks([dist + 0.25 for dist in range(len(homens))], meses)

grafico.legend()
grafico.ylabel('Quantidade em milhares')
grafico.title('Quantidade de livros lançados em 2023')
grafico.show()