import sys
import time
import pygame
import random
from pygame.locals import *


# 全局参数初始化
pygame.init()
size = width,height = 840, 640
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

black = pygame.Color(0, 0, 0)  # RGB
white = 255, 255, 255
grey = pygame.Color(50, 50, 50)
green = 0, 255, 0


snake_head_position = [random.randrange(20, width), random.randrange(20, height)]
snake_head_size = 20, 20
snake_head_color = white
snake_head = pygame.Rect(snake_head_position, snake_head_size)

snake_body = [],
snake_body_position = [[80, 20], [60, 20], [40,20]]
snake_body_color = white

food_position = [random.randrange(20, width), random.randrange(20, height)]
food_color = green
food_flag = 1

def drawSnake():
  pygame.draw.rect(screen, snake_head_color, snake_head)


def drawFood():
  pygame.draw.rect(screen,food_color, food_position )

'''def drawSnake(snake_body):
    for i in snake_body:
        pygame.draw.rect(screen, white, Rect(i[0], i[1], 20, 20))

def drawFood(food_position):
    pygame.draw.rect(screen, green, Rect(food_position[0], food_position, 20, 20))
'''


#边界碰撞返回
def borderBounce():
    if snake_head.left < 0 or snake_head.right > 840:
        direction = -direction
    if snake_head.top < 0 or snake_head.bottom > 640:
        direction = -direction


# 初始方向
direction = 'right'

# 游戏循环，移动
while 1:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == KEYDOWN:
      if event.key == K_UP and direction != K_DOWN:
        direction = 'up'
      if event.key == K_DOWN and direction != K_UP:
        direction = 'down'
      if event.key == K_LEFT and direction != K_RIGHT:
        direction = 'left'
      if event.key == K_RIGHT and direction != K_LEFT:
        direction = 'right'


    #判断是否吃掉食物
    if snake_head_position[0] == food_position[0] and snake_head_position[1] == food_position[1]:
      food_flag = 0
    else:
      snake_body_position.pop()
    #？为什么snake_head后面可以[]赋值？

    #生成新的食物
    if food_flag == 0:
        x = random.randrange(1,32)
        y = random.randrange(1,24)
        food_position = [int(x*20),int(y*20)]
        food_flag = 1

    screen.fill(black)

    drawSnake()

    # drawFood()

    borderBounce()

    pygame.display.flip()

    clock.tick(7)


