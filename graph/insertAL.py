def add_node(v):
    if v in graph:
        print(v ,'is already in graph')
    else:
        graph[v]=[]

def add_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1,'not found in graph!')        
    elif v2 not in graph:
        print(v2,'not found in graph!')
    else:
        list1=[v1,cost]
        list2=[v2,cost]
        graph[v1].append(list2)
        graph[v2].append(list1)



graph={}
add_node('A')
add_node('B')
add_node('C')

add_edge('A','B',4)
add_edge('C','B',5)
add_edge('A','C',12)
print(graph)