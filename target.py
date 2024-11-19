import random
from configs import *
from direction import *

class Target:
    def __init__(self, x, y, direction):
        self.__x = x
        self.__y = y
        self.__direction = direction
        self.__speed = 2
        self.__skin = random.choice(Image.skin["target"])
        self.__mask = pygame.mask.from_surface(self.__skin)
        self.__is_going_forward = True

    def move(self, location, dt):        
        self.__x += self.__speed
        if self.__x > Window.WIDTH:
            self.__x = -self.__skin.get_width()

    def draw(self, scrn):
        scrn.blit(self.__skin, [self.__x, self.__y])

    def get_overlapping_area(self, mouse_pos):
        self_mask = pygame.mask.from_surface(self.__skin)
        offset = (int(self.__x - mouse_pos[0]), int(self.__y - mouse_pos[1]))
        return self_mask.overlap_area(pygame.mask.Mask((1, 1), fill=True), offset)

    def was_hit(self, mouse_pos):
        offset_x = int(mouse_pos[0] - self.__x)
        offset_y = int(mouse_pos[1] - self.__y)

        if 0 <= offset_x < self.__skin.get_width() and 0 <= offset_y < self.__skin.get_height():
            return self.__mask.get_at((offset_x, offset_y))
        return False

