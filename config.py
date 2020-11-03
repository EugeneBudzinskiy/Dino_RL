import os
WIDTH = 1280
HEIGHT = 720
FPS = 60

BIRD_SIZE = tuple([48, 48])
CACTUS_SIZE = [tuple([64, 64]), tuple([40, 64])]
HERO_SIZE = tuple([64, 64])
HERO_SIT_SIZE = tuple([36, 88])

GLOBAL_OFFSET = 30
GROUND_LEVEL = 10
FIRST_SPAWN_DISTANCE = HERO_SIZE[0] * 10
NUMBER_OF_EXISTING_PROP = 20

SPAWN_DISTANCE = [HERO_SIZE[0] * 8, HERO_SIZE[0] * 9, HERO_SIZE[0] * 10]
BIRD_SPAWN_CHANCE = 10  # 1/10
BIRD_SPAWN_HEIGHT = (-16, -50)

BACKGROUND_IMAGE = []
DINO_SIT_IMAGE = []
DINO_IMAGE = []
for i in range(1, 13):
    BACKGROUND_IMAGE.append(os.path.join("texture", 'BG-{}.png'.format(i)))

for i in range(1, 7):
    DINO_SIT_IMAGE.append(os.path.join("texture", 'DinoSit-{}.png'.format(i)))
    DINO_IMAGE.append(os.path.join("texture", 'Dino-{}.png'.format(i)))

CACTUS_IMAGE = [os.path.join("texture", 'Cactus1.png'), os.path.join("texture", 'Cactus2.png')]
BIRD_IMAGE = [os.path.join("texture", 'Bird-1.png'), os.path.join("texture", 'Bird-2.png')]
