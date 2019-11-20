import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,ai_setting,screen,ai_ship):
        #super的作用！！！！！！
        super(Bullet, self).__init__()
        self.screen = screen
        self.color = ai_setting.bullet_color
        self.bullet_width =ai_setting.bullet_width
        self.bullet_height = ai_setting.bullet_height
        self.bullet_speed = ai_setting.bullet_speed

        self.rect = pygame.Rect(0,0,self.bullet_width,self.bullet_height)
        self.rect.centerx = ai_ship.rect.centerx
        self.rect.top = ai_ship.rect.top
        self.y = float(self.rect.y)
    def update(self):
        #让子弹上移，直到遇到窗口上边缘消失
        self.y -= self.bullet_speed
        self.rect.y =self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

