import GAME

import heapq
global initial_state, num_colors, empty_tanks, full_tanks,  size

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
        self.state = state  # Current state of the node
        self.parent = parent  # Parent node
        self.g = g  # Cost from start node to current node
        self.h = h  # Heuristic estimate from current node to goal node
    
    def f(self):
        return self.g + self.h  # Total estimated cost of the cheapest path from start to goal through current node

def list_to_tuple(lst):
    """
    Recursively converts a list to a tuple.
    """
    if isinstance(lst, list):
        return tuple(list_to_tuple(item) for item in lst)
    else:
        return lst

def astar(start_state, goal_state, heuristic, successors):
    open_list = []  # Priority queue of nodes to be evaluated
    closed_set = set()  # Set of evaluated nodes
    
    start_node = Node(start_state, None, 0, heuristic(start_state))
    heapq.heappush(open_list, (start_node.f(), id(start_node), start_node))
    
    while open_list:
        _, _, current_node = heapq.heappop(open_list)  # Pop node with lowest f value
        
        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path
            
        state_tuple = list_to_tuple(current_node.state)  # Convert list to tuple recursively
        closed_set.add(state_tuple)  # Add tuple to closed_set
        
        for successor_state, cost in successors(current_node.state):
            if list_to_tuple(successor_state) in closed_set:  # Convert list to tuple for comparison
                continue
            
            g = current_node.g + cost
            h = heuristic(successor_state, goal_state)
            successor_node = Node(successor_state, current_node, g, h)
            
            heapq.heappush(open_list, (successor_node.f(), id(successor_node), successor_node))
    
    return None  # No path found


#  heuristic function ( distance)

# def distance(current_state, goal_state):
#     """
#     Calculates the total Manhattan distance between each fluid unit in the current state and its corresponding 
#     position in the goal state.

#     Args:
#         current_state: The current game state.
#         goal_state: The goal state.

#     Returns:
#         The heuristic value.
#     """
#     total_distance = 0
    
#     for i in range(len(current_state)):
#         for j in range(len(current_state[i])):
#             fluid_unit = current_state[i][j]
#             if fluid_unit:
#                 # Find the position of the fluid unit in the goal state
#                 goal_position = find_fluid_unit_position(goal_state, fluid_unit)
#                 # Calculate Manhattan distance
#                 distance = abs(i - goal_position[0]) + abs(j - goal_position[1])
#                 total_distance += distance
    
#     return total_distance

# def find_fluid_unit_position(state, fluid_unit):
#     """
#     Finds the position of a fluid unit in the given state.

#     Args:
#         state: The game state.
#         fluid_unit: The fluid unit to find.

#     Returns:
#         The position of the fluid unit as a tuple (row, column).
#     """
#     for i in range(len(state)):
#         for j in range(len(state[i])):
#             if state[i][j] == fluid_unit:
#                 return (i, j)
            
def distance(current_state):
    """
    מחשבת את המרחק של כל יחידת נוזל מראש הערימה
    וסכום המרחק המצטבר של יחידות נוזל מאותו צבע.

    Args:
        current_state: מצב המשחק הנוכחי (רשימה של רשימות, כאשר כל רשימה פנימית מייצגת מכל).

    Returns:
        הערך של הוריסטיקה.
   """
     

    total_heuristic = 0
    color_unit_distances = {}
    unit_positions = {}
    unique_ids = 0

    # עוברים על כל המכלים
    for tank_index, tank in enumerate(current_state):
        # Check if tank is not empty before accessing its elements
        if tank:  # מזהים את צבע הנוזל העליון
            top_color = tank[0]

            # עוברים על כל יחידת נוזל במכל
            for color, quantity in enumerate(tank[1:]):
                # מקצים מזהה ייחודי
                unit_id = unique_ids
                unique_ids += 1

                # מעדכנים את מיקום יחידת הנוזל
                unit_positions[unit_id] = tank_index

    # מחשבים סכום מרחקים לכל צבע
    for positions in unit_positions.values():
        total_heuristic += positions

    return total_heuristic


# Example successors function (4-connected grid)
def successors(current_state):
  """
  מחזירה רשימה של צעדים אפשריים במצב הנוכחי.

  Args:
    current_state: מצב המשחק הנוכחי.

  Returns:
    רשימה של צעדים אפשריים (המכל מה, למכל לאן, איזה צבע).
  """

  successors = []
  # לולאה על כל המכלים
  for from_tank in range(len(current_state)):
    # לולאה על כל המכלים (למעט המכל הנוכחי)
    for to_tank in range(len(current_state)):
      if from_tank != to_tank:
        # בדיקת אם ניתן להעביר נוזל מהמכל הנוכחי למכל היעד
        if can_move_liquid(current_state, from_tank, to_tank):
          if (if_exist_next_top(current_state, from_tank , to_tank)):
          # מציאת צבע הנוזל העליון במכל הנוכחי
            color = current_state[from_tank][0]

          # הוספת הצעד לרשימה
          successors.append(((from_tank, to_tank, color), 1))

  return successors


