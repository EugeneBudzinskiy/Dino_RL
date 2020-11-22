import pygame as pg

from Hero import Hero
from config import HEIGHT, BACKGROUND_IMAGE, WIDTH, WASTED_IMAGE
from image import Image
from prop import Prop


class Graphics:
    def __init__(self, screen):
        self.screen = screen

        self.color_white = (255, 255, 255)

    def draw(self, hero, visible_objects: list, score: int):
        self.draw_background()
        self.draw_scores(score)
        self.draw_obj(hero)
        self.draw_obj(visible_objects)

    def draw_obj(self, obj):
        if isinstance(obj, list):
            for el in obj:
                self.draw_single_obj(el)
        else:
            self.draw_single_obj(obj)

    def draw_single_obj(self, obj):
        a_f = obj.animation_frame
        cur_coord = obj.get_coord_normalized(HEIGHT - obj.size[1])
        obj.texture[a_f].change_location([cur_coord[0], cur_coord[1]])
        self.screen.blit(obj.texture[a_f].image, obj.texture[a_f].rect)

    def draw_background(self):
        self.screen.fill((0, 0, 0))

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

    def draw_scores(self, score):
        score_position = (int(WIDTH * .8), 50)
        score_text = f'score: {score}'

        self.draw_text(score_text, score_position, self.color_white)

    def draw_text(self, text: str, coord: tuple, color: tuple):
        f1 = pg.font.Font(None, 32)
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
