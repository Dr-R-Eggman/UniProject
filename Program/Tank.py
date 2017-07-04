import pygame
import math


class Tank:

    def __init__(self, x, y, bearing, images):
        self.posX = x
        self.posY = y
        self.bearing = bearing
        self.surf_body = images[0]
        self.surf_head = images[1]

    # rotate tank
    def rotate(self, bearing):
        # new_bear = (bearing - self.bearing) % 360
        self.bearing = bearing
        surf = pygame.transform.rotate(self.surf_body, self.bearing)  # rotate original image
        rect = surf.get_rect(center=(self.posX, self.posY))  # centered and get image rect
        return surf, rect

    # move tank forward
    def forward(self):
        dx = math.sin(math.radians(self.bearing))
        dy = math.cos(math.radians(self.bearing))
        self.posX = self.posX - dx
        self.posY = self.posY - dy
        surf = pygame.transform.rotate(self.surf_body, self.bearing)  # rotate original image
        rect = surf.get_rect(center=(self.posX, self.posY))  # centered and get image rect
        return surf, rect

    def head(self):
        mx, my = pygame.mouse.get_pos()
        bearing = math.degrees(math.atan2(self.posX - mx, self.posY - my))
        surf = pygame.transform.rotate(self.surf_head, bearing)  # rotate original image
        rect = surf.get_rect(center=(self.posX, self.posY))  # centered and get image rect
        return surf, rect
