import random
import pygame
pygame.init()

win_x = 1366
win_y = 768
win = pygame.display.set_mode((win_x, win_y))
pygame.display.set_caption("Archer vs Archer")
font = pygame.font.SysFont("comicsans", 25, True)
font1 = pygame.font.SysFont("comicsans", 50, True)
###load every image what I needed       green arrcher
walk_left = [pygame.image.load("L1.png"), pygame.image.load("L2.png"),
             pygame.image.load("L3.png"), pygame.image.load("L4.png"),
             pygame.image.load("L5.png"), pygame.image.load("L6.png"),
             pygame.image.load("L7.png"), pygame.image.load("L8.png")]
walk_right = [pygame.image.load("R1.png"), pygame.image.load("R2.png"),
              pygame.image.load("R3.png"), pygame.image.load("R4.png"),
              pygame.image.load("R5.png"), pygame.image.load("R6.png"),
              pygame.image.load("R7.png"), pygame.image.load("R8.png")]
shoot_left = [pygame.image.load("AL2.png"), pygame.image.load("AL3.png")]
shoot_right = [pygame.image.load("AR2.png"), pygame.image.load("AR3.png")]
############################### -red archer- ###########################
walk_left1 = [pygame.image.load("L21.png"), pygame.image.load("L22.png"),
              pygame.image.load("L23.png"), pygame.image.load("L24.png"),
              pygame.image.load("L25.png"), pygame.image.load("L26.png"),
              pygame.image.load("L27.png"), pygame.image.load("L28.png")]
walk_right1 = [pygame.image.load("R21.png"), pygame.image.load("R22.png"),
               pygame.image.load("R23.png"), pygame.image.load("R24.png"),
               pygame.image.load("R25.png"), pygame.image.load("R26.png"),
               pygame.image.load("R27.png"), pygame.image.load("R28.png")]
shoot_left1 = [pygame.image.load("AL22.png"), pygame.image.load("AL23.png")]
shoot_right1 = [pygame.image.load("AR22.png"), pygame.image.load("AR23.png")]
right_arrow = pygame.image.load("Arrow.png")
left_arrow = pygame.image.load("Arrow_L.png")
bg = pygame.image.load("bg.jpg")
m_plat = pygame.image.load("plat_m.png")
s_plat = pygame.image.load("plat_s.png")
bg1 = pygame.image.load("bg1.png")


