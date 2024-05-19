import heapq
import time

class GameVariables:
    def __init__(self):
        self.empty_tanks = 2
        self.full_tanks = 8
        self.size = 8
        self.num_colors = 8
        self.initial_state = [
            [1, 3, 5, 4, 4, 7, 6, 1], [2, 2, 0, 0, 4, 3, 6, 7],
            [2, 1, 1, 4, 5, 6, 0, 2], [0, 6, 6, 5, 4, 7, 7, 3],
            [3, 4, 1, 0, 5, 7, 4, 4], [7, 6, 2, 2, 3, 1, 0, 0],
            [7, 3, 3, 1, 2, 5, 5, 6], [7, 6, 5, 5, 3, 2, 1, 0], [], []
        ]

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h

    def f(self):
        return self.g + self.h

def list_to_tuple(lst):
    if isinstance(lst, list):
        return tuple(list_to_tuple(item) for item in lst)
    else:
        return lst

def astar(start_state, goal_state, heuristic, successors):
    open_list = []
    closed_set = set()
    
    start_node = Node(start_state, None, 0, heuristic(start_state, goal_state))
    heapq.heappush(open_list, (start_node.f(), id(start_node), start_node))
    
    iteration = 0
    while open_list:
        iteration += 1
        if iteration % 1000 == 0:
            print(f"Iteration: {iteration}, Open list size: {len(open_list)}, Closed set size: {len(closed_set)}")
        
        _, _, current_node = heapq.heappop(open_list)
        
        if current_node.state == goal_state:
            print("Goal reached!")
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            path = path[::-1]
            print(f"Number of steps in the solution path: {len(path) - 1}")
            return path
        
        state_tuple = list_to_tuple(current_node.state)
        closed_set.add(state_tuple)
        
        for successor_state, cost in successors(current_node.state):
            successor_tuple = list_to_tuple(successor_state)
            if successor_tuple in closed_set:
                continue
            
            g = current_node.g + cost
            h = heuristic(successor_state, goal_state)
            successor_node = Node(successor_state, current_node, g, h)
            
            heapq.heappush(open_list, (successor_node.f(), id(successor_node), successor_node))
    
    return None

def improved_heuristic(current_state, goal_state):
    total_distance = 0
    
    for i, tank in enumerate(current_state):
        if tank:
            for j, fluid in enumerate(tank):
                try:
                    goal_position = next((gi, gj) for gi, goal_tank in enumerate(goal_state) for gj, goal_fluid in enumerate(goal_tank) if goal_fluid == fluid)
                    total_distance += abs(i - goal_position[0]) + abs(j - goal_position[1])
                    
                    # Penalize if the current fluid is not on top of the same fluid
                    if j > 0 and tank[j - 1] != fluid:
                        total_distance += 2
                except StopIteration:
                    pass
    
    return total_distance

def successors(current_state):
    successors = []
    for from_tank in range(len(current_state)):
        for to_tank in range(len(current_state)):
            if from_tank != to_tank:
                if can_move_liquid(current_state, from_tank, to_tank):
                    new_state = [list(tank) for tank in current_state]
                    new_state[to_tank].insert(0, new_state[from_tank].pop(0))
                    successors.append((new_state, 1))

    return successors

def can_move_liquid(current_state, from_tank, to_tank):
    if from_tank >= len(current_state) or from_tank < 0:
        return False
    if not current_state[from_tank]:
        return False
    if to_tank >= len(current_state) or to_tank < 0:
        return False
    if is_full(current_state, to_tank):
        return False

    from_top_color = current_state[from_tank][0]
    to_top_color = current_state[to_tank][0] if current_state[to_tank] else None

    if from_top_color == to_top_color or is_empty(current_state, to_tank):
        return True

    return False

def is_full(current_state, tank):
    game_vars = GameVariables()
    max_size = game_vars.size
    return len(current_state[tank]) >= max_size

def is_empty(current_state, tank):
    return len(current_state[tank]) == 0

# Example usage
game_vars = GameVariables()
start_state = game_vars.initial_state
goal_state = [
    [1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6, 6, 6],
    [7, 7, 7, 7, 7, 7, 7, 7], [0, 0, 0, 0, 0, 0, 0, 0], [], []
]

start_time = time.time()
path = astar(start_state, goal_state, improved_heuristic, successors)
end_time = time.time()

if path:
    print("Path found!")
    for state in path:
        print(state)
else:
    print("No path found.")
print(f"Elapsed time: {end_time - start_time:.2f} seconds")