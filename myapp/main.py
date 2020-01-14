#---Bibliotecas---#
import numpy as np #Álgebra
from bokeh.io import output_file, show, curdoc
from bokeh.layouts import gridplot, column, row
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Slider, TextInput
from bokeh.resources import CDN
from bokeh.embed import file_html

# Data
N = 200
Mo_max = 1000
Mo = np.linspace(0,Mo_max,N)
p = np.linspace(0,0.99999,N)
r = np.linspace(0,1,N)
DP = (r + 1)/(1 + r - 2*p*r)
M =  Mo/(1.0-p)

source1 = ColumnDataSource(data=dict(x=p,y=DP))
source2 = ColumnDataSource(data=dict(x=p, y=M))

#Gráficos
fig1 = figure(plot_width=400, plot_height=250, title='DP  1+r/1+r-2pr')
fig1.line('x','y', source=source1, color="navy", alpha=0.5)

fig2 = figure(plot_width=400, plot_height=250, title='M  M_o/{1-p}')
fig2.line('x','y', source=source2, color="navy", alpha=0.5)

fig = gridplot([[fig1,fig2]])

# Sliders para os parâmetros de entrada 'Mo', 'p' e 'r'
mass = Slider(start=0, end=400, value=1, step=.1, title="Massa Molar (Mo)")
extention = Slider(start=0,end=0.999, step=0.01, value=0, title="Extensão da reação de polimerização (p)")
imbalance = Slider(start=0, end=1, step=0.01, value=0, title="Fator de desbalanço estequiométrico(r)")

#callbacks
def update_data(attrname, old, new):
    # Get the current slider values
    Mo = np.linspace(0,mass.value,N)
    p = np.linspace(0,extention.value,N)
    r = np.linspace(0,imbalance.value,N)
    DP = (r + 1)/(1 + r - 2*p*r)
    M =  Mo/(1.0-p)

    source1.data= dict(x=p, y=DP)
    source2.data= dict(x=p, y=M)

for w in [mass, extention, imbalance]:
    w.on_change('value', update_data)

# Set up layouts and add to document
layout = column(mass, extention, imbalance)
curdoc().add_root(row(layout, fig, width=800))
curdoc().title = "Polimerizator 1.1"
