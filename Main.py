import tkinter as tk
from Snake import Body
class Game:

  #Class 
  

  def __init__(self, canvas, limits):
    self._canvas = canvas
    self._limits = limits

    # create snake
    self._snake = Body(self._canvas)

    # create walls
    self._walls = []
    self._create_walls()

    self._apples = []
    self._count = 1

    self.points = 0

def _key_press(self, event):
    if event.keycode == 37:
      # left arrow
      self._game.change_snake_direction("left")
    elif event.keycode == 38:
      # up arrow
      self._game.change_snake_direction("up")
    elif event.keycode == 39:
      # right arrow
      self._game.change_snake_direction("right")
    elif event.keycode == 40:
      # down arrow
      self._game.change_snake_direction("down")


class Window(tk.Tk):
  """
  Class that manages the window
  """

  def __init__(self, screenName=None, width=100, height=100):
    # create main window
    super().__init__(screenName=screenName)

    # create canvas, where everything is drawn
    self._canvas = tk.Canvas(
        self,
        width=width,
        height=height,
        borderwidth=0,
        highlightthickness=0,
        bg="white")
    # align canvas
    self._canvas.grid()

    self._game = Game(self._canvas, [10, 10, width - 10, height - 10])

    # bind events
    self.bind("<Key>", self._key_press)

    # run game loop every x ms
    self.after(100, self._loop)

    # start tkinter
    self.mainloop()
if __name__ == "__main__":
  # Start
  Window("Snakes", 500, 500)
