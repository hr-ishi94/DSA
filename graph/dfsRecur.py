from collections import deque

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

def DFS(node,visited,graph):
    if node not in graph:
        print('Node not found in graph!')
        return
    if node not in visited:
        print(node,end=' ')
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)
        for i in graph:
            if i not in visited:
                print(i,end=' ')
                visited.add(i)

def BFS(node,graph):
    if node not in graph:
        print('node not found!')
        return
    visit=set()
    arr=deque([node])
    while arr:
        vertex=arr.popleft()
        
        visit.add(vertex)
        for i in graph[vertex]:
            if i not in visit:
                arr.append(i)
    for i in visit:
        print(i,end=' ')
    for i in graph:
        if i not in visit:
            print(i,end=' ')
            visit.add(i)


    

visited=set()
graph={}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')

add_edge('A','B')
add_edge('A','C')
add_edge('C','B')
# add_edge('E','B')
# add_edge('D','B')
print('DFS:',end=' ')
DFS('A',visited,graph)
print()
print('BFS:',end=' ')
BFS('A',graph)
print()
# print(graph)