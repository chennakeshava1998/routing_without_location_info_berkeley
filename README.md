# routing_without_location_info_berkeley
**Input:** 2-hop neighbourhood information for every node, Geographic Coordinates of Perimeter Nodes
**Output:** Virtual Coordinates of all the nodes, which closely resemble the geographic map.

**How to Execute:**
1. Run `python3 relaxation/get_perimeter_location.py` and `relaxation/get_perimeter_location.py` initially to determine the location and the identity of the perimeter nodes.
2. Run `python3 relaxation/init_VC.py` to calculate the virtual cordinates.
3. Finally run `python3 relaxation/iterative_relaxation.py` to execute the algorithm proposed in the below paper.
4. Run `python3 relaxation/display_points.py` to visiualise the output of the algorithm.

## References
1. Rao, Ananth, et al. "Geographic routing without location information." 
Proceedings of the 9th annual international conference on Mobile computing and networking. ACM, 2003.
