import pygame
from random import randrange, randint
from main import HEIGHT, WIDTH


class Candy:
    def __init__(self, size, image):
        self.candy = pygame.Rect(randrange(WIDTH),
                                 randrange(HEIGHT),
                                 size, size)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (size, size))
        self.size = size
        self.pickup = pygame.mixer.Sound('Resources/pickup.wav')
        self.mute = False
        self.type = 0 #normal candy (default)
    def move(self):
        if self.mute == False:
            self.pickup.play()
        self.set_type()
        self.candy.top = randrange(self.size, HEIGHT) - self.size
        self.candy.left = randrange(self.size, WIDTH) - self.size
        
    def timeout(self):
        self.set_type()
        self.candy.top = randrange(self.size, HEIGHT) - self.size
        self.candy.left = randrange(self.size, WIDTH) - self.size


    def set_type(self):
        r = randint(0,9)
        if r == 0:
            self.type = 1
            self.image = pygame.image.load("Resources/candy3.png")
            self.pickup = pygame.mixer.Sound('Resources/smb3_power-up.wav')
        elif r == 9:
            self.type = 2
            self.image = pygame.image.load("Resources/candy2.png")
            self.pickup = pygame.mixer.Sound('Resources/1-up.wav')
        else:
            self.type = 0
            self.image = pygame.image.load("Resources/candy.png")
            self.pickup = pygame.mixer.Sound('Resources/pickup.wav')
        self.image = pygame.transform.scale(self.image, (50, 50))
