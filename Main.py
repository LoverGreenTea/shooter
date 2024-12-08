import pygame
import time
import mixer
import random

pygame.mixer.init()
pygame.init()
window = pygame.display.set_mode((700, 500))
fps = pygame.time.Clock()

background = pygame.transform.scale(pygame.image.load("galaxy.jpg"), [700, 500])
pygame.mixer.music.load('space.ogg')
pygame.mixer.music.play(-1)

kick_sound = pygame.mixer.Sound('fire.ogg')

class Player:
    def __init__(self, speed, x, y, width, height, img):
        self.texture = pygame.image.load(img)
        self.texture = pygame.transform.scale(self.texture, [width, height])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.width = width
        self.height = height

    def draw(self, window):
        window.blit(self.texture, self.hitbox)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.hitbox.x += self.speed

        if keys[pygame.K_LEFT]:
            self.hitbox.x -= self.speed

class UFO:
    def __init__(self, speed, x, y, width, height, img):
        self.texture = pygame.image.load(img)
        self.texture = pygame.transform.scale(self.texture, [width, height])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed

    def draw(self, window):
        window.blit(self.texture, self.hitbox)

background = pygame.image.load('galaxy.jpg')
background = pygame.transform.scale(background, [700, 500])
game = True

listenemy = [
    UFO(3, 300, 20, 90, 50, "ufo.png"),
    UFO(3, 600, 70, 90, 50, "ufo.png"),
    UFO(3, 100, 40, 90, 50, "ufo.png")
]


player = Player(3, 300, 350, 100, 150, "rocket.png")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    player.draw(window)
    player.move()
    pygame.display.flip()
    window.blit(background, [0, 0])
    fps.tick(60)

    for ufo in listenemy:
        ufo.draw(window)