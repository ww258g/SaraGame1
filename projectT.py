# encoding: utf-8
import moviepy.editor
from time import sleep
import pygame
import random
import math
pygame.init()
def load_vedio(path):
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN, 32)
    clip = moviepy.editor.VideoFileClip(path)
    clip.preview()
    clip.end
    clip.close()
def load_text(string,RGB,size,x,y,TTF,screen):
  TTF = pygame.font.Font(TTF, size)
  text = TTF.render(string, True, (RGB[0],RGB[1],RGB[2]))
  screen.blit(text, (x, y))
def load_background():
    global background_image_filename
    a = random.uniform(0,1)
    if a < 0.35:
        background_image_filename = "image/backgrounds/a.jpg"
    elif 0.35 <= a < 0.50:
        background_image_filename = "image/backgrounds/b.jpg"
    elif 0.50 <= a < 0.65:
        background_image_filename = "image/backgrounds/c.jpg"
    elif 0.65 <= a < 1:
        background_image_filename = "image/backgrounds/d.jpg"
    background = pygame.image.load(background_image_filename).convert()
    return background
class saratoga():
    def __init__(self):
        self.x = 960
        self.y = 500
        self.x_velocity = 0
        self.y_velocity = 0
        self.image = pygame.image.load("image/saratoga/saratoga.png")
sara = saratoga()
class npc_zero_type():
    def __init__(self):
        self.x = random.uniform(640,1180)
        self.y = -100
        self.image = pygame.image.load("image/npcplanes/零战.png",)
        self.velocity = 3
        self.hit_count = 0#1
        self.type = 1
class npc_G10N():
    def __init__(self):
        self.x = 960
        self.y = -200
        self.image = pygame.image.load("image/npcplanes/富士山.png",)
        self.velocity = 1
        self.hit_count = 0#6
        self.type = 2
class npc_fubuki():
    def __init__(self):
        self.x = 0
        self.y = -500
        self.image = pygame.image.load("image/npcships/fubuki.png")
        self.velocity = 0.5
        self.hit_count = 0#5
        self.hit_counte = 4
        self.type = 1.1
class npc_firefly():
    def __init__(self):
        self.x = 960
        self.y = -200
        self.image = pygame.image.load("image/npcplanes/firefly.png",)
        self.velocity = 3
        self.hit_count = 0#2
        self.type = 3
class npc_Lancastrian():
    def __init__(self):
        self.x = 960
        self.y = -200
        self.image = pygame.image.load("image/npcplanes/兰开斯特.png",)
        self.velocity = 1
        self.hit_count = 0#8
        self.type = 4
class npc_javelin():
    def __init__(self):
        self.x = 0
        self.y = -500
        self.image = pygame.image.load("image/npcships/test_j.png")
        self.velocity = 0.6
        self.hit_count = 0#6
        self.hit_counte = 4
        self.type = 1.2
class npc_F6F():
    def __init__(self):
        self.x = 960
        self.y = -200
        self.image = pygame.image.load("image/npcplanes/F6F.png",)
        self.velocity = 4
        self.hit_count = 0#3
        self.type = 5
class npc_B17():
    def __init__(self):
        self.x = 960
        self.y = -200
        self.image = pygame.image.load("image/npcplanes/B17.png",)
        self.velocity = 1
        self.hit_count = 0#10
        self.type = 6
class npc_Fletcher():
    def __init__(self):
        self.x = 0
        self.y = -500
        self.image = pygame.image.load("image/npcships/test_flc.png")
        self.velocity = 0.5
        self.hit_count = 0  # 7
        self.hit_counte = 6
        self.type = 1.3
class sara_bullte():
    def __init__(self):
        self.x = sara.x + 100
        self.y = sara.y
        self.image = pygame.image.load("image/saratoga/bullte.png")
        self.velocity = -13
class sara_torpedo():
    def __init__(self):
        self.x = sara.x + 50
        self.y = sara.y
        self.image = pygame.image.load("image/saratoga/torpedo.png")
        self.velocity = -5
        self.velocityx = 0
        self.velocityy = 0
        self.angle_lock = 0
class enemy_torpedo():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("image/npcships/torpedo.png")
        self.velocity = -2.5
class enemy_bullte():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("image/npcplanes/bullte.png")
        self.velocity = 1
        self.velocityx = 0
        self.velocityy = 0
class enemy_sbuttle():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("image/npcships/bullte.png")
        self.velocity = 1
        self.velocityx = 0
        self.velocityy = 0
class Bismarck_380():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("image/npcboss/380.png")
        self.rect = 0
        self.bis_380_count = 0
        self.bis_380_counte = 1000
        self.mixer = pygame.mixer.Sound("sounds/380.ogg")
        # self.length = self.image.get_rect().width/2
        self.angle = 0
        # self.v = pygame.math.Vector2(self.length,0)
    def rotate(self,x, y, angle, screen):
        self.angle = math.atan(tan(self.x + 123, self.y + 31, sara.x + 50, sara.y + 50)) * 50
        self.rect = self.image.get_rect(center = (x, y))
        u = pygame.transform.rotate(self.image, -angle)
        # vv = self.v.rotate(angle)
        # a,b = (x, y) + vv
        # rec = u.get_rect()
        r = u.get_rect(center = self.rect.center)
        screen.blit(u, r)
    def attack380(self, enemy_buttles):
        if self.bis_380_count == self.bis_380_counte:
            load_enemy_buttle(self, 0, 20, enemy_buttles, bis_380_shell())
            load_enemy_buttle(self, 0, 40, enemy_buttles, bis_380_shell())
            self.mixer.play(0)
            self.bis_380_count = 0
            self.bis_380_counte = random.randint(300, 1000)
        else:self.bis_380_count += 1
class bis_150():
    def __init__(self):
        self.x = 0
        self.y = 0
