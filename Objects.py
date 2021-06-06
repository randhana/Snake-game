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