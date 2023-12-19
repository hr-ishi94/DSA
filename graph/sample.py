#adjascency matrix
def add_node(v):
    global nodes_count
    if v in nodes:
        print(v,'already in graph!')
        return
    else:
        nodes_count+=1
        nodes.append(v)
        for i in graph:
            i.append(0)
        temp=[]
        for i in range(nodes_count):
            temp.append(0)
        graph.append(temp)
def print_graph():
    for i in range(nodes_count):
        for j in range(nodes_count):
            print(graph[i][j],end=' ')
        print()

def add_edge(v1,v2,cost):
    if v1 not in nodes:
        print('not found in nodes!')
    elif v2 not in nodes:
        print('not found in nodes!')
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=cost
        graph[index2][index1]=cost

def delete_node(v):
    global nodes_count
    if v not in nodes:
        print(v,'not found in nodes!')
        return
    else:
        index1=nodes.index(v)
        nodes.pop(index1)
        nodes_count-=1
        graph.pop(index1)
        for i in graph:
            i.pop(index1)

def delete_edge(v1,v2,):
    if v1 not in nodes:
        print(v1,'not found in nodes!')
    elif v2 not in nodes:
        print(v2,'not found in nodes!')
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=0
        graph[index2][index1]=0

graph=[]
nodes=[]
nodes_count=0

add_node('A')
add_node('B')
add_node('C')
add_edge('B','C',3)
add_edge('A','C',3)
# print_graph()
delete_edge('B','C')
delete_edge('A','C')
# print_graph()


#adjascency List


graph1=dict()

def add_node1(v):
    if v in graph1:
        print('Already in the graph!')
    else:
        graph1[v]=[]

def add_edge1(v1,v2):
    if v1 not in graph1:
        print('Node not found in nodes!')
    elif v2 not in graph1:
        print('Nodes not found in nodes!')
    else:
        
        graph1[v1].append(v2)
        graph1[v2].append(v1)

def delete_node1(v):
    if v not in  graph1:
        print('Node not in nodes!')
    else:
        graph1.pop(v)
        for i in graph1:
            list1=graph1[i]
            if v in list1:
                list1.remove(v)

def delete_edge1(v1,v2):
    if v1 not in graph1:
        print('Not found!')
    elif v2 not in graph1:
        print('Not found!')
    else:
        graph1[v1].remove(v2)
        graph1[v2].remove(v1)

def DFS(node,graph,visited):
    if node not in graph:
        print('Node not found in graph!')
        return
    if node not in visited:
        print(node,end=' ')
        visited.add(node)
        for i in graph[node]:
            DFS(i,graph,visited)
    for i in graph:
        if i not in visited:
            print(i,end=' ')
            visited.add(i)

def DFS_iter(node,graph):
    visited=set()
    if node not in graph:
        print('Node not found!')
        return
    stack=[]
    stack.append(node)
    while stack:
        curr=stack.pop()
        if curr not in visited:
            print(curr,end=' ')
            visited.add(curr)
            for i in graph[curr]:
                stack.append(i)
    for i in graph:
        if i not in visited:
            print(i,end=' ')
            visited.add(i)

from collections import deque

def BFS(node,graph):
    visited=set()
    if node not in graph:
        print('Node not in graph!')
        return
    queue=deque([node])

    while queue:
        curr=queue.popleft()
        if curr not in visited:
            print(curr,end=' ')
            visited.add(curr)
            for i in graph[curr]:
                queue.append(i)
    for i in graph:
        if i not in visited:
            print(i,end=' ')
            visited.add(i)

    

visited=set()
add_node1("A")
add_node1("B")
add_node1("C")
add_node1("D")
add_edge1('B','C')
add_edge1('B','A')
# delete_edge1('B','C')
print(graph1)
print('DFS Recursion: ',end=' ')
DFS('B',graph1,visited)
print()
print('DFS Iterative using stack: ',end=' ')
DFS_iter('B',graph1)
print()
print('BFS:',end=' ')
BFS('B',graph1)