class bis_380_shell():
    def __init__(self):
        self.x = sara.x + 100
        self.y = sara.y
        self.image = pygame.image.load("image/npcboss/380shell.png")
        self.velocity = 2
        self.velocityx = 0
        self.velocityy = 0
class bis_bigattack_shell():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("image/npcboss/bigattackshell.png")
        self.velocityx = -10
        self.velocityy = 0
def sara_attack(sara_bulltes):
    a = sara_bullte()
    sara_bulltes.append(a)
def sara_torpedo_attack(sara_torpedos):
    a = [sara_torpedo(), sara_torpedo(), sara_torpedo()]
    sara_torpedos.append(a)
def load_enemy_buttle(enemy, deltax, deltay, enemy_bulltes, buttle_type):
    buttle_type.x = enemy.x + deltax
    buttle_type.y = enemy.y + deltay
    rndx = random.uniform(-1,1)
    rndy = random.uniform(-1,1)
    try:
        buttle_type.velocityx = int((sara.x + 50 - buttle_type.x) / distance(sara.x + 50, sara.y + 50, buttle_type.x, buttle_type.y) * 7 * buttle_type.velocity) + rndx
        buttle_type.velocityy = int((sara.y + 50 - buttle_type.y) / distance(sara.x + 50, sara.y + 50, buttle_type.x, buttle_type.y) * 7 * buttle_type.velocity) + rndy
    except:
        pass
    enemy_bulltes.append(buttle_type)
def sara_action(sara_attack_lock, keys, shut_sound, screen, sara_bulltes, sara_torpedos, sara_torpedo_lock, mode):
    pause = 0
    a = 0
    if keys[pygame.K_F5]:
        sleep(1)
        pause = 1
    while pause == 1:
        keys = pygame.key.get_pressed()
        e = pygame.event.get()
        if keys[pygame.K_F6]:
            pause = 0
            break
    if keys[pygame.K_a]:
        sara.x_velocity = -8
    if keys[pygame.K_d]:
        sara.x_velocity = 8
    if keys[pygame.K_w]:
        sara.y_velocity = -8
    if keys[pygame.K_s]:
        sara.y_velocity = 8
    if keys[pygame.K_j] and sara_attack_lock == True:
        shut_sound.set_volume(0.1)
        shut_sound.play(0)
        sara_attack(sara_bulltes)
    if keys[pygame.K_k] and sara_torpedo_lock == True:
        shut_sound.set_volume(0.1)
        shut_sound.play(0)
        sara_torpedo_attack(sara_torpedos)
    if keys[pygame.K_a] == 0 and keys[pygame.K_d] == 0:
        sara.x_velocity = 0
    if keys[pygame.K_w] == 0 and keys[pygame.K_s] == 0:
        sara.y_velocity = 0
    sara.x += sara.x_velocity
    sara.y += sara.y_velocity
    if 1160 <= sara.x:
        sara.x_velocity = 0
        sara.x = 1160
    if sara.x <= 640:
        sara.x_velocity = 0
        sara.x = 640
    if 950 <= sara.y:
        sara.y_velocity = 0
        sara.y = 950
    if sara.y <= 20:
        sara.y_velocity = 0
        sara.y = 20
    screen.blit(sara.image,(sara.x, sara.y ))
    if mode == 1:
        for bullet in sara_bulltes:
            if bullet.y < 40:
                sara_bulltes.remove(bullet)
            bullet.y += bullet.velocity
            screen.blit(bullet.image, (bullet.x, bullet.y))
        for torpedo in sara_torpedos:
            i = -2
            for a in torpedo:
                i += 1
                if a.y < -20 or a.x > 1250 or a.x < 680:
                    torpedo.remove(a)
                if a.angle_lock == 0:
                    a.image = pygame.transform.rotate(a.image, i * 15)
                    a.velocityx = a.velocity * math.sin(i * 15) / 2
                    a.velocityy = a.velocity * abs(math.cos(i * 15))
                    a.angle_lock = 1
                a.y += a.velocityy
                a.x += a.velocityx
                screen.blit(a.image, (a.x, a.y))
            if torpedo == None:
                sara_torpedos.remove(torpedo)
    elif mode == 2:
        for bullet in sara_bulltes:
            if bullet.x > 1920:
                sara_bulltes.remove(bullet)
            bullet.x -= bullet.velocity
            screen.blit(bullet.image, (bullet.x, bullet.y))
        for torpedo in sara_torpedos:
            i = -2
            for a in torpedo:
                i += 1
                if a.x > 1920:
                    torpedo.remove(a)
                if a.angle_lock == 0:
                    a.image = pygame.transform.rotate(a.image, i * 15 + 90)
                    a.velocityy = a.velocity * math.sin(i * 15) / 2
                    a.velocityx = a.velocity * abs(math.cos(i * 15))
                    a.angle_lock = 1
                a.y += a.velocityy
                a.x -= a.velocityx
                screen.blit(a.image, (a.x, a.y))
            if torpedo == None:
                sara_torpedos.remove(torpedo)
#加载舰船
def load_enemy_ship(position,enemy_ships_count, i, ship_type, enemy_ships, enemy_bullte, enemy_torpedos):
    if enemy_ships_count == i * 45:
        a = ship_type
        a.x = position
        enemy_ships.append(a)
#加载飞机
def load_enemy_plane_group(count1,count2,position,enemy_planes_count,plane_type, enemy_planes, enemy_bulltes):
    for i in range(count1,count2):
        if enemy_planes_count == i * 45:
            a = plane_type
            a.x = position
            enemy_planes.append(a)
            x = enemy_bullte()
            load_enemy_buttle(a, 50, 50, enemy_bulltes,x)
#加载零式1
def load_enemy_plane_A(enemy_planes_count, i, enemy_planes, enemy_buttles):
    load_enemy_plane_group(i, i + 4, random.uniform(680, 1100), enemy_planes_count,npc_zero_type(), enemy_planes, enemy_buttles)
    load_enemy_plane_group(i + 3, i + 7, random.uniform(680, 1100), enemy_planes_count, npc_zero_type(), enemy_planes, enemy_buttles)
