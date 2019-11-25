import pygame

class Button():
    def __init__(self,screen,msg):
        #按钮属性
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.button_width = 200
        self.button_height = 40
        # self.button_bg_color =(0,255,0)
        self.button_color = (50,180,180)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,50)
        self.rect = pygame.Rect(0,0,self.button_width,self.button_height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.bottom/2
        #将文本转换为图片显示
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        #使文字图片在按钮上居中
        self.msg_image_rect.center = self.rect.center
        self.msg_image_rect.bottom = self.rect.bottom
    def draw_button(self):
        #绘制一个用颜色填充的按钮
        self.screen.fill(self.button_color,self.rect)
        #文字图片画到矩形上
        self.screen.blit(self.msg_image,self.msg_image_rect)
