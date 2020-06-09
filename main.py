
import sys  # 系统标准
import pygame  # 游戏依赖
# 引入所需要的依赖库


# 初始化游戏库
pygame.init()
# 定义窗口默认尺寸
size = width, height = 820, 640  # 620 W x 440 H
# 设置好相关参数
speed = [2, 2]  # X,Y
black = 0, 0, 0  # RGB
white = 255, 255, 255

# 声明一个窗口对象
screen = pygame.display.set_mode(size)
# 加载一个球的图片作为一个操控对象
ball = pygame.image.load("assets/ball.gif")
ball = pygame.transform.scale(ball, (50, 50))
ballreact = ball.get_rect()

# 循环帧
while 1:  # 1 = true
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # 移动小球
    ballreact = ballreact.move(speed)
    # 碰撞判断
    if ballreact.left < 0 or ballreact.right > width:
        speed[0] = -speed[0]
    if ballreact.top < 0 or ballreact.bottom > height:
        speed[1] = -speed[1]
    # 复原画布
    screen.fill(black)
    screen.blit(ball, ballreact)
    pygame.display.flip()