#加载零式2
def load_enemy_plane_B(enemy_planes_count,i, enemy_planes, enemy_buttles):
    load_enemy_plane_group(i + 1, i + 2, 680, enemy_planes_count, npc_zero_type(),enemy_planes, enemy_buttles)
    load_enemy_plane_group(i + 1, i + 2, 790, enemy_planes_count, npc_zero_type(),enemy_planes, enemy_buttles)
    load_enemy_plane_group(i + 1, i + 3, 900, enemy_planes_count, npc_zero_type(),enemy_planes, enemy_buttles)
    load_enemy_plane_group(i + 1, i + 1, 1010, enemy_planes_count, npc_zero_type(),enemy_planes, enemy_buttles)
    load_enemy_plane_group(i + 1, i + 2, 1120, enemy_planes_count, npc_zero_type(),enemy_planes, enemy_buttles)
#加载g10n
def load_enemy_plane_C(enemy_planes_count,i,enemy_planes, enemy_buttles):
    load_enemy_plane_group(i, i + 3, random.uniform(700,1000), enemy_planes_count, npc_G10N(),enemy_planes, enemy_buttles)
#加载萤火虫1
def load_enemy_plane_D(enemy_planes_count,i,enemy_planes, enemy_buttles):
    load_enemy_plane_group(i, i + 1, 680, enemy_planes_count, npc_firefly(), enemy_planes, enemy_buttles)
    load_enemy_plane_group(i + 1, i + 2, 800, enemy_planes_count, npc_firefly(), enemy_planes, enemy_buttles)
    load_enemy_plane_group(i + 2, i + 3, 920, enemy_planes_count, npc_firefly(), enemy_planes, enemy_buttles)
    load_enemy_plane_group(i + 1, i + 2, 1060, enemy_planes_count, npc_firefly(), enemy_planes, enemy_buttles)
    load_enemy_plane_group(i , i + 1, 1180, enemy_planes_count, npc_firefly(), enemy_planes, enemy_buttles)
#加载萤火虫2
def load_enemy_plane_E(enemy_planes_count,i,enemy_planes, enemy_buttles):
    load_enemy_plane_group(i, i + 1, 680, enemy_planes_count, npc_firefly(), enemy_planes, enemy_buttles)
    load_enemy_plane_group(i + 1, i + 2, 800, enemy_planes_count, npc_firefly(), enemy_planes, enemy_buttles)
    load_enemy_plane_group(i + 2, i + 3, 920, enemy_planes_count, npc_firefly(), enemy_planes, enemy_buttles)
    load_enemy_plane_group(i + 3, i + 4, 1060, enemy_planes_count, npc_firefly(), enemy_planes, enemy_buttles)
    load_enemy_plane_group(i + 4, i + 5, 1180, enemy_planes_count, npc_firefly(), enemy_planes, enemy_buttles)
    load_enemy_plane_group(i + 6, i + 7, 1060, enemy_planes_count, npc_firefly(), enemy_planes, enemy_buttles)
    load_enemy_plane_group(i + 7, i + 8, 920, enemy_planes_count, npc_firefly(), enemy_planes, enemy_buttles)
    load_enemy_plane_group(i + 8, i + 9, 800, enemy_planes_count, npc_firefly(), enemy_planes, enemy_buttles)
    load_enemy_plane_group(i + 9, i + 10, 680, enemy_planes_count, npc_firefly(), enemy_planes, enemy_buttles)
#加载兰开斯特
def load_enemy_plane_F(enemy_planes_count,i,enemy_planes, enemy_buttles):
    load_enemy_plane_group(i, i + 1, random.uniform(700, 900), enemy_planes_count, npc_Lancastrian(), enemy_planes, enemy_buttles)
    load_enemy_plane_group(i, i + 1, random.uniform(900, 1100), enemy_planes_count, npc_Lancastrian(), enemy_planes, enemy_buttles)
#加载F6F1
def load_enemy_plane_G(enemy_planes_count,i,enemy_planes, enemy_buttles):
    a = random.uniform(700,1100)
    load_enemy_plane_group(i, i + 4, a, enemy_planes_count, npc_F6F(), enemy_planes,enemy_buttles)
#加载F6F2
def load_enemy_plane_H(enemy_planes_count,i,enemy_planes, enemy_buttles):
    a = random.uniform(800, 1000)
    load_enemy_plane_group(i, i + 3, a, enemy_planes_count, npc_F6F(), enemy_planes, enemy_buttles)
    load_enemy_plane_group(i + 1, i + 2, a - 120, enemy_planes_count, npc_F6F(), enemy_planes, enemy_buttles)
    load_enemy_plane_group(i + 1, i + 2, a + 120, enemy_planes_count, npc_F6F(), enemy_planes, enemy_buttles)
#加载b17
def load_enemy_plane_I(enemy_planes_count,i,enemy_planes, enemy_buttles):
    load_enemy_plane_group(i, i + 3, random.uniform(800, 1000), enemy_planes_count, npc_B17(), enemy_planes, enemy_buttles)
