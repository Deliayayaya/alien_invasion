#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-11 17:18:23
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_setting,screen):
        # ships = Sprite()
        super(Ship, self).__init__()
        self.ship_limit = 3
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.ship_speed_factor = 20
        self.screen = screen
        self.ai_setting =ai_setting
        #引入飞船图片
        self.image =  pygame.image.load('./images/rocket-2442125_640.png')
        #将飞船图片放在屏幕下正中间
        #获取飞船矩形
        self.rect = self.image.get_rect()
        self.width,self.height = self.image.get_size()
        #获取屏幕矩形
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        #将飞船中心x位置变为小数
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
         #将飞船中心y位置变为小数
        self.align =float(self.rect.bottom)
    def drawship (self):
        self.screen.blit(self.image,self.rect)

    def update (self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ship_speed_factor
        self.rect.centerx = self.center

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.align +=self.ship_speed_factor

        if self.moving_up and self.rect.top > 0:
            self.align -=self.ship_speed_factor
        self.rect.bottom = self.align
    def reset(self):
        self.center = self.screen_rect.centerx
        self.align = self.screen_rect.bottom






