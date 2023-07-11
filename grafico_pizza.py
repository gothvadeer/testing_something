import matplotlib.pyplot as grafico

musicas = [150,  74, 200, 23, 97, 120]
bandas = ['The Cure', 'The Smiths', 'The Beatles', 'Joy Division', 'Oasis', 'Blur']
grafico.pie(musicas, labels=bandas, autopct='%1.1f%%')
grafico.title('Número de músicas gravadas das maiores bandas britânicas'.title(),  fontdict={'fontsize': 15, 'fontname': 'georgia', 'color': 'blue'})
grafico.show()
