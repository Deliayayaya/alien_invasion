import sys,pygame
from settings import Settings
from ship import Ship
from alien import Alien
from button import Button
from game_status import Status
import game_functions as gf
from pygame.sprite import Group
def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption('alien Invasion')
    ai_ship = Ship(ai_setting,screen)
    button = Button(screen,'Play')
    #创建一个group收集子弹
    bullets = Group()
    #外星人集
    aliens = Group()
    #游戏控制类
    status = Status()
    # 创建外星人群
    gf.make_aliens(ai_setting, screen,ai_ship, aliens)
    while 1:
        #检查监听事件
        gf.check_event(ai_setting, screen, ai_ship,bullets,status,button,aliens)
        # print(status.game_status)
        if status.game_status == True:
            #更新外星ufo的位置
            gf.update_aliens(ai_setting,screen,ai_ship,bullets,aliens,status)
            #更新飞船的位置
            ai_ship.update()
            #更新子弹的位置
            gf.update_bullets(ai_setting,screen,ai_ship,bullets,aliens)
            #更新屏幕
        gf.update_screen(screen,ai_setting,ai_ship,bullets,aliens,button,status)

run_game()


