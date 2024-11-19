import random
import math
from configs import *

class Gun:
    def __init__(self):
        self.skin = Image.skin["gun"][0]
        self.points = 0
        self.total_shots = 20
    
    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()        
        
        if mouse_pos[1] >= 500:
            return
        
        gun_point = (Window.WIDTH/2, Window.HEIGHT - 178)
        lasers = ['red']
        click = pygame.mouse.get_pressed()

        #Calcular angulo e declive
        if mouse_pos[0] != gun_point[0]:
            slope = (mouse_pos[1] - gun_point[1]) / (mouse_pos[0] - gun_point[0]) 
        else:
            slope = -100000
        angle = math.atan(slope)
        rotation = math.degrees(angle)

        #Roda a arma se o rato estiver no lado esquero do ecrã
        if mouse_pos[0] < Window.WIDTH / 2:
            gun_flipped = pygame.transform.flip(self.skin, True, False)
            rotated_gun = pygame.transform.rotate(gun_flipped, 90 - rotation)
            screen.blit(rotated_gun, (Window.WIDTH / 2 - 90, Window.HEIGHT - 250))
        else:
            rotated_gun = pygame.transform.rotate(self.skin, 270 - rotation)
            screen.blit(rotated_gun, (Window.WIDTH / 2 - 30, Window.HEIGHT - 250))

        # Desenha o laser quando o jogador clica
        if click[0]:
            laser_color = 'red'
            pygame.draw.circle(screen, pygame.Color(laser_color), mouse_pos, 5)

    def is_shot(self):
        if self.total_shots > 0:
            self.total_shots -= 1

    def add_points(self, value):
        self.points += value

    def reset(self):
        self.points = 0
        self.total_shots = 20
