import pygame as pg


class Image(pg.sprite.Sprite):
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)
        self.image = image_file
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def change_location(self, location):
        self.rect.left, self.rect.top = location
