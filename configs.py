import pygame.image
pygame.init()

class Window:
    TITLE = "Duck Hunt"
    WIDTH = 800
    HEIGHT = 678
    FPS = 30

class Image:
    icon = pygame.image.load("assets/screen/icon.png")

    background = {
        "background": pygame.image.load("assets/screen/background.jpg"),
        "banner": pygame.image.load("assets/screen/banner.png"),
    }

    skin = {
        "target": [
            pygame.image.load("assets/targets/duck-1-1.png"),
            pygame.image.load("assets/targets/duck-1-2.png"),
            pygame.image.load("assets/targets/duck-2-1.png"),
            pygame.image.load("assets/targets/duck-2-2.png"),
            pygame.image.load("assets/targets/duck-3-1.png"),
            pygame.image.load("assets/targets/duck-3-2.png"),
        ],
        "gun": [
            pygame.image.load("assets/guns/gun.png")
        ]
    }
    gameover = pygame.image.load("assets/screen/gameover.png")
    winner = pygame.image.load("assets/screen/winner.png")

class Sound:
    #background = pygame.mixer.Sound("assets/sounds/bg_music.mp3")
    duck_shot = pygame.mixer.Sound("assets/sounds/duck.mp3")
    gameover_sound = pygame.mixer.Sound("assets/sounds/gameover.ogg")
    winner_sound = pygame.mixer.Sound("assets/sounds/winner.ogg")