#第一关敌方出场顺序
def load_enemy_plane_1(ememy_planes_count,enemy_planes, enemy_buttles, enemy_ships, enemy_torpedos, enemy_ships_count):
    load_enemy_plane_A(ememy_planes_count, 10, enemy_planes, enemy_buttles)
    load_enemy_ship(1000,enemy_ships_count, 11, npc_fubuki(), enemy_ships, enemy_bullte, enemy_torpedos)
    load_enemy_plane_B(ememy_planes_count, 25, enemy_planes, enemy_buttles)
    load_enemy_plane_A(ememy_planes_count, 40, enemy_planes, enemy_buttles)
    load_enemy_plane_C(ememy_planes_count, 55, enemy_planes, enemy_buttles)
    load_enemy_ship(700, enemy_ships_count, 56, npc_fubuki(), enemy_ships, enemy_bullte, enemy_torpedos)
    load_enemy_plane_B(ememy_planes_count, 70, enemy_planes, enemy_buttles)
    load_enemy_plane_A(ememy_planes_count, 85, enemy_planes, enemy_buttles)
    load_enemy_ship(800, enemy_ships_count, 86, npc_fubuki(), enemy_ships, enemy_bullte, enemy_torpedos)
    load_enemy_ship(1100, enemy_ships_count, 87, npc_fubuki(), enemy_ships, enemy_bullte, enemy_torpedos)
    load_enemy_plane_C(ememy_planes_count, 100, enemy_planes, enemy_buttles)
#第二关敌方出场顺序
def load_enemy_plane_2(ememy_planes_count,enemy_planes, enemy_buttles, enemy_ships, enemy_torpedos, enemy_ships_count):
    load_enemy_plane_D(ememy_planes_count, 10 ,enemy_planes, enemy_buttles)
    load_enemy_ship(900, enemy_ships_count, 11, npc_javelin(), enemy_ships, enemy_bullte, enemy_torpedos)
    load_enemy_plane_E(ememy_planes_count, 25, enemy_planes, enemy_buttles)
    load_enemy_plane_F(ememy_planes_count, 26, enemy_planes, enemy_buttles)
    load_enemy_plane_D(ememy_planes_count, 40, enemy_planes, enemy_buttles)
    load_enemy_plane_D(ememy_planes_count, 55, enemy_planes, enemy_buttles)
    load_enemy_plane_F(ememy_planes_count, 70, enemy_planes, enemy_buttles)
    load_enemy_ship(900, enemy_ships_count, 71, npc_javelin(), enemy_ships, enemy_bullte, enemy_torpedos)
    load_enemy_plane_D(ememy_planes_count, 72, enemy_planes, enemy_buttles)
    load_enemy_plane_D(ememy_planes_count, 76, enemy_planes, enemy_buttles)
    load_enemy_plane_F(ememy_planes_count, 100, enemy_planes, enemy_buttles)
#第三关敌方出场顺序
def load_enemy_plane_3(ememy_planes_count,enemy_planes, enemy_buttles, enemy_ships, enemy_torpedos, enemy_ships_count):
    load_enemy_plane_G(ememy_planes_count, 10, enemy_planes, enemy_buttles)
    load_enemy_ship(1000, enemy_ships_count, 11, npc_Fletcher(), enemy_ships, enemy_bullte, enemy_torpedos)
    load_enemy_plane_H(ememy_planes_count, 15, enemy_planes, enemy_buttles)
    load_enemy_plane_H(ememy_planes_count, 20, enemy_planes, enemy_buttles)
    load_enemy_plane_I(ememy_planes_count, 35, enemy_planes, enemy_buttles)
    load_enemy_plane_G(ememy_planes_count, 40, enemy_planes, enemy_buttles)
    load_enemy_plane_H(ememy_planes_count, 38, enemy_planes, enemy_buttles)
    load_enemy_ship(900, enemy_ships_count, 40, npc_Fletcher(), enemy_ships, enemy_bullte, enemy_torpedos)
    load_enemy_plane_G(ememy_planes_count, 55, enemy_planes, enemy_buttles)
    load_enemy_plane_H(ememy_planes_count, 70, enemy_planes, enemy_buttles)
    load_enemy_plane_H(ememy_planes_count, 85, enemy_planes, enemy_buttles)
    load_enemy_ship(1100, enemy_ships_count, 86, npc_Fletcher(), enemy_ships, enemy_bullte, enemy_torpedos)
    load_enemy_ship(900, enemy_ships_count, 87, npc_Fletcher(), enemy_ships, enemy_bullte, enemy_torpedos)
    load_enemy_plane_I(ememy_planes_count, 100, enemy_planes, enemy_buttles)
def distance(x1,y1,x2,y2):
    a = x1 - x2
    b = y1 - y2
    return math.sqrt(a ** 2 + b ** 2)
def tan(x1, y1, x2, y2):
    return (y1 - y2 ) / (x1 - x2)
def kill(score,sara_bulltes, enemy_planes, enemy_bulltes, enemy_torpedos ,sara_torpedos, enemy_ships):
    try:
        for bullte in sara_bulltes:
            for plane in enemy_planes:
                dis =distance(bullte.x, bullte.y,plane.x + 50,plane.y + 50)
                lev = 2 * level - 1
                if dis < 90 and plane.type == lev:
                    if plane.hit_count < lev - 1:
                        sara_bulltes.remove(bullte)
                        del bullte
                        plane.hit_count += 1
                    else:
                        enemy_planes.remove(plane)
                        sara_bulltes.remove(bullte)
                        del bullte
                        del plane
                        score += 5 * lev
                elif dis < 90 and plane.type == lev + 1:
                    if plane.hit_count < 2 * lev + 1:
                        sara_bulltes.remove(bullte)
                        del bullte
                        plane.hit_count += 1
                    else:
                        enemy_planes.remove(plane)
                        sara_bulltes.remove(bullte)
                        del bullte
                        del plane
                        score += 20 * 2 * lev
        for a in sara_torpedos:
            for torpedo in a:
                for ship in enemy_ships:
                    dis = distance(torpedo.x, torpedo.y, ship.x + 41, ship.y + 200)
                    if ship.x - 10 < torpedo.x < ship.x + 70 and ship.y - 10 < torpedo.y < ship.y + 400 and ship.hit_count < ship.hit_counte:
                        ship.hit_count += 1
                        a.remove(torpedo)
                        del torpedo
                    elif ship.hit_counte == ship.hit_count:
                        enemy_ships.remove(ship)
                        a.remove(torpedo)
                        del torpedo
                        del ship
                        score += level * 100
        for bullte in enemy_bulltes:
            if distance(bullte.x,bullte.y,sara.x + 50,sara.y + 50) < 75:
                enemy_bulltes.remove(bullte)
                del bullte
                score -= 20
                continue
        for torpedo in enemy_torpedos:
            if distance(torpedo.x, torpedo.y, sara.x + 50, sara.y + 50) < 75:
                enemy_torpedos.remove(torpedo)
                del torpedo
                score -= 50
                continue
        return score
    except:return score
