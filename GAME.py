def initialize_game():
  """
  מאתחל את המשחק ומגדיר משתנים גלובליים.
  """

  global initial_state, num_colors, empty_tanks, full_tanks,  MaxColorsInTank 

  # הגדרת מצב התחלתי
  initial_state = [
    [1, 2],
    [3, 4, 5],
    [6],
  ]

  # הגדרת מספר צבעים
  num_colors = get_number_of_unique_colors(initial_state)

  # ספירת מבחנות ריקות ומלאות
  empty_tanks = count_empty_tanks(initial_state)
  full_tanks = count_full_tanks(initial_state) 
  MaxColorsInTank = get_tank_size(initial_state)

# פונקציות עזר (לא מוצגות כאן)
def count_empty_tanks(state):
  # סופרת את מספר המבחנות הריקות במצב נתון
  pass

def count_full_tanks(state):
  # סופרת את מספר המבחנות המלאות במצב נתון
  pass
def get_tank_size(state):
    # סופרת כמה צבעים לכל היותר יש במבחנה
    pass

def get_number_of_unique_colors(initial_state):
  """
  מחשבת את מספר הצבעים השונים במצב התחלתי.

  Args:
    initial_state: מערך דו מימדי המייצג את מצב ההתחלה של המשחק.

  Returns:
    מספר הצבעים השונים.
  """

  unique_colors = set()

  for tank in initial_state:
    for color in tank:
      unique_colors.add(color)

  return len(unique_colors)   
# הפעלת פונקציית האתחול
initialize_game()

