def add_node(v):
    if v in graph:
        print(v ,'is already in graph')
    else:
        graph[v]=[]

def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,'not found in graph!')        
    elif v2 not in graph:
        print(v2,'not found in graph!')
    else:
        # list1=[v1,cost]
        # list2=[v2,cost]
        graph[v1].append(v2)
        graph[v2].append(v1)

def DFSiterative(node,graph):
    visited=set()
    if node not in graph:
        print('node not in graph!')
        return
    stack=[]
    stack.append(node)
    while stack:
        curr= stack.pop()
        if curr not in visited:
            print(curr,end=' ')
            visited.add(curr)
            for i in graph[node]:
                stack.append(i)
    for i in graph:
        if i not in visited:
            print(i,end=' ')
            visited.add(i)





graph={}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')

add_edge('A','B')
add_edge('C','B')
add_edge('A','C')
print(graph)
DFSiterative('B',graph)


# print(graph)