def load_level(level, bgm_path,score):
    backgroundT = pygame.image.load("image/backgrounds/background.png")
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN|pygame.DOUBLEBUF|pygame.HWSURFACE, 32)
    background = load_background()
    clockdps = pygame.time.Clock()
    dp_count_s = 0
    dp_count_m = 0
    dp_count_h = 0
    end_say = 0
    sara_attack_fluency = 15
    sara_torpedo_fluency = 90
    sara_bulltes = []
    enemy_bulltes = []
    enemy_torpedos = []
    sara_torpedos = []
    enemy_planes = []
    enemy_ships = []
    shut_sound = pygame.mixer.Sound("sounds/shut.ogg")
    enemy_planes_move_count = 0
    enemy_ships_move_count = 0
    score = 0
    bgm = pygame.mixer.Sound(bgm_path)
    bgm.play(-1)
    sara_attack_count = 0
    sara_attack_lock = True
    sara_torpedo_lock = True
    sara_torpedo_count = 0
    while True:
        if level == 1:
            load_enemy_plane_1(enemy_planes_move_count, enemy_planes, enemy_bulltes, enemy_ships, enemy_torpedos,enemy_ships_move_count)
        elif level == 2:
            load_enemy_plane_2(enemy_planes_move_count, enemy_planes, enemy_bulltes, enemy_ships, enemy_torpedos,enemy_ships_move_count)
        elif level == 3:
            load_enemy_plane_3(enemy_planes_move_count, enemy_planes, enemy_bulltes, enemy_ships, enemy_torpedos,enemy_ships_move_count)
        dp_count_s += 1
        if dp_count_s == 60:
            dp_count_s = 0
            dp_count_m += 1
        if dp_count_m == 60:
            dp_count_m = 0
            dp_count_h += 1
        strtime = str(dp_count_h) + ":" + str(dp_count_m) + ":" + str(dp_count_s)
        time = 60 ** 2 * dp_count_h + 60 * dp_count_m + dp_count_s
        screen.blit(background, (0, 0))
        screen.blit(backgroundT, (620, 0))
        load_text(strtime, [255, 0, 0], 100, 0, 250, "BRITANIC.TTF",screen)
        keys = pygame.key.get_pressed()
        sara_attack_count += 1
        if sara_attack_fluency > 10:
            sara_attack_fluency = 15 - (dp_count_m + 60 * dp_count_h) / 7
        if sara_attack_count > sara_attack_fluency:
            sara_attack_lock = True
            sara_attack_count = 0
        sara_torpedo_count += 1
        if sara_torpedo_fluency > 60:
            sara_torpedo_fluency = 90 - (dp_count_m + 60 * dp_count_h) / 10
        if sara_torpedo_count > sara_torpedo_fluency:
            sara_torpedo_lock = True
            sara_torpedo_count = 0
        sara_action(sara_attack_lock, keys, shut_sound, screen, sara_bulltes, sara_torpedos, sara_torpedo_lock, 1)
        sara_attack_lock = False
        sara_torpedo_lock = False
        enemy_planes_move_count += 1
        enemy_ships_move_count += 1
        for torpedo in enemy_torpedos:
            torpedo.y -= torpedo.velocity
            if torpedo.x > 1280 or torpedo.x < 680 or torpedo.y > 1080:
                enemy_torpedos.remove(torpedo)
                continue
            screen.blit(torpedo.image, (torpedo.x,torpedo.y))
        for ship in enemy_ships:
            if ship.y < 300:
                ship.y += ship.velocity
            if time % 120 == 0 and ship.type == 1.1:
                load_enemy_buttle(ship, 50, 75, enemy_bulltes, enemy_sbuttle())
                load_enemy_buttle(ship, 50, 400, enemy_bulltes, enemy_sbuttle())
            if time % 200 == 0 and ship.type == 1.1:
                load_enemy_buttle(ship, 0, 200, enemy_torpedos, enemy_torpedo())
                load_enemy_buttle(ship, 70, 200, enemy_torpedos, enemy_torpedo())
            if time % 120 == 0 and ship.type == 1.2:
                load_enemy_buttle(ship, 50, 75, enemy_bulltes, enemy_sbuttle())
                load_enemy_buttle(ship, 50, 200, enemy_bulltes, enemy_sbuttle())
                load_enemy_buttle(ship, 50, 400, enemy_bulltes, enemy_sbuttle())
            if time % 200 == 0 and ship.type == 1.2:
                load_enemy_buttle(ship, 0, 200, enemy_torpedos, enemy_torpedo())
                load_enemy_buttle(ship, 70, 200, enemy_torpedos, enemy_torpedo())
            if time % 120 == 0 and ship.type == 1.3:
                load_enemy_buttle(ship, 50, 75, enemy_bulltes, enemy_sbuttle())
                load_enemy_buttle(ship, 50, 200, enemy_bulltes, enemy_sbuttle())
                load_enemy_buttle(ship, 50, 400, enemy_bulltes, enemy_sbuttle())
            if time % 200 == 0 and ship.type == 1.3:
                load_enemy_buttle(ship, 0, 200, enemy_torpedos, enemy_torpedo())
                load_enemy_buttle(ship, -50, 200, enemy_torpedos, enemy_torpedo())
                load_enemy_buttle(ship, 120, 200, enemy_torpedos, enemy_torpedo())
                load_enemy_buttle(ship, 70, 200, enemy_torpedos, enemy_torpedo())
            screen.blit(ship.image, (ship.x, ship.y))
        for plane in enemy_planes:
            plane.y += plane.velocity
            if time % 60 == 0 and plane.type == level * 2 - 1:
                a = enemy_bullte()
                load_enemy_buttle(plane, 50, 50, enemy_bulltes,a)
            elif time % 60 == 0 and plane.type == level * 2:
                for i in range(0, level * 2):
                    a = enemy_bullte()
                    load_enemy_buttle(plane, 30 + int(200 / (i + 1)), 70, enemy_bulltes,a)
            if plane.y > 1080:
                enemy_planes.remove(plane)
                continue
            if plane.type == 3:
                plane.x += math.sin(time/30)
                screen.blit(plane.image, (plane.x, plane.y))
            elif plane.type == 1 or 2 or 4 or 6:
                screen.blit(plane.image, (plane.x, plane.y))
            elif plane.type == 5:
                screen.blit(plane.image, (plane.x, plane.y))
        for bullte in enemy_bulltes:
            bullte.x += bullte.velocityx
            bullte.y += bullte.velocityy
            if bullte.x > 1280 or bullte.x < 680 or bullte.y > 1080:
                enemy_bulltes.remove(bullte)
                continue
            screen.blit(bullte.image, (bullte.x, bullte.y))
        score = kill(score,sara_bulltes, enemy_planes, enemy_bulltes, enemy_torpedos, sara_torpedos, enemy_ships)
        load_text(("score:" + str(score)), [255, 0, 0], 100, 0, 0, "BRITANIC.TTF", screen)
        load_text("wasd to move", [255, 0, 0], 100, 1300, 0, "BRITANIC.TTF", screen)
        load_text("j to attack", [255, 0, 0], 100, 1300, 200, "BRITANIC.TTF", screen)
        load_text("k to torpedo", [255, 0, 0], 100, 1300, 300, "BRITANIC.TTF", screen)
        load_text("F5 to pause", [255, 0, 0], 100, 1300, 400, "AGENCYB.TTF", screen)
        load_text("F6 to continue", [255, 0, 0], 100, 1300, 500, "AGENCYB.TTF", screen)
        c = "level:" + str(level)
        load_text(c, [255, 0, 0], 100, 0, 400, "BRITANIC.TTF", screen)
        if time > 5700:
            load_text("the end", [255, 0, 0], 100, 680, 500, "BRITANIC.TTF", screen)
            if score >= 350 + level * 200:
                end_say = "Perfect!"
            elif 350 + level * 200 > score > 300 + level * 200:
                end_say = "Execllent!"
            elif 300 + level * 200 >= score > 200 + level * 100:
                end_say = "Good!"
            elif 100 + level * 100 >= score:
                end_say = "noob"
            load_text(end_say, [255, 0, 0], 100, 680, 650, "BRITANIC.TTF", screen)
        if time > 5900:
            bgm.fadeout(5000)
            sleep(5)
            level = load_cg(score, level)
            return level,score
            break
        clockdps.tick(90)
        pygame.event.pump()
        pygame.display.update()
