from graphviz import Digraph



g = Digraph('unix', filename='unix.gv',
            node_attr={'color': 'lightblue2', 'style': 'filled'})
g.attr(size='6,6')
g.edge('1', '2')
g.edge('1', '3')
g.edge('2', '4')
g.edge('2', '5')
g.edge('3', '6')
g.edge('3', '7')
g.edge('4', '8')
g.edge('4', '9')
g.edge('5', '10')
g.edge('5', '11')
g.edge('6', '12')
g.edge('6', '13')
g.edge('7', '14')
g.edge('7', '15')
# g.edge('8', '9')
# g.edge('8', '10')
# g.edge('8', '11')
# g.edge('9', '11')
g.view()