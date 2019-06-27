import get_perimeter_location as gpl
import numpy as np

def init_VC(perimeter, num_of_nodes):
    VC = np.empty([num_of_nodes, num_of_nodes])

    for i in range(num_of_nodes):
        if i in perimeter:
            VC[i][0], VC[i][1] = gpl.get_perimeter_location(i)
        else:
            VC[i][0], VC[i][1] = 100, 100 # some default value. To change in step-2


    return VC