nodes = []
nodes_count = 0
graph = [] 

def add_node(v):
    global nodes_count
    if v in nodes:
        print("Node already present!")
    else:
        nodes.append(v)
        nodes_count += 1
        for n in graph:
            n.append(0)
        temp = []
        for i in range(nodes_count):
            temp.append(0)
        graph.append(temp)

def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1," is not found!")
    elif v2 not in nodes:
        print(v2,"is not found!")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 1
        graph[index2][index1] = 1

def print_graph(graph):
    for i in range(nodes_count):
        for j in range(nodes_count):
            print(graph[i][j],end = " ")
        print()

def delete_node(v):
    global nodes_count
    if v not in nodes:
        print(v, "is not found!")
    else:
        nodes_count -=1
        index = nodes.index(v)
        nodes.pop(index)
        graph.pop(index)
        for n in graph:
            n.pop(index)

def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1, "not found!")
    elif v2 not in nodes:
        print(v2 , "not found!")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2) 
        graph[index1][index2] = 0
        graph[index2][index1] = 0

add_node('A')
add_node('B')
add_node('C')
add_edge('C',"A")
# delete_node('B')
delete_edge('A','C')
# delete_node('C')
# delete_node('A')
print(nodes)
print()
print_graph(graph)
