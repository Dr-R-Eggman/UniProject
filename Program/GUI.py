import pygame
import Tank as Tanky

pygame.init()  # launch initial program

WIDTH = 400  # resolution
HEIGHT = 300  # resolution
DISPLAY = pygame.display
screen = DISPLAY.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()  # for fps purpose

colour = (0, 128, 255)

image1 = pygame.image.load('images/tank_body.png')
image2 = pygame.image.load('images/tank_head.png')
images = (image1, image2)
player_tank = Tanky.Tank(100, 140, 0, images)

done = False
while not done:

    # any events that is being activated such as KeyEvent, ActionEvent, MouseEvent, etcs..
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # when 'close' button is pressed
            print('exiting...')
            done = True

    screen.fill((0, 0, 0))

    surf, rect = player_tank.rotate(player_tank.bearing)
    pressed_key = pygame.key.get_pressed()  # get a key that is being pressed
    if pressed_key[pygame.K_w] or pressed_key[pygame.K_UP]:
        surf, rect = player_tank.forward()
    if pressed_key[pygame.K_s] or pressed_key[pygame.K_DOWN]:
        player_tank.posY += 1  # go down
    if pressed_key[pygame.K_a] or pressed_key[pygame.K_LEFT]:
        surf, rect = player_tank.rotate(player_tank.bearing + 1)  # rotate left
    if pressed_key[pygame.K_d] or pressed_key[pygame.K_RIGHT]:
        surf, rect = player_tank.rotate(player_tank.bearing - 1)  # rotate right

    # draw an image onto background, top-left corner of
    # the rect is a coord to place image onto background
    screen.blit(surf, rect)

    surf, rect = player_tank.head()
    screen.blit(surf, rect)

    DISPLAY.flip()  # update whole screen
    clock.tick(60)  # throttled to 60 FPS

print('exited')
