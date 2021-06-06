import random

class StaticObject:
 #initialize
  def __init__(self, tag, x, y):
    self._id = tag
    self._x = x
    self._y = y


class MovableObject(StaticObject):

  def __init__(self, tag, x, y, direction):
    super().__init__(tag, x, y)
    self._direction = direction 
    

class Apple(StaticObject):

  def __init__(self, tag, x, y):
    super().__init__(tag, x, y)
    self._value = random.randint(0, 10)

    if self._value < 3:
      self._color = (255, 0, 0)
    elif self._value >= 3 and self._value < 6:
      self._color = (0, 255, 0)
    elif self._value >= 6 and self._value <= 9:
      self._color = (0, 0, 255)
    elif self._value == 10:
      self._color = (255, 235, 0)


