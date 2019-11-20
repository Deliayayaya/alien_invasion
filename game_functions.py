import pygame,sys
from bullet import Bullet
from alien import Alien
def check_event(setting, screen, ship, bullets):
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                keydown_event(event,setting,screen,ship,bullets);
            elif event.type == pygame.KEYUP:
                keyup_event(event,ship);

def update_event(screen,setting,ship,bullets,aliens):
      #每次循环时都要重新绘制背景色
        screen.fill(setting.bg_color)
        #绘制飞船
        ship.drawship()
        #绘制外星人
        aliens.draw(screen)
        #绘制子弹
        for bullet in bullets.sprites():
            bullet.draw_bullet()
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

def update_bullets(setting,screen,ship,bullets,aliens):
     #子弹移动到窗口上边缘移除group中的子弹
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(setting,screen,ship,bullets,aliens)
    # collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    # #如果外星人被消灭后再创建一波
    # if len(aliens) == 0:
    #     make_aliens(setting,screen,ship,aliens)

def check_bullet_alien_collision(setting,screen,ship,bullets,aliens):
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    #如果外星人被消灭后再创建一波
    if len(aliens) == 0:
        make_aliens(setting,screen,ship,aliens)

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
    # print(alien_rows)
    for row in range(alien_rows):
        for a in range(alien_number):
            create_aliens(a,row,setting,screen,aliens)

def get_rows_aliens(setting, ship_height, alien_height):
    screen_space = setting.screen_height -3*ship_height - alien_height
    rows = int(screen_space/(alien_height*2))
    return rows

def update_aliens(setting,screen,ship,bullets,aliens,status):
    check_fleet_edges(setting,aliens)
    aliens.update(setting)
    if status.ship_limit > 0:
        #飞船和外星人相撞
        if pygame.sprite.spritecollideany(ship, aliens):

            ship_hit(setting,screen,ship,bullets,aliens,status)
        #外星人和下边缘相撞
        for alien in aliens.sprites():
            if alien.rect.y >= setting.screen_height:
                ship_hit(setting,screen,ship,bullets,aliens,status)
                break
    else:
        status.reset_game()

def ship_hit(setting,screen,ship,bullets,aliens,status):
    print("status==",status.ship_limit)
    status.ship_limit -= 1
    #外星人和子弹清空
    aliens.empty()
    bullets.empty()
    #重新初始化飞船和外星人
    make_aliens(setting,screen,ship,aliens)
    ship.ship_speed_factor +=1
    print(ship.ship_speed_factor)
    ship.reset()

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

