import pygame
import time
import mixer
import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from File_Save import write_in_file


def game():
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
            self.bullets = []

        def draw(self, window):
            window.blit(self.texture, self.hitbox)
            for bullet in self.bullets:
                bullet.draw(window)
        def move(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self.hitbox.x += self.speed

            if keys[pygame.K_LEFT]:
                self.hitbox.x -= self.speed

            if keys[pygame.K_SPACE]:
                self.bullets.append(Bullet('bullet.png',
                                           40, 40,
                                           self.hitbox.x +30, self.hitbox.y,
                                           10))

            for bullet in self.bullets:
                bullet.move()
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

        def move(self):
                self.hitbox.y += self.speed
    class Bullet:
        def __init__(self, img, width, height, x, y, speed):
            pass
            self.texture = pygame.image.load(img)
            self.texture = pygame.transform.scale(self.texture, [width, height])
            self.hitbox = self.texture.get_rect()
            self.hitbox.x = x
            self.hitbox.y = y
            self.speed = speed
            self.width = width
            self.height = height
            self.bullets = []
        def move(self):
                self.hitbox.y -= self.speed
        def draw(self, window):
            window.blit(self.texture, self.hitbox)
            for bullet in self.bullets:
                bullet.draw(window)

    background = pygame.image.load('galaxy.jpg')
    background = pygame.transform.scale(background, [700, 500])
    game = True

    listenemy = []
    y = 200
    for i in range(4):
        listenemy.append(UFO(0.650, random.randint(0, 650), 5, 90, 50, "ufo.png"))
        y -= 100


    score = data["score"]
    write_in_file(data)
    weapon = Bullet('bullet.png', 50, 60, 1000,10, 10)
    player = Player(3, 300, 350, 100, 150, "rocket.png")


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        for e in listenemy:
            e.move()
            if e.hitbox.y > 500:
                e.hitbox.y = -100
                e.hitbox.x = random.randint(0, 650)

        for e in listenemy:
            for b in player.bullets:
                if e.hitbox.colliderect(b.hitbox):
                    b.hitbox.x = 5000
                    player.bullets.remove(b)
                    e.hitbox.y = -100
                    e.hitbox.x = random.randint(0, 650)
                    score += 1
                    break

        score_lbl = pygame.font.Font(None, 23).render("Score: " + str(score), True, [255, 255, 255])
        weapon.move()
        player.draw(window)
        player.move()
        weapon.draw(window)
        pygame.display.flip()
        window.blit(background, [0, 0])
        fps.tick(60)
        window.blit(score_lbl, [0,0])
        for ufo in listenemy:
            ufo.draw(window)

