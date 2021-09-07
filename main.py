import pygame
import random
from pygame import mixer

screen_size = [360, 600]
surface = pygame.image.load('fish.jpg')
pygame. display. set_caption("BASKET-PIKA")
pygame.display.set_icon(surface)
screen = pygame.display.set_mode(screen_size)
mixer.init()
mixer.music.set_volume(0.1)
mixer.music.load('gamebackmusic.mp3')
mixer.music.play(-1)
pygame.font.init()
score = 0


def randomness():

  return -1.2 * random.randint(100, 1500)


fish_y = [randomness(), randomness(), randomness()]
clock = pygame.time.Clock()


def fish_posy(idx):

  if fish_y[idx] > 600:
    fish_y[idx] = randomness()
    global score
    score = score-50
    print('BALL MISSED:  ', score)
  else:
    fish_y[idx] = fish_y[idx] + 2


def crashed(idx):
  pos = idx + 1
  print(' BALL CAUGHT : ', pos)
  global score
  score = score + 50
  print('score', score)
  fish_y[idx] = randomness()


def scoreboard(scor):
  font = pygame.font.SysFont('Comic Sans MS', 20, bold=True)
  scorebod = 'SCORES: ' + str(scor)
  scorebodtext = font.render(scorebod, True, (0, 255, 0))
  screen.blit(scorebodtext, [10, 15])


def alive():
  done = False
  user_x = 150
  background = pygame.image.load('game-background.jpg')
  pikachu = pygame.image.load('pikachu.png')
  pikachu.set_colorkey((0, 0, 0))
  fish = pygame.image.load('fish.jpg')
  fish.set_colorkey((0, 0, 0))
  keep_alive = True
  while keep_alive and not done:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
    pygame.display.flip()
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and user_x < 269:
      user_x = user_x+5
    elif keys[pygame.K_LEFT] and user_x > 0:
      user_x = user_x-5
    fish_posy(0)
    fish_posy(1)
    fish_posy(2)
    screen.blit(background, [0, 0])
    screen.blit(pikachu, [user_x, 510])
    screen.blit(fish, [1, fish_y[0]])
    screen.blit(fish, [157, fish_y[1]])
    screen.blit(fish, [307, fish_y[2]])
    if 520 > fish_y[0] > 483 and user_x < 25:
      crashed(0)
    if 520 > fish_y[1] > 483 and 100 < user_x < 183:
      crashed(1)
    if 520 > fish_y[2] > 483 and user_x > 255:
      crashed(2)


    scoreboard(score)
    pygame.display.update()
    clock.tick(150)


alive()