class first_screen(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.play_b = False

    def screen(self, win):
        win.blit(bg1, (0, 0))
        # pygame.draw.rect(win, (255,0,0),(self.x,self.y,self.width,self.height))
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(x, y)
            if x >= 539 and x <= 795 and y >= 413 and y <= 530:
                self.play_b = True


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.left = False
        self.right = False
        self.isjump = True
        self.v = 8
        self.m = 2
        self.gravity = False
        self.walkCount = 0
        self.stand = True
        self.shooting = False
        self.walking = False
        self.shootCount = 0
        self.facing = 0
        self.platform = False
        self.visible = True
        self.shoot_s = 1
        self.alive = True
        self.health = 3
        self.death = False
        self.score = 0
        self.hitbox = (self.x + 48, self.y + 33, 35, 60)

    def draw(self, win):#-- in this function is code for walking and shooting (animation)
        if self.alive:
            if self.visible:
                if self.walking:
                    if self.walkCount + 1 >= 24:
                        self.walkCount = 0
                    if not (self.stand):
                        if self.left:
                            win.blit(walk_left[self.walkCount // 3], (self.x, self.y))
                            self.walkCount += 1
                        if self.right:
                            win.blit(walk_right[self.walkCount // 3], (self.x, self.y))
                            self.walkCount += 1
                    if self.stand == True:
                        if self.right:
                            win.blit(walk_right[0], (self.x, self.y))
                        else:
                            win.blit(walk_left[0], (self.x, self.y))
                else:
                    if self.right:
                        win.blit(walk_right[0], (self.x, self.y))
                    if self.left:
                        win.blit(walk_left[0], (self.x, self.y))

            if self.shooting and self.stand:
                if self.shootCount >= 16:
                    self.shootCount = 0
                if self.facing == -1:
                    win.blit(shoot_left[1], (self.x, self.y))
                if self.facing == 1:
                    win.blit(shoot_right[1], (self.x, self.y))
            self.hitbox = (self.x + 48, self.y + 33, 35, 60)
            #pygame.draw.rect(win, (0, 255, 0), self.hitbox, 2)
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 255, 0),
                             (self.hitbox[0], self.hitbox[1] - 20, 50 - ((50 / 3) * (3 - self.health)), 10))

    def hit(self):
        if self.health > 0:
            self.health -= 1
            self.death = False
        else:
            self.x = random.randint(200, win_x - 128 - 200)
            self.y = 600 - 96
            self.walkCount = 0
            self.death = True
            self.score += 1
            self.health = 3

        pygame.display.update()
        print("red hit")

    def fall_down(self, player_2):
        self.x = (random.randint(200, win_x - 128 - 200))
        self.y = 600 - 96
        self.death = True
        player_2.score -= 1
        self.health = 3
        self.x = self.x


class player_2(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.left = False
        self.right = False
        self.isjump = True
        self.v = 8
        self.m = 2
        self.gravity = False
        self.walkCount = 0
        self.stand = True
        self.shooting = False
        self.walking = False
        self.shootCount = 0
        self.facing = 0
        self.visible = True
        self.platform = False
        self.color = 0, 0, 200
        self.shoot_s = 1
        self.alive = True
        self.health = 3
        self.death = False
        self.score = 0
        self.hitbox = (self.x + 50, self.y + 37, 35, 60)

    def draw(self, win):
        if self.alive:
            if self.visible:
                if self.walkCount + 1 >= 24:
                    self.walkCount = 0
                if not (self.stand):
                    if self.right:
                        win.blit(walk_right1[self.walkCount // 3], (self.x, self.y))
                        self.walkCount += 1
                    if self.left:
                        win.blit(walk_left1[self.walkCount // 3], (self.x, self.y))
                        self.walkCount += 1
                else:
                    if self.right:
                        win.blit(walk_right1[0], (self.x, self.y))
                    if self.left:
                        win.blit(walk_left1[0], (self.x, self.y))
            if self.shooting and self.stand:
                if self.facing == -1:
                    win.blit(shoot_left1[1], (self.x, self.y))
                if self.facing == 1:
                    win.blit(shoot_right1[1], (self.x, self.y))
            self.hitbox = (self.x + 50, self.y + 37, 35, 60)
            #pygame.draw.rect(win, (0, 255, 0), self.hitbox, 2)
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 255, 0),
                             (self.hitbox[0], self.hitbox[1] - 20, 50 - ((50 / 3) * (3 - self.health)), 10))

    def hit(self):
        if self.health > 0:
            self.health -= 1
            self.death = False
        else:
            self.x = random.randint(200, win_x - 128 - 200)
            self.y = 600 - 96
            self.walkCount = 0
            self.death = True
            self.score += 1
            self.health = 3
        print("green hit")

    def fall_down(self, player):
        self.x = (random.randint(200, win_x - 128 - 200))
        self.y = 600 - 96
        self.death = True
        player.score -= 1
        self.health = 3
        self.x = self.x


class projectile(object):
    def __init__(self, x, y, width, height, facing):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.facing = facing
        self.vel = 16 * facing

    def draw(self, win):
        if self.facing == 1:
            self.facing = 1
            win.blit(right_arrow, (self.x, self.y))
        elif self.facing == -1:
            self.facing = -1
            win.blit(left_arrow, (self.x, self.y))


class main_platform(object):
    def __init__(self, x, y, ex, ey, color):
        self.x = x
        self.y = y
        self.ex = ex
        self.ey = ey
        self.color = color

    def draw(self, win):
        # pygame.draw.line(win,self.color,(self.x,self.y),(self.ex,self.ey))
        win.blit(m_plat, (0, 255))


class platform(object):
    def __init__(self, x, y, ex, ey, color):
        self.x = x
        self.y = y
        self.ex = ex
        self.ey = ey
        self.color = color


class platforms(object):
    def __init__(self):
        self.container = list([])

    def add(self, p):
        self.container.append(p)

    def collision_man(self, player, main_platform):
        for p in self.container:
            if player.y >= main_platform.y - 90 and player.x >= main_platform.x - 60 and player.x <= main_platform.ex - 50:
                player.y = main_platform.y - 90
                player.isjump = False
                player.v = 8
            if player.y == main_platform.y - 90 and player.x >= 0 and player.x <= main_platform.x - 60:
                player.y += 4 ** 2
            elif player.y == main_platform.y - 90 and player.x >= main_platform.ex - 25 and player.x <= win_x:
                player.y += 4 ** 2
            if player.y >= p.y - 100 and player.x >= p.x - 60 and player.x <= p.ex - 60:
                player.isjump = False
                player.v = 0
                player.y = p.y - 90
                if keys[pygame.K_UP]:
                    player.v = 8

    def gravity_man(self, player, main_platform):
        for p in self.container:
            if player.y >= main_platform.y - 90 and player.x >= main_platform.x - 60 and player.x <= main_platform.ex - 60:
                player.y = main_platform.y - 90
            elif player.y >= p.y - 100 and player.x >= p.x - 60 and player.x <= p.ex - 60:
                player.y = p.y - 90
            else:
                player.y += 4 ** 2

    def collision_woman(self, player_2, main_platform):
        for p in self.container:
            if player_2.y >= main_platform.y - 90 and player_2.x >= main_platform.x - 60 and player_2.x <= main_platform.ex - 60:
                player_2.y = main_platform.y - 90
                player_2.isjump = False
                player_2.v = 8
            if player_2.y == main_platform.y - 90 and player_2.x >= 0 and player_2.x <= main_platform.x - 60:
                player_2.y += 4 ** 2
            elif player_2.y == main_platform.y - 90 and player_2.x >= main_platform.ex - 60 and player_2.x <= win_x:
                player_2.y += 4 ** 2
            if player_2.y >= p.y - 100 and player_2.x >= p.x - 60 and player_2.x <= p.ex - 60:
                player_2.isjump = False
                player_2.v = 0
                player_2.y = p.y - 90
                if keys[pygame.K_w]:
                    player_2.v = 8

    def gravity_woman(self, player_2, main_platform):
        for p in self.container:
            if player_2.y >= main_platform.y - 90 and player_2.x >= main_platform.x - 60 and player_2.x <= main_platform.ex - 60:
                player_2.y = main_platform.y - 90
            elif player_2.y >= p.y - 100 and player_2.x >= p.x - 60 and player_2.x <= p.ex - 60:
                player_2.y = p.y - 90
            else:
                player_2.y += 4 ** 2

    def draw(self, win):
        # for p in self.container:
        #    pygame.draw.line(win,p.color,(p.x,p.y),(p.ex,p.ey))
        win.blit(s_plat, (-350, 65))
        win.blit(s_plat, (360, 80))


def resetButton(win, man, woman):
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        if x >= 1226 and x <= 1326 and y >= 15 and y <= 45:
            pygame.draw.rect(win, (255, 0, 0), (1226, 15, 100, 45))
            man.score = 0
            woman.score = 0
            man.health = 3
            woman.health = 3
            man.x = random.randint(200, win_x - 128 - 200)
            woman.x = random.randint(200, win_x - 128 - 200)


def redrawWin():
    menu.screen(win)
    if menu.play_b == True:
        win.blit(bg, (0, 0))
        resetButton(win, man, woman)
        msg = "RESET"
        text_reset = font.render(msg, True, (0, 0, 0))
        win.blit(text_reset, (1247, 30))
        text_r = font.render("Kills_Red: " + str(man.score), 1, (255, 0, 0))
        win.blit(text_r, (40, 10))
        text_g = font.render("Kills_Green: " + str(woman.score), 1, (0, 255, 2))
        win.blit(text_g, (40, 28))
        plat_s.draw(win)
        plat_m.draw(win)
        man.draw(win)
        woman.draw(win)
        for bullet in m_bullets:
            bullet.draw(win)
        for bullet in w_bullets:
            bullet.draw(win)
    pygame.display.update()


# mainloop
menu = first_screen(580, 424, 190, 75)
plat_m = main_platform(200, 600, win_x - 200, 600, (0, 150, 255))
plat_s = platforms()
plat_s.add(platform(200, win_y - 350, 450, win_y - 350, (0, 150, 255)))
plat_s.add(platform(win_x - 450, win_y - 350 + 32, win_x - 200, win_y - 350 + 32, (0, 150, 255)))
man = player(random.randint(200, win_x - 128 - 200), 600 - 96, 64, 64)
woman = player_2(random.randint(200, win_x - 128 - 200), 600 - 96, 64, 64)
m_bullets = []
w_bullets = []
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(80)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for m_bullet in m_bullets:#
        if m_bullet.y - m_bullet.height < woman.hitbox[1] and m_bullet.y + m_bullet.height > woman.hitbox[1]:
            if m_bullet.x + m_bullet.width > woman.hitbox[0] and m_bullet.x - m_bullet.width < woman.hitbox[0] - 87:#<-- if the bullet hit red archer
                woman.hit()
                m_bullets.pop(m_bullets.index(m_bullet))
        if m_bullet.x < win_x and m_bullet.x > 0:
            m_bullet.x += m_bullet.vel
        else:
            m_bullets.pop(m_bullets.index(m_bullet))
    for w_bullet in w_bullets:
        if w_bullet.y - w_bullet.height < man.hitbox[1] and w_bullet.y + w_bullet.height > man.hitbox[1]:
            if w_bullet.x + w_bullet.width > man.hitbox[0] and w_bullet.x - w_bullet.width < man.hitbox[0] - 87:#<-- if the bullet hit green archer
                man.hit()
                w_bullets.pop(w_bullets.index(w_bullet))
        if w_bullet.x < win_x and w_bullet.x > 0:
            w_bullet.x += w_bullet.vel
        else:
            w_bullets.pop(w_bullets.index(w_bullet))
    if man.y >= win_x - 96:
        man.fall_down(woman)
    if woman.y >= win_x - 96:
        woman.fall_down(man)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        man.shooting = True
        man.stand = True
        man.inTension = True
        man.visible = False
        man.shoot_s += 1
        redrawWin()

        if man.left:
            facing = -1
        else:
            facing = 1
        if len(m_bullets) < 8:
            if man.shoot_s == 2:
                m_bullets.append(projectile(round(man.x + man.width // 15),
                                            round(man.y + man.height // 13), 64, 64, facing))
    else:
        man.shooting = False
        man.shoot_s = 1
    if keys[pygame.K_LEFT] and man.x > 0:
        man.visible = True
        man.walking = True
        man.facing = -1
        man.x -= man.vel
        man.left = True
        man.right = False
        man.stand = False
        man.shooting = False
    if keys[pygame.K_RIGHT] and man.x < win_x - 128:
        man.visible = True
        man.walking = True
        man.facing = 1
        man.x += man.vel
        man.left = False
        man.right = True
        man.shooting = False
        man.stand = False
    if not (keys[pygame.K_SPACE]) and not (keys[pygame.K_LEFT]) and not (keys[pygame.K_RIGHT]):
        man.visible = True
        man.stand = True
        man.walking = False
        man.shooting = False
        man.walkCount = 0
    if man.isjump == False:
        plat_s.gravity_man(man, plat_m)

    if man.isjump == False:
        if keys[pygame.K_UP]:
            man.visible = True
            man.isjump = True

    else:
        if man.v > 0:
            F = (0.5 * man.m * (man.v * man.v))
        else:
            F = -(0.5 * man.m * (man.v * man.v))

        man.y -= F
        man.v -= 1

        plat_s.collision_man(man, plat_m)

    #################################################################################
    if keys[pygame.K_t]:
        woman.visible = False
        woman.shooting = True
        woman.stand = True
        woman.shoot_s += 1
        redrawWin()
        if woman.left:
            facing = -1
        else:
            facing = 1

        if len(w_bullets) < 7:
            if woman.shoot_s == 2:
                w_bullets.append(projectile(round(woman.x + woman.width // 15),
                                            round(woman.y + woman.height // 13), 64, 64, facing))
    else:
        woman.shooting = False
        woman.shoot_s = 1
    if keys[pygame.K_d] and woman.x < win_x - 128:
        woman.visible = True
        woman.walking = True
        woman.facing = 1
        woman.x += woman.vel
        woman.left = False
        woman.right = True
        woman.shooting = False
        woman.stand = False
    if keys[pygame.K_a] and woman.x > 0:
        woman.visible = True
        woman.walking = True
        woman.facing = -1
        woman.x -= woman.vel
        woman.left = True
        woman.right = False
        woman.shooting = False
        woman.stand = False
    if not (keys[pygame.K_t]) and not (keys[pygame.K_a]) and not (keys[pygame.K_d]):
        woman.visible = True
        woman.stand = True
        woman.walking = False
        woman.shooting = False
        woman.walkCount = 0
    if woman.isjump == False:
        plat_s.gravity_woman(woman, plat_m)
    if woman.isjump == False:
        if keys[pygame.K_w]:
            woman.visible = True
            woman.isjump = True

    else:
        if woman.v > 0:
            F = (0.5 * woman.m * (woman.v * woman.v))
        else:
            F = -(0.5 * woman.m * (woman.v * woman.v))

        woman.y -= F
        woman.v -= 1

        plat_s.collision_woman(woman, plat_m)

    redrawWin()

pygame.quit()
