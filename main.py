
import sys  # 系统标准
import random  # 随机函数
import pygame # 游戏依赖
import time
# 引入所需要的依赖库


# 初始化游戏库
pygame.init(
# 定义窗口默认尺寸
size = width, height = 841, 641  # 620 W x 440 H
# 设置好相关参数
speed = [1, 0]  # X,Y
black = 0, 0, 0  # RGB
white = 255, 255, 255
grey = 50, 50, 50
green = 0, 255, 0

# 声明一个窗口对象
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock() #控制游戏速度
# 加载一个球的图片作为一个操控对象
# ball = pygame.image.load("assets/ball.gif")
# ball = pygame.transform.scale(ball, (50, 50))
# ballreact = ball.get_rect()


#方格
usize = 20

def randomPosOnScreen():
    return (random.randrange(2, (width-1) / usize - 2) * usize + 1,
            random.randrange(2, (height-1) / usize - 2) * usize + 1)


initialized = False
total_score = 0
snack_head_velocity = 1 * usize
snack_head_speed_vector = [snack_head_velocity, 0]
snack_head_position = randomPosOnScreen()
snack_head_size = (usize, usize)
snack_head_color = white
snack_head = pygame.Rect(snack_head_position, snack_head_size)
#snack_body = []

food_color = green
food_position = randomPosOnScreen()
food = pygame.Rect(food_position, snack_head_size)


def control(key):
    print(key)
    if(key[pygame.K_UP] or key[pygame.K_w]):
        snack_head_speed_vector[0] = 0
        snack_head_speed_vector[1] = -snack_head_velocity
    if(key[pygame.K_DOWN] or key[pygame.K_s]):
        snack_head_speed_vector[0] = 0
        snack_head_speed_vector[1] = snack_head_velocity
    if(key[pygame.K_LEFT] or key[pygame.K_a]):
        snack_head_speed_vector[1] = 0
        snack_head_speed_vector[0] = -snack_head_velocity
    if(key[pygame.K_RIGHT] or key[pygame.K_d]):
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
    if snack_head.left < 0 or snack_head.right > width:
        snack_head_speed_vector[0] = -snack_head_speed_vector[0]
    if snack_head.top < 0 or snack_head.bottom > height:
        snack_head_speed_vector[1] = -snack_head_speed_vector[1]

 # 碰撞判断


def detectCollision():
    global total_score
    if snack_head_position == food_position:
        total_score += total_score
        print('吃到了食物!')
        print('总分:', total_score)
        placeFood()


def drawBackground():
    screen.fill(black)
    for x in range(0, width, usize):
        pygame.draw.aaline(screen, grey, (x, 0), (x, height))
    for y in range(0, height, usize):
        pygame.draw.aaline(screen, grey, (0, y), (width, y))


# 初始化函数


def initialization():
    global initialized, total_score
    if not initialized:
        total_score = 0
        placeFood()
        initialized = True

timer = 0

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
            control(event.type)

    # 绘制画布
    drawBackground()
    pygame.draw.rect(screen, snack_head_color, snack_head)
    pygame.draw.rect(screen, food_color, food)

    # 边界碰撞判断
    borderBounce()

    # 移动蛇头
    snack_head = snack_head.move(snack_head_speed_vector)  
    snack_head_position = (snack_head.x, snack_head.y)
    # 碰撞判断
    detectCollision()

    # 更新画面
    pygame.display.flip()
    # 绘制每一帧所需时间
    timer += clock.tick(60)
