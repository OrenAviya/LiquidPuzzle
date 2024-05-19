
class GameVariables:
  empty_tanks = 2
  full_tanks = 8
  size = 8
  num_colors = 8

  initial_state = [[1,3,5,4,4,7,6,1],[2,2,0,0,4,3,6,7],
          [2,1,1,4,5,6,0,2],[0,6,6,5,4,7,7,3],
        [3,4,1,0,5,7,4,4],[7,6,2,2,3,1,0,0],
        [7,3,3,1,2,5,5,6],[7,6,5,5,3,2,1,0],[],[]]

  def __init__(self, initial_state, num_colors, empty_tanks, full_tanks, size):
      self.initial_state = initial_state
      self.num_colors = num_colors
      self.empty_tanks = empty_tanks
      self.full_tanks = full_tanks
      self.size = size


"""
game_variables = GAME.game_variables  # גישה לאובייקט המחלקה

    initial_state = game_variables.initial_state
    num_colors = game_variables.num_colors
    empty_tanks = game_variables.empty_tanks
    full_tanks = game_variables.full_tanks
    size = game_variables.size

game_variables = GameVariables(initial_state, num_colors, empty_tanks, full_tanks, size)

global initial_state, num_colors, empty_tanks, full_tanks,  size 

def initialize_game(init, colors, empty, full,  size ):


    # הגדרת מצב התחלתי
  empty_tanks = empty
  full_tanks = full
  tank_size = size
  num_colors = colors

  initial_state = init

  
# הפעלת פונקציית האתחול
initialize_game()
"""
"""
empty_tanks = 2
full_tanks = 8
size = 8
num_colors = 8

initial_state = [[1,3,5,4,4,7,6,1],[2,2,0,0,4,3,6,7],
        [2,1,1,4,5,6,0,2],[0,6,6,5,4,7,7,3],
        [3,4,1,0,5,7,4,4],[7,6,2,2,3,1,0,0],
        [7,3,3,1,2,5,5,6],[7,6,5,5,3,2,1,0],[],[]]

self.initial_state =[[0,1,2,3],[2,4,1,2],[4,0,1,4],[2,3,1,3],[4,0,0,3],[],[]]
goal_state = [[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4],[],[]]

"""
