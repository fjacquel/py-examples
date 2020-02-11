# -*- coding: utf-8 -*-
"""
Snake example game

https://www.pygame.org/docs/ref/key.html

@author: Florian Jacquelet
"""

from random import randint

import pygame
import pygame.locals as pycst

class Snake():
  """ Snake datastructure """

  def __init__(self, win_size=50):
    """ Constructor """

    self._board    = win_size
    self._dead     = False
    self._body     = [ (0, 2), (0, 1), (0, 0) ]
    self._fruit    = (0, 0)
    self._move     = 0
    self._max_move = win_size * 2

  def place_fruit(self):
    """ Place a fruit on the board """

    while self._fruit in self._body or self._move > self._max_move:
      x = randint(0, self._board - 1)
      y = randint(0, self._board - 1)
      self._fruit = (x, y)
      self._move = 0

  def move(self, direction):
    """ Move the snake """

    self._move = self._move + 1

    # Create a new head
    head = self._body[0]
    if direction == 'LEFT':
      x = head[0] - 1
      y = head[1]
    elif direction == 'RIGHT':
      x = head[0] + 1
      y = head[1]
    elif direction == 'UP':
      x = head[0]
      y = head[1] + 1
    elif direction == 'DOWN':
      x = head[0]
      y = head[1] - 1
    head = (x%self._board, y%self._board)

    # Is snake eating itself?
    self._dead = head in self._body

    # Add head
    self._body.insert(0, head)

    # Check if apple is eaten (Keep tail & move fruit if it is)
    if head == self._fruit:
      self.place_fruit()
    else:
      del self._body[-1]
      if self._move > self._max_move: self.place_fruit()

    return not self._dead

  def get_body(self):
    """ Method returning the snake body """
    return self._body

  def get_fruit(self):
    """ Method returning the fruit position """
    return self._fruit

def start_game(board_size=50, direction='UP'):
  """ Method starting the game"""
  snake = Snake(board_size)

  # RGB colors (Red, Green, Blue)
  COLOR_APPLE = (0,   255,   0) # Green
  COLOR_SNAKE = (0,     0, 255) # Blue
  COLOR_BOARD = (255, 255, 255) # White

  # Create board (board size is position of 10x10 pixels)
  pygame.init()
  board = pygame.display.set_mode((board_size * 10, board_size * 10))

  # Apple - image 10x10 pixels green
  apple = pygame.Surface((10, 10))
  apple.fill(COLOR_BOARD)
  for i in range(0, 5): apple.fill(COLOR_APPLE, (i, 4-i, 10-i*2, 2+i*2))

  # Snake piece - image 10x10 pixels blue
  snake_piece = pygame.Surface((10, 10))
  for i in range(0, 10): snake_piece.fill(COLOR_SNAKE if i%2 == 0 else COLOR_BOARD, (i,0,1,10))

  pygame.time.Clock()
  pygame.time.set_timer(1, 100)
  lost  = False
  pause = False

  while not lost:
    e = pygame.event.wait()

    # Quit game
    if e.type == pycst.QUIT:
      lost = True

    # Directions
    elif e.type == pycst.KEYDOWN: # Keyboard pressed
      if not e or not e.key:
        pass
      elif e.key == pycst.K_UP:
        direction = 'UP'
      elif e.key == pycst.K_DOWN:
        direction = 'DOWN'
      elif e.key == pycst.K_LEFT:
        direction = 'LEFT'
      elif e.key == pycst.K_RIGHT:
        direction = 'RIGHT'
      elif e.key == pycst.K_SPACE:
        pause = not pause

    # Tick
    elif not pause and e.type == pycst.ACTIVEEVENT:
      lost = not snake.move(direction)

    # Paint the board in white (Clearing snake & apple)
    board.fill(COLOR_BOARD)

    # Repaint snake
    for bit in snake.get_body():
      board.blit(snake_piece, (bit[0] * 10, (board_size - bit[1] - 1) * 10))

    # Repaint apple
    fruit = snake.get_fruit()
    board.blit(apple, (fruit[0] * 10, (board_size - fruit[1]-1) * 10))

    pygame.display.flip()

  pygame.quit()

if __name__ == '__main__':
  start_game(20)
