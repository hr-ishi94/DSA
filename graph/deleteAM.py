
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

def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1,'is not found in nodes')
    elif v2 not in nodes:
        print(v2,'is not found in nodes')
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=1
        graph[index2][index1]=1

def delete_node(v):
    global nodes_count
    if v not in nodes:
        print(v,'is not found in graph')
    else:
        index1=nodes.index(v)
        nodes_count-=1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)

def delete_edge(v1,v2):
    if v1 not in nodes:
        print('not found!')
    elif v2 not in nodes:
        print('not found!')
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=0
        # graph[index2][index1]=0




nodes=[]
graph=[]
nodes_count=0



add_node('A')
add_node('B')
add_node('C')


print(nodes_count)
print(nodes)
add_edge('A','C')
add_edge('B','C')
add_edge('A','B')

print_AM()
delete_edge('A','C')
delete_edge('A','B')
delete_edge('C','B')
print()
print_AM()