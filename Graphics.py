import pygame as pg

from config import FPS, HEIGHT, WIDTH
from config import BACKGROUND_IMAGE, WASTED_IMAGE
from image import Image


class Graphics:
    def __init__(self, screen):
        self.screen = screen

        self.color_white = (255, 255, 255)

        self.bg_image = []
        for image in BACKGROUND_IMAGE:
            self.bg_image.append(Image(image, [0, 0]))

        self._current_frame = 0
        self._animation_frame = 0

        self._animation_frame_count = 12
        self._animation_delay = 5

        self._waiter_counter = 0
        self._max_waiter_count = FPS * 3

        self._waiter_animation_counter = 0
        self._waiter_animation_delay = FPS // 10

    def draw(self, hero, visible_objects: list, score: int, flag=True):
        self._current_frame = (self._current_frame + 1) % self._animation_delay
        if self._current_frame == 0:
            self._animation_frame = (self._animation_frame + 1) % self._animation_frame_count

        self.screen.fill((0, 0, 0))

        if flag:
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
        cur_coord = obj.get_coord_normalized()
        obj.texture[a_f].change_location([cur_coord[0], cur_coord[1]])
        self.screen.blit(obj.texture[a_f].image, obj.texture[a_f].rect)

    def draw_background(self):
        a_f = self._animation_frame
        draw_img = self.bg_image[a_f].image
        draw_rect = self.bg_image[a_f].rect
        self.screen.blit(draw_img, draw_rect)

    def draw_scores(self, score):
        score_position = (int(WIDTH * .8), 50)
        score_text = f'score: {score}'

        self.draw_text(score_text, score_position, self.color_white)

    def draw_text(self, text: str, coord: tuple, color: tuple):
        f1 = pg.font.Font(None, 32)
        text_r = f1.render(text, True, color)
        self.screen.blit(text_r, coord)

    def draw_wasted_screen(self):
        self._waiter_counter = (self._waiter_counter + 1) % self._max_waiter_count

        if self._waiter_animation_counter == 0:
            s = pg.Surface((WIDTH, HEIGHT))
            s.set_alpha(128)
            s.fill((48, 34, 34))
            wasted = Image(WASTED_IMAGE, [0, 0])
            self.screen.blit(s, (0, 0))
            self.screen.blit(wasted.image, wasted.rect)
            self.draw_text("Press SPACE to continue.", (500, 650), (186, 186, 186))

        self._waiter_animation_counter = (self._waiter_animation_counter + 1) % self._waiter_animation_delay

        return self._waiter_counter == 0
