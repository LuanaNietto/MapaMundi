import geopandas
import matplotlib.pyplot as plt

world = geopandas.read_file("ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp")

world['color'] = 'grey'

paises_para_destacar = ['Brazil', 'United States of America', 'China', 'Germany', 'Ghana']

world.loc[world['ADMIN'].isin(paises_para_destacar), 'color'] = '#4B0082'

fig, ax = plt.subplots(1, 1, figsize=(15, 10))

world.plot(color=world['color'], linewidth=0.5, ax=ax, edgecolor='0.8')

ax.set_axis_off()

fig.canvas.manager.set_window_title('Mapa Mundi com Destaque de Países')

plt.show()