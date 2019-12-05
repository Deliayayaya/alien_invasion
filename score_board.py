import pygame
from pygame.sprite import Group
from ship import Ship

# from game_status import status
class Score():
    def __init__(self,screen,setting,status):
        self.screen = screen
        self.setting = setting
        self.status = status
        self.screen_rect = self.screen.get_rect()
        self.width = self.setting.screen_width
        self.height = 30
        self.score_number = 0
        self.score = 50
        self.heigh_score = 0
        self.font_color = (0,0,0)
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.font = pygame.font.SysFont(None,30)
        self.render_sb()
        self.render_heigh_score()

    def render_sb(self):
        self.rounded_score = int(round(self.score_number,-1))
        self.score_str = "{:,}".format(self.rounded_score)
        self.img = self.font.render(self.score_str,True,self.font_color)
        self.img_rect = self.img.get_rect()
        self.img_rect.right = self.screen_rect.right-20
        self.img_rect.top =10
    def render_heigh_score(self):
        self.heigh_score = self.score_number
        self.rounded_score = int(round(self.score_number,-1))
        self.score_str = "{:,}".format(self.rounded_score)
        self.h_img = self.font.render('HS:'+self.score_str,True,self.font_color)
        self.h_img_rect = self.h_img.get_rect()
        self.h_img_rect.centerx = self.screen_rect.centerx;
        self.h_img_rect.top = 10

    def show_ships(self):
        self.ships = Group()
        for ship_number in range(self.status.ship_limit):
            ship = Ship(self.setting,self.screen)
            ship.image = pygame.image.load('./images/rocket-2442125_6401.png')
            ship.rect.left = 6 + ship_number * ship.rect.width
            ship.rect.top = 6
            self.ships.add(ship)

    def draw_sb(self):
        self.screen.blit(self.img,self.img_rect)
        self.screen.blit(self.h_img,self.h_img_rect)
        self.ships.draw(self.screen)





