import tkinter as tk


#Classes concerning the snake body and movement



class Body:

  def __init__(self, canvas):
    self._canvas = canvas
    self._body = []
    self._current_direction = "right"

   
    self._create_initial(20, 20)

  def add(self, n):
    # add or remove body parts from the snake
    if n < 0 and len(self._body) > 1:
      if len(self._body) <= abs(n):
        n = len(self._body) - 1

      for _ in range(abs(n)):
        i = self._body.pop()
        self._canvas.delete(i._id)

      return

    for _ in range(n):
      x = self._body[-1]._x
      y = self._body[-1]._y

      if self._body[-1]._direction == self._get_dir("left"):
        x += 10
      elif self._body[-1]._direction == self._get_dir("right"):
        x -= 10
      elif self._body[-1]._direction == self._get_dir("up"):
        y += 10
      elif self._body[-1]._direction == self._get_dir("down"):
        y -= 10

      self._body.append(
          MovableObject(
              self._create_circle(x, y, 5, fill="#BBB", outline=""), x, y,
              self._body[-1]._direction))

 


 def change_direction(self, direction):
    if direction == self._current_direction:
      return
    if direction == "left" and self._current_direction == "right":
      return
    elif direction == "right" and self._current_direction == "left":
      return
    elif direction == "up" and self._current_direction == "down":
      return
    elif direction == "down" and self._current_direction == "up":
      return

    self._current_direction = direction
    self._body[0]._direction = self._get_dir(direction)
