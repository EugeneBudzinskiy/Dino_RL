import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import pygame as pg

# >>> Global Part <<<

WIDTH = 1280
HEIGHT = 720

FPS = 60
STANDARD_MODE = True


# >>> Object Part <<<

PROP_MOVE_VEL = 350
HERO_JUMP_VEL = 1300

GRAVITY_ACC = -70
MAX_GRAVITY_ACC = 6 * GRAVITY_ACC

MAX_VEL = 3000 / FPS
MAX_ACC = 600 / FPS

HERO_SIZE = tuple([64, 64])
HERO_SIT_SIZE = tuple([88, 36])

BIRD_SIZE = tuple([48, 48])
CACTUS_SIZE = tuple([
    tuple([40, 64]),
    tuple([64, 64])
])

SPAWN_DISTANCE = [HERO_SIZE[0] * 8, HERO_SIZE[0] * 9, HERO_SIZE[0] * 10]
FIRST_SPAWN_DISTANCE = HERO_SIZE[0] * 10

BIRD_SPAWN_CHANCE = 10  # 1/10
BIRD_SPAWN_HEIGHT = (20, 50, 80)


# >>> Game Part <<<

GLOBAL_OFFSET = 30
GROUND_LEVEL = 80
NUMBER_OF_EXISTING_PROP = 5

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


# >>> Neural Network Part <<<

EPISODE_COUNT = 10000
MAX_STEPS_PER_EPISODE = 1000

BUFFER_SIZE = int(1e6)
BATCH_SIZE = 32

UPDATE_AFTER_FRAME = 4
SYNC_AFTER_FRAME = 10000

LEARNING_RATE = 1e-4
GAMMA = 0.99

EPSILON = 1.0
EPSILON_MIN = 0.001
EPSILON_MAX = 1.0
EPSILON_INTERVAL = EPSILON_MAX - EPSILON_MIN

EPSILON_GREEDY_FRAMES = 10000
EPSILON_RANDOM_FRAMES = 5000

FILE_PATH = "weights"
