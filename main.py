import pygame as pg
import random
import time

pg.init()
pg.font.init()
clock = pg.time.Clock()

#координаты
WIDTH = 800
HEIGHT = 600
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
GREEN_COLOR = (34, 177, 76)
YELLOW_COLOR = (255, 242, 0)
FPS = 60
surface = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Прыжки по платформам')


# меню старта




















#платформа
platform_width  = 400
platform_height = 800

#создание персонажа
hero.img = pg.image.load ('img.png')


#cоздание платформ
platforms = pg.sprite.Group()
platform_list = [ (100, 500, 200, 20), (400, 400, 200, 20),(200, 300, 200, 20), (500, 200, 200, 20)]

for platform_data in platform_list:
    platform = Platform(platform_data)
    platforms.add(platform)
    all_sprites.add(platform)



#гравитация
speed = 5
jump_speed = -20
gravity = 0,3
on_ground = True


#жизни
lives = 3

# цикл игры
score = 0

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                move_right = True
            elif event.key == pg.K_a:
                move_left = True

            elif event.key == pg.KEYUP:
                if event.key == pg.K_d:
                    move_right = False
                elif event.key == pg.K_a:
                    move_left = False
# повороты(право, лево)
    if move_right:
        if sprite_rect.x + current_sprite.get_rect().width + speed < WIDTH:
            sprite_rect.x += speed
    elif move_left:
        if sprite_rect.x - speed > 0:
            sprite_rect.x -= speed
#проверка на столкновение с платформами
    if hero.speed_y > 0:
        hits =pg.sprite.spritecollide(hero, platforms, False)
        if hits:
            hero.rect.bottom = hits[0].rect.top
            hero.speed_y = 0
            hero.jump = False



#создание монет
collide = pg.Rect.colliderect(hero, coin)
if collide:
    bonus += 1

#проверка на столкновение персонажа с монетами
hits = pygame.sprite.spritecollide(player, coins, True)
   for hit in hits:
       score += 1

#очистка экрана
surface.fill(WHITE,( 0, 0, 0))

#отрисовка спрайтов
all_sprites.draw(surface)

#подсчет очков
score_text = FONT.render(f'Score: {score}', True, BLACK_COLOR)
surface.blit(score_text, (15, 15))

pg.display.update()
