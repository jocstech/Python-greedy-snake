
import sys  # 系统标准
import random  # 随机函数
import pygame  # 游戏依赖
# 引入所需要的依赖库


# 初始化游戏库
pygame.init()
# 定义窗口默认尺寸
size = width, height = 820, 640  # 620 W x 440 H
# 设置好相关参数
speed = [1, 0]  # X,Y
black = 0, 0, 0  # RGB
white = 255, 255, 255

# 声明一个窗口对象
screen = pygame.display.set_mode(size)
# 加载一个球的图片作为一个操控对象
# ball = pygame.image.load("assets/ball.gif")
# ball = pygame.transform.scale(ball, (50, 50))
# ballreact = ball.get_rect()


snack_head_speed = [1, 0]
snack_head_position = (random.randrange(0, width), random.randrange(0, height))
snack_head_size = (20, 20)
snack_head_color = white
snack_head = pygame.Rect(snack_head_position, snack_head_size)
snack_body = []


# 循环帧
while 1:  # 1 = true
    key = pygame.key.get_pressed()  # checking pressed keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # 移动蛇头
    snack_head = snack_head.move(snack_head_speed)
    # 碰撞判断
    if snack_head.left < 0 or snack_head.right > width:
        snack_head_speed[0] = -snack_head_speed[0]
    if snack_head.top < 0 or snack_head.bottom > height:
        snack_head_speed[1] = -snack_head_speed[1]
    # 按键控制逻辑
    if(key[pygame.K_UP]):
        snack_head_speed[0] = 0
        snack_head_speed[1] = -1
    if(key[pygame.K_DOWN]):
        snack_head_speed[0] = 0
        snack_head_speed[1] = 1
    if(key[pygame.K_LEFT]):
        snack_head_speed[1] = 0
        snack_head_speed[0] = -1
    if(key[pygame.K_RIGHT]):
        snack_head_speed[1] = 0
        snack_head_speed[0] = 1
    # 复原画布
    screen.fill(black)
    pygame.draw.rect(screen, snack_head_color, snack_head)
    # 更新画面
    pygame.display.flip()
