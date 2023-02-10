import heapq

def run_dijkstra(s_init, s_g, map):  
    open = []
    closed = {}
    node_counter = 0
    heapq.heappush(open, s_init) 
    closed[s_init.state_hash()] = s_init

    #While still nodes in open list
    while len(open) > 0:
        n = heapq.heappop(open)

        #If we found the goal
        if n == s_g:
            # map.plot_map(closed, s_init, s_g, "plotted_map_dijkstra.png")
            # Return the g value of n in the closed list
            return closed[n.state_hash()].get_g(), node_counter
        
        #For each connected node in the map
        for neighbor in map.successors(n):
            neighbor_cost = neighbor.get_g()
            neighbor_hash = neighbor.state_hash()

            #If it is not in the closed list, add it to the open and closed list
            if neighbor_hash not in closed:
                heapq.heappush(open, neighbor)
                closed[neighbor_hash] = neighbor

            #If a better path is found
            if neighbor_hash in closed and neighbor_cost < closed[neighbor_hash].get_g():
                closed[neighbor_hash] = neighbor
                heapq.heapify(open)
        node_counter += 1
    # map.plot_map(closed, s_init, s_g, "plotted_map_dijkstra.png")
    return -1, node_counter

def run_bibs(s_init, s_g, map):
    open_f = []
    open_b = []
    closed_f = {}
    closed_b = {}
    u = float("inf") 
    node_counter = 0

    heapq.heappush(open_f, s_init) 
    heapq.heappush(open_b, s_g)
    closed_f[s_init.state_hash()] = s_init
    closed_b[s_g.state_hash()] = s_g

    #While nodes are in both the open list for the backwards direction and the open list for the forwards direction
    while len(open_f) > 0 and len(open_b) > 0:

        #Stopping condition
        if u <= open_f[0].get_g() + open_b[0].get_g():
            # closed_f.update(closed_b)
            # map.plot_map(closed_f, s_init, s_g, "plotted_map_bibs.png")
            return u, node_counter

        #Expanding forward search
        if open_f[0].get_g() < open_b[0].get_g(): #expand forwards
            n = heapq.heappop(open_f)

            #For each connected node to n
            for neighbor in map.successors(n):
                neighbor_hash = neighbor.state_hash()
                neighbor_cost = neighbor.get_g()
                
                #Found a solution path
                if neighbor_hash in closed_b:
                    u = min(u, neighbor_cost + closed_b[neighbor_hash].get_g())

                #If it is not in the closed forward list 
                if neighbor_hash not in closed_f:
                    heapq.heappush(open_f, neighbor)
                    closed_f[neighbor_hash] = neighbor 

                #If it found a better path
                if neighbor_hash in closed_f and neighbor_cost < closed_f[neighbor_hash].get_g():
                    closed_f[neighbor_hash] = neighbor
                    heapq.heapify(open_f)
        else: #expand backwards
            n = heapq.heappop(open_b)

            for neighbor in map.successors(n):
                neighbor_hash = neighbor.state_hash()
                neighbor_cost = neighbor.get_g()

                if neighbor_hash in closed_f:
                    u = min(u, neighbor_cost + closed_f[neighbor_hash].get_g())

                if neighbor_hash not in closed_b:
                    heapq.heappush(open_b, neighbor)
                    closed_b[neighbor_hash] = neighbor

                if neighbor_hash in closed_b and neighbor_cost < closed_b[neighbor_hash].get_g():

                    closed_b[neighbor_hash] = neighbor
                    heapq.heapify(open_b)
        node_counter += 1

    # closed_f.update(closed_b)
    # map.plot_map(closed_f, s_init, s_g, "plotted_map_bibs.png")
    return -1, node_counter