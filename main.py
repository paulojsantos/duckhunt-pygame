import pygame
import math
from pygame.locals import *
from configs import *
from direction import *
from world import *
from target import *
from gun import *

pygame.init()

screen = pygame.display.set_mode([Window.WIDTH, Window.HEIGHT])
pygame.display.set_icon(Image.icon)
pygame.display.set_caption(Window.TITLE)

clock = pygame.time.Clock()
font = pygame.font.Font('assets/font/myFont.ttf', 32)
#Sound.background.set_volume(0.5)
#Sound.background.play()
world = World()
banner = Banner()
gun = Gun()
targets = World.define_targets()
gameover = False
game_won = False

while True:
    dt = clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not gameover and not game_won:
            mouse_pos = pygame.mouse.get_pos()
            
            if mouse_pos[1] >= 500:
                continue

            gun.is_shot()  
                    
            for target in reversed(targets):
                if target.was_hit(mouse_pos):
                    print("Target hit!")
                    Sound.duck_shot.set_volume(0.1)
                    Sound.duck_shot.play()
                    gun.add_points(10)
                    targets.remove(target)
                    break
    
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and (gameover or game_won):
        world.reset_game()
        gun.reset()
        targets = World.define_targets()
        gameover = False
        game_won = False
        screen.fill((0, 0, 0))
        pygame.display.update()
        continue
    
    if not gameover and not game_won:
        world.draw(screen)
        gun.draw(screen)
        
        for target in targets:
            target.draw(screen)
            target.move(world, dt)        
        
        banner.draw_score(screen, font, gun.points)
        banner.draw_shots_left(screen, font, gun.total_shots)

    if gun.total_shots == 0 and not gameover and not game_won:
        gameover = True
        Sound.gameover_sound.set_volume(0.1)
        Sound.gameover_sound.play()

    if not gameover and not game_won and len(targets) == 0 and gun.total_shots < 20:
        game_won = True
        Sound.winner_sound.set_volume(0.1)
        Sound.winner_sound.play()
    
    if gameover:
        screen.blit(Image.gameover, (0, 0))

    if game_won:
        screen.blit(Image.winner, (0, 0))

    pygame.display.update()

