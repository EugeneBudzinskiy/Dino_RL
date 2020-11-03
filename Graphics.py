from prop import Prop
from Hero import Hero
from config import HEIGHT
import pygame as pg


class Graphics:
    def __init__(self, screen):
        self.screen = screen

    def draw_obj(self, obj, i):
        if isinstance(obj, Prop) or isinstance(obj, Hero):
            if self.screen:
                try:
                    cur_coord = obj.get_coord_normalized(HEIGHT - obj.size[1])
                    obj.texture[i].change_location([cur_coord[0], cur_coord[1]])
                    self.screen.blit(obj.texture[i].image, obj.texture[i].rect)
                except pg.error:
                    exit(500)
            else:
                raise Exception('Screen is not initialize.')
        else:
            raise Exception('Function draw_obj can`t draw this obj.')



