
import sys  # 系统标准
import random  # 随机函数
import pygame  # 游戏依赖
import pygame.freetype
import datetime
# 引入所需要的依赖库


# 初始化游戏库
pygame.init()
# 定义窗口默认尺寸
size = width, height = 841, 641  # 620 W x 440 H
# 设置好相关参数
speed = [1, 0]  # X,Y
black = 0, 0, 0  # RGB
white = 255, 255, 255
grey = 50, 50, 50
green = 0, 255, 0
red = 255, 0, 0

# 声明一个窗口对象
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()  # 控制游戏速度
GAME_FONT = pygame.freetype.Font("assets/front.ttf", 18)
timer = 0
fps = 120
last_move = datetime.datetime.now().timestamp()
time_gap = 0.2

# 游戏记分系统
total_score = 0



# 方格
usize = 20


def randomPosOnScreen():
    return (random.randrange(2, (width-1) / usize - 2) * usize + 1,
            random.randrange(2, (height-1) / usize - 2) * usize + 1)


initialized = False
snack_head_velocity = 1 * usize
snack_head_speed_vector = [snack_head_velocity, 0]
snack_head_position = randomPosOnScreen()
snack_head_size = (usize, usize)
snack_head_color = white
snack_head = pygame.Rect(snack_head_position, snack_head_size)
snack_body = []
snack_body_length = 0

food_color = green
food_position = randomPosOnScreen()
food = pygame.Rect(food_position, snack_head_size)


def control(keyCode):
  # 上键
  if keyCode == 119 or keyCode == pygame.K_UP:
        snack_head_speed_vector[0] = 0
        snack_head_speed_vector[1] = -snack_head_velocity
   # 下键
  if keyCode == 115 or keyCode == pygame.K_DOWN:
        snack_head_speed_vector[0] = 0
        snack_head_speed_vector[1] = snack_head_velocity
  # 左键
  if keyCode == 97 or keyCode == pygame.K_LEFT:
        snack_head_speed_vector[1] = 0
        snack_head_speed_vector[0] = -snack_head_velocity
  # 右键
  if keyCode == 100 or keyCode == pygame.K_RIGHT:
        snack_head_speed_vector[1] = 0
        snack_head_speed_vector[0] = snack_head_velocity


def placeFood():
    global food_position
    food_position = randomPosOnScreen()
    while snack_head_position == food_position:
        food_position = randomPosOnScreen()
    food.x, food.y = food_position

# 边界碰撞判断
def borderBounce():
    if snack_head.left < 0:
      snack_head_speed_vector[0] = abs(snack_head_speed_vector[0])
    if snack_head.right > width:
      snack_head_speed_vector[0] = -abs(snack_head_speed_vector[0])
    if snack_head.top < 0:
      snack_head_speed_vector[1] = abs(snack_head_speed_vector[1])
    if snack_head.bottom > height:
      snack_head_speed_vector[1] = -abs(snack_head_speed_vector[1])


def growBody():
  global snack_body_length
  snack_body_length += 1

 # 碰撞判断
def detectCollision():
    global total_score
    if snack_head.x == food.x and snack_head.y == food.y:
        total_score += 1
        growBody()
        placeFood()


def drawBackground():
    screen.fill(black)
    for x in range(0, width, usize):
        pygame.draw.aaline(screen, grey, (x, 0), (x, height))
    for y in range(0, height, usize):
        pygame.draw.aaline(screen, grey, (0, y), (width, y))

def drawObjects():
    for body in snack_body:
      pygame.draw.rect(screen, snack_head_color, body)
    pygame.draw.rect(screen, snack_head_color, snack_head)
    pygame.draw.rect(screen, food_color, food)

def moving():
    # 移动蛇头
    global snack_head,snack_body, last_move
    if datetime.datetime.now().timestamp() - last_move > time_gap:
      snack_body.insert(0,snack_head)
      if len(snack_body) > snack_body_length:
        snack_body.pop(-1)
      snack_head = snack_head.move(snack_head_speed_vector)
      snack_head_position = (snack_head.x, snack_head.y)
      last_move = datetime.datetime.now().timestamp()

# 初始化函数
def initialization():
    global initialized, total_score
    if not initialized:
        total_score = 0
        placeFood()
        initialized = True

# 循环帧
while 1:  # 1 = true
    # 初始化函数
    initialization()
    # key = pygame.key.get_pressed()  # checking pressed keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # 按键控制逻辑
            control(event.key)


    # 绘制画布
    drawBackground()
    # 边界碰撞判断
    borderBounce()
    # 绘制物体
    drawObjects()
    # 移动动作
    moving()
    # 碰撞判断
    detectCollision()
    # 绘制文字
    GAME_FONT.render_to(screen, (20, 20), 'Total Score: ' + str(total_score), white)
    GAME_FONT.render_to(screen, (20, 50), 'FPS: ' + str(fps), white)
    # 更新画面
    pygame.display.flip()
    # 绘制每一帧所需时间
    timer += clock.tick(fps)
