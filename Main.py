import tkinter as tk
from Snake import Body


class Game:

  #Class 
  
  def __init__(self, canvas, limits):
    self._canvas = canvas
    self._limits = limits

    # snake
    self._snake = Body(self._canvas)

    # walls
    self._walls = []
    self._create_walls()

    self._apples = []
    self._count = 1

    self.points = 0

  def _check_hit(self):
    # Check if hit or not
    head = self._snake._body[0]
    self._apple_rule(head)
    self._wall_rule(head)
    self._eat_itself_rule(head)

  def loop(self):
  
    self._snake.iterate()
   
    self._count -= 1
    if self._count == 0:
      self.generate_apple()

    self._check_hit()

  def _from_rgb(self, rgb):
    
    return "#%02x%02x%02x" % rgb  #rgb code represented as a tuple of integers.


  def generate_apple(self):
    
    self._count = random.randint(50, 70)
    x = ((random.randint(self._limits[0], self._limits[2]) * 10) %
         self._limits[2])

    if x <= self._limits[0]:
      x += 20
    elif x >= self._limits[2]:
      x -= 20

    y = ((random.randint(self._limits[1], self._limits[3]) * 10) %
         self._limits[3])

    if y <= self._limits[1]:
      y += 20
    elif x >= self._limits[3]:
      y -= 20

    self._apples.append(
        Apple(
            self._canvas.create_oval(x - 5, y - 5, x + 5, y + 5, outline=""), x,
            y))

    self._canvas.itemconfig(
        self._apples[-1]._id, fill=self._from_rgb(self._apples[-1]._color))

  def change_snake_direction(self, direction):
    self._snake.change_direction(direction)
    
class Window(tk.Tk):
  

  def __init__(self, screenName=None, width=100, height=100):
    #  main window
    super().__init__(screenName=screenName)

    # canvas
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

def _loop(self):
    self.after(100, func=self._loop)
    self._game.loop()



if __name__ == "__main__":
  # Start
  Window("Snakes", 450, 450)
