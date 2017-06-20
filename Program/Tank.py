import pygame


class Tank:

    def __init__(self, x, y, bearing, image):
        self.posX = x
        self.posY = y
        self.bearing = bearing
        self.surf = image

    def rotate(self, bearing):
        # new_bear = (bearing - self.bearing) % 360
        surf = pygame.transform.rotate(self.surf, bearing)
        rect = surf.get_rect(center=(self.posX/2, self.posY/2))
        self.bearing = bearing
        return surf, rect
