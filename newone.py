import heapq
import time

class GameVariables:
    def __init__(self):
        self.empty_tanks = 2
        self.full_tanks = 6
        self.size = 6
        self.num_colors = 6
        self.initial_state =[[], [], [1, 2, 3, 0, 0, 0], [2, 2, 1, 2, 3, 1], [3, 3, 4, 1, 4, 0], [4, 3, 2, 4, 5, 3], [5, 5, 5, 2, 5, 1], [5, 4, 1, 0, 4, 0]]
class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
    def f(self):
        return self.g + self.h
    def __lt__(self, other):
        """
        Defines the less-than comparison for Nodes based on their f values.
        If f values are equal, compare g values to prioritize nodes with lower costs.
        """
        return (self.f(), self.g) < (other.f(), other.g)  # Tuple comparison for tie-breaking on g

def list_to_tuple(lst):
    if isinstance(lst, list):
        return tuple(list_to_tuple(item) for item in lst)
    else:
        return lst


def successors(current_state, max_colors_per_tube):
    """
    Generates valid successor states, transferring contiguous colors in one move.
    """
    successors = []

    for from_tube in range(len(current_state)):
        if not current_state[from_tube]:  # Skip empty source tubes
            continue

        top_color = current_state[from_tube][-1]
        transfer_count = 1  # Start with transferring one color

        # Check for contiguous colors
        while transfer_count < len(current_state[from_tube]) and current_state[from_tube][-1 - transfer_count] == top_color:
            transfer_count += 1

        for to_tube in range(len(current_state)):
            if from_tube != to_tube:
                is_to_tube_empty = not current_state[to_tube]
                is_same_color = current_state[to_tube] and current_state[to_tube][-1] == top_color
                is_to_tube_not_full = len(current_state[to_tube]) + transfer_count <= max_colors_per_tube
                is_to_tube_valid = is_to_tube_empty or (is_same_color and is_to_tube_not_full)

                if is_to_tube_valid:
                    new_state = [tube[:] for tube in current_state]
                    for _ in range(transfer_count):  # Transfer the entire contiguous block
                        new_state[to_tube].append(new_state[from_tube].pop())
                    successors.append((new_state, 1))  # Cost remains 1 per move, regardless of colors transferred

    return successors

def improved_heuristic(current_state, goal_state, weights):
    """
    Heuristic function for the tube sorting puzzle, prioritizing colors with fewer empty tubes to target,
    and giving a bonus for longer sequences of the same color.
    """
    total_distance = 0
    color_counts = {}

    # Determine the maximum color value in the goal_state
    max_color = max(color for tube in goal_state for color in tube if tube)

    # Initialize color_positions with the appropriate range
    color_positions = {color: [] for color in range(max_color + 1)}

    for i, tank in enumerate(goal_state):
        for j, color in enumerate(tank):
            color_positions[color].append((i, j))
            color_counts[color] = color_counts.get(color, 0) + 1

    for i, tank in enumerate(current_state):
        current_color = None
        sequence_length = 0
        for j, color in enumerate(tank):
            if color_positions[color]:
                goal_i, goal_j = color_positions[color][0]  # Use the first goal position for this color

                # Calculate Manhattan distance and penalize if not in correct order
                if j > goal_j:  # Color is too low in the current tube
                    total_distance += 2 * abs(j - goal_j)
                else:
                    total_distance += abs(i - goal_i) + abs(j - goal_j)

                # Add bonus for top colors
                if j == len(tank) - 1:
                    total_distance -= weights['top_color_weight']

                # Add bonus for bottom colors
                if j == 0:
                    total_distance -= weights['bottom_color_weight']

                # Add bonus for consolidating colors
                if j > 0 and tank[j - 1] == color:
                    total_distance -= weights['color_consolidation_weight']

                # Add penalty for abundant colors not in their goal tube
                if i != goal_i:
                    total_distance += color_counts[color] * weights['abundant_color_weight']

            # Check for sequences and add bonus
            if color == current_color:
                sequence_length += 1
            else:
                current_color = color
                sequence_length = 1
            total_distance -= weights['sequence_bonus'] * (sequence_length - 1)  # Bonus only for sequences of length 2 or more

    # Prioritize colors with fewer empty tubes to target:
    for color, positions in color_positions.items():
        empty_tubes_for_color = sum(1 for tube in current_state if not tube or tube[-1] == color)
        total_distance += (10 - empty_tubes_for_color) * weights['abundant_color_weight']  # Adjust the weight as needed

    # Add bonus for empty tubes
    empty_tubes = sum(1 for tank in current_state if not tank)
    total_distance -= empty_tubes * weights['empty_tube_weight']

    return total_distance



