from configs import *
from target import Target
from direction import Direction

class World:
    def __init__(self):
        self.__background = Image.background["background"]
        self.__banner = Image.background["banner"]
        
    def draw(self, screen):
        screen.blit(self.__background, [0, 0])
        screen.blit(self.__banner, [0, 500]) 

    @classmethod
    def define_targets(cls):
        return [
            Target(50, 10, Direction.HORIZONTAL),
            Target(150, 76, Direction.HORIZONTAL),
            Target(50, 142, Direction.HORIZONTAL),
            Target(150, 208, Direction.HORIZONTAL),
            Target(50, 274, Direction.HORIZONTAL),
            Target(100, 340, Direction.HORIZONTAL),
            Target(-350, 10, Direction.HORIZONTAL),
            Target(-250, 76, Direction.HORIZONTAL),
            Target(-350, 142, Direction.HORIZONTAL),
            Target(-250, 208, Direction.HORIZONTAL),
            Target(-350, 274, Direction.HORIZONTAL),
            Target(-250, 340, Direction.HORIZONTAL),
        ]
    
    def reset_game(self):        
        global points, total_shots, gameover, game_won  
        points = 0
        total_shots = 20
        gameover = False
        game_won = False    


class Banner:
    def draw_score(self, screen, font, points):
        points_text = font.render(f'Points: {points}', True, 'black')
        screen.blit(points_text, (300, 565))

    def draw_shots_left(self, screen, font, total_shots):
        points_text = font.render(f'Shots left: {total_shots}', True, 'black')
        screen.blit(points_text, (300, 605))
