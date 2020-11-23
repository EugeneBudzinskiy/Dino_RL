import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import pygame as pg

WIDTH = 1280
HEIGHT = 720
FPS = 60

HUMAN = 0
AGENT = 1

BIRD_SIZE = tuple([48, 48])
CACTUS_SIZE = [tuple([64, 64]), tuple([40, 64])]
HERO_SIZE = tuple([64, 64])
HERO_SIT_SIZE = tuple([88, 36])

GLOBAL_OFFSET = 30
GROUND_LEVEL = 85
FIRST_SPAWN_DISTANCE = HERO_SIZE[0] * 10
NUMBER_OF_EXISTING_PROP = 20

SPAWN_DISTANCE = [HERO_SIZE[0] * 8, HERO_SIZE[0] * 9, HERO_SIZE[0] * 10]
BIRD_SPAWN_CHANCE = 10  # 1/10
BIRD_SPAWN_HEIGHT = (-16, -38, -80)

BACKGROUND_IMAGE = []
DINO_SIT_IMAGE = []
DINO_IMAGE = []
for i in range(1, 13):
    BACKGROUND_IMAGE.append(pg.image.load(os.path.join("texture", 'BG-{}.png'.format(i))))

for i in range(1, 7):
    DINO_SIT_IMAGE.append(pg.image.load(os.path.join("texture", 'DinoSit-{}.png'.format(i))))
    DINO_IMAGE.append(pg.image.load(os.path.join("texture", 'Dino-{}.png'.format(i))))

CACTUS_IMAGE = [pg.image.load(os.path.join("texture", 'Cactus1.png')),
                pg.image.load(os.path.join("texture", 'Cactus2.png'))]
BIRD_IMAGE = [pg.image.load(os.path.join("texture", 'Bird-1.png')),
              pg.image.load(os.path.join("texture", 'Bird-2.png'))]
WASTED_IMAGE = pg.image.load(os.path.join("texture", "wasted-1.png"))


# Neural Network Part

EPISODE_COUNT = 5000
MAX_STEPS_PER_EPISODE = 1000

BUFFER_SIZE = int(1e6)
BATCH_SIZE = 32

UPDATE_AFTER_FRAME = 2
SYNC_AFTER_FRAME = 5000

LEARNING_RATE = 1e-4
GAMMA = 0.99

EPSILON = 1.0
EPSILON_MIN = 0.001
EPSILON_MAX = 1.0
EPSILON_INTERVAL = EPSILON_MAX - EPSILON_MIN

EPSILON_GREEDY_FRAMES = 10000
EPSILON_RANDOM_FRAMES = 5000
