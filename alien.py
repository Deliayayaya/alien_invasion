import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,setting,screen):
        super(Alien, self).__init__()
        self.screen = screen
        # self.move_step = 0.3
        # self.move_direction = 1
        # self.move_speed = 0.5
        # self.move_dropspeed = 0.2
        self.image = pygame.image.load('./images/alien.png')
        #获取外星人矩形
        self.rect = self.image.get_rect()
        #初始化原点位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x =float(self.rect.x)
    def draw_alien(self):
        self.screen.blit(self.image,self.rect)
    def update(self,setting):
         self.x += setting.move_step*setting.move_direction*setting.move_speed
         self.rect.x = self.x
    def check_edges(self):
        if(self.rect.right >= self.screen.get_rect().width):
            return True
        elif(self.rect.right <=0 ):
            return True



