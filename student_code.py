import math
import heapq

def euclidean_dist(a_coor_lst, b_coor_lst):
    return math.sqrt(sum([(a - b)**2 for a, b in zip(a_coor_lst, b_coor_lst)]))


def create_graph(m):
    adj_lst = [list() for _ in range(len(m.roads))]
    for source in range(len(m.roads)):
        for dest in m.roads[source]:
            cost = euclidean_dist(m.intersections[source], m.intersections[dest])
            adj_lst[source].append((dest, cost))
    return adj_lst
        

def shortest_path(M,start,goal):
    print("shortest path called")
    graph = create_graph(M)
    heap = [(0, start)]
    cost_so_far = {}
    cost_so_far[start] = 0
    came_from = {}
    came_from[start] = None
    path = []
    
    while len(heap) > 0:
        priority, curr_vertex = heapq.heappop(heap)
        
        if curr_vertex == goal:
            break
            
        for neighbor, edge_cost in graph[curr_vertex]:
            new_cost = cost_so_far[curr_vertex] + edge_cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                p = new_cost + euclidean_dist(M.intersections[neighbor], M.intersections[goal])
                heapq.heappush(heap, (p, neighbor)) 
                came_from[neighbor] = curr_vertex
    
    # reconstruct path
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path