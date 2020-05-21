'''
Created on 21 may. 2020

@author: Cris
'''

def DFS(G, s):
    vis, pila = {s}, [s]
    print(vis)
    print(pila)
    print(G[pila[-1]])

    print("\n<< PROFUNDIDAD >> nodo de salida -->", s , end=" ")
    while pila:
        flag = 0
        for i in G[pila[-1]]:
            if i not in vis:
                pila.append(i)
                vis.add(i)
                flag = 1
                print(i, end = " ")
                break
        if not flag:
            pila.pop()

def BFS(G, s):
    vis, Q = {s}, deque([s])
    print("\n<<   ANCHURA   >> nodo de salida -->", s , end=" ")
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v not in vis:
                vis.add(v)
                Q.append(v)
                print(v, end = " ")


def PRIM(G, s):
    dist, known, path = {s: 0}, set(), {s: 0}
    while True:
        if len(known) == len(G) - 1:
            break
        mini = 100000
        for i in dist:
            if i not in known and dist[i] < mini:
                mini = dist[i]
                u = i
        known.add(u)
        for v in G[u]:
            if v[0] not in known:
                if v[1] < dist.get(v[0], 100000):
                    dist[v[0]] = v[1]
                    path[v[0]] = u

def DIJKSTRA(G, s):
    dist, known, path = {s: 0}, set(), {s: 0}
    while True:
        if len(known) == len(G) - 1:
            break
        mini = 100000
        for i in dist:
            if i not in known and dist[i] < mini:
                mini = dist[i]
                u = i
        known.add(u)
        for v in G[u]:
            if v[0] not in known:
                if dist[u] + v[1] < dist.get(v[0], 100000):
                    dist[v[0]] = dist[u] + v[1]
                    path[v[0]] = u
    for i in dist:
        if i != s:
            print(dist[i])