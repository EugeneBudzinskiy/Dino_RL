import pygame as pg

from Hero import Hero
from config import HEIGHT, BACKGROUND_IMAGE, WIDTH, WASTED_IMAGE
from image import Image
from prop import Prop


class Graphics:
    def __init__(self, screen):
        self.screen = screen
        self.bg_image = []
        for image in BACKGROUND_IMAGE:
            self.bg_image.append(Image(image, [0, 0]))

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

    def draw_background(self, anim_counter, is_hero):
        self.screen.fill((0, 0, 0))
        if is_hero:
            self.screen.blit(self.bg_image[(anim_counter // 5) % 12].image,
                             self.bg_image[(anim_counter // 5) % 12].rect)

    def draw_obj_without_image(self, obj):
        if isinstance(obj, Prop) or isinstance(obj, Hero):
            if self.screen:
                try:
                    cur_coord = obj.get_coord_normalized(HEIGHT - obj.size[1])
                    pg.draw.rect(self.screen, (0, 128, 255),
                                 pg.Rect(cur_coord[0], cur_coord[1], obj.size[0], obj.size[1]))
                except pg.error:
                    exit(500)
            else:
                raise Exception('Screen is not initialize.')
        else:
            raise Exception('Function draw_obj can`t draw this obj.')

    def draw_text(self, text: str, coord: tuple, color: tuple):
        f1 = pg.font.Font(None, 36)
        text_r = f1.render(text, True, color)
        self.screen.blit(text_r, coord)

    def draw_wasted_screen(self):
        s = pg.Surface((WIDTH, HEIGHT))
        s.set_alpha(128)
        s.fill((48, 34, 34))
        wasted = Image(WASTED_IMAGE, [0, 0])
        self.screen.blit(s, (0, 0))
        self.screen.blit(wasted.image, wasted.rect)
        self.draw_text("Press SPACE to continue.", (500, 650), (186, 186, 186))