def load_cg(score, level):
    a = random.randint(1, 6)
    a = "image/backgrounds/cg/" + str(a) + ".png"
    screen = pygame.display.set_mode((1920, 1080), 0, 32)
    backgroundT = pygame.image.load(a)
    clock1 = pygame.time.Clock()
    while True:
        screen.blit(backgroundT, (0, 0))
        load_text(("Your score:" + str(score)), [255, 0, 0], 75, 700, 300, "BRITANIC.TTF",screen)
        load_text("press SPACE to contiune", [255, 0, 0], 75, 700, 425, "BRITANIC.TTF",screen)
        load_text("you can get your scores in score.txt", [255, 0, 0], 75, 700, 550, "BRITANIC.TTF", screen)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    level += 1
                    if level == 4:
                        load_boss(level, "sounds/boss.ogg")
                    if level > 4:
                        pygame.quit()
                    return level
        clock1.tick(60)
        pygame.display.update()
def load_bis_bigattack_shell(big_attack_shells, x, y, enemy_buttlesbig):
    a = bis_bigattack_shell()
    a.x = x
    a.y = y
    big_attack_shells.append(a)
    enemy_buttlesbig.append(a)
def load_bis_bigatttack(big_attack_shells, x, shell_count, enemy_buttlesbig):
    deltay = 1080 / ( shell_count + 1 )
    y = 0
    for i in range(0, shell_count):
        y += deltay
        load_bis_bigattack_shell(big_attack_shells, x, y, enemy_buttlesbig)
def killB(score, sara, enemy_buttles380, enemy_buttles150, enemy_buttlesbig):
    for u in enemy_buttles380:
        if distance(u.x, u.y, sara.x + 50, sara.y + 50) < 70:
            score -= 100
            enemy_buttles380.remove(u)
            del u
    for u in enemy_buttles150:
        if distance(u.x, u.y, sara.x + 50, sara.y + 50) < 60:
            score -= 20
            enemy_buttles150.remove(u)
            del u
    for u in enemy_buttlesbig:
        if (u.x < sara.x < u.x + 70 or u.x < sara.x + 100 < u.x + 70) and (u.y < sara.y < u.y +100 or u.y < sara.y + 100 < u.y +100):
            score -= 1
    return score
def load_bis150_shells(bis_150,enemy_bulltes150,enemy_sbuttle):
    load_enemy_buttle(bis_150(), 1780, 404, enemy_bulltes150, enemy_sbuttle())
    load_enemy_buttle(bis_150(), 1780, 415, enemy_bulltes150, enemy_sbuttle())
    load_enemy_buttle(bis_150(), 1780, 598, enemy_bulltes150, enemy_sbuttle())
    load_enemy_buttle(bis_150(), 1780, 609, enemy_bulltes150, enemy_sbuttle())
    load_enemy_buttle(bis_150(), 1780, 712, enemy_bulltes150, enemy_sbuttle())
    load_enemy_buttle(bis_150(), 1780, 723, enemy_bulltes150, enemy_sbuttle())
