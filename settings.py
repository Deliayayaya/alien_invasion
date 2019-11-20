class Settings():
    def __init__(self):
        #屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (61,185,247)
        #子弹设置
        self.bullet_speed = 0.3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_allowed = 3
        self.bullet_color = (60,60,60)
        #外星人设置
        self.move_direction = 1
        self.move_dropspeed = 20
        self.move_step = 0.3
        self.move_speed = 0.5