from pyvis.network import Network
import networkx as nx
nx_graph = nx.Graph()
# В [] - номер узла
# title - название при наведении
# group - К какой группе/системе относится
# label - Подпись узла
label_list = ['Рост прибыли', 'Увеличение количества клиентов', 'Сокращение издержек'
              'Сохранение клиентской базы', 'Привлечение клиентов',
              'Повышение удовлетворенности клиентов', 'Своевременное выполнение проектных работ',
              'Повышение качества проектных работ', 'Оптимизация запасов ТМЦ и инструмента',
              'Закупка качественных ТМЦ и инструмента', 'Усиление контроля строительно-монтажных работ',
              'Своевременная доставка ТМЦ и инструмента', 'Точное планирование проектов',
              'Повышение квалификации сотрудников'
              ]
#####
# nx_graph.nodes[1]['title'] = 'Number 1'

# i = 0
# for label in label_list:
    # print(nx_graph.nodes[i]['title'])
    # i += 1
i = 0
for label in label_list:
   nx_graph.add_node(i, title=f'{label}')
   i += 1
nx_graph.add_edges_from([(0, 1), (0, 2)])
nx_graph.add_edges_from([(1, 3), (1, 4)])
nx_graph.add_edges_from([(2, 8)])
nx_graph.add_edges_from([(3, 5)])
nx_graph.add_edges_from([(4, 7)])
nx_graph.add_edges_from([(5, 6), (5, 7)])
nx_graph.add_edges_from([(6, 11)])
nx_graph.add_edges_from([(7, 9), (7, 10), (7, 13)])
nx_graph.add_edges_from([(8, 11)])
nx_graph.add_edges_from([(11, 12)])
nx_graph.add_edges_from([(12, 13)])



#
# nx_graph.nodes[1]['group'] = 1
# nx_graph.nodes[3]['title'] = 'I belong to a different group!'
# nx_graph.nodes[3]['group'] = 10


# nx_graph.add_node(20, size=20, title='couple', group=2)
# nx_graph.add_node(21, size=15, title='couple', group=2)
# nx_graph.add_edge(20, 21, weight=5)
# nx_graph.add_node(25, size=25, label='lonely', title='lonely node', group=3)
nt = Network('500px', '500px')
# populates the nodes and edges data structures
nt.from_nx(nx_graph)
nt.show('nx.html')