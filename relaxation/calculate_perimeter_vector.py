import numpy as np
import queue
def calculate_perimeter_vector(adj):
    perimeter_vec = np.empty([adj.shape[0], adj.shape[1]])

    for i in range(adj.shape[0]):
        perimeter_vec[i] = bfs(i, adj)


    return perimeter_vec

def bfs(source, adj):
    perimeter_vec = np.zeros([adj.shape[0]])
    visited = np.zeros([adj.shape[0]])

    Q = queue.Queue(maxsize=adj.shape[0])
    while not Q.empty():
        a = Q.get()

        if not visited[a]:
            visited[a] = True

            # traverse all the neighbours of a
            for i in range(adj.shape[0]):
                if adj[a][i] and not visited[i]:
                    Q.put(i)
                    perimeter_vec[i] = perimeter_vec[a] + 1


    return perimeter_vec

