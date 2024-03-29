import pygame,sys
from bullet import Bullet
from alien import Alien
import warnings
warnings.filterwarnings('ignore')
def check_event(setting, screen, ship, bullets,status,button,aliens,sb):
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                keydown_event(event,setting,screen,ship,bullets);
            elif event.type == pygame.KEYUP:
                keyup_event(event,ship)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                check_play_button(setting,screen,ship,button,status,aliens,bullets,mouse_x,mouse_y,sb)
def check_play_button(setting,screen,ship,button,status,aliens,bullets,mouse_x,mouse_y,sb):

    clicked = button.rect.collidepoint(mouse_x, mouse_y)
    if clicked and not status.game_status:
        status.game_status = True
        #重置飞船命数
        status.ship_limit =3
        #重置/设置分数

        sb.show_ships()
        sb.score_number =0
        sb.heigh_score =0
        #外星人和子弹清空
        aliens.empty()
        bullets.empty()
        #重新初始化飞船和外星人
        make_aliens(setting,screen,ship,aliens)
        ship.reset()
        # pygame.mouse.set_visible(False)

def update_screen(screen,setting,ship,bullets,aliens,button,status,sb):
      #每次循环时都要重新绘制背景色
        screen.fill(setting.bg_color)
        # pygame.transform.scale(ship.image,(10,20))
        sb.show_ships()
        sb.draw_sb()
        #绘制飞船
        ship.drawship()
        #绘制外星人
        aliens.draw(screen)
        #绘制子弹
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        #绘制按钮（在最上层）
        if status.game_status == False:
            button.draw_button()
        #更新整个显示屏
        pygame.display.flip()

def keydown_event(event,setting,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left =True
    elif event.key == pygame.K_UP:
        ship.moving_up =True
    elif event.key == pygame.K_DOWN:
        ship.moving_down =True
    elif event.key == pygame.K_SPACE:
        #按空格键发送子弹ai_setting,screen,ai_ship
        fire_bullet(event,setting,screen,ship,bullets)
    elif event.key ==pygame.K_q:
        sys.exit()

def keyup_event(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key ==pygame.K_LEFT:
        ship.moving_left =False
    elif event.key == pygame.K_UP:
        ship.moving_up =False
    elif event.key == pygame.K_DOWN:
        ship.moving_down =False

def update_bullets(setting,screen,ship,bullets,aliens,sb):
     #子弹移动到窗口上边缘移除group中的子弹
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(setting,screen,ship,bullets,aliens,sb)
    # collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    # #如果外星人被消灭后再创建一波
    # if len(aliens) == 0:
    #     make_aliens(setting,screen,ship,aliens)

def check_bullet_alien_collision(setting,screen,ship,bullets,aliens,sb):
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    #如果外星人被消灭后再创建一波
    if len(aliens) == 0:
        make_aliens(setting,screen,ship,aliens)
    else:
        sb.score_number += 50*len(collisions)
        sb.render_sb()


def fire_bullet(event,setting,screen,ship,bullets):
    if len(bullets) < setting.bullet_allowed:
        new_bullet = Bullet(setting,screen,ship)
        bullets.add(new_bullet)

def get_number_aliens_x(setting,screen):
    alien = Alien(setting,screen)
    alien_border = alien.rect.width*2
    alien_space = setting.screen_width-alien_border
    alien_number = int(alien_space/(2*alien.rect.width))
    return alien_number

def create_aliens(a,row,setting,screen,aliens):
    alien = Alien(setting,screen)
    alien.x = alien.rect.width*2*a
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height+alien.rect.height*2*row
    # alien.move_speed
    aliens.add(alien)

def make_aliens(setting,screen,ship,aliens):
    alien = Alien(setting,screen)
    alien_number = get_number_aliens_x(setting,screen)
    alien_rows = get_rows_aliens(setting,ship.rect.height,alien.rect.height)
    for row in range(alien_rows):
        for a in range(alien_number):
            create_aliens(a,row,setting,screen,aliens)

def get_rows_aliens(setting, ship_height, alien_height):
    screen_space = setting.screen_height -3*ship_height - alien_height
    rows = int(screen_space/(alien_height*2))
    return rows

def update_aliens(setting,screen,ship,bullets,aliens,status,sb):
    check_fleet_edges(setting,aliens)
    aliens.update(setting)
    if status.ship_limit > 0:
        sb.show_ships()
        #飞船和外星人相撞
        if pygame.sprite.spritecollideany(ship, aliens):

            ship_hit(setting,screen,ship,bullets,aliens,status,sb)
        #外星人和下边缘相撞
        for alien in aliens.sprites():
            if alien.rect.y >= setting.screen_height:
                ship_hit(setting,screen,ship,bullets,aliens,status,sb)
                break

    else:
        status.game_status =False
        # check_heigh_score(status,sb)
        #光标可见
        # pygame.mouse.set_visible(True)

def ship_hit(setting,screen,ship,bullets,aliens,status,sb):
    #game over
        status.ship_limit -= 1
        ship.ship_speed_factor +=1
        sb.show_ships()
        # sb.draw_sb()
        check_heigh_score(status,sb)
        sb.score_number = 0
        #外星人和子弹清空
        aliens.empty()
        bullets.empty()
        #重新初始化飞船和外星人
        make_aliens(setting,screen,ship,aliens)
        ship.reset()
def check_heigh_score(status,sb):
    if sb.score_number > sb.heigh_score:
        sb.heigh_score = sb.score_number
        sb.render_heigh_score()

def check_fleet_edges(setting,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            #改变方向并下移外星人
            change_direction_drop(setting,aliens)
            break

def change_direction_drop(setting,aliens):
    for alien in aliens.sprites():
        alien.rect.y +=  setting.move_dropspeed
    setting.move_direction *= -1

def check_aliens_bottom(setting, status, screen, ship, aliens, bullets):
    for alien in aliens.sprites():
        if alien.rect.y >= setting.screen_height:
            ship_hit(setting, status, screen, ship, aliens, bullets)
            break

