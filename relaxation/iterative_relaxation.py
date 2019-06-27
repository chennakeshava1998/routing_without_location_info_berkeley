def iterative_relation(adj, VC, perimeter):

    n = adj.shape[0] # number of nodes

    for i in range(n):
        if i not in perimeter: # perimeter nodes remain fixed
            # relaxation formula    
            num_of_neighbours = 0
            sum_neighbours_x = 0
            sum_neighbours_y = 0

            for j in adj[i]:
                if adj[i][j] != 0:
                    num_of_neighbours+=1
                    sum_neighbours+=VC[i][j]

            VC[i][0] = sum_neighbours_x/num_of_neighbours
            VC[i][1] = sum_neighbours_y/num_of_neighbours

    return VC