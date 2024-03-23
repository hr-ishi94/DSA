graph = {}

def add_node(v):
    if v in graph:
        print("node already present!")
    else:
        graph[v] = []
def add_edge(v1, v2):
    if v1 not in graph:
        print("node not found!")
    elif v2 not in graph:
        print("node not found!")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

def delete_node(v):
    if v not in graph:
        print("node not found!")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            if v in list1:
                list1.remove(v)

def delete_edge(v1,v2):
    if v1 not in graph:
        print("node not found!")
    elif v2 not in graph:
        print("node not found!")
    else:
        graph[v1].remove(v2)
        graph[v2].remove(v1)

visited = set()

def dfs_recur(node,visited,graph):

    if node not in graph:
        print("node not found!")
        return 
    if node not in visited:
        visited.add(node)
        print(node,end=" ")
        for i in graph[node]:
            dfs_recur(i,visited,graph)
    

add_node('A')
add_node('B')
add_node('C')
add_edge('A','B')
add_edge('A','C')
# delete_edge('A','B')
# delete_node("A")
print(graph)
dfs_recur('C',visited,graph)