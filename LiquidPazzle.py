import GAME

import heapq
global initial_state, num_colors, empty_tanks, full_tanks,  size

class GameVariables:
    def _init_(self):
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
    
    def _init_(self, state, parent=None, g=0, h=0):
        self.state = state  # Current state of the node
        self.parent = parent  # Parent node
        self.g = g  # Cost from start node to current node
        self.h = h  # Heuristic estimate from current node to goal node
    
    def f(self):
        return self.g + self.h  # Total estimated cost of the cheapest path from start to goal through current node

def astar(start_state, goal_state, heuristic, successors):
    open_list = []  # Priority queue of nodes to be evaluated
    closed_set = set()  # Set of evaluated nodes
    
    start_node = Node(start_state, None, 0, heuristic(start_state, goal_state))
    heapq.heappush(open_list, (start_node.f(), id(start_node), start_node))
    
    while open_list:
        _, _, current_node = heapq.heappop(open_list)  # Pop node with lowest f value
        
        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path
            
        closed_set.add(current_node.state)
        
        for successor_state, cost in successors(current_node.state):
            if successor_state in closed_set:
                continue
            
            g = current_node.g + cost
            h = heuristic(successor_state, goal_state)
            successor_node = Node(successor_state, current_node, g, h)
            
            heapq.heappush(open_list, (successor_node.f(), id(successor_node), successor_node))
    
    return None  # No path found

#  heuristic function ( distance)
def distance(current_state):
    """
    מחשבת את המרחק של כל יחידת נוזל מראש הערימה 
    וסכום המרחק המצטבר של יחידות נוזל מאותו צבע.

    Args:
        current_state: מצב המשחק הנוכחי (רשימה של רשימות, כאשר כל רשימה פנימית מייצגת מכל).

    Returns:
        שתי מילונים:
            * color_distances: מילון הממפה כל צבע למרחק המצטבר של יחידות הנוזל שלו.
            * color_unit_distances: מילון הממפה כל צבע לסכום המרחקים של יחידות הנוזל שלו.
    """

    color_distances = {}
    color_unit_distances = {}
    unit_positions = {}
    unique_ids = 0

    # עוברים על כל המכלים
    for tank_index, tank in enumerate(current_state):
        # מזהים את צבע הנוזל העליון
        top_color = tank[0]

        # עוברים על כל יחידת נוזל במכל
        for color, quantity in enumerate(tank[1:]):
            # מקצים מזהה ייחודי
            unit_id = unique_ids
            unique_ids += 1

            # בודקים אם צבע הנוזל קיים במילונים
            if color in color_distances:
                color_distances[color] += unit_id
            else:
                color_distances[color] = unit_id

            if color in color_unit_distances:
                color_unit_distances[color].append(unit_id)
            else:
                color_unit_distances[color] = [unit_id]

            # מעדכנים את מיקום יחידת הנוזל
            unit_positions[unit_id] = tank_index

    # מחשבים סכום מרחקים לכל צבע
    for color, positions in color_unit_distances.items():
        total_distance = 0
        for position in positions:
            total_distance += unit_positions[position]
        color_unit_distances[color] = total_distance

    return color_distances #, color_unit_distances
 

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
          successors.append((from_tank, to_tank, color), 1)

  return successors


def can_move_liquid(current_state, from_tank, to_tank):
  """
  בודקת אם ניתן להעביר נוזל מהמכל "from_tank" למכל "to_tank".

  Args:
    current_state: מצב המשחק הנוכחי.
    from_tank: מספר המכל שממנו רוצים להעביר נוזל.
    to_tank: מספר המכל שאליו רוצים להעביר נוזל.

  Returns:
    True אם ניתן להעביר נוזל, False אחרת.
  """

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

def is_full(current_state, tank):
  """
  בודקת אם המכל "tank" מלא.

  Args:
    current_state: מצב המשחק הנוכחי (רשימה של רשימות).
    tank: מספר המכל שרוצים לבדוק.

  Returns:
    True אם המכל מלא, False אחרת.
  """

  max_size = size
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
    בודקת אם קיימת מחסנית במצב הנוכחי שהצבע העליון שלה זהה לצבע השני במחסנית "from_tank".

    Args:
        current_state: מצב המשחק הנוכחי.
        from_tank: מספר המחסנית שממנה רוצים להעביר נוזל (לא רלוונטי).
        to_tank: מספר המחסנית שאליה רוצים להעביר נוזל (לא רלוונטי).

    Returns:
        True אם קיימת מחסנית כזו, False אחרת.
    """

    for tank_index in range(len(current_state)):
        # דילוג על המחסנית "from_tank"
        if tank_index == from_tank:
            continue

        # בדיקת צבע הנוזל העליון במחסנית הנוכחית
        top_color = current_state[tank_index][0]

        # בדיקת צבע הנוזל השני במחסנית "from_tank"
        second_color = current_state[from_tank][1]

        # אם צבע הנוזל העליון זהה לצבע השני, קיימת מחסנית מתאימה
        if top_color == second_color:
            return True

    # לא נמצאה מחסנית מתאימה
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

path = astar(start_state, goal_state, distance, successors)

if path:
    print("Path:", path)
else:
    print("No path found.")













