def load_boss(level, bgm_path):
    backgroundB = pygame.image.load("image/backgrounds/backgroundT.png")
    screen = pygame.display.set_mode((1920, 1080), 0, 32)
    background = load_background()
    clockdps = pygame.time.Clock()
    dp_count = 0
    dp_counts = 90
    end_say = 0
    sara_attack_fluency = 15
    sara_torpedo_fluency = 90
    sara_bulltes = []
    sara_torpedos = []
    enemy_bulltes380 = []
    enemy_bulltes150 = []
    enemy_bulltesbig = []
    shut_sound = pygame.mixer.Sound("sounds/shut.ogg")
    score = 2000
    bgm = pygame.mixer.Sound(bgm_path)
    bgm.play(-1)
    sara_attack_count = 0
    sara_attack_lock = True
    sara_torpedo_lock = True
    sara_torpedo_count = 0
    bismarck_150_count = 0
    bismarck_bigattack_count = [300,400,500]
    bismarck_bigattack_shells = []
    bismarck_bigattack_wait_shells = []
    bismarck_bigattack_shells0 = []
    bismarck_bigattack_shells1 = []
    bismarck_bigattack_shells2 = []
    bismarck_bigattack_wait_shells0 = []
    bismarck_bigattack_wait_shells1 = []
    bismarck_bigattack_wait_shells2 = []
    bismarck_bigattack_shells.append(bismarck_bigattack_shells0)
    bismarck_bigattack_shells.append(bismarck_bigattack_shells1)
    bismarck_bigattack_shells.append(bismarck_bigattack_shells2)
    bismarck_bigattack_wait_shells.append(bismarck_bigattack_wait_shells0)
    bismarck_bigattack_wait_shells.append(bismarck_bigattack_wait_shells1)
    bismarck_bigattack_wait_shells.append(bismarck_bigattack_wait_shells2)
    anton = Bismarck_380()
    bruno = Bismarck_380()
    ceaser = Bismarck_380()
    dora = Bismarck_380()
    anton.x = 1750
    anton.y = 65
    bruno.x = 1750
    bruno.y = 173
    ceaser.x = 1750
    ceaser.y = 823
    dora.x = 1750
    dora.y = 931
    while True:
        screen.blit(background,(0, 0))
        screen.blit(backgroundB,(1920 - 640, 0))
        screen.blit(backgroundB, (1920 - 640 - 640, 0))
        screen.blit(pygame.image.load("image/npcboss/bsm船底.png"),(1920 - 177, 0))
        keys = pygame.key.get_pressed()
        if sara_attack_fluency > 10:
            sara_attack_fluency = 15 - dp_count/ 7
        if sara_attack_count > sara_attack_fluency:
            sara_attack_lock = True
            sara_attack_count = 0
        sara_torpedo_count += 1
        if sara_torpedo_fluency > 60:
            sara_torpedo_fluency = 90 - dp_count/ 10
        if sara_torpedo_count > sara_torpedo_fluency:
            sara_torpedo_lock = True
            sara_torpedo_count = 0
        sara_attack_count += 1
        sara_action(sara_attack_lock, keys, shut_sound, screen, sara_bulltes, sara_torpedos, sara_torpedo_lock, 2)
        sara_attack_lock = False
        sara_torpedo_lock = False
        bismarck_bigattack_count[0] += 1
        bismarck_bigattack_count[1] += 1
        bismarck_bigattack_count[2] += 1
        bismarck_150_count += 1
        i = 1
        for a in bismarck_bigattack_count:
            if a == 500 + i * 100:
                if i == 1:
                    load_bis_bigatttack(bismarck_bigattack_wait_shells0, i * 100 + 1180, 3, enemy_bulltesbig)
                elif i == 2:
                    load_bis_bigatttack(bismarck_bigattack_wait_shells1, i * 100 + 1180, 5, enemy_bulltesbig)
                elif i == 3:
                    load_bis_bigatttack(bismarck_bigattack_wait_shells2, i * 100 + 1180, 4, enemy_bulltesbig)
            if a == 1000 + i * 100:
                if i == 1:
                    bismarck_bigattack_shells0 = bismarck_bigattack_wait_shells0
                    bismarck_bigattack_wait_shells0 = []
                    bismarck_bigattack_count[0] = 0
                elif i == 2:
                    bismarck_bigattack_shells1 = bismarck_bigattack_wait_shells1
                    bismarck_bigattack_wait_shells1 = []
                    bismarck_bigattack_count[1] = 0
                elif i == 3:
                    bismarck_bigattack_shells2 = bismarck_bigattack_wait_shells2
                    bismarck_bigattack_wait_shells2 = []
                    bismarck_bigattack_count[2] = 0
            i += 1
        for b in bismarck_bigattack_shells0:
            b.x += b.velocityx
            if b.x <500:
                bismarck_bigattack_shells0.remove(b)
                del  b
                continue
            screen.blit(b.image, (b.x, b.y))
        for b in bismarck_bigattack_shells1:
            b.x += b.velocityx
            if b.x <500:
                bismarck_bigattack_shells1.remove(b)
                del b
                continue
            screen.blit(b.image, (b.x, b.y))
        for b in bismarck_bigattack_shells2:
            b.x += b.velocityx
            if b.x <500:
                bismarck_bigattack_shells2.remove(b)
                del  b
                continue
            screen.blit(b.image, (b.x, b.y))
        for b in bismarck_bigattack_wait_shells0:
            screen.blit(b.image, (b.x, b.y))
        for b in bismarck_bigattack_wait_shells1:
            screen.blit(b.image, (b.x, b.y))
        for b in bismarck_bigattack_wait_shells2:
            screen.blit(b.image, (b.x, b.y))
        if bismarck_150_count == 75:
            load_bis150_shells(bis_150, enemy_bulltes150, enemy_sbuttle)
        if bismarck_150_count == 85:
            load_bis150_shells(bis_150, enemy_bulltes150, enemy_sbuttle)
        if bismarck_150_count == 95:
            load_bis150_shells(bis_150, enemy_bulltes150, enemy_sbuttle)
            bismarck_150_count = 0
        for a in enemy_bulltes380:
            a.x += a.velocityx * 1.5
            a.y += a.velocityy * 1.5
            if a.x < 640:
                enemy_bulltes380.remove(a)
                continue
            screen.blit(a.image, (a.x, a.y))
        for a in enemy_bulltes150:
            a.x += a.velocityx * 1.5
            a.y += a.velocityy * 1.5
            if a.x < 640:
                enemy_bulltes150.remove(a)
                continue
            screen.blit(a.image, (a.x, a.y))
        anton.attack380(enemy_bulltes380)
        bruno.attack380(enemy_bulltes380)
        ceaser.attack380(enemy_bulltes380)
        dora.attack380(enemy_bulltes380)
        anton.rotate(1866, 95,anton.angle,screen)
        bruno.rotate(1866, 204,bruno.angle,screen)
        ceaser.rotate(1866, 854,ceaser.angle,screen)
        dora.rotate(1866, 962,dora.angle,screen)
        score = killB(score,sara,enemy_bulltes380,enemy_bulltes150,enemy_bulltesbig)
        load_text(str(score),[255, 0, 0], 100 , 0, 0,"BRITANIC.TTF",screen)
        c = dp_counts - int(dp_count / 90)
        load_text(str(c), [255, 0, 0], 100, 0, 100, "BRITANIC.TTF", screen)
        load_text("you can miss", [255, 0, 0], 100, 0, 200, "BRITANIC.TTF", screen)
        load_text("but not attack", [255, 0, 0], 100, 0, 300, "BRITANIC.TTF", screen)
        load_text("level:EX", [255, 0, 0], 100, 0, 400, "BRITANIC.TTF", screen)
        if c == 0:
            bgm.fadeout(5000)
            return score
            sleep(5)
            break
        dp_count += 1
        clockdps.tick(90)
        pygame.event.pump()
        pygame.display.update()
