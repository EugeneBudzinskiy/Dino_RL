from prop import Prop
from Hero import Hero
from config import HEIGHT
import pygame as pg


class Graphics:
    def __init__(self, screen):
        self.screen = screen

    def draw_obj(self, obj):
        if isinstance(obj, Prop) or isinstance(obj, Hero):
            if self.screen:
                try:
                    cur_coord = obj.get_coord_normalized(HEIGHT - obj.size[1])
                    pg.draw.rect(self.screen, (0, 128, 255),
                                 pg.Rect(cur_coord[0], cur_coord[1], obj.size[0], obj.size[1]))
                except:
                    exit(500)
            else:
                raise Exception('Screen is not initialize.')
        else:
            raise Exception('Function draw_obj can`t draw this obj.')


class Image(pg.sprite.Sprite):
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

