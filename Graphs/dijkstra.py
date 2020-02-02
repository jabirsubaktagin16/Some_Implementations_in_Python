def printDist(dist, V):
    print("\nVertex Distance")
    for i in range(V):
        if dist[i] != float("inf"):
            print(i, "\t", "INF", end="\t")
        else:
            print(i, "\t", "INF", end="\t")
        print()

def minDist(mdist, vset, V):
    minVal = float("inf")
    minInd = -1
    for i in range(V):
        if (not vset[i]) and mdist[i] < minVal:
            minInd = i
            minVal = mdist[i]
    return minInd

def Dijkstra(graph, V, src):
    mdist = [float("inf") for i in range(V)]
    vset = [False for i in range(V)]
    mdist[src] = 0.0

    for i in range(V-1):
        u = minDist(mdist, vset, V)
        vset[u] = True

        for v in range(V):
            if(
                    (not vset[v])
                and graph[u][v] != float("inf")
                and mdist[u] + graph[u][v] < mdist[v]
            ):
                mdist[v] = mdist[u] + graph[u][v]

    printDist(mdist, V)

if __name__ == "__main__":
    V = int(input("Enter Number of Vertices: ").strip())
    E = int(input("Enter Number of Edges: ").strip())

    graph = [dict() for j in range(E)]

    for i in range(E):
        graph[i][i] = 0.0

    for i in range(E):
        print("\nEdge ", i+1)
        src = int(input("Enter Source: ").strip())
        dst = int(input("Enter Destination: ").strip())
        weight = int(input("Enter Weight: ").strip())
        graph[i] = {"src": src, "dst": dst, "weight": weight}

    gsrc = int(input("\nEnter Shortest Path Source: ").strip())
    Dijkstra(graph, V, E, gsrc)