def astar(start_state, goal_state, heuristic, successors, max_colors_per_tube):
    """
    A* search algorithm with loop prevention.
    """
    open_list = []
    closed_set = set()
    previous_states = set()

    start_node = Node(start_state, None, 0, heuristic(start_state, goal_state, weights))
    heapq.heappush(open_list, (start_node.f(), start_node))
    previous_states.add(list_to_tuple(start_state))

    while open_list:
        _, current_node = heapq.heappop(open_list)

        if current_node.state == goal_state:
            # (reconstruct and return path)
            print("Goal reached!")
            path = []
            cost = 0
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
                cost += 1 # Each node represents a step
            return path[::-1], cost  # Reverse the path and return it along with the cost

        state_tuple = list_to_tuple(current_node.state)
        closed_set.add(state_tuple)

        for successor_state, cost in successors(current_node.state, max_colors_per_tube):
            successor_tuple = list_to_tuple(successor_state)

            if successor_tuple in closed_set or successor_tuple in previous_states:
                continue

            g = current_node.g + cost
            h = heuristic(successor_state, goal_state, weights)
            successor_node = Node(successor_state, current_node, g, h)

            heapq.heappush(open_list, (successor_node.f(), successor_node))
            previous_states.add(successor_tuple)

    return None , None # No solution found


def can_move_liquid(current_state, from_tank, to_tank):
    if from_tank >= len(current_state) or from_tank < 0:
        return False
    if not current_state[from_tank]:
        return False
    if to_tank >= len(current_state) or to_tank < 0:
        return False
    if is_full(current_state, to_tank):
        return False
   # if the top is most left:
    from_top_color = current_state[from_tank][0]
    to_top_color = current_state[to_tank][0] if current_state[to_tank] else None
    # if the top is most right:
    # from_top_color = current_state[from_tank][-1]
    # to_top_color = current_state[to_tank][-1] if current_state[to_tank] else None
    if from_top_color == to_top_color or is_empty(current_state, to_tank):
        return True
    return False

def is_full(current_state, tank):
    game_vars = GameVariables()
    max_size = game_vars.size
    return len(current_state[tank]) >= max_size

def is_empty(current_state, tank):
    return len(current_state[tank]) == 0

def create_goal_state(initial_state, empty_tanks):
    """
    Creates the goal state for the tube sorting puzzle given an initial state.

    Args:
        initial_state: The initial state of the puzzle (list of lists).
        empty_tanks: The number of empty tubes in the initial state.

    Returns:
        The goal state (list of lists) where each tube contains a single color,
        and the number of empty tubes matches the initial state.
    """
    unique_colors = set()
    for tube in initial_state:
        for color in tube:
            unique_colors.add(color)

    max_size = max(len(tube) for tube in initial_state if tube)  # Find max size of non-empty tubes

    goal_state = []
    for color in sorted(unique_colors):
        goal_state.append([color] * max_size)

    # Add empty tubes to the goal state
    goal_state.extend([[]] * empty_tanks)

    return goal_state

# Example usage
game_vars = GameVariables()
start_state = game_vars.initial_state
goal_state =  create_goal_state (start_state , game_vars.empty_tanks )
print ("goal_state: ", goal_state)
# הגדרת המשקלים:
weights = {'empty_tube_weight': 10, 'color_consolidation_weight': 5, 'abundant_color_weight': 2,
           'top_color_weight': 1, 'bottom_color_weight': 1, 'sequence_bonus': 3}

start_time = time.time()

path, cost = astar(start_state, goal_state, improved_heuristic, successors, game_vars.size)
end_time = time.time()
end_time = time.time()

if path:
    print("Path found!")
    for state in path:
        print(state)
    print(f"Number of steps:{cost}")
else:
    print("No path found.")
print(f"Elapsed time: {end_time - start_time:.2f} seconds")
