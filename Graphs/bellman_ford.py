from typing import Dict, List

def printDist(dist, V):
    print("Vertex Distance")
    distances = ("INF" if d == float("inf") else d for d in dist)
    print("\t".join(f"{i}\t{d}" for i, d in enumerate(distances)))

def BellmanFord(graph: List[Dict[str, int]], V: int, E: int, src: int) -> int:
    mdist = [float("inf") for i in range(V)]
    mdist[src] = 0.0

    for i in range(V-1):
        for j in range(E):
            u = graph[j]["src"]
            v = graph[j]["dst"]
            w = graph[j]["weight"]

            if mdist[u] != float("inf") and mdist[u] + w < mdist[v]:
                mdist[v] = mdist[u] + w

    for j in range(E):
        u = graph[j]["src"]
        v = graph[j]["dst"]
        w = graph[j]["weight"]

        if mdist[u] != float("inf") and mdist[u] + w < mdist[v]:
            print("Negative Cycle Found. Solution not possible")
            return

    printDist(mdist, V)
    return src

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
    BellmanFord(graph, V, E, gsrc)