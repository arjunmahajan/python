from dijkstar import Graph, find_path
graph = Graph()
num=int(input("Enter the number of edges: "))
for n in range(num):
    edge1=int(input("Enter the node from which edge will be started: "))
    edge2=int(input("Enter the node upto which edge will be ended: "))
    cost=int(input("Enter the cost of this edge: "))
    graph.add_edge(edge1, edge2, {'cost': cost})

node1=int(input("Enter the intial node of the edge whose cost is to be found out: "))
node2=int(input("Enter the final node of the edge whose cost is to be found out: "))
cost_func = lambda u, v, e, prev_e: e['cost']
print(find_path(graph, node1, node2, cost_func=cost_func))


