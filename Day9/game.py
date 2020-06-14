import pygame

pygame.init()   #初始化pygame

screen = pygame.display.set_mode((600, 600))

# 事件循环

run = True

x = 100
y = 100

while run:

    pygame.time.delay(100)   # 暂停0.1秒
    for event in pygame.event.get():   # TODO 代办的list  人机交互
        if event.type == pygame.QUIT:
            run = False
    x = x + 5
    y = y + 5
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(255,0,0),(x, y),50)
    print(x, y)
    # x, y = pygame.mouse.get_pos()   # 获取当前鼠标的位置坐标
    # print(x, y)
    pygame.display.update()


pygame.quit()
