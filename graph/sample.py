#----------------------------------------------------------ADJASCENCY MATRIX------------------------------------------------------------#
def add_node(v):
    global nodes_count
    if v in nodes:
        print('Node already in graph!')
        return
    else:
        nodes_count+=1
        nodes.append(v)
        for i in graph:
            i.append(0)
        temp=[]
        for i in range(len(nodes)):
            temp.append(0)
        graph.append(temp)

def add_edge(v1,v2,cost):
    if v1 not in nodes:
        print('Node not found!')
        return
    elif v2 not in nodes:
        print('Node not found!')
        return
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=cost
        graph[index2][index1]=cost

def delete_node(v):
    global nodes_count
    if v not in nodes:
        print('Node not found!')
    else:
        index=nodes.index(v)
        nodes_count-=1
        nodes.remove(v)
        graph.pop(index)
        for i in graph:
            i.pop(index)

def delete_edge(v1,v2):
    if v1 not in nodes:
        print('Node not found!')
    elif v2 not in nodes:
        print('Node not found!')
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=0
        graph[index2][index1]=0

def print_graph():
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            print(graph[i][j],end=' ')
        print()


graph=[]
nodes=[]
nodes_count=0

add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_edge('A','B',2)
add_edge('C','B',4)
add_edge('C','D',5)
add_edge('A','D',7)
delete_node('D')

delete_edge('A','B')
delete_edge('C','B')
print(nodes)

print_graph()

#----------------------------------------------------------ADJASCENCY LIST------------------------------------------------------------#
def add_node1(v):
    if v in graph1:
        print('Node already in graph!')
        return
    else:
        graph1[v]=[]

def add_edge1(v1,v2,cost):
    if v1 not in graph1:
        print('Node not found!')
        return
    elif v2 not in graph1:
        print('Node not found!')
        return
    else:
        # list1=(v1,cost)
        # list2=(v2,cost)
        graph1[v1].append(v2)
        graph1[v2].append(v1)
        
def delete_node1(v):
    if v not in graph1:
        print('node not found!')
        return
    else:
        graph1.pop(v)
        for i in graph1:
            list1=graph1[i]
            if v in list1:
                list1.remove(v)

def delete_edge1(v1,v2,cost):
    if v1 not in graph1:
        print('Node not found!')
        return
    elif v2 not in graph1:
        print('Node not found!')
    else:
        # temp1=(v1,cost)
        # temp2=(v2,cost)
        graph1[v1].remove(v2)
        graph1[v2].remove(v1)

def DFS(node,visited,graph):
    if node not in graph:
        print('Node not found!')
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
def DFS_iter(node,graph):
    if node not in graph:
        print('Node not found!')
        return
    stack=[]
    stack.append(node)
    visit=set()
    while stack:
        curr=stack.pop()
        if curr not in visit:
            print(curr,end=' ')
            visit.add(curr)
            for i in graph[curr]:
                stack.append(i)
    for i in graph:
        if i not in visit:
            print(i,end=' ')
from collections import deque
def BFS(node,graph):
    if node not in graph:
        print('node not found!')
        return
    queue=deque([node])
    visit= set()
    while queue:
        curr=queue.popleft()
        if curr not in visit:
            print(curr,end=' ')
            visit.add(curr)
            for i in  graph[curr]:
                queue.append(i)

    for i in graph:
        if i not in visit:
            print(i,end=' ')
            visit.add(i)



visited=set()
graph1={}
add_node1('A')
add_node1('B')
add_node1('C')
add_node1('D')
add_edge1('A','B',3)
add_edge1('C','B',1)
add_edge1('C','D',7)
# delete_node1('C')
delete_edge1('A','B',3)
print(graph1)
print('<-------------------------------DFS RECURSIVE------------------------------->')
DFS('A',visited,graph1)
print()
print('<-------------------------------DFS ITERATIVE------------------------------->')
DFS_iter('A',graph1)
print()
print('<-------------------------------BFS ITERATIVE------------------------------->')
BFS('A',graph1)