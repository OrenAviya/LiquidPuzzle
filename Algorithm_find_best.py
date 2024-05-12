


def choose_best_move(current_state):
  """
  בוחר את הצעד הטוב ביותר במצב הנוכחי.

  Args:
    current_state: מצב המשחק הנוכחי.

  Returns:
    הצעד הטוב ביותר (המכל מה, למכל לאן, איזה צבע).
  """

  # מציאת צעדים אפשריים
  possible_moves = get_possible_moves(current_state)

  # חישוב ערך יוריסטיקה עבור כל צעד אפשרי
  for move in possible_moves:
    # חישוב "עליונים אחרים"
    other_tops = count_other_tops(current_state, move[1], move[2])

    # חישוב מרחק מנהטן
    manhattan_distance = calculate_manhattan_distance(current_state, move[1], move[2])

    # שילוב הערכים
    heuristic_value = other_tops + manhattan_distance

    # שמירת הערך והצעד
    move.heuristic_value = heuristic_value

  # בחירת הצעד עם הערך הנמוך ביותר
  best_move = min(possible_moves, key=lambda move: move.heuristic_value)

  # מתן עדיפות לצבעים שאינם ריקים
  if not is_empty(current_state, best_move[1]):
    return best_move

  # מתן עדיפות לצבעים עם "עליונים אחרים" רבים
  for move in possible_moves:
    if move.heuristic_value == best_move.heuristic_value:
      if count_other_tops(current_state, move[1], move[2]) > count_other_tops(current_state, best_move[1], best_move[2]):
        best_move = move

  return best_move

# פונקציות עזר 
  def get_possible_moves(current_state):
  """
  מחזירה רשימה של צעדים אפשריים במצב הנוכחי.

  Args:
    current_state: מצב המשחק הנוכחי.

  Returns:
    רשימה של צעדים אפשריים (המכל מה, למכל לאן, איזה צבע).
  """

  possible_moves = []

  # לולאה על כל המכלים
  for from_tank in range(len(current_state)):
    # לולאה על כל המכלים (למעט המכל הנוכחי)
    for to_tank in range(len(current_state)):
      if from_tank != to_tank:
        # בדיקת אם ניתן להעביר נוזל מהמכל הנוכחי למכל היעד
        if can_move_liquid(current_state, from_tank, to_tank):
          # מציאת צבע הנוזל העליון במכל הנוכחי
          color = current_state[from_tank][0]

          # הוספת הצעד לרשימה
          possible_moves.append((from_tank, to_tank, color))

  return possible_moves

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
    if len(current_state[to_tank]) < MaxColorsInTank:
      return True

  return False

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

def is_full(current_state, tank):
  """
  בודקת אם המכל "tank" מלא.

  Args:
    current_state: מצב המשחק הנוכחי (רשימה של רשימות).
    tank: מספר המכל שרוצים לבדוק.

  Returns:
    True אם המכל מלא, False אחרת.
  """

  max_colors = get_number_of_unique_colors(current_state)
  return len(current_state[tank]) >= max_colors


def count_other_tops(current_state, from_tank, color):
  # מחשיבה את מספר המכלים הריקים ששלבם העליון בצבע "color" במכלים אחרים
  pass

def calculate_manhattan_distance(current_state, from_tank, to_tank):
  # מחשיבה את מרחק מנהטן בין המכלים "from_tank" ו-"to_tank"
  pass

def is_empty(current_state, tank):
  # בודקת אם המכל "tank" ריק
  pass