def load_loading_screen(a):
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN, 32)
    background = pygame.image.load("image/backgrounds/loading/1.png")
    rgb1 = [255,0,0]
    rgb2 = [0,255,255]
    icon_position = 0
    clock = pygame.time.Clock()
    bgm = pygame.mixer.Sound("sounds/Beginning.ogg")
    bgm.play(-1)
    while a == 1:
        screen.blit(background,(0,0))
        high_score_lock = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if icon_position > 0:
                        icon_position -= 1
                if event.key == pygame.K_s:
                    if icon_position < 2:
                        icon_position += 1
                if event.key == pygame.K_SPACE:
                    if icon_position == 2:
                        pygame.quit()
                    elif icon_position == 0:
                        bgm.fadeout(5000)
                        a = 0
                    elif icon_position == 1:
                        if high_score_lock == False:
                            high_score_lock = True
        if high_score_lock == True:
            load_high_score_list(screen)
            c = True
            while c:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if high_score_lock == True:
                                high_score_lock = False
                                c = False
                clock.tick(80)
                pygame.display.update()
        if icon_position == 0:
            rgba = rgb1
            rgbb = rgb2
            rgbc = rgb2
        elif icon_position == 1:
            rgba = rgb2
            rgbb = rgb1
            rgbc = rgb2
        elif icon_position == 2:
            rgba = rgb2
            rgbb = rgb2
            rgbc = rgb1
        load_text("Start game!!", rgba, 100, 100, 100, "AGENCYB.TTF", screen)
        load_text("High score list", rgbb, 100, 100, 250, "AGENCYB.TTF", screen)
        load_text("Exit", rgbc, 100, 100, 400, "AGENCYB.TTF", screen)
        clock.tick(80)
        pygame.display.update()
def load_high_score_list(screen):
    a = open("erocs.axs", "r")
    lines = a.readlines()
    a.close()
    i = 100
    for line in lines:
        load_text(line, [0, 0, 255], 100, 1300, i, "BRITANIC.TTF", screen)
        i += 100
    load_text("level 1 :", [0, 0, 255], 100, 900, 100, "BRITANIC.TTF", screen)
    load_text("level 2 :", [0, 0, 255], 100, 900, 200, "BRITANIC.TTF", screen)
    load_text("level 3 :", [0, 0, 255], 100, 900, 300, "BRITANIC.TTF", screen)
    load_text("level EX:", [0, 0, 255], 100, 900, 400, "BRITANIC.TTF", screen)
    load_text("Press SPACE to back", [0, 0, 255], 100, 900, 500, "BRITANIC.TTF", screen)
def save_score(score,level):
    a = open("erocs.axs", "r")
    c = a.readlines()
    a.close()
    d = []
    for b in c:
        b = int(b)
        d.append(b)
    if d[level - 2] < score:
        d[level - 2] = score
        b = open("erocs.axs", "w")
        for e in d:
            e = str(e)
            e += "\n"
            b.write(e)
load_vedio("start.ascc")
while True:
    score = 0
    load_loading_screen(1)
    level = 1
    if level == 1:
        level,score = load_level(level, "sounds/bgm1.ogg",score)
        save_score(score,level)
    if level == 2:
        level,score = load_level(level, "sounds/bgm2.ogg",score)
        save_score(score,level)
    if level == 3:
        level,score = load_level(level, "sounds/bgm3.ogg",score)
        save_score(score,level)
    if level == 4:
        score = load_boss(level, "sounds/boss.ogg")
        save_score(score, level)
        level += 1
    load_vedio("ending.ascc")