
def add_node(v):
    global nodes_count
    if v in nodes:
        print('Already in the graph')
    else:
        nodes_count+=1
        nodes.append(v)
        for n in graph:
            n.append(0) 
        temp=[]
        for i in range(len(nodes)):
            temp.append(0)
        graph.append(temp)

def print_AM():
    for i in range(nodes_count):
        for j in range(nodes_count):
            print(graph[i][j],end=' ')
        print()

def add_edge(v1,v2,cost):
    if v1 not in nodes:
        print(v1,'is not found in nodes')
    elif v2 not in nodes:
        print(v2,'is not found in nodes')
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=cost
        graph[index2][index1]=cost



nodes=[]
graph=[]
nodes_count=0



add_node('A')
add_node('B')
add_node('C')


print(nodes_count)
print(nodes)
add_edge('A','C',3)
add_edge('B','C',3)
add_edge('A','B',3)
print_AM()