
import heapq

def run_dijkstra(s_init, s_g, map):  
    open = []
    closed = {}
    node_counter = 0
    heapq.heappush(open, s_init) 
    closed[s_init.state_hash()] = s_init
    while len(open) > 0:
        n = heapq.heappop(open)

        if n == s_g:
            return closed[n.state_hash()].get_g(), node_counter
        
        for neighbor in map.successors(n):
            neighbor_cost = neighbor.get_g()
            neighbor_hash = neighbor.state_hash()
            if neighbor_hash not in closed:
                heapq.heappush(open, neighbor)
                closed[neighbor_hash] = neighbor
            if neighbor_hash in closed and neighbor_cost < closed[neighbor_hash].get_g():
                heapq.heapify(open)
        node_counter += 1
    return -1, node_counter

# def run_bibs():
    
