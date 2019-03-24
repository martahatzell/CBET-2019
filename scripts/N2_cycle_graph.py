from graphviz import Digraph

dot = Digraph(comment='Photochemical N2 Cycle',engine='dot',format='svg')
dot.graph_attr['size'] = '10'

TiO2 = 'blue'
FeOx = 'orange'
fontsize0 = '24'
fontsize1 = '22'
fontsize3 = '22'

dot.node_attr['style'] = 'filled'
dot.node_attr['fillcolor'] = 'white'

dot.node('N2', '<N<sub>2</sub>>',fontsize=fontsize0)
dot.node('NH3', '<NH<sub>3</sub>>',fontsize=fontsize0)
dot.node('NH4', '<NH<sub>4</sub><sup>+</sup>>',fontsize=fontsize0)
dot.node('N2O', '<N<sub>2</sub>O>',fontsize=fontsize0)
dot.node('NOx', '<NO<sub>x</sub>>',fontsize=fontsize0)
dot.node('Nitrate', '<NO<sub>x</sub><sup>-</sup>>',fontsize=fontsize0)

dot.node('NH3-N2','',color=TiO2,fillcolor=TiO2,shape='point')
dot.edge('NH3','NH3-N2',color=TiO2)
dot.edge('NH3-N2','N2',color=TiO2)

dot.node('NH3-Nitrate','',color=TiO2,fillcolor=TiO2,shape='point')
dot.edge('NH3','NH3-Nitrate',color=TiO2)
dot.edge('NH3-Nitrate','Nitrate',color=TiO2)

dot.node('NH3-NOx','',color=TiO2,fillcolor=TiO2,shape='point')
dot.edge('NH3','NH3-NOx',color=TiO2)
dot.edge('NH3-NOx','NOx',color=TiO2)

dot.node('NH4-Nitrate-N2','',color=TiO2,fillcolor=TiO2,shape='point')
dot.edge('NH4','NH4-Nitrate-N2',color=TiO2)
dot.edge('Nitrate','NH4-Nitrate-N2',color=TiO2)
dot.edge('NH4-Nitrate-N2','N2',color=TiO2)

dot.node('NH4-Nitrate-N2_FeOx','',color=FeOx,fillcolor=FeOx,shape='point')
dot.edge('NH4','NH4-Nitrate-N2_FeOx',color=FeOx)
dot.edge('Nitrate','NH4-Nitrate-N2_FeOx',color=FeOx)
dot.edge('NH4-Nitrate-N2_FeOx','N2',color=FeOx)

dot.node('N2-NH3','',color=TiO2,fillcolor=TiO2,shape='point')
dot.edge('N2','N2-NH3',color=TiO2)
dot.edge('N2-NH3','NH3',color=TiO2)

dot.node('N2-NH3_FeOx','',color=FeOx,fillcolor=FeOx,shape='point')
dot.edge('N2','N2-NH3_FeOx',color=FeOx)
dot.edge('N2-NH3_FeOx','NH3',color=FeOx)

dot.node('N2-NOx','',color=TiO2,fillcolor=TiO2,shape='point')
dot.edge('N2','N2-NOx',color=TiO2)
dot.edge('N2-NOx','NOx',color=TiO2)

dot.node('N2-Nitrate','',color=TiO2,fillcolor=TiO2,shape='point')
dot.edge('N2','N2-Nitrate',color=TiO2)
dot.edge('N2-Nitrate','Nitrate',color=TiO2)

dot.node('N2-Nitrate_FeOx','',color=FeOx,fillcolor=FeOx,shape='point')
dot.edge('N2','N2-Nitrate_FeOx',color=FeOx)
dot.edge('N2-Nitrate_FeOx','Nitrate',color=FeOx)

dot.node('NOx-N2O','',color=TiO2,fillcolor=TiO2,shape='point')
dot.edge('NOx','NOx-N2O',color=TiO2)
dot.edge('NOx-N2O','N2O',color=TiO2)

dot.node('Nitrate-NH3','',color=TiO2,fillcolor=TiO2,shape='point')
dot.edge('Nitrate','Nitrate-NH3',color=TiO2)
dot.edge('Nitrate-NH3','NH3',color=TiO2)

dot.node('Nitrate-N2','',color=TiO2,fillcolor=TiO2,shape='point')
dot.edge('Nitrate','Nitrate-N2',color=TiO2)
dot.edge('Nitrate-N2','N2',color=TiO2)


dot.node('Nitrate-N2O','',color=TiO2,fillcolor=TiO2,shape='point')
dot.edge('Nitrate','Nitrate-N2O',color=TiO2)
dot.edge('Nitrate-N2O','N2O',color=TiO2)

dot.node('Nitrate-N2O_FeOx','',color=FeOx,fillcolor=FeOx,shape='point')
dot.edge('Nitrate','Nitrate-N2O_FeOx',color=FeOx)
dot.edge('Nitrate-N2O_FeOx','N2O',color=FeOx)


dot.node('Nitrate-NOx','',color=TiO2,fillcolor=TiO2,shape='point')
dot.edge('Nitrate','Nitrate-NOx',color=TiO2)
dot.edge('Nitrate-NOx','NOx',color=TiO2)

dot.node('Nitrate-NOx_FeOx','',color=FeOx,fillcolor=FeOx,shape='point')
dot.edge('Nitrate','Nitrate-NOx_FeOx',color=FeOx)
dot.edge('Nitrate-NOx_FeOx','NOx',color=FeOx)

dot.format = 'pdf'
dot.render('../figures/N2_cycle_graph',view=True)

