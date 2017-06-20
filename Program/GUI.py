import pygame
import Tank as tanky

pygame.init()  # launch initial program

WIDTH = 400  # resolution
HEIGHT = 300  # resolution
DISPLAY = pygame.display
screen = DISPLAY.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

colour = (0, 128, 255)

image = pygame.image.load('images/tank_body.png')
image.get_rect().center = (100/2, 140/2)
player_tank = tanky.Tank(100, 140, 0, image)

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
        player_tank.posY -= 1  # go up
    if pressed_key[pygame.K_s] or pressed_key[pygame.K_DOWN]:
        player_tank.posY += 1  # go down
    if pressed_key[pygame.K_a] or pressed_key[pygame.K_LEFT]:
        surf, rect = player_tank.rotate(player_tank.bearing - 1)
    if pressed_key[pygame.K_d] or pressed_key[pygame.K_RIGHT]:
        surf, rect = player_tank.rotate(player_tank.bearing + 1)

    screen.blit(surf, rect)

    DISPLAY.flip()  # update whole screen
    clock.tick(60)  # throttled to 60 FPS

print('exited')