def can_move_liquid(current_state, from_tank, to_tank):
    """
    Checks if liquid can be moved from the "from_tank" to the "to_tank".

    Args:
        current_state: The current game state.
        from_tank: The index of the tank from which liquid is being moved.
        to_tank: The index of the tank to which liquid is being moved.

    Returns:
        True if liquid can be moved, False otherwise.
    """
    # Check if "from_tank" is a valid index for "current_state"
    if from_tank >= len(current_state) or from_tank < 0:
        return False

    # Check if "current_state[from_tank]" is not empty
    if not current_state[from_tank]:
        return False

    # Check if "to_tank" is a valid index for "current_state"
    if to_tank >= len(current_state) or to_tank < 0:
        return False

    # Check if "to_tank" is not full
    if is_full(current_state, to_tank):
        return False

    # Check if the top color of the "from_tank" matches the top color of the "to_tank"
    from_top_color = current_state[from_tank][0]
    to_top_color = current_state[to_tank][0] if current_state[to_tank] else None

    if from_top_color == to_top_color:
        return True

    return False
    
    """
  בודקת אם ניתן להעביר נוזל מהמכל "from_tank" למכל "to_tank".

  Args:
    current_state: מצב המשחק הנוכחי.
    from_tank: מספר המכל שממנו רוצים להעביר נוזל.
    to_tank: מספר המכל שאליו רוצים להעביר נוזל.

  Returns:
    True אם ניתן להעביר נוזל, False אחרת.

  # בדיקת אם המכל היעד ריק
  if is_empty(current_state, to_tank):
    return True

  # בדיקת צבע הנוזל העליון במכל הנוכחי
  from_top_color = current_state[from_tank][0]

  # בדיקת צבע הנוזל העליון במכל היעד
  to_top_color = current_state[to_tank][0]

  # בדיקת אם צבע הנוזל העליון במכלים זהה
  if from_top_color == to_top_color:
    # בדיקת אם המכל היעד מלא
    if is_full(current_state, to_tank):
      return False

    # בדיקת אם מספר הצבעים במכל היעד פחות מהמקסימום
    if len(current_state[to_tank]) < size:
      return True

  return False

    """


def is_full(current_state, tank):
  """
  בודקת אם המכל "tank" מלא.

  Args:
    current_state: מצב המשחק הנוכחי (רשימה של רשימות).
    tank: מספר המכל שרוצים לבדוק.

  Returns:
    True אם המכל מלא, False אחרת.
  """
  game_vars= GameVariables()
  max_size = game_vars.size
  return len(current_state[tank]) >= max_size


def is_empty(current_state, tank):
  """
  בודקת אם המכל "tank" ריק.

  Args:
    current_state: מצב המשחק הנוכחי (רשימה של רשימות, כאשר כל רשימה פנימית מייצגת מכל).
    tank: מספר המכל שרוצים לבדוק.

  Returns:
    True אם המכל ריק, False אחרת.
  """

  return len(current_state[tank]) == 0

def if_exist_next_top(current_state, from_tank, to_tank):
    """
    Check if there exists a stack in the current state whose top color matches the second color in stack "from_tank".

    Args:
        current_state: The current game state.
        from_tank: The stack from which fluid is being moved (not relevant).
        to_tank: The stack to which fluid is being moved (not relevant).

    Returns:
        True if such a stack exists, False otherwise.
    """
    for tank_index in range(len(current_state)):
        # Skip the "from_tank" stack
        if tank_index == from_tank:
            continue

        # Check if the tank index is within bounds
        if tank_index < len(current_state):
            # Check if the tank has at least one element
            if current_state[tank_index]:
                top_color = current_state[tank_index][0]  # Access the first element
                second_color = current_state[from_tank][1]  # Second color in the "from_tank" stack

                # If the top color matches the second color, return True
                if top_color == second_color:
                    return True

    # No matching stack found
    return False



# Example usage
game_vars = GameVariables()
start_state = game_vars.initial_state
goal_state = [
            [1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4, 4],
            [5, 5, 5, 5, 5, 5, 5, 5], [6, 6, 6, 6, 6, 6, 6, 6],
            [7, 7, 7, 7, 7, 7, 7, 7], [8, 8, 8, 8, 8, 8, 8, 8], [], []
        ]  

#path = astar(start_state, goal_state, distance, successors)
path = astar(start_state, goal_state, lambda state: distance(state, goal_state), successors)

if path:
    print("Path:", path)
else:
    print("No path found.")













































