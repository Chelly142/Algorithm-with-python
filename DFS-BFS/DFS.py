def dfs(graph, v ,visited):
    visitied[v] = True
    print(v,end = ' ')
    for i in graph[v]:
        if not vitited[i]:
            dfs(graph[i],i,vitited)
 
