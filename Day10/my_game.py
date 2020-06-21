import pygame

pygame.init()  # 初始化pygame

MAX_X = 600
MAX_Y = 600
screen = pygame.display.set_mode((MAX_X, MAX_Y))

# 事件循环

run = True
stop = False

x = 50
y = 50

first_run = True

speedx = 15
speedy = 10

while run:

    pygame.time.delay(100)  # 暂停0.1秒
    for event in pygame.event.get():  # TODO 代办的list  人机交互
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                stop = not stop

    if not stop:
        x = x + speedx
        y = y + speedy
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 50)
        if y>=MAX_Y - 50:
            speedy = -speedy
        if x >= MAX_X - 50:
            speedx = -speedx
        if y <= 50:
            speedy = -speedy
        if x <=50:
            speedx = -speedx
    pygame.display.update()

pygame.quit()
