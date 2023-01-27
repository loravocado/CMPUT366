
import heapq
import math

def run_dijkstra(s_init, s_g, map):  
    open = []
    closed = {}
    node_counter = 0
    heapq.heappush(open, s_init) 
    closed[s_init.state_hash()] = s_init.get_g()
    while len(open) > 0:
        n = heapq.heappop(open)

        if n == s_g:
            return closed[n.state_hash()], node_counter
        
        for neighbor in map.successors(n):
            neighbor_cost = neighbor.get_g()
            neighbor_hash = neighbor.state_hash()
            if neighbor_hash not in closed:
                heapq.heappush(open, neighbor)
                closed[neighbor_hash] = neighbor.get_g()
            if neighbor_hash in closed and neighbor_cost < closed[neighbor_hash]:
                closed[neighbor_hash] = neighbor_cost
                heapq.heapify(open)
        node_counter += 1
    return -1, node_counter

def run_bibs(s_init, s_g, map):
    open_f = []
    open_b = []
    closed_f = {}
    closed_b = {}
    U = math.inf
    
    heapq.heappush(open_f, s_init) 
    heapq.heappush(open_b, s_g)
    closed_f[s_init.state_hash()] = s_init.get_g()
    closed_b[s_g.state_hash()] = s_g.get_g()

    while len(open_f) > 0 and len(open_b) > 0:
        

  
    
