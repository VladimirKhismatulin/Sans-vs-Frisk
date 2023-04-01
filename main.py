#pgzero
import random

WIDTH = 600
HEIGHT = 450

TITLE = "Sans vs frisk"
FPS = 30
blx = 0
wow = 0
bly = 0
dor_x = -50
maxstamina = 300
magic = 0
magical = 0
rest = 0
resting = 0
char = 0
number = 1
stamina = maxstamina
b_char = 2
blast_char = 8
d_char = 10
b_st = 10
blast_st = 10
d_st = 10
b_cd = "Кости готовы(лкм)"
b_cd1 = 0
blast_cd1 = 0
blast_cd = "Бластер готов(e)"
d_cd1 = d_char
d_cd = "Уворот через:" + str(d_cd1)
bl = "ready"
level = "Сложность: лёгкая"
diff = "white"
energy = "Выносливость: "
codetext = "Достижения - 3"
smin = 2
smax = 8
bosscount = 50
bossphase = 10
sans_assist = False
max_hp = 1
hp = 1
heal = 0
miss = Actor("Miss", (-100, -50))
boss = Actor("Weakdust", (300, -100))
miss.dorge = 0
Sans = Actor("HelpSoul", (300, 400))
Sans.hp = 3
soul = Actor("Soul", (300, 400))
sweat = Actor("Sweat")
soul1 = Actor("Soul1", (0, 0))
soul2 = Actor("Soul2", (0, 0))
fon = Actor("fon")
blaster = Actor("Blaster", (blx, bly))
enemies = []
bullets = [[], [], []]
dorges = []
attacks = []
achievments = []
souls = []
messages = []
dust = 0
det = 0
chara = 0
hyper = 0
achieve = [dust]
bosses = 0
base_attack1 = ["upknife", 5, 30]
base_attack2 = ["sideknife", 5, 30]
base_attack3 = ["slash", 10, 60]
base_attack4 = ["slashforward", 5, 30]
base_attack5 = ["knifes", 4, 20]
base_attack = [base_attack1, base_attack2, base_attack3, base_attack4, base_attack5]
mode = 'menu'
codemode = 1
gamemode = "boss"
notover = "GAME OVER"
modeboss = False
count = 0
blast = 0
dorge = 0
coins = 100
bonus = 0
inv = 0
kill = 0
enx = 570
eny = 175
a = 0
boost = 0
lifetime = 120
cutscene = 0
speed = 5
ghost = 0
ghost_hp = 6
blink = 0
Blink = Actor("Blink")
SlashAnim = ["SlashAnim1", "SlashAnim2", "SlashAnim3", "SlashAnim4", "SlashAnim5", "SlashAnim6", "SlashAnim7"]
Block = []
dialogs = []
weapons = []
so = []
repeat = 0
attackbuff = 0
b_repeat = 0
special = 0
charge = 0
bruh = 0
chance = 0
guide = 0
clickguide = 0
password = ["-", "-", "-", "-"]
hyperboost = ["?????????(?? монет)", 
              "Остановись(?? монет)", 
              "Пожалуйста(?? монет)", 
              "Пока не поздно(?? монет)", 
              "Он придёт за ними, потом за тобой.", 
              "И ты ничего не сможешь сделать.", 
              "Прошу, не надо...", 
              "Это того не стоит.", 
              "Одумайся.", 
              "Это твой последний шанс.", 
              "..."]
cod = " "
HYPER = False
atkmode = False
shield = False
speedboost = False
stamboost = False
cdboost = False
bossrush = False
enraged = False
charging = False
def bone_cd():
    global b_cd
    global b_cd1
    if b_cd1 > 0:
        b_cd1 -= 0.1
        if b_cd1 <= 0:
            if char == "dust" and atkmode == False:
                b_cd = "Нож готов(лкм)"
            elif char == "frisk":
                b_cd = "Атака(лкм)"
            else:
                b_cd = "Кости готовы(лкм)"
        else:
            if char == "dust" and atkmode == False:
                b_cd = "Нож через:" + str(b_cd1)
            elif char == "frisk":
                b_cd = "Атака через:" + str(b_cd1)
            else:
                b_cd = "Кости через:" + str(b_cd1)
schedule_interval(bone_cd, 0.1)
def blaster_cd():
    global blast_cd
    global blast_cd1
    global modeboss
    if blast_cd1 > 0:
        blast_cd1 -= 0.1
        if blast_cd1 <= 0:
            if char == "dust" and atkmode == False:
                blast_cd = "Кости готовы(e)"
            elif char == "uspaps":
                blast_cd = "Тако (e)"
            elif char == "frisk":
                if attackbuff <= 0:
                    blast_cd = "Особая атака(e)"
                else:
                    blast_cd = "+ Скорость атаки!"
            else:
                blast_cd = "Бластер готов(e)"
            if modeboss == True:
                modeboss = False
                for i in range(5):
                    new_enemy()
        elif modeboss == False:
            if char == "dust" and atkmode == False:
                blast_cd = "Кости через:" + str(blast_cd1)
            elif char == "uspaps" or char == "frisk":
                blast_cd = "Перезарядка:" + str(blast_cd1)
            else:
                blast_cd = "Бластер через:" + str(blast_cd1)
def text_last():
    global miss
    global Block
    if miss.dorge > 0:
        miss.dorge -= 0.1
    else:
        Block = []
schedule_interval(text_last, 0.1)
schedule_interval(blaster_cd, 0.1)
def dorge_cd():
    global d_cd
    global d_cd1
    global heal
    if d_cd1 > 0:
        d_cd1 -= 0.1
        if d_cd1 <= 0:
            if char == "sans" or (char == "dust" and atkmode == False) or char == "snowdust":
                d_cd = "Уворот готов(space + a или d)"
            elif char == "uspaps":
                d_cd = "Блок готов(пробел)"
            elif char == "frisk":
                heal += 1
                healing(1)
            elif atkmode:
                d_cd = "Синяя душа готова(пробел)"
            elif char == "dtsans":
                d_cd = "Отталкивание готово(пробел)"
        else:
            if char == "sans" or (char == "dust" and atkmode == False) or char == "snowdust":
                d_cd = "Уворот через:" + str(d_cd1)
            elif char == "uspaps":
                d_cd = "Блок через:" + str(d_cd1)
            elif char == "frisk":
                heal += 1
                healing(1)
            elif atkmode:
                d_cd = "Синяя душа через:" + str(d_cd1)
            elif char == "dtsans":
                d_cd = "Отталкивание через:" + str(d_cd1)
schedule_interval(dorge_cd, 0.1)
def blast_last():
    global blast
    if blast > 0:
        blast -= 0.1
def energyrest():
    global stamina
    global resting
    global rest
    global dt
    if keyboard.w or keyboard.a or keyboard.s or keyboard.d:
        resting -= 0.1
        if resting < 0:
            resting = 0
    else:
        resting += 0.02
        if resting > 7:
            resting = 7
    rest += 0.5 + resting
    if char == "uspaps":
        rest += 0.1 * (magic // 10)
    if stamina < 0:
        rest -= 0.5 + resting / 2
    if hp == 0.1:
        rest -= 7 - 2 * det
    while True:
        if rest >= 30:
            rest -= 30
            stamina += 1
        if rest <= -30:
            rest += 30
            stamina -= 1
            if stamina < 0:
                dmg()
        else:
            break
    if stamina > max_stamina:
        stamina = max_stamina
def Magic(mag):
    global magic
    magic += mag
    if magic > 300:
        magic = 300
    if magic < 0:
        magic = 0
def magic_gain():
    global magical
    magical += 0.3
    if sans_assist:
        magical += 1
    while True:
        if magical >= 30:
            magical -= 30
            Magic(1)
        else:
            break
schedule_interval(energyrest, 1)
def evade():
    global inv
    if inv > 0:
        inv -= 0.1
def atkblink():
    global blink
    global attacks
    global mode
    if blink > 0:
        blink -= 1
        if blink <= 0:
            if Blink.image == "Blink":
                if bossphase == 3:
                    attacks = []
                    soul.pos = (300, 300)
            if Blink.image == "999999":
                mode = "end"
schedule_interval(evade, 0.1)
def bosstime():
    global bosses
    global b_cd
    global attacks
    global bullets
    global b_cd
    global b_cd1
    global blast_cd
    global blast_cd1
    global enemies
    global modeboss
    global bossphase
    global boss
    global attacking
    if bosses == 0:
        if dust >= 3:
            buff = random.randint(1, 1)
            if buff == 1:
                boss = Actor("Snowdindust", (300, -100))
                boss.dorge = 4
                boss.block = 0
                boss.hp = 2
                attacking = ["dustblasters", "dustpuzzle", "confusejump"]
                blast_cd = "..."
            else:
                boss = Actor("Weakdust", (300, -100))
                boss.dorge = 5
                boss.block = 0
                boss.hp = 1
                attacking = ["dustspindown", "dustspinleft", "bonejump"]
                blast_cd = "Текущий босс - Dusttale Санс"
        else:
            boss = Actor("Weakdust", (300, -100))
            boss.dorge = 5
            boss.block = 0
            boss.hp = 1
            attacking = ["dustspindown", "dustspinleft", "bonejump"]
            blast_cd = "Текущий босс - Dusttale Санс"
    elif bosses == 1:
        boss = Actor("Soul", (300, -100))
        boss.dorge = 2
        boss.block = 0
        boss.hp = 1
        attacking = ["bonerush", "sidejump", "blasters"]
        blast_cd = "Текущий босс - Санс?"
    blast_cd1 = -1
    modeboss = True
    boss.speed = 5
    enemies = []
    bullets = [[], [], []]
    enemies.append(boss)
    b_cd1 = -1
    b_cd = "..."
    bossphase = 0
def counting(numder):
    global count
    global bosscount
    global stamina
    global lv
    global exp
    global exp_cap
    global maxstamina
    global max_stamina
    global lifetime
    global b_char
    global heal
    global hp
    global max_hp
    global special
    global weapon
    global weapons
    count += number
    if char == "dust":
        stamina += number * 2
        exp += number
        if exp >= exp_cap:
            exp -= exp_cap
            if dust > lv and lv < 5:
                lv += 1
                lifetime += 10
                b_char -= 0.2
                if stamboost:
                    max_stamina += 6
                    maxstamina += 6
                else:
                    max_stamina += 5
                    maxstamina += 5
                exp_cap = (lv + 1) * 5
                if lv == 5:
                    max_hp += 1
                    hp += 1
                if dust == lv or lv == 5:
                    exp_cap = 10
            else:
                stamina += 4 + lv * 2
                heal += 1
                if heal >= 4:
                    heal -= 4
                    hp += 1
                    if hp > max_hp:
                        hp = max_hp
    elif char == "frisk":
        exp += number
        if exp >= exp_cap:
            exp -= exp_cap
            if chara * 2 > lv:
                lv += 1
                #if weapon == "knife" or weapon == "stick":
                b_char -= 0.1
                exp_cap = (lv + 1) * 5
                if lv == 3:
                    max_hp += 1
                    weapon = "knife"
                    weapons.append("knife")
                    if cdboost:
                        b_char = 1.6
                    else:
                        b_char = 2
                elif lv == 6:
                    max_hp += 1
                    weapon = "glove"
                    weapons.append("glove")
                    if cdboost:
                        b_char = 1.2
                    else:
                        b_char = 1.5
                if chara * 2 == lv:
                    exp_cap = 0
    if char == "snowdust":
        stamina += number
        exp += number
        special += 1
        if exp >= exp_cap:
            exp -= exp_cap
            if dust > lv and lv < 9:
                lv += 1
                if stamboost:
                    max_stamina += 6
                    maxstamina += 6
                else:
                    max_stamina += 5
                    maxstamina += 5
                exp_cap = (lv + 1) * 5
                if lv == 9:
                    max_hp += 1
                    hp + 1
                if dust == lv or lv == 9:
                    exp_cap = 10
            else:
                stamina += lv * 2
                heal += 1
                if heal >= 4:
                    heal -= 4
                    hp += 1
                    if hp > max_hp:
                        hp = max_hp
    if count == bosscount and HYPER == False and gamemode == "boss":
        bosstime()
def boss_atk():
    global bossphase
    global b_cd1
    global d_cd1
    global blink
    global repeat
    global attack
    if blink <= 0:
        for i in range(len(attacks)):
            if attacks[i].types == "spinbone":
                if attacks[i].direct == "left":
                    attacks[i].x -= attacks[i].speed
                    attacks[i].angle -= attacks[i].speed * 2
                    if attacks[i].x < attacks[i].dis:
                        attacks.pop(i)
                        if bossphase == 2 and len(attacks) == 0:
                            b_cd1 = 0.1
                            bossphase = 3
                            if char == "dust":
                                soul.image = "Weakdust"
                            elif char == "snowdust":
                                soul.image = "Snowdindust"
                            elif char == "frisk":
                                soul.image = "FriskChar"
                                soul.angle = 0
                            else:
                                soul.image = "Soul"
                        break
                elif attacks[i].direct == "right":
                    attacks[i].x += attacks[i].speed
                    attacks[i].angle += attacks[i].speed * 2
                    if attacks[i].x > attacks[i].dis:
                        attacks.pop(i)
                        if bossphase == 2 and len(attacks) == 0:
                            b_cd1 = 0.1
                            bossphase = 3
                            if char == "dust":
                                soul.image = "Weakdust"
                            elif char == "snowdust":
                                soul.image = "Snowdindust"
                            elif char == "frisk":
                                soul.image = "FriskChar"
                                soul.angle = 0
                            else:
                                soul.image = "Soul"
                        break
                elif attacks[i].direct == "up":
                    attacks[i].y -= attacks[i].speed
                    attacks[i].angle -= attacks[i].speed * 2
                    if attacks[i].y < attacks[i].dis:
                        attacks.pop(i)
                        if bossphase == 2 and len(attacks) == 0:
                            b_cd1 = 0.1
                            bossphase = 3
                            if char == "dust":
                                soul.image = "Weakdust"
                            elif char == "snowdust":
                                soul.image = "Snowdindust"
                            elif char == "frisk":
                                soul.image = "FriskChar"
                                soul.angle = 0
                            else:
                                soul.image = "Soul"
                        break
                elif attacks[i].direct == "down":
                    attacks[i].y += attacks[i].speed
                    attacks[i].angle += attacks[i].speed * 2
                    if attacks[i].y > attacks[i].dis:
                        attacks.pop(i)
                        if bossphase == 2 and len(attacks) == 0:
                            b_cd1 = 0.1
                            bossphase = 3
                            if char == "dust":
                                soul.image = "Weakdust"
                            elif char == "snowdust":
                                soul.image = "Snowdindust"
                            elif char == "frisk":
                                soul.image = "FriskChar"
                                soul.angle = 0
                            else:
                                soul.image = "Soul"
                        break
            elif attacks[i].types == "sidebone" or attacks[i].types == "bluebone":
                if attacks[i].direct == "left":
                    attacks[i].x -= attacks[i].speed
                    if attacks[i].x < attacks[i].dis:
                        attacks.pop(i)
                        if bossphase == 2 and len(attacks) == 0:
                            b_cd1 = 0.1
                            bossphase = 3
                            if char == "dust":
                                soul.image = "Weakdust"
                            elif char == "snowdust":
                                soul.image = "Snowdindust"
                            elif char == "frisk":
                                soul.image = "FriskChar"
                                soul.angle = 0
                            else:
                                soul.image = "Soul"
                        break
                if attacks[i].direct == "right":
                    attacks[i].x += attacks[i].speed
                    if attacks[i].x > attacks[i].dis:
                        attacks.pop(i)
                        if bossphase == 2 and len(attacks) == 0:
                            b_cd1 = 0.1
                            bossphase = 3
                            if char == "dust":
                                soul.image = "Weakdust"
                            elif char == "snowdust":
                                soul.image = "Snowdindust"
                            elif char == "frisk":
                                soul.image = "FriskChar"
                                soul.angle = 0
                            else:
                                soul.image = "Soul"
                        break
            elif attacks[i].types == "bonerush" or attacks[i].types == "bluebonerush":
                if attacks[i].direct == "up":
                    if attacks[i].image == "Dustsidebone" and attacks[i].y <= 450:
                        attacks[i].y -= attacks[i].speeed
                    else:
                        attacks[i].y -= attacks[i].speed
                    if attacks[i].y < attacks[i].dis:
                        if attacks[i].image == "HyperBoneUp":
                            repeat -= 1
                            if repeat > 0:
                                attacks[i].y += 550
                                attacks[i].x = random.randint(50, 550)
                            else:
                                attacks.pop(i)
                        else:
                            attacks.pop(i)
                        if bossphase == 2 and len(attacks) == 0:
                            b_cd1 = 0.1
                            bossphase = 3
                            if char == "dust":
                                soul.image = "Weakdust"
                            elif char == "snowdust":
                                soul.image = "Snowdindust"
                            elif char == "frisk":
                                soul.image = "FriskChar"
                                soul.angle = 0
                            elif char != "paps":
                                soul.image = "Soul"
                        break
                elif attacks[i].direct == "down":
                    if attacks[i].image == "Dustsidebone" and attacks[i].y >= 0:
                        attacks[i].y += attacks[i].speeed
                    else:
                        attacks[i].y += attacks[i].speed
                    if attacks[i].y > attacks[i].dis:
                        if attacks[i].image == "HyperBoneUp":
                            repeat -= 1
                            if repeat > 0:
                                attacks[i].y -= 550
                                attacks[i].x = random.randint(50, 550)
                            else:
                                attacks.pop(i)
                        else:
                            attacks.pop(i)
                        if bossphase == 2 and len(attacks) == 0:
                            b_cd1 = 0.1
                            bossphase = 3
                            if char == "dust":
                                soul.image = "Weakdust"
                            elif char == "snowdust":
                                soul.image = "Snowdindust"
                            elif char == "frisk":
                                soul.image = "FriskChar"
                                soul.angle = 0
                            elif char != "paps":
                                soul.image = "Soul"
                        break
                elif attacks[i].direct == "left":
                    attacks[i].x -= attacks[i].speed
                    if attacks[i].x < attacks[i].dis:
                        if attacks[i].image == "HyperBoneLeft":
                            repeat -= 1
                            if repeat > 0:
                                attacks[i].x += 700
                                attacks[i].y = random.randint(50, 400)
                            else:
                                attacks.pop(i)
                        elif attacks[i].image == "HyperSideBone":
                            repeat -= 1
                            if repeat > 0:
                                attacks[i].x += 1200
                                if repeat == 6 or repeat == 4 or repeat == 2:
                                    atk = Actor("BlasterWarn1", (soul.x, 225))
                                    atk.w0 = 0
                                    atk.w1 = 25
                                    atk.blast = 17
                                    atk.types = "blaster"
                                    attacks.append(atk)
                            else:
                                attacks.pop(i)
                        else:
                            attacks.pop(i)
                        if bossphase == 2 and len(attacks) == 0:
                            b_cd1 = 0.1
                            bossphase = 3
                            if char == "dust":
                                soul.image = "Weakdust"
                            elif char == "snowdust":
                                soul.image = "Snowdindust"
                            elif char == "frisk":
                                soul.image = "FriskChar"
                                soul.angle = 0
                            elif char != "paps":
                                soul.image = "Soul"
                        break
                elif attacks[i].direct == "right":
                    attacks[i].x += attacks[i].speed
                    if attacks[i].x > attacks[i].dis:
                        if attacks[i].image == "HyperBoneLeft":
                            repeat -= 1
                            if repeat > 0:
                                attacks[i].x -= 700
                                attacks[i].y = random.randint(50, 400)
                            else:
                                attacks.pop(i)
                                if attack == "hyperbonerush":
                                    blink = 10
                                    b_cd1 = 0.1
                                    bossphase = 3
                        elif attacks[i].image == "HyperSideBone":
                            repeat -= 1
                            if repeat > 0:
                                attacks[i].x -= 1200
                                if repeat == 6 or repeat == 4 or repeat == 2:
                                    atk = Actor("BlasterWarn1", (soul.x, 225))
                                    atk.w0 = 0
                                    atk.w1 = 25
                                    atk.blast = 17
                                    atk.types = "blaster"
                                    attacks.append(atk)
                            else:
                                attacks.pop(i)
                        else:
                            attacks.pop(i)
                        if bossphase == 2 and len(attacks) == 0:
                            b_cd1 = 0.1
                            bossphase = 3
                            if char == "dust":
                                soul.image = "Weakdust"
                            elif char == "snowdust":
                                soul.image = "Snowdindust"
                            elif char == "frisk":
                                soul.image = "FriskChar"
                                soul.angle = 0
                            elif char != "paps":
                                soul.image = "Soul"
                        break
            elif attacks[i].types == "puzzle" or attacks[i].types == "bluepuzzle":
                if attacks[i].direct == "up":
                    attacks[i].y -= attacks[i].speed
                    if attacks[i].y <= attacks[i].dis:
                        attacks[i].direct = "down"
                        attacks[i].dis = 450 - attacks[i].dis
                        if bossphase == 2 and soul.x >= 550:
                            blink = 10
                            b_cd1 = 0.1
                            d_cd1 = 0.1
                            bossphase = 3
                        break
                elif attacks[i].direct == "down":
                    attacks[i].y += attacks[i].speed
                    if attacks[i].y >= attacks[i].dis:
                        attacks[i].direct = "up"
                        attacks[i].dis = 450 - attacks[i].dis
                        if bossphase == 2 and soul.x >= 550:
                            blink = 10
                            b_cd1 = 0.1
                            d_cd1 = 0.1
                            bossphase = 3
                        break
            elif attacks[i].types == "blaster" or attacks[i].types == "slash":
                if attacks[i].w0 > 0:
                    attacks[i].w0 -= 1
                    attacks[i].image = "BlasterWarn0"
                    if attacks[i].w0 <= 0:
                        attacks[i].image = "BlasterWarn1"
                elif attacks[i].w1 > 0:
                    attacks[i].w1 -= 1
                    if attacks[i].types == "slash":
                        if (attacks[i].w1 % 4) == 0 and attacks[i].image == "SlashWarn1":
                            attacks[i].image = "SlashWarn2"
                        elif (attacks[i].w1 % 4) == 0 and attacks[i].image == "SlashWarn2":
                            attacks[i].image = "SlashWarn1"
                    else:
                        if (attacks[i].w1 % 4) == 0 and attacks[i].image == "BlasterWarn1":
                            attacks[i].image = "BlasterWarn2"
                        elif (attacks[i].w1 % 4) == 0 and attacks[i].image == "BlasterWarn2":
                            attacks[i].image = "BlasterWarn1"
                    if attacks[i].w1 <= 0:
                        if boss.image == "HYPER":
                            attacks[i].image = "HyperBlast"
                        elif attacks[i].types == "slash":
                            attacks[i].image = "SlashBlast"
                        elif enemies[0].image == "SSChara":
                            attacks[i].image = "SSblast"
                        else:
                            attacks[i].image = "Blaster"
                else:
                    attacks[i].blast -= 1
                    if attacks[i].blast <= 0:
                        if attack == "dustblasters" and repeat > 0:
                            attacks[i].x = random.randint(50, 550)
                            attacks[i].w0 = 30
                            if level == "Сложность: средняя":
                                attacks[i].w0 -= 5
                            elif level == "Сложность: сложная":
                                attacks[i].w0 -= 10
                            attacks[i].w1 = 30
                            attacks[i].blast = 15
                            if level == "Сложность: средняя":
                                attacks[i].blast += 5
                            elif level == "Сложность: сложная":
                                attacks[i].blast += 10
                            attacks[i].image = "BlasterWarn0"
                            repeat -= 1
                        else:
                            attacks.pop(i)
                            if bossphase == 2 and len(attacks) == 0:
                                b_cd1 = 0.1
                                bossphase = 3
                                if char == "dust":
                                    soul.image = "Weakdust"
                                elif char == "snowdust":
                                    soul.image = "Snowdindust"
                                elif char == "frisk":
                                    soul.image = "FriskChar"
                                    soul.angle = 0
                                else:
                                    soul.image = "Soul"
                            break
            elif attacks[i].types == "hit":
                attacks[i].count += 1
                if attacks[i].count <= 6:
                    attacks[i].image = SlashAnim[attacks[i].count]
                else:
                    if soul.colliderect(attacks[i]):
                        Blink.image = "999999"
                        blink = 45
                    attacks.pop(i)
                    break
def message():
    for i in range(len(messages)):
        if messages != True:
            messages[i][3] -= 1
            if messages[i][3] <= 0:
                messages.pop(i)
def draw():
    fon.draw()
    if mode == 'game':
        soul.draw()
        if stamina < 0:
            sweat.pos = soul.pos
            sweat.draw()
        for i in range(len(attacks)):
            attacks[i].draw()
        for i in range(len(enemies)):
            enemies[i].draw()
            if enemies[i] != boss:
                if enemies[i].charge > 0:
                    screen.draw.text("!", center = (enemies[i].x, enemies[i]. y - 3), color = "yellow", fontsize = 50)
                elif enemies[i].maxhp > 1 and enemies[i].dodge == False:
                    screen.draw.text(enemies[i].hp, center = (enemies[i].x, enemies[i]. y - 3), color = "white", fontsize = 30)
        for i in range(len(messages)):
            screen.draw.text(messages[i][0], center = messages[i][1], color = messages[i][2], fontsize = 20)
        if blast > 0:
            blaster.draw()
        for i in range(len(bullets[0])):
            bullets[0][i].draw()
        for i in range(len(bullets[1])):
            bullets[1][i].draw()
        for i in range(len(bullets[2])):
            bullets[2][i].draw()
        for i in range(len(Block)):
            Block[i].draw()
        if charging:
            screen.draw.text("Подготовка...", center = (soul.x, soul.y - 40), color = "white", fontsize = 20)
        screen.draw.text(count, (40, 25), color = "white", fontsize = 20)
        screen.draw.text(b_cd, (40, 55), color = "white", fontsize = 20)
        if char == "uspaps" and sans_assist == False and modeboss == False:
            screen.draw.text("Нужен Санс", (40, 105), color = "white", fontsize = 20)
        else:
            screen.draw.text(blast_cd, (40, 105), color = "white", fontsize = 20)
        screen.draw.text(d_cd, (40, 155), color = "white", fontsize = 20)
        if modeboss:
            screen.draw.text("Хп:" + str(boss.hp), (350, 55), color = "white", fontsize = 20)
            if cutscene != 0 and len(dialogs) != 0:
                screen.draw.text(dialogs[0], center = (300, 120), color = "white", fontsize = 20)
        if miss.dorge >= 0:
            miss.draw()
        if char == "dust":
            screen.draw.text("Смена атак - Q", (40, 205), color = "white", fontsize = 20)
            screen.draw.text("Ур: " + str(lv) + " (" + str(exp) + "/" + str(exp_cap) + ")", (40, 390), color = "white", fontsize = 20)
        elif char == "snowdust":
            if special >= 50:
                screen.draw.text("Специальная атака - Q", (40, 205), color = "white", fontsize = 20)
            else:
                screen.draw.text("(" + str(special) + "/50)", (40, 205), color = "white", fontsize = 20)
            screen.draw.text("Ур: " + str(lv) + " (" + str(exp) + "/" + str(exp_cap) + ")", (40, 390), color = "white", fontsize = 20)
            if inv > 0 and kill == 1:
                if len(so) == 5:
                    soul2.draw()
                elif len(so) >= 3:
                    soul1.draw()
        elif char == "frisk":
            screen.draw.text("Смена оружия - Q", (40, 205), color = "white", fontsize = 20)
            if weapon == "stick":
                screen.draw.text("Оружие - палка", (40, 235), color = "white", fontsize = 20)
            elif weapon == "knife":
                screen.draw.text("Оружие - игр. нож", (40, 235), color = "white", fontsize = 20)
            elif weapon == "glove":
                screen.draw.text("Оружие - перчатки", (40, 235), color = "white", fontsize = 20)
            if exp_cap > 0:
                screen.draw.text("Ур: " + str(lv) + " (" + str(exp) + "/" + str(exp_cap) + ")", (40, 390), color = "white", fontsize = 20)
            else:
                screen.draw.text("Ур: " + str(lv) + " (макс.)", (40, 390), color = "white", fontsize = 20)
        elif char == "uspaps":
            if sans_assist:
                screen.draw.text("Активно", (40, 205), color = "white", fontsize = 20)
            elif Sans.hp == 0:
                screen.draw.text("Убит", (40, 205), color = "white", fontsize = 20)
            elif blast_cd1 <= 0:
                screen.draw.text("Помощь Санса - Q", (40, 205), color = "white", fontsize = 20)
            else:
                screen.draw.text("Отдых: " + str(blast_cd1), (40, 205), color = "white", fontsize = 20)
            screen.draw.text("Магия: " + str(magic), (40, 390), color = "white", fontsize = 20)
        if maxstamina > 0:
            screen.draw.text(energy, (400, 425), color = "white", fontsize = 20)
            if char != "dtsans":
                screen.draw.text(stamina, (560, 425), color = "white", fontsize = 20)
            else:
                screen.draw.text("∞", (560, 425), color = "white", fontsize = 20)
        if sans_assist and modeboss == False:
            Sans.draw()
        if shield:
            screen.draw.text("Хп: (" + str(hp) + "/" + str(max_hp) + ")", (490, 390), color = "white", fontsize = 20)
        else:
            screen.draw.text("Хп: " + str(hp) + "/" + str(max_hp), (500, 390), color = "white", fontsize = 20)
        if blink > 0:
            Blink.draw()
    elif mode == 'end':
        screen.draw.text("GAME OVER!", center = (300, 200), color = "white", fontsize = 36)
        screen.draw.text("(Нажмите 1 для рестарта)", center = (300, 235), color = "white", fontsize = 20)
        screen.draw.text(count, (40, 25), color = "white", fontsize = 20)
        screen.draw.text("+ " + str(bonus) + " монет!", center = (300, 150), color = "white", fontsize = 30)
        for i in range(len(achievments)):
            screen.draw.text(achievments[i], (35, 260 + i * 30), color = "white", fontsize = 20)
    elif mode == 'fakeend':
        screen.draw.text("+ 0 монет!", center = (300, 160), color = "white", fontsize = 30)
        screen.draw.text(notover, center = (300, 200), color = "white", fontsize = 36)
        screen.draw.text("(Нажмите 1, чтобы продолжить)", center = (300, 235), color = "white", fontsize = 20)
    elif mode == 'yourend':
        screen.draw.text("Конец, навсегда.", center = (300, 200), color = "white", fontsize = 36)
    elif mode == 'menu' or mode == "menu?":
        screen.draw.text("Персонажи - 1", center = (300, 100), color = "white", fontsize = 40)
        screen.draw.text("Усиления - 2", center = (300, 200), color = "white", fontsize = 40)
        screen.draw.text(codetext, center = (300, 300), color = "white", fontsize = 40)
        if clickguide == 1:
            screen.draw.text("Нажми символ после тире, чтобы сделать это действие.", center = (300, 50), color = "white", fontsize = 20)
            screen.draw.text("Тебе будет нужна мышь только в самой игре.", center = (300, 375), color = "white", fontsize = 20)
        elif guide == 1:
            screen.draw.text("Нажми символ после тире, чтобы сделать это действие.", center = (300, 50), color = "white", fontsize = 20)
    elif mode == "char" or mode == "char?":
        screen.draw.text("Ut!Санс - 1", (40, 45), color = "white", fontsize = 20)
        screen.draw.text("Us!Папирус - 2", (40, 90), color = "white", fontsize = 20)
        if dust == 0:
            screen.draw.text("Dt!Санс - победите Dusttale Санса", (40, 135), color = "white", fontsize = 20)
        else:
            screen.draw.text("Dt!Санс - 3", (40, 135), color = "white", fontsize = 20)
        if chara == 0:
            screen.draw.text("Фриск - победите минибосса", (40, 180), color = "white", fontsize = 20)
        else:
            screen.draw.text("Фриск - 4", (40, 180), color = "white", fontsize = 20)
        screen.draw.text(level, (300, 250), color = diff, fontsize = 20)
        if mode == "char":
            screen.draw.text("Менять сложность - d", (300, 300), color = "white", fontsize = 20)
            screen.draw.text("Режимы - a", (40, 300), color = "white", fontsize = 20)
            if gamemode == "boss":
                screen.draw.text("Режим игры - боссы", (40, 250), color = "white", fontsize = 20)
            if gamemode == "enemy":
                screen.draw.text("Режим игры - противники", (40, 250), color = "white", fontsize = 20)
            if gamemode == "none":
                screen.draw.text("Режим игры - свободный", (40, 250), color = "white", fontsize = 20)
        screen.draw.text("Назад - 5", (40, 370), color = "white", fontsize = 20)
    elif mode == "gamemode":
        if gamemode == "boss":
            screen.draw.text("Режим боссов.", (40, 50), color = "white", fontsize = 20)
            screen.draw.text("В режиме с боссами на определённом количестве очков", (40, 80), color = "white", fontsize = 20)
            screen.draw.text("появляется босс, которого надо победить.", (40, 110), color = "white", fontsize = 20)
            screen.draw.text("Боссы дают различные награды за победу над ними.", (40, 140), color = "white", fontsize = 20)
            screen.draw.text("Коды помогут вернуть прогресс достижений.", (40, 170), color = "white", fontsize = 20)
            screen.draw.text("Этот режим хорош для проверки своих сил", (40, 200), color = "white", fontsize = 20)
            screen.draw.text("и получения новых персонажей.", (40, 230), color = "white", fontsize = 20)
        if gamemode == "enemy":
            screen.draw.text("Режим особых противников.", (40, 50), color = "white", fontsize = 20)
            screen.draw.text("В этом режиме противники с шансом преображаются.", (40, 80), color = "white", fontsize = 20)
            screen.draw.text("Они малоизучены и вы сможете их изучить сами.", (40, 110), color = "white", fontsize = 20)
            screen.draw.text("Некоторые из них требуют особого к ним подхода,", (40, 140), color = "white", fontsize = 20)
            screen.draw.text("который вы вправе выработать самостоятельно.", (40, 170), color = "white", fontsize = 20)
            screen.draw.text("Этот режим неизведан и таинственнен,", (40, 200), color = "white", fontsize = 20)
            screen.draw.text("так что играйте в него на свой страх и риск!.", (40, 230), color = "white", fontsize = 20)
        if gamemode == "none":
            screen.draw.text("Свободый режим. Ничего особенного.", (40, 50), color = "white", fontsize = 20)
            screen.draw.text("Мало, что можно про него сказать.", (40, 80), color = "white", fontsize = 20)
            screen.draw.text("Обычные противники, ничем не сменяемые.", (40, 110), color = "white", fontsize = 20)
            screen.draw.text("Идеальный режим для теста персонажей", (40, 140), color = "white", fontsize = 20)
            screen.draw.text("и бысрого накопления монет.", (40, 170), color = "white", fontsize = 20)
        screen.draw.text("Другой режим - a/d", (40, 300), color = "white", fontsize = 20)
        screen.draw.text("Выбрать - 1", (40, 350), color = "white", fontsize = 20)
    elif mode == "boost":
        screen.draw.text("Монеты: " + str(coins), (350, 250), color = "white", fontsize = 20)
        if shield:
            screen.draw.text("Щит включён!", (40, 50), color = "yellow", fontsize = 20)
        elif boost <= 1:
            screen.draw.text("Щит(10 монет) - 1", (40, 50), color = "white", fontsize = 20)
        if speedboost:
            screen.draw.text("Скорость повышена!", (40, 100), color = "yellow", fontsize = 20)
        elif boost <= 1:
            screen.draw.text("Усиление скорости(5 монет) - 2", (40, 100), color = "white", fontsize = 20)
        if stamboost:
            screen.draw.text("Больше выносливости!", (40, 150), color = "yellow", fontsize = 20)
        elif boost <= 1:
            screen.draw.text("Усиление выносливости(7 монет) - 3", (40, 150), color = "white", fontsize = 20)
        if cdboost:
            screen.draw.text("Уменьшение перезарядки!", (40, 200), color = "yellow", fontsize = 20)
        elif boost <= 1:
            screen.draw.text("Меньше перезарядка(7 монет) - 4", (40, 200), color = "white", fontsize = 20)
        if bossrush:
            screen.draw.text("Ранний босс!", (40, 250), color = "yellow", fontsize = 20)
        elif boost <= 1:
            screen.draw.text("Босс пораньше(10 монет) - 5", (40, 250), color = "white", fontsize = 20)
        if HYPER:
            screen.draw.text("Ты обрёк нас всех...", (40, 300), color = "red", fontsize = 20)
        elif len(hyperboost):
            screen.draw.text(hyperboost[0], (40, 300), color = "white", fontsize = 20)
        screen.draw.text("Назад - 7", (40, 350), color = "white", fontsize = 20)
    elif mode == "boost?":
        screen.draw.text("Здесь ничего...", center = (300, 180), color = "white", fontsize = 40)
        screen.draw.text("ТОЛЬКО Я", center = (300, 250), color = "red", fontsize = 70)
        screen.draw.text("Назад - 7", (40, 350), color = "white", fontsize = 20)
    elif mode == 'sans':
        screen.draw.text("Undertale Санс", (40, 50), color = "white", fontsize = 20)
        screen.draw.text("Класс: атакующий.", (40, 100), color = "white", fontsize = 20)
        screen.draw.text("Атаки - 6/10", (40, 130), color = "white", fontsize = 20)
        screen.draw.text("Выносливость - 8/10", (40, 160), color = "white", fontsize = 20)
        screen.draw.text("Живучесть - 3/10", (40, 190), color = "white", fontsize = 20)
        if det > 0:
            screen.draw.text("Победа над сансом даёт ему силу второго шанса.", (40, 220), color = "white", fontsize = 20)
            screen.draw.text("Играть - 1", (40, 280), color = "white", fontsize = 20)
            screen.draw.text("Назад - 2", (40, 330), color = "white", fontsize = 20)
        else:
            screen.draw.text("Играть - 1", (40, 250), color = "white", fontsize = 20)
            screen.draw.text("Назад - 2", (40, 300), color = "white", fontsize = 20)
    elif mode == 'uspaps':
        screen.draw.text("Underswap Папирус", (40, 50), color = "white", fontsize = 20)
        screen.draw.text("Класс: защитник/выживатель.", (40, 100), color = "white", fontsize = 20)
        screen.draw.text("Атаки - 4/10", (40, 130), color = "white", fontsize = 20)
        screen.draw.text("Выносливость - 5/10", (40, 160), color = "white", fontsize = 20)
        screen.draw.text("Живучесть - 8/10", (40, 190), color = "white", fontsize = 20)
        screen.draw.text("Играть - 1", (40, 250), color = "white", fontsize = 20)
        screen.draw.text("Назад - 2", (40, 300), color = "white", fontsize = 20)
        screen.draw.text("Объяснение механик - 3", (40, 350), color = "white", fontsize = 20)
    elif mode == 'mechanics':
        screen.draw.text("Папирус постепенно получает магию.", (40, 50), color = "white", fontsize = 20)
        screen.draw.text("Магия делает персонажа сильнее.", (40, 80), color = "white", fontsize = 20)
        screen.draw.text("Санс поможет быстрее получать магию,", (40, 110), color = "white", fontsize = 20)
        screen.draw.text("но враги будут стараться его ударить.", (40, 140), color = "white", fontsize = 20)
        screen.draw.text("Тако требует 30 магии.", (40, 170), color = "white", fontsize = 20)
        screen.draw.text("Лечит 1 хп и 30 выносливости.", (40, 200), color = "white", fontsize = 20)
        screen.draw.text("Назад - 1", (40, 300), color = "white", fontsize = 20)
    elif mode == 'dust':
        screen.draw.text("Dusttale Санс", (40, 50), color = "white", fontsize = 20)
        screen.draw.text("Класс: ассасин.", (40, 100), color = "white", fontsize = 20)
        screen.draw.text("Атаки - 9/10", (40, 130), color = "white", fontsize = 20)
        screen.draw.text("Выносливость - 2/10", (40, 160), color = "white", fontsize = 20)
        screen.draw.text("Живучесть - 4/10", (40, 190), color = "white", fontsize = 20)
        screen.draw.text("Чем более сложный босс пройден, тем персонаж сильнее.", (40, 220), color = "white", fontsize = 20)
        screen.draw.text("Играть - 1", (40, 280), color = "white", fontsize = 20)
        screen.draw.text("Назад - 2", (40, 330), color = "white", fontsize = 20)
        if dust >= 6:
            screen.draw.text("Сноудин - 3", (40, 380), color = "white", fontsize = 20)
    elif mode == 'snowdust':
        screen.draw.text("Dusttale Санс из сноудина", (40, 50), color = "white", fontsize = 20)
        screen.draw.text("Класс: выживатель/атакующий.", (40, 100), color = "white", fontsize = 20)
        screen.draw.text("Атаки - 8/10", (40, 130), color = "white", fontsize = 20)
        screen.draw.text("Выносливость - 3/10", (40, 160), color = "white", fontsize = 20)
        screen.draw.text("Живучесть - 6/10", (40, 190), color = "white", fontsize = 20)
        screen.draw.text("Играть - 1", (40, 250), color = "white", fontsize = 20)
        screen.draw.text("Назад - 2", (40, 300), color = "white", fontsize = 20)
        screen.draw.text("Объяснение механик - 3", (40, 350), color = "white", fontsize = 20)
    elif mode == 'dustmechanics':
        screen.draw.text("Основная атака может выстрелить фиолетовой костью.", (40, 50), color = "white", fontsize = 20)
        screen.draw.text("Она даёт больше выносливости и заряда спец. атаки.", (40, 80), color = "white", fontsize = 20)
        screen.draw.text("Бластер имеет шанс быть фиолетовым.", (40, 110), color = "white", fontsize = 20)
        screen.draw.text("Каждый убитый им враг перезаряжает простые атаки.", (40, 140), color = "white", fontsize = 20)
        screen.draw.text("Уворот имеет шанс убивать урагов.", (40, 170), color = "white", fontsize = 20)
        screen.draw.text("Специальная атака заряжается от убийств.", (40, 200), color = "white", fontsize = 20)
        screen.draw.text("Во время её активации вы замедлены и не атакуете.", (40, 230), color = "white", fontsize = 20)
        screen.draw.text("Назад - 1", (40, 300), color = "white", fontsize = 20)
    elif mode == 'friskmechanics':
        screen.draw.text("Порог уровня зависит от сложности минибосса.", (40, 50), color = "white", fontsize = 20)
        screen.draw.text("С повышением уровня вы получаете новые оружия.", (40, 80), color = "white", fontsize = 20)
        screen.draw.text("На 3 ур. - игрушечный нож.", (40, 110), color = "white", fontsize = 20)
        screen.draw.text("На 6 ур. - грубая перчатка.", (40, 140), color = "white", fontsize = 20)
        screen.draw.text("У каждого оружия есть особые атаки атаки.", (40, 170), color = "white", fontsize = 20)
        screen.draw.text("Особ. атака у палки бьёт на большее расстояние.", (40, 200), color = "white", fontsize = 20)
        screen.draw.text("У ножа - удар, двигающийся вперёд.", (40, 230), color = "white", fontsize = 20)
        screen.draw.text("У перчаток - быстрая перезарядка осн. атаки.", (40, 260), color = "white", fontsize = 20)
        screen.draw.text("Назад - 1", (40, 300), color = "white", fontsize = 20)
    elif mode == 'frisk':
        screen.draw.text("Фриск", (40, 50), color = "white", fontsize = 20)
        screen.draw.text("Класс: танк/выживатель.", (40, 100), color = "white", fontsize = 20)
        screen.draw.text("Атаки - 2/10", (40, 130), color = "white", fontsize = 20)
        screen.draw.text("Выносливость - 10/10", (40, 160), color = "white", fontsize = 20)
        screen.draw.text("Живучесть - 8/10", (40, 190), color = "white", fontsize = 20)
        screen.draw.text("Играть - 1", (40, 250), color = "white", fontsize = 20)
        screen.draw.text("Назад - 2", (40, 300), color = "white", fontsize = 20)
        screen.draw.text("Объяснение механик - 3", (40, 350), color = "white", fontsize = 20)
    elif mode == 'sans?':
        screen.draw.text("Undertale Санс", (40, 50), color = "white", fontsize = 20)
        screen.draw.text("Класс: мертвец.", (40, 100), color = "white", fontsize = 20)
        screen.draw.text("Атаки - 0/10", (40, 130), color = "white", fontsize = 20)
        screen.draw.text("Выносливость - 0/10", (40, 160), color = "white", fontsize = 20)
        screen.draw.text("Живучесть - 0/10", (40, 190), color = "white", fontsize = 20)
        screen.draw.text("-3--", (460, 60), color = (40, 40, 40), fontsize = 20)
        if det > 0:
            if det < 3:
                screen.draw.text("И никакого второго шанса.", (40, 220), color = "white", fontsize = 20)
            else:
                screen.draw.text("Решимость надолго его не спасла.", (40, 220), color = "white", fontsize = 20)
                screen.draw.text("---6", (300, 400), color = (50, 50, 50), fontsize = 20)
            screen.draw.text("Убит", (40, 280), color = "white", fontsize = 20)
            screen.draw.text("Назад - 2", (40, 330), color = "white", fontsize = 20)
        else:
            screen.draw.text("Убит", (40, 250), color = "white", fontsize = 20)
            screen.draw.text("Назад - 2", (40, 300), color = "white", fontsize = 20)
    elif mode == 'uspaps?':
        screen.draw.text("Underswap Папирус", (40, 50), color = "white", fontsize = 20)
        screen.draw.text("Класс: слабак.", (40, 100), color = "white", fontsize = 20)
        screen.draw.text("Атаки - 0/10", (40, 130), color = "white", fontsize = 20)
        screen.draw.text("Выносливость - 0/10", (40, 160), color = "white", fontsize = 20)
        screen.draw.text("Живучесть - 0/10", (40, 190), color = "white", fontsize = 20)
        screen.draw.text("Стёрт в порошок", (40, 250), color = "white", fontsize = 20)
        screen.draw.text("Назад - 2", (40, 300), color = "white", fontsize = 20)
        screen.draw.text("7---", (520, 200), color = (40, 40, 40), fontsize = 20)
    elif mode == 'dust?':
        screen.draw.text("Dusttale Санс", (40, 50), color = "white", fontsize = 20)
        screen.draw.text("Класс: трус.", (40, 100), color = "white", fontsize = 20)
        screen.draw.text("Атаки - 0/10", (40, 130), color = "white", fontsize = 20)
        screen.draw.text("Выносливость - 0/10", (40, 160), color = "white", fontsize = 20)
        screen.draw.text("Живучесть - 0/10", (40, 190), color = "white", fontsize = 20)
        screen.draw.text("Его ур НИЧТО для меня.", (40, 220), color = "white", fontsize = 20)
        screen.draw.text("Сбежал", (40, 280), color = "white", fontsize = 20)
        screen.draw.text("Назад - 2", (40, 330), color = "white", fontsize = 20)
        screen.draw.text("--5-", (50, 400), color = (15 * dust, 15 * dust, 15 * dust), fontsize = 20)
    elif mode == 'frisk?':
        screen.draw.text("Фриск", (40, 50), color = "white", fontsize = 20)
        screen.draw.text("Класс: забытые.", (40, 100), color = "white", fontsize = 20)
        screen.draw.text("Атаки - 0/10", (40, 130), color = "white", fontsize = 20)
        screen.draw.text("Выносливость - 0/10", (40, 160), color = "white", fontsize = 20)
        screen.draw.text("Живучесть - 0/10", (40, 190), color = "white", fontsize = 20)
        screen.draw.text("Пересилены", (40, 250), color = "white", fontsize = 20)
        screen.draw.text("Назад - 2", (40, 300), color = "white", fontsize = 20)
    elif mode == 'paps':
        screen.draw.text("Фантом Папирус", (40, 50), color = "white", fontsize = 20)
        screen.draw.text("Класс: ", (40, 100), color = "white", fontsize = 20)
        screen.draw.text("Атаки - 0/10", (40, 130), color = "white", fontsize = 20)
        screen.draw.text("Выносливость - -1/10", (40, 160), color = "white", fontsize = 20)
        screen.draw.text("Живучесть - 1/10", (40, 190), color = "white", fontsize = 20)
        screen.draw.text("Играть - 1", (40, 250), color = "white", fontsize = 20)
        screen.draw.text("Назад - 2", (40, 300), color = "white", fontsize = 20)
    elif mode == 'code':
        screen.draw.text("Код:", center = (80, 50), color = "white", fontsize = 40)
        screen.draw.text(" ".join(password), center = (180, 50), color = "white", fontsize = 40)
        screen.draw.text(cod, center = (300, 100), color = "white", fontsize = 20)
        if codemode == 1:
            if dust == 0:
                screen.draw.text("Чтобы открыть, пройди первого босса.", (40, 150), color = "white", fontsize = 20)
            else:
                screen.draw.text("Dt!Санс из руин побеждён!", (40, 150), color = "white", fontsize = 20)
                if dust == 1:
                    screen.draw.text("Лёгкая", (400, 150), color = "white", fontsize = 20)
                elif dust == 2:
                    screen.draw.text("Средняя", (400, 150), color = "yellow", fontsize = 20)
                elif dust >= 3:
                    screen.draw.text("Сложная", (400, 150), color = "red", fontsize = 20)
            if dust < 3:
                screen.draw.text("Пройди первое достижение на сложном.", (40, 200), color = "white", fontsize = 20)
            elif dust == 3:
                screen.draw.text("Новый босс имеет 33% шанс появится вместо первого.", (40, 200), color = "white", fontsize = 20)
            elif dust > 3:
                screen.draw.text("Dt!Санс из сноудина побеждён!", (40, 200), color = "white", fontsize = 20)
                if dust == 4:
                    screen.draw.text("Лёгкая", (400, 200), color = "white", fontsize = 20)
                elif dust == 5:
                    screen.draw.text("Средняя", (400, 200), color = "yellow", fontsize = 20)
                elif dust >= 6:
                    screen.draw.text("Сложная", (400, 200), color = "red", fontsize = 20)
            if det == 0:
                screen.draw.text("Чтобы открыть, пройди второго босса.", (40, 250), color = "white", fontsize = 20)
            else:
                screen.draw.text("Решительный Санс побеждён!", (40, 250), color = "white", fontsize = 20)
                if det == 1:
                    screen.draw.text("Лёгкая", (400, 250), color = "white", fontsize = 20)
                elif det == 2:
                    screen.draw.text("Средняя", (400, 250), color = "yellow", fontsize = 20)
                elif det >= 3:
                    screen.draw.text("Сложная", (400, 250), color = "red", fontsize = 20)
        if codemode == 2:
            screen.draw.text("Особые достижения", center = (300, 150), color = "white", fontsize = 20)
            if chara == 0:
                screen.draw.text("Особый минибосс.", (40, 200), color = "white", fontsize = 20)
            else:
                screen.draw.text("SS!Чара побеждена!", (40, 200), color = "white", fontsize = 20)
                if chara == 1:
                    screen.draw.text("Лёгкая", (400, 200), color = "white", fontsize = 20)
                elif chara == 2:
                    screen.draw.text("Средняя", (400, 200), color = "yellow", fontsize = 20)
                elif chara >= 3:
                    screen.draw.text("Сложная", (400, 200), color = "red", fontsize = 20)
        if codemode == 3:
            screen.draw.text("Секретные достижения", center = (300, 150), color = "white", fontsize = 20)
            if hyper > 0:
                screen.draw.text("Нерассказанная история...", (40, 200), color = "white", fontsize = 20)
        screen.draw.text("Листать - a/d", (40, 300), color = "white", fontsize = 20)
        screen.draw.text("Назад - e", (40, 350), color = "white", fontsize = 20)
    elif mode == "code?":
        screen.draw.text("Код:", center = (300, 50), color = "white", fontsize = 20)
        screen.draw.text(" ".join(password), center = (300, 225), color = "white", fontsize = 60)
        screen.draw.text(cod, center = (300, 300), color = "white", fontsize = 20)
        screen.draw.text("Назад - e", (40, 350), color = "white", fontsize = 20)
def new_enemy():
    global chance
    global enemies
    if modeboss == False:
        if sans_assist:
            x = random.randint(150, 450)
        else:
            x = random.randint(25, 575)
        y = -50
        enemy = Actor("FriskSoul", (x, y))
        enemy.speed = random.randint(smin, smax)
        if gamemode != "enemy" or mode == "end":
            enemy.maxhp = 1
            enemy.maxstamina = 0
            enemy.dodge = False
            enemy.beh = "none"
            enemy.charge = 0
            enemy.cost = 1
        else:
            chance = random.randint(1, 1000)
            if chance <= 50:
                enemy.maxhp = 2
                enemy.maxstamina = 0
                enemy.dodge = False
                enemy.speed *= 0.75
                enemy.charge = 0
                enemy.beh = "none"
                enemy.cost = 2
            elif chance <= 100:
                enemy.maxhp = 3
                enemy.maxstamina = 0
                enemy.dodge = False
                enemy.speed *= 0.4
                enemy.charge = 0
                enemy.beh = "none"
                enemy.cost = 3
            elif chance <= 150:
                enemy.maxhp = 1
                enemy.maxstamina = 15
                enemy.dodge = True
                enemy.beh = "none"
                enemy.charge = 0
                enemy.cost = 2
            elif chance <= 200:
                enemy.maxhp = 1
                enemy.maxstamina = 25
                enemy.dodge = False
                enemy.beh = "attack"
                enemy.attacks = [base_attack[random.randint(0, 4)]]
                enemy.cd = 0
                enemy.charge = 0
                enemy.cost = 2
            elif chance <= 220:
                enemy.maxhp = 10
                enemy.maxstamina = 0
                enemy.dodge = False
                enemy.beh = "loop"
                enemy.charge = 0
                enemy.cost = 12
            elif chance <= 240:
                enemy.maxhp = 1
                enemy.maxstamina = 35
                enemy.dodge = False
                enemy.beh = "attack"
                enemy.attacks = [base_attack[random.randint(0, 4)], base_attack[random.randint(0, 4)]]
                enemy.cd = 0
                enemy.charge = 0
                enemy.cost = 2
            elif chance <= 260:
                enemy.maxhp = 1
                enemy.maxstamina = 0
                enemy.dodge = False
                enemy.charge = 0
                enemy.beh = "follow"
                enemy.cost = 2
            elif chance <= 270 and difficulty > chara:
                enemy.maxhp = 15
                enemy.maxstamina = 200
                enemy.dodge = True
                enemy.beh = "attack"
                enemy.image = "SSChara"
                enemy.attacks = [["upknife", 5, 30],
                                 ["sideknife", 5, 30],
                                 ["slash", 10, 60],
                                 ["slashforward", 5, 30],
                                 ["knifes", 4, 20],
                                 ["blaster", 5, 30]]
                mess = ["StoryShift Чара", [300, 200], "white", 90]
                messages.append(mess)
                enemy.cd = 0
                enemy.charge = 0
                enemy.heal = 1
                enemy.cost = 50
                enemy.x = 300
                enemies = []
            else:
                enemy.maxhp = 1
                enemy.maxstamina = 0
                enemy.dodge = False
                enemy.beh = "none"
                enemy.cost = 1
                enemy.charge = 0
        enemy.stamina = enemy.maxstamina
        enemy.slash = True
        enemy.blast = True
        enemy.hp = enemy.maxhp
        enemy.inv = 0
        enemies.append(enemy)
for i in range(5):
    new_enemy()
def enemy_dmg(dmg):
    global bruh
    global chara
    if enemies[bruh].dodge and enemies[bruh].stamina >= 10:
        if enemies[bruh].x >= 300:
            animate(enemies[bruh], tween ='decelerate', duration = 0.5, x = enemies[bruh].x - 150)
        if enemies[bruh].x <= 300:
            animate(enemies[bruh], tween ='decelerate', duration = 0.5, x = enemies[bruh].x + 150)
        enemies[bruh].inv = 30
        miss.pos = (enemies[bruh].x, enemies[bruh].y + 50)
        miss.dorge = 2
        enemies[bruh].stamina -= 10
    else:
        enemies[bruh].hp += dmg
        enemies[bruh].dodge = False
        if enemies[bruh].image == "SSChara" and enemies[bruh].hp == 14:
            enemies[bruh].maxstamina = 500
            enemies[bruh].stamina = enemies[bruh].maxstamina
            enemies[bruh].attacks = [["upknife", 5, 30],
                                     ["sideknife", 5, 30],
                                     ["slash", 10, 60],
                                     ["slashforward", 5, 30],
                                     ["knifes", 4, 20],
                                     ["blaster", 5, 30],
                                     ["knifezone", 20, 60]]
            mess = ["Ты ранил меня?..", [300, 200], "white", 90]
            messages.append(mess)
        if enemies[bruh].hp <= 0:
            if enemies[bruh].image == "SSChara" and enemies[bruh].beh == "attack":
                enemies[bruh].maxstamina = 125
                enemies[bruh].stamina = enemies[bruh].maxstamina
                enemies[bruh].hp = 1
                enemies[bruh].maxhp = 1
                enemies[bruh].beh = "survival"
                mess = ["Ещё рано...", [300, 200], "white", 90]
                messages.append(mess)
            else:
                if enemies[bruh].image == "SSChara":
                    enemies.pop(bruh)
                    mess = ["Даже этого... Было недостаточно...", [300, 200], "white", 90]
                    messages.append(mess)
                    if level == "Сложность: лёгкая":
                        achiev = "Storyshift Чара на лёгкой сложности (Код: 1834)"
                        chara = 1
                    if level == "Сложность: средняя":
                        achiev = "Storyshift Чара на средней сложности (Код: 2536)"
                        chara = 2
                    if level == "Сложность: сложная":
                        achiev = "Storyshift Чара на сложной сложности (Код: 9374)"
                        chara = 3
                    achievments.append(achiev)
                    for i in range(5):
                        new_enemy()
                else:
                    for i in range(enemies[bruh].cost):
                        counting(1)
                    if modeboss == False:
                        enemies.pop(bruh)
                        if level == "Сложность: #@&%$!":
                            new_enemy()
                        new_enemy()
        if char == "frisk":
            healing(1)
def enemy_soul():
    global mode
    global count
    global attac
    global modeboss
    global bossphase
    global boss
    global attacking
    global side
    global image
    global b_cd
    global blast_cd
    global d_cd
    global b_cd1
    global blast_cd1
    global d_cd1
    global cutscene
    global dialogs
    global ax
    global ay
    global repeat
    global attack
    global blink
    global now
    for i in range(len(enemies)):
        if modeboss == False and len(enemies) - 1 >= i:
            if enemies[i].stamina < enemies[i].maxstamina and enemies[i].beh != "survival":
                enemies[i].stamina += 0.1
            if enemies[i].inv > 0:
                enemies[i].inv -= 1
            if enemies[i].beh == "none" or enemies[i].beh == "loop" or enemies[i].beh == "follow":
                if enemies[i].y < 650:
                    enemies[i].y += enemies[i].speed
                    if enemies[i].beh == "follow":
                        if enemies[i].speed < soul.x - enemies[i].x:
                            enemies[i].x += enemies[i].speed
                        elif enemies[i].speed < enemies[i].x - soul.x:
                            enemies[i].x -= enemies[i].speed
                elif enemies[i].beh == "none" or enemies[i].beh == "follow":
                    enemies.pop(i)
                    new_enemy()
                elif enemies[i].beh == "loop":
                    if sans_assist:
                        enemies[i].x = random.randint(150, 450)
                    else:
                        enemies[i].x = random.randint(25, 575)
                    enemies[i].y = -50
            elif enemies[i].beh == "attack" or enemies[i].beh == "survival":
                if enemies[i].charge > 0:
                    enemies[i].charge -= 1
                    if enemies[i].charge <= 0:
                        direc = "down"
                        pop = 550
                        if enemies[i].image == "SSChara":
                            atk = Actor("RedSlash", (enemies[i].x, enemies[i].y + 10))
                        else:
                            atk = Actor("Slash", (enemies[i].x, enemies[i].y + 10))
                        atk.angle = 180
                        atk.speed = 10
                        if level == "Сложность: средняя":
                            atk.speed += 1
                        elif level == "Сложность: сложная":
                            atk.speed += 2
                        atk.direct = direc
                        atk.dis = pop
                        atk.types = "bonerush"
                        attacks.append(atk)
                        enemies[i].stamina -= enemies[i].attacks[attac][1]
                        enemies[i].cd = enemies[i].attacks[attac][2]
                elif enemies[i].y < 100:
                    enemies[i].y += enemies[i].speed
                elif enemies[i].cd <= 0:
                    attac = random.randint(0, len(enemies[i].attacks) - 1)
                    attack = enemies[i].attacks[attac]
                    if enemies[i].image == "SSChara" and ((enemies[i].hp <= 7 and enemies[i].stamina <= 200) or enemies[i].hp <= 3) and enemies[i].heal > 0:
                        enemies[i].hp += 1
                        enemies[i].stamina += 25
                        if level == "Сложность: средняя":
                            enemies[i].hp += 1
                            enemies[i].stamina += 25
                        elif level == "Сложность: сложная":
                            enemies[i].hp += 2
                            enemies[i].stamina += 75
                        enemies[i].heal -= 1
                        mess = ["Чара использует шоколад.", [300, 200], "white", 90]
                        messages.append(mess)
                    if (enemies[i].x - soul.x < 50 and enemies[i].x - soul.x > -50) and (enemies[i].y - soul.y < 20 and enemies[i].y - soul.y > -70) and enemies[i].image == "SSChara":
                        atk = Actor("SlashAnim1", soul.pos)
                        atk.types = "hit"
                        atk.count = 0
                        attacks.append(atk)
                        enemies[i].cd = 7
                    if enemies[i].attacks[attac][0] == "upknife" and enemies[i].stamina >= enemies[i].attacks[attac][1]:
                        side = random.randint(1, 2)
                        if side == 1:
                            ay = 550
                            direc = "up"
                            pop = -100
                            angle = 180
                        else:
                            ay = -100
                            direc = "down"
                            pop = 550
                            angle = 0
                        ax = soul.x
                        atk = Actor("KnifeDown", (ax, ay))
                        atk.angle = angle
                        atk.speed = 5
                        if level == "Сложность: средняя":
                            atk.speed += 1
                        elif level == "Сложность: сложная":
                            atk.speed += 2
                        atk.direct = direc
                        atk.dis = pop
                        atk.types = "bonerush"
                        attacks.append(atk)
                        enemies[i].stamina -= enemies[i].attacks[attac][1]
                        enemies[i].cd = enemies[i].attacks[attac][2]
                    elif enemies[i].attacks[attac][0] == "sideknife" and enemies[i].stamina >= enemies[i].attacks[attac][1]:
                        side = random.randint(1, 2)
                        if side == 1:
                            ax = 700
                            direc = "left"
                            pop = -100
                            angle = 0
                        else:
                            ax = -100
                            direc = "right"
                            pop = 700
                            angle = 180
                        ay = soul.y
                        atk = Actor("Knife", (ax, ay))
                        atk.angle = angle
                        atk.speed = 5
                        if level == "Сложность: средняя":
                            atk.speed += 1
                        elif level == "Сложность: сложная":
                            atk.speed += 2
                        atk.direct = direc
                        atk.dis = pop
                        atk.types = "bonerush"
                        attacks.append(atk)
                        enemies[i].stamina -= enemies[i].attacks[attac][1]
                        enemies[i].cd = enemies[i].attacks[attac][2]
                    elif enemies[i].attacks[attac][0] == "slash" and enemies[i].stamina >= enemies[i].attacks[attac][1]:
                        pop = 30
                        atk = Actor("SlashWarn1", (soul.x, 225))
                        atk.w0 = 0
                        atk.w1 = 20
                        atk.blast = 30
                        atk.types = "slash"
                        attacks.append(atk)
                        enemies[i].stamina -= enemies[i].attacks[attac][1]
                        enemies[i].cd = enemies[i].attacks[attac][2]
                    elif enemies[i].attacks[attac][0] == "slashforward" and enemies[i].stamina >= enemies[i].attacks[attac][1] and enemies[i].x - soul.x < 50 and enemies[i].x - soul.x > -50:
                        enemies[i].charge = 30
                        if level == "Сложность: средняя":
                            enemies[i].charge -= 5
                        elif level == "Сложность: сложная":
                            enemies[i].charge -= 10
                    elif enemies[i].attacks[attac][0] == "knifes" and enemies[i].stamina >= enemies[i].attacks[attac][1]:
                        side = random.randint(1, 2)
                        if side == 1:
                            ax = 700
                            direc = "left"
                            pop = -100
                            angle = 0
                        else:
                            ax = -100
                            direc = "right"
                            pop = 700
                            angle = 180
                        ay = random.randint(25, 425)
                        atk = Actor("Knife", (ax, ay))
                        atk.angle = angle
                        atk.speed = 5
                        if level == "Сложность: средняя":
                            atk.speed += 1
                        elif level == "Сложность: сложная":
                            atk.speed += 2
                        atk.direct = direc
                        atk.dis = pop
                        atk.types = "bonerush"
                        attacks.append(atk)
                        enemies[i].stamina -= enemies[i].attacks[attac][1]
                        enemies[i].cd = enemies[i].attacks[attac][2]
                    elif enemies[i].attacks[attac][0] == "blaster" and enemies[i].stamina >= enemies[i].attacks[attac][1]:
                        pop = 30
                        atk = Actor("BlasterWarn1", (random.randint(25, 575), 225))
                        atk.w0 = 0
                        atk.w1 = 20
                        atk.blast = 30
                        atk.types = "blaster"
                        attacks.append(atk)
                        enemies[i].stamina -= enemies[i].attacks[attac][1]
                        enemies[i].cd = enemies[i].attacks[attac][2]
                    elif enemies[i].attacks[attac][0] == "knifezone" and enemies[i].stamina >= enemies[i].attacks[attac][1]:
                        ay = 15
                        for i2 in range(7):
                            atk = Actor("Knife", (650, ay))
                            atk.direct = "left"
                            atk.dis = -100
                            atk.types = "bonerush"
                            atk.speed = 5
                            if level == "Сложность: средняя":
                                atk.speed += 1
                            elif level == "Сложность: сложная":
                                atk.speed += 2
                            attacks.append(atk)
                            ay += 70
                        ay = 50
                        for i2 in range(6):
                            atk = Actor("Knife", (-50, ay))
                            atk.direct = "right"
                            atk.dis = 700
                            atk.angle = 180
                            atk.types = "bonerush"
                            atk.speed = 5
                            if level == "Сложность: средняя":
                                atk.speed += 1
                            elif level == "Сложность: сложная":
                                atk.speed += 2
                            attacks.append(atk)
                            ay += 70
                        enemies[i].stamina -= enemies[i].attacks[attac][1]
                        enemies[i].cd = enemies[i].attacks[attac][2]
                    elif enemies[i].beh == "survival":
                        if enemies[i].stamina < enemies[i].attacks[attac][1]:
                            enemies[i].attacks.pop(attac)
                            if len(enemies[i].attacks) == 0:
                                bruh = i
                                enemy_dmg(-1)
                    else:
                        enemies[i].stamina += enemies[i].maxstamina * 0.01
                        if enemies[i].stamina > enemies[i].maxstamina:
                            enemies[i].stamina = enemies[i].maxstamina
                        enemies[i].cd = 30
                else:
                    enemies[i].cd -= 1
        elif bossphase == 0:
            enemies[i].y += boss.speed
            if enemies[i].y >= 85:
                bossphase = -1
                b_cd = "(Нажмите 1,"
                blast_cd = " "
                d_cd = "чтобы продолжить)"
                b_cd1 = -1
                blast_cd1 = -1
                d_cd1 = -1
                if boss.image == "Weakdust":
                    cutscene = 1
                    dialogs = ["Кто ты?", 
                               "Что ты здесь делаешь?", 
                               "...", 
                               "Это не важно.", 
                               "Я просто с тобой по-быстрому разберусь..."]
                elif boss.image == "Snowdindust":
                    cutscene = 9
                    dialogs = ["Привет", 
                               "Давно не виделись.", 
                               "Ты, наверно, забыл, что я говорил?", 
                               "Но я вернулся, сильнее, чем прежде.", 
                               "Я не буду мелочиться на этот раз."]
                elif bosses == 1:
                    cutscene = 3
                    dialogs = ["...", 
                               "Ты наконец-то здесь...", 
                               "Ты реально не сдаёшься, да?", 
                               "Но я не могу тебя пропустить.", 
                               "Ты не представляешь, с чем имеешь дело.", 
                               "У тебя не будет ни шанса против него."]
                elif bosses == 99:
                    cutscene = 6
                    dialogs = ["...", 
                               "Я не знаю, чего ты добиваешься, но...", 
                               "Ты не уйдёшь отсюда живым.", 
                               "Поверь мне, я знаю, о чём говорю.", 
                               "Поэтому у меня есть предложение.", 
                               "Выключи игру и мы представим, что этого не произошло.", 
                               "Ты будешь относительно жив, а я...", 
                               "Просто не потрачу своё время.", 
                               "Иначе...", 
                               "Тебе твоя судьба не понравится.", 
                               "Хорошенько подумай."]
        elif bossphase == 1:
            attac = random.randint(0, len(attacking) - 1)
            #attac = random.randint(1, 1)
            attack = attacking[attac]
            if attack == "dustspinleft":
                attx = -100
                for i in range(10):
                    side = random.randint(1, 2)
                    if side == 2:
                        ax = -(attx) + 600
                        direc = "left"
                        pop = -100
                    else:
                        ax = attx
                        direc = "right"
                        pop = 700
                    ay = random.randint(75, 375)
                    atk = Actor("Dustrush", (ax, ay))
                    atk.speed = 5
                    if level == "Сложность: средняя":
                        atk.speed += 1
                    elif level == "Сложность: сложная":
                        atk.speed += 2
                    atk.direct = direc
                    atk.dis = pop
                    atk.types = "bonerush"
                    attacks.append(atk)
                    attx -= 75
            elif attack == "dustspindown":
                atty = -100
                for i in range(10):
                    side = random.randint(1, 2)
                    if side == 2:
                        ay = -(atty) + 450
                        direc = "up"
                        pop = -100
                    else:
                        ay = atty
                        direc = "down"
                        pop = 600
                    ax = random.randint(50, 550)
                    atk = Actor("Dustrush", (ax, ay))
                    atk.angle = 90
                    atk.speed = 5
                    if level == "Сложность: средняя":
                        atk.speed += 1
                    elif level == "Сложность: сложная":
                        atk.speed += 2
                    atk.direct = direc
                    atk.dis = pop
                    atk.types = "bonerush"
                    attacks.append(atk)
                    atty -= 75
            elif attack == "bonejump":
                attx = 700
                side = 1
                soul.image = "BlueSoul"
                if char == "frisk":
                    soul.angle = 180
                animate(soul, tween = "linear", duration = 1, y = 430)
                for i in range(10):
                    if side == 1:
                        ay = 425
                        types = "sidebone"
                        image = "JumpDustbone"
                        side = 2
                    else:
                        ay = 400
                        types = "bluebone"
                        image = "Bluebone"
                        side = 1
                    atk = Actor(image, (attx, ay))
                    atk.speed = 5
                    atk.types = types
                    if level == "Сложность: средняя":
                        atk.speed += 1
                    elif level == "Сложность: сложная":
                        atk.speed += 2
                    atk.direct = "left"
                    atk.dis = -100
                    attacks.append(atk)
                    attx += 150
            elif attack == "sidejump":
                attx = 700
                soul.image = "BlueSoul"
                if char == "frisk":
                    soul.angle = 180
                animate(soul, tween = "linear", duration = 1, y = 430)
                if enraged:
                    for i in range(12 + (boss.hp * 2)):
                        if i % 2 == 1:
                            atk = Actor("Bluebone", (attx, 400))
                            atk.types = "bluebone"
                        else:
                            atk = Actor("Bonejump", (attx, 450))
                            atk.types = "sidebone"
                        atk.speed = 17 + (boss.hp * 3)
                        if level == "Сложность: средняя":
                            atk.speed += 1
                        elif level == "Сложность: сложная":
                            atk.speed += 2
                        atk.direct = "left"
                        atk.dis = -100
                        attacks.append(atk)
                        attx += 200
                    attx = -100
                    for i in range(12 + (boss.hp * 2)):
                        if i % 2 == 1:
                            atk = Actor("Bluebone", (attx, 400))
                            atk.types = "bluebone"
                        else:
                            atk = Actor("Bonejump", (attx, 450))
                            atk.types = "sidebone"
                        atk.speed = 17 + (boss.hp * 3)
                        if level == "Сложность: средняя":
                            atk.speed += 1
                        elif level == "Сложность: сложная":
                            atk.speed += 2
                        atk.direct = "right"
                        atk.dis = 700
                        attacks.append(atk)
                        attx -= 200
                else:
                    for i in range(5):
                        atk = Actor("Bonejump", (attx, 450))
                        atk.speed = 5
                        atk.types = "sidebone"
                        if level == "Сложность: средняя":
                            atk.speed += 1
                        elif level == "Сложность: сложная":
                            atk.speed += 2
                        atk.direct = "left"
                        atk.dis = -100
                        attacks.append(atk)
                        attx += 200
                    attx = -100
                    for i in range(5):
                        atk = Actor("Bonejump", (attx, 450))
                        atk.speed = 5
                        atk.types = "sidebone"
                        if level == "Сложность: средняя":
                            atk.speed += 1
                        elif level == "Сложность: сложная":
                            atk.speed += 2
                        atk.direct = "right"
                        atk.dis = 700
                        attacks.append(atk)
                        attx -= 200
            elif attack == "bonerush":
                atty = -100
                if enraged:
                    for i in range(24 + (boss.hp * 4)):
                        side = random.randint(1, 2)
                        if side == 2:
                            ay = -(atty) + 450
                            direc = "up"
                            pop = -100
                        else:
                            ay = atty
                            direc = "down"
                            pop = 600
                        ax = random.randint(50, 550)
                        side = random.randint(1, 10)
                        if side <= 6 + boss.hp:
                            atk = Actor("Bonejump", (ax, ay))
                            atk.types = "bonerush"
                        else:
                            atk = Actor("Bluebonejump", (ax, ay))
                            atk.types = "bluebonerush"
                        atk.speed = 17 + (boss.hp * 3)
                        if level == "Сложность: средняя":
                            atk.speed += 1
                        elif level == "Сложность: сложная":
                            atk.speed += 2
                        atk.direct = direc
                        atk.dis = pop
                        attacks.append(atk)
                        atty -= 60
                else:
                    for i in range(20):
                        side = random.randint(1, 2)
                        if side == 2:
                            ay = -(atty) + 450
                            direc = "up"
                            pop = -100
                        else:
                            ay = atty
                            direc = "down"
                            pop = 600
                        ax = random.randint(50, 550)
                        side = random.randint(1, 2)
                        if side == 2:
                            atk = Actor("Bonejump", (ax, ay))
                            atk.types = "bonerush"
                        else:
                            atk = Actor("Bluebonejump", (ax, ay))
                            atk.types = "bluebonerush"
                        atk.speed = 5
                        if level == "Сложность: средняя":
                            atk.speed += 1
                        elif level == "Сложность: сложная":
                            atk.speed += 2
                        atk.direct = direc
                        atk.dis = pop
                        attacks.append(atk)
                        atty -= atk.speed * 12
            elif attack == "blasters":
                if enraged:
                    side = random.randint(1, 2)
                    if side == 1:
                        pop = 30
                        if level == "Сложность: средняя":
                            pop -= 5
                        elif level == "Сложность: сложная":
                            pop -= 10
                        for i in range(12 + (boss.hp * 2)):
                            ax = 25 + 500 / (12 + boss.hp * 2) * i
                            atk = Actor("BlasterWarn0", (ax, 225))
                            atk.w0 = pop
                            atk.w1 = 20
                            atk.blast = 15
                            if level == "Сложность: средняя":
                                atk.blast += 5
                            elif level == "Сложность: сложная":
                                atk.blast += 10
                            atk.types = "blaster"
                            attacks.append(atk)
                            pop += 5 - boss.hp * 3
                            if level == "Сложность: средняя":
                                pop -= 1
                            elif level == "Сложность: сложная":
                                pop -= 2
                    else:
                        pop = 30
                        if level == "Сложность: средняя":
                            pop -= 5
                        elif level == "Сложность: сложная":
                            pop -= 10
                        for i in range(12 + (boss.hp * 2)):
                            ax = 575 - 500 / (12 + boss.hp * 2) * i
                            atk = Actor("BlasterWarn0", (ax, 225))
                            atk.w0 = pop
                            atk.w1 = 20
                            atk.blast = 15
                            if level == "Сложность: средняя":
                                atk.blast += 5
                            elif level == "Сложность: сложная":
                                atk.blast += 10
                            atk.types = "blaster"
                            attacks.append(atk)
                            ax -= (500 / (12 - boss.hp * 2))
                            pop += 5 - boss.hp * 3
                            if level == "Сложность: средняя":
                                pop -= 1
                            elif level == "Сложность: сложная":
                                pop -= 2
                else:
                    pop = 30
                    if level == "Сложность: средняя":
                        pop -= 5
                    elif level == "Сложность: сложная":
                        pop -= 10
                    for i in range(5):
                        ax = random.randint(50, 550)
                        atk = Actor("BlasterWarn0", (ax, 225))
                        atk.w0 = pop
                        atk.w1 = 20
                        atk.blast = 15
                        if level == "Сложность: средняя":
                            atk.blast += 5
                        elif level == "Сложность: сложная":
                            atk.blast += 10
                        atk.types = "blaster"
                        attacks.append(atk)
                        pop += 30
                        if level == "Сложность: средняя":
                            pop -= 5
                        elif level == "Сложность: сложная":
                            pop -= 10
            elif attack == "dustblasters":
                pop = 30
                if level == "Сложность: средняя":
                    pop -= 5
                elif level == "Сложность: сложная":
                    pop -= 10
                repeat = 12
                for i in range(3):
                    ax = random.randint(50, 550)
                    atk = Actor("BlasterWarn0", (ax, 225))
                    atk.w0 = pop
                    atk.w1 = 30
                    atk.blast = 15
                    if level == "Сложность: средняя":
                        atk.blast += 5
                    elif level == "Сложность: сложная":
                        atk.blast += 10
                    atk.types = "blaster"
                    attacks.append(atk)
            elif attack == "dustpuzzle":
                blink = 10
                soul.pos = (100, 225)
                d_cd1 = -1
                d_cd = "--->" 
                atk = Actor("LongerDustbone", (150, 175))
                atk.types = "none"
                attacks.append(atk)
                atk = Actor("LongerDustbone", (280, 275))
                atk.types = "none"
                attacks.append(atk)
                atk = Actor("LongerDustbone", (390, 175))
                atk.types = "none"
                attacks.append(atk)
                atk = Actor("LongerDustbone", (520, 275))
                atk.types = "none"
                attacks.append(atk)
                atk = Actor("Dustsidebone", (180, 5))
                atk.types = "puzzle"
                atk.speed = 5
                if level == "Сложность: средняя":
                    atk.speed += 1
                elif level == "Сложность: сложная":
                    atk.speed += 2
                atk.direct = "down"
                atk.dis = 445
                attacks.append(atk)
                atk = Actor("Dustsidebone", (250, 445))
                atk.types = "puzzle"
                atk.speed = 5
                if level == "Сложность: средняя":
                    atk.speed += 1
                elif level == "Сложность: сложная":
                    atk.speed += 2
                atk.direct = "up"
                atk.dis = 5
                attacks.append(atk)
                atk = Actor("Bluesidebone", (335, 440))
                atk.types = "bluepuzzle"
                atk.speed = 10
                if level == "Сложность: средняя":
                    atk.speed += 1
                elif level == "Сложность: сложная":
                    atk.speed += 2
                atk.direct = "up"
                atk.dis = 10
                attacks.append(atk)
                atk = Actor("Dustsidebone", (490, 5))
                atk.types = "puzzle"
                atk.speed = 5
                if level == "Сложность: средняя":
                    atk.speed += 1
                elif level == "Сложность: сложная":
                    atk.speed += 2
                atk.direct = "down"
                atk.dis = 445
                attacks.append(atk)
                atk = Actor("Bluesidebone", (455, 440))
                atk.types = "bluepuzzle"
                atk.speed = 10
                if level == "Сложность: средняя":
                    atk.speed += 1
                elif level == "Сложность: сложная":
                    atk.speed += 2
                atk.direct = "up"
                atk.dis = 10
                attacks.append(atk)
                atk = Actor("LongDustbone", (-150, 100))
                atk.types = "bonerush"
                atk.speed = 0.5
                if level == "Сложность: средняя":
                    atk.speed += 0.25
                elif level == "Сложность: сложная":
                    atk.speed += 0.5
                atk.direct = "right"
                atk.dis = 600
                attacks.append(atk)
                atk = Actor("LongDustbone", (-150, 350))
                atk.types = "bonerush"
                atk.speed = 0.5
                if level == "Сложность: средняя":
                    atk.speed += 0.25
                elif level == "Сложность: сложная":
                    atk.speed += 0.5
                atk.direct = "right"
                atk.dis = 600
                attacks.append(atk)
            elif attack == "confusejump":
                atty = 500
                side = 1
                soul.image = "SideSoul"
                if char == "frisk":
                    soul.angle = 180
                animate(soul, tween = "linear", duration = 1, x = 580)
                for i in range(14):
                    ax = 575
                    types = "bonerush"
                    image = "Dustsidebone"
                    atk = Actor(image, (ax, 0))
                    atk.y = -(atty) + 450
                    atk.direct = "down"
                    atk.dis = 550
                    atk.speeed = random.randint(4, 5)
                    atk.speed = 5
                    atk.types = types
                    if level == "Сложность: средняя":
                        atk.speed += 1
                        atk.speeed += 1
                    elif level == "Сложность: сложная":
                        atk.speed += 2
                        atk.speeed += 2
                    attacks.append(atk)
                    atty += 180
            elif attack == "hyperbonerush":
                blink = 10 
                ax = -30
                soul.pos = (300, 225)
                atk = Actor("HyperSideBone", (270, 100))
                atk.types = "none"
                attacks.append(atk)
                atk = Actor("HyperSideBone", (270, 350))
                atk.types = "none"
                attacks.append(atk)
                atk = Actor("HyperSideBone", (330, 100))
                atk.types = "none"
                attacks.append(atk)
                atk = Actor("HyperSideBone", (330, 350))
                atk.types = "none"
                attacks.append(atk)
                atk = Actor("HyperBoneLeft", (300, 5))
                atk.types = "bonerush"
                atk.speed = 0.5
                atk.direct = "down"
                atk.dis = 600
                attacks.append(atk)
                atk = Actor("HyperBoneLeft", (300, 445))
                atk.types = "bonerush"
                atk.speed = 0.5
                atk.direct = "up"
                atk.dis = 0
                attacks.append(atk)
                repeat = 22
                for i in range(11):
                    direc = "right"
                    pop = 670
                    ay = random.randint(50, 550)
                    atk = Actor("HyperBoneLeft", (ax, ay))
                    atk.types = "bonerush"
                    atk.speed = 10
                    atk.direct = direc
                    atk.dis = pop
                    attacks.append(atk)
                    ax -= 60
            elif attack == "rushallsides":
                repeat = 25
                ay = 475
                for i in range(3):
                    ax = random.randint(50, 550)
                    atk = Actor("HyperBoneUp", (ax, ay))
                    atk.types = "bonerush"
                    atk.speed = 10
                    atk.direct = "up"
                    atk.dis = -100
                    attacks.append(atk)
                    ay += 150
                ay = -25
                for i in range(3):
                    ax = random.randint(50, 550)
                    atk = Actor("HyperBoneUp", (ax, ay))
                    atk.types = "bonerush"
                    atk.speed = 10
                    atk.direct = "down"
                    atk.dis = 425
                    attacks.append(atk)
                    ay -= 150
                ax = -25
                for i in range(4):
                    ay = random.randint(20, 430)
                    atk = Actor("HyperBoneLeft", (ax, ay))
                    atk.types = "bonerush"
                    atk.speed = 10
                    atk.direct = "right"
                    atk.dis = 625
                    attacks.append(atk)
                    ax -= 150
                ax = 625
                for i in range(4):
                    ay = random.randint(20, 430)
                    atk = Actor("HyperBoneLeft", (ax, ay))
                    atk.types = "bonerush"
                    atk.speed = 10
                    atk.direct = "left"
                    atk.dis = -25
                    attacks.append(atk)
                    ax += 150
            elif attack == "hypersidebone":
                repeat = 12
                ax = 700
                for i in range(4):
                    atk = Actor("HyperSideBone", (ax, 100))
                    atk.speed = 7
                    atk.types = "bonerush"
                    atk.direct = "left"
                    atk.dis = -100
                    attacks.append(atk)
                    ax += 300
                ax = -100
                for i in range(4):
                    atk = Actor("HyperSideBone", (ax, 350))
                    atk.speed = 7
                    atk.types = "bonerush"
                    atk.direct = "right"
                    atk.dis = 700
                    attacks.append(atk)
                    ax -= 300
            bossphase += 1
        if enraged and boss.hp > -6:
            if boss.x >= 300:
                boss.x += boss.hp / 2
            else:
                boss.x -= boss.hp / 2 
def take_dmg():
    global boss
    global bossphase
    global b_cd
    global blast_cd
    global d_cd
    global b_cd1
    global blast_cd1
    global d_cd1
    global cutscene
    global dialogs
    global count
    global enemies
    global block
    global Block
    if boss.dorge > 0:
        miss.pos = (boss.x, boss.y - 40)
        miss.dorge = 2
        if boss.dorge % 2 == 0:
            animate(boss, tween ='decelerate', duration = 0.5, x = boss.x + 100)
        else:
            animate(boss, tween ='decelerate', duration = 0.5, x = boss.x - 100)
        boss.dorge -= 1
        if bosses == 0 and boss.dorge == 0 and boss.image == "Weakdust":
                bossphase = -1
                b_cd = "(Нажмите 1,"
                blast_cd = " "
                d_cd = "чтобы продолжить)"
                b_cd1 = -1
                blast_cd1 = -1
                d_cd1 = -1
                dialogs = ["У меня нет на это времени.", 
                           "Но не волнуйся...", 
                           "Мы ещё встретимся.", 
                           "Санс убежал..."]
                cutscene = 2
        else:
            bossphase = 1
            b_cd1 = -1
            b_cd = "Босс атакует..."
    elif boss.block > 0:
        boss.block -= 1
        miss.pos = (boss.x, boss.y - 40)
        miss.image = "Block"
        miss.dorge = 2
        block = Actor("HyperBoneLeft", (boss.x, boss.y + 25))
        Block.append(block)
        if boss.block == 8:
            bossphase = -1
            b_cd = "(Нажмите 1,"
            blast_cd = " "
            d_cd = "чтобы продолжить)"
            b_cd1 = -1
            dialogs = ["Ха-ха.", 
                       "Ты реально думал, что ударишь меня так легко?", 
                       "В любом случае, ты сделал свой выбор.", 
                       "Посмотрим, на что ты способен."]
            cutscene = 7
        else:
            bossphase = 1
            b_cd1 = -1
            b_cd = "Босс атакует..."
    else:
        boss.hp -= 1
        if boss.hp == 98:
            bossphase = -1
            b_cd = "(Нажмите 1,"
            blast_cd = " "
            d_cd = "чтобы продолжить)"
            b_cd1 = -1
            dialogs = ["Что?", 
                       "Как?", 
                       "Это-", 
                       "ЭТОГО НЕ МОЖЕТ БЫТЬ!", 
                       "КАК ты умудрился меня задеть?", 
                       "...", 
                       "Если ты такой смелый, то мне ничего не мешает...", 
                       "ПОКАЗАТЬ ТЕБЕ ВСЮ СВОЮ МОЩЬ.", 
                       "(К сожалению, это конец 1 фазы.)", 
                       "(Далее битва ещё не сделана.)", 
                       "(Но вы получите код, который вам поможет в будущем.)", 
                       "(Запомните его: 4910)", 
                       "(Он позволит пользоваться более сильным папирусом.)", 
                       "(Удачи!)"]
            cutscene = 8
        elif bosses == 0 and boss.hp == 1 and boss.image == "Snowdindust":
                bossphase = -1
                b_cd = "(Нажмите 1,"
                blast_cd = " "
                d_cd = "чтобы продолжить)"
                b_cd1 = -1
                blast_cd1 = -1
                d_cd1 = -1
                dialogs = ["...", 
                           "Ты...", 
                           "Ударил...", 
                           "Меня?..", 
                           "Санс убежал..."]
                cutscene = 10
        elif boss.hp == 0 and bosses == 1:
            bossphase = -1
            b_cd = "(Нажмите 1,"
            blast_cd = " "
            d_cd = "чтобы продолжить)"
            b_cd1 = -1
            blast_cd1 = -1
            d_cd1 = -1
            dialogs = ["...", 
                       "Санс отказывается умирать.", 
                       "Хей, кем бы ты ни был.", 
                       "Ты очень решителен пройти этот путь, верно?", 
                       "Но это будет не так просто как ты думаешь",
                       "Я тоже решителен тебя остановить.",
                       "И поверь мне...",
                       "Это станет твоим концом раз и навсегда."]
            cutscene = 4
        elif boss.hp == -6:
            boss.hp = -99
            bossphase = -1
            b_cd = "(Нажмите 1,"
            blast_cd = " "
            d_cd = "чтобы продолжить)"
            b_cd1 = -1
            blast_cd1 = -1
            d_cd1 = -1
            if level == "Сложность: сложная":
                dialogs = ["...", 
                           "И ты всё равно победил...", 
                           "Даже на высокой сложности...", 
                           "Видимо, я недооценил тебя, да?", 
                           "Слушай...", 
                           "Ты видел то странное усиление?", 
                           "Я не знаю, что оно в себе хранит, но...", 
                           "Если ты чувствуешь себя достаточно сильным...", 
                           "Я слышал, что оно стоит 99 монет.", 
                           "Но я не советовал бы тебе его использовать.", 
                           "Слишком плохое у меня предчувствие.", 
                           "Хотя я уже понял, что я не в силах тебя остановить.", 
                           "В любом случае, это меня не касается.", 
                           "Удачи..."]
            else:
                dialogs = ["...", 
                           "И ты всё равно победил...", 
                           "В конце концов, я не думал, что смогу одолеть тебя.", 
                           "Только...", 
                           "Помнишь, что я говорил тебе?", 
                           "Не говори, что я не предупреждал тебя..."]
            cutscene = 5
        else:
            bossphase = 1
            b_cd1 = -1
            b_cd = "Босс атакует..."
def collisions():
    global mode
    global count
    global repeat
    global sans_assist
    global b_cd1
    global blast_cd1
    global d_cd1
    global wow
    global stamina
    global special
    global bruh
    global blink
    for i in range(len(enemies)):
        bruh = i
        if modeboss == False:
            if len(enemies) - 1 >= i:
                if soul.colliderect(enemies[i]):
                    if inv <= 0:
                        dmg()
                        if enemies[i].inv <= 0 and enemies[i].beh != "survival":
                            enemy_dmg(-1)
                        break
                    elif kill == 1 and enemies[i].inv <= 0:
                        enemy_dmg(-1)
                        break
                    else:
                        miss.pos = (enemies[i].x, enemies[i].y - 50)
                        miss.dorge = 2
            if len(enemies) - 1 >= i:
                if blast > 0:
                    if blaster.colliderect(enemies[i]) and enemies[i].blast and enemies[i].inv <= 0 and enemies[i].beh != "survival":
                        if blaster.image == "HyperBlast":
                            b_cd1 -= 1
                            blast_cd1 -= 1
                            d_cd1 -= 1
                        enemies[i].blast = False
                        enemy_dmg(-1)
            if len(enemies) - 1 >= i:
                for i2 in range(len(bullets[0])):
                    if bullets[0][i2].colliderect(enemies[i]) and enemies[i].inv <= 0 and enemies[i].beh != "survival":
                        if char == "uspaps":
                            if bullets[0][i2].turn == "block":
                                miss.pos = (bullets[0][i2].x,bullets[0][i2].y - 10)
                                miss.image = "Block"
                                miss.dorge = 2
                        if bullets[0][i2].image == "Bluebonejump":
                            enemies[i].speed -= 3
                            if enemies[i].speed <= 0:
                                enemy_dmg(-1)
                                enemies[i].speed = 1
                        elif bullets[0][i2].image == "HyperBoneUp":
                            stamina += 4
                            special += 4
                            enemy_dmg(-1)
                        elif bullets[0][i2].image == "Slash" or char == "frisk":
                            if enemies[i].slash:
                                enemies[i].slash = False
                                enemy_dmg(-1)
                        else:
                            enemy_dmg(-1)
                        if modeboss == False:
                            if bullets[0][i2].image != "Slash" and char != "frisk":
                                bullets[0].pop(i2)
                        break
            if len(enemies) - 1 >= i:
                for i2 in range(len(bullets[1])):
                    if bullets[1][i2].colliderect(enemies[i]) and enemies[i].inv <= 0 and enemies[i].beh != "survival":
                        wow = 0
                        if bullets[1][i2].image == "SpecSpin1":
                            bullets[1][i2].hp -= 1
                            if bullets[1][i2].hp != 0:
                                wow = 1
                        if wow == 0:
                            bullets[1].pop(i2)
                        enemy_dmg(-1)
                        break
            if len(enemies) - 1 >= i:
                for i2 in range(len(bullets[2])):
                    if bullets[2][i2].colliderect(enemies[i]) and enemies[i].inv <= 0 and enemies[i].beh != "survival":
                        bullets[2].pop(i2)
                        enemy_dmg(-1)
                        break
            if len(enemies) - 1 >= i and sans_assist:
                if Sans.colliderect(enemies[i]):
                    sans_assist = False
                    if enemies[i].inv <= 0 and enemies[i].beh != "survival":
                        enemy_dmg(-1)
                    Magic(-20)
                    blast_cd1 = 60
                    Sans.hp -= 1
                    if Sans.hp == 0:
                        Magic(-30)
                    break
        elif bossphase == 3:
            for i2 in range(len(bullets[0])):
                if bullets[0][i2].colliderect(boss):
                    if char == "uspaps":
                        if bullets[0][i2].turn != "block":
                            bullets[0].pop(i2)
                            if bossphase == 3:
                                take_dmg()
                                break
                    else:
                        if bullets[0][i2].image != "Slash" and char != "frisk":
                            bullets[0].pop(i2)
                        if char == "paps":
                            just_a_ghost()
                        elif char == "frisk":
                            healing(3)
                        if bossphase == 3:
                            take_dmg()
                            break
            for i2 in range(len(bullets[1])):
                if bullets[1][i2].colliderect(boss):
                    bullets[1].pop(i2)
                    if bossphase == 3:
                        take_dmg()
                        break
            for i2 in range(len(bullets[2])):
                if bullets[2][i2].colliderect(boss):
                    bullets[2].pop(i2)
                    if bossphase == 3:
                        take_dmg()
                        break
    for i in range(len(attacks)):
        if soul.colliderect(attacks[i]):
            if attacks[i].types != "hit":
                if (attacks[i].types != "bluebone" and attacks[i].types != "bluebonerush" and attacks[i].types != "bluepuzzle") or (keyboard.w or keyboard.a or keyboard.s or keyboard.d):
                    if ((attacks[i].types == "blaster" or attacks[i].types == "slash") and attacks[i].w0 <= 0 and attacks[i].w1 <= 0) or (attacks[i].types != "blaster" and attacks[i].types != "slash"):
                        if inv <= 0:
                            if attacks[i].image == "RedSlash":
                                Blink.image = "999999"
                                blink = 45
                            else:
                                dmg()
                            if attacks[i].image == "HyperSideBone":
                                repeat -= 1
                                if repeat > 0:
                                    if attacks[i].direct == "right":
                                        attacks[i].x -= 1200
                                    else:
                                        attacks[i].x += 1200
                                    if repeat == 6 or repeat == 4 or repeat == 2:
                                        atk = Actor("BlasterWarn1", (soul.x, 225))
                                        atk.w0 = 0
                                        atk.w1 = 25
                                        atk.blast = 20
                                        atk.types = "blaster"
                                        attacks.append(atk)
                            else:
                                attacks.pop(i)
                            break
                        else:
                            miss.pos = (attacks[i].x,attacks[i].y - 50)
                            miss.dorge = 2
def dmg():
    global hp
    global mode
    global bonus
    global coins
    global shield
    global notover
    global b_char
    global blast_char
    global d_char
    if shield:
        shield = False
    else:
        hp -= 1
        if hp <= 0:
            if (char == "sans" or char == "dtsans") and det > 0 and hp != -0.9:
                if det < 3:
                    hp = 0.1
                elif det == 3:
                    if char == "sans":
                        mode = "fakeend"
                        notover = "GAME OVER!"
                    elif hp < -5:
                        mode = 'end'
                        bon = 11
                        if level == "Сложность: средняя":
                            bon -= 1
                        elif level == "Сложность: сложная":
                            bon -= 2
                        if gamemode != "none":
                            bon -= 1
                        bonus = int(count / bon)
                        coins += bonus
                    else:
                        if cdboost:
                            b_char += 0.8
                            blast_char += 0.4
                            d_char += 0.8
                        else:
                            b_char += 1
                            blast_char += 0.5
                            d_char += 1
            elif char == "paps":
                mode = "yourend"
            else:
                mode = 'end'
                if level == "Сложность: лёгкая":
                    bonus = int(count / 10)
                elif level == "Сложность: средняя":
                    bonus = int(count / 9)
                elif level == "Сложность: сложная":
                    bonus = int(count / 8)
                coins += bonus
def on_mouse_down(button, pos):
    global stamina
    global b_st
    global blast_cd1
    global attackbuff
    global char
    global b_char
    global b_cd
    global b_cd1
    global ax
    global ghost
    global clickguide
    if mode == "game" and charging == False:
        if button == mouse.LEFT:
            if b_cd == "Кости готовы(лкм)" or b_cd == "Нож готов(лкм)":
                if stamina >= -50:
                    if char != "dtsans":
                        stamina -= b_st
                        if stamina < 0 and char != "paps":
                            stamina -= 5
                    if char == "sans":
                        bullet = Actor("Bone", soul.pos)
                        bullet1 = Actor("Bone", soul.pos)
                        bullet2 = Actor("Bone", soul.pos)
                        bullets[0].append(bullet)
                        bullets[1].append(bullet1)
                        bullets[2].append(bullet2)
                    elif char == "dust" and b_cd == "Нож готов(лкм)":
                        bullet = Actor("Slash", soul.pos)
                        bullet.time = 10
                        bullets[0].append(bullet)
                        for i in range(len(enemies)):
                            enemies[i].slash = True
                    elif char == "dust" and b_cd == "Кости готовы(лкм)":
                        bullet = Actor("Dustbone", (soul.x, 500))
                        bullets[2].append(bullet)
                    elif char == "uspaps":
                        stamina -= len(bullets[0]) * 1
                        if stamina < 0:
                            stamina -= 5
                        bullet = Actor("Bonetest", soul.pos)
                        bullet.turn = "up"
                        bullets[0].append(bullet)
                        if magic >= 250:
                            stamina -= 5
                            bullet = Actor("Bonetest", soul.pos)
                            bullet.turn = "down"
                            bullets[0].append(bullet)
                    elif char == "snowdust":
                        b = random.randint(1, 10)
                        if b == 1:
                            bullet = Actor("HyperBoneUp", (soul.x - 10, soul.y))
                        else:
                            bullet = Actor("JumpDustbone", (soul.x - 10, soul.y))
                        bullets[0].append(bullet)
                        b = random.randint(1, 10)
                        if b == 1:
                            bullet = Actor("HyperBoneUp", (soul.x + 10, soul.y))
                        else:
                            bullet = Actor("JumpDustbone", (soul.x + 10, soul.y))
                        bullets[0].append(bullet)
                    elif char == "paps":
                        bullet = Actor("PapsBone", soul.pos)
                        bullet.speed = 2 + hyper
                        bullets[0].append(bullet)
                    elif char == "dtsans":
                        if modeboss:
                            bullet = Actor("Bonejump", soul.pos)
                            bullet.speed = 18 + hp * 3
                            bullets[0].append(bullet)
                        else:
                            ax = 475
                            for i in range(24 + hp * 4):
                                b = random.randint(1, 10)
                                a = random.randint(10, 590)
                                if b <= 6 + hp:
                                    bullet = Actor("Bonejump", (a, ax))
                                else:
                                    bullet = Actor("Bluebonejump", (a, ax))
                                bullet.speed = 18 + hp * 3
                                bullets[0].append(bullet)
                                ax += 60
                    if stamina >= 0 or char == "paps":
                        b_cd1 = b_char
                        if magic >= 50:
                            b_cd1 -= 0.2
                    else:
                        b_cd1 = b_char * 2
                        if magic >= 50:
                            b_cd1 -= 0.4
            if b_cd == "Атака(лкм)":
                if weapon == "knife" or weapon == "stick":
                    bullet = Actor("SlashAnim1", (soul.x, soul.y - 40))
                    bullet.anim = ["SlashAnim1", "SlashAnim2", "SlashAnim3", "SlashAnim4", "SlashAnim5", "SlashAnim6", "SlashAnim7"]
                    bullet.types = "hit"
                    bullets[0].append(bullet)
                    for i in range(len(enemies)):
                        enemies[i].slash = True
                    b_cd1 = b_char
                elif weapon == "glove":
                    bullet = Actor("GloveAnim1", (soul.x + random.randint(-10, 10), soul.y - random.randint(40, 60)))
                    bullet.anim = ["GloveAnim1", "GloveAnim1", "GloveAnim2", "GloveAnim2", "GloveAnim1", "GloveAnim1"]
                    bullet.types = "hit"
                    bullets[0].append(bullet)
                    for i in range(len(enemies)):
                        enemies[i].slash = True
                    if attackbuff > 0:
                        b_cd1 = 0.2
                        attackbuff -= 1
                        if attackbuff <= 0:
                            blast_cd1 = b_char * 4
                    else:
                        b_cd1 = b_char
    elif mode == "menu":
        clickguide = 1
def update(dt):
    global mode
    global count
    global stamina
    global b_char
    global blast_char
    global d_char
    global b_st
    global blast_st
    global d_st
    global b_cd
    global b_cd1
    global blast_cd1
    global blast_cd
    global d_cd1
    global d_cd
    global char
    global speed
    global charge
    global charging
    if mode == 'game':
        global dorge
        enemy_soul()
        collisions()
        if inv > 0 and kill == 1:
            Souls()
        blast_last()
        energyrest()
        message()
        if char == "uspaps" and modeboss == False:
            magic_gain()
        if charging:
            charge -= 1
            if charge <= 0:
                ax = 475
                stamina -= 30
                bullet = Actor("SpecSpin1", soul.pos)
                bullet.hp = 3
                bullets[1].append(bullet)
                for i in range(20):
                    a = random.randint(10, 590)
                    bullet = Actor("JumpDustbone", (a, ax))
                    bullet.speed = 10
                    bullets[0].append(bullet)
                    ax += 60
                charging = False
        boss_atk()
        atkblink()
        for i in range(len(enemies)):
            if enemies[i].image == "BlueSoul":
                if enemies[i].y <= 0:
                    enemies[i].image = "FriskSoul"
                    enemies[i].angle = 0
        if char == "sans":
            for i in range(len(bullets[0])):
                if bullets[0][i].y < 0:
                    bullets[0].pop(i)
                    break
                else:
                    bullets[0][i].y -= 10
                    bullets[0][i].x -= 10
                    bullets[0][i].angle += 10
            for i in range(len(bullets[1])):
                if bullets[1][i].y < 0:
                    bullets[1].pop(i)
                    break
                else:
                    bullets[1][i].y -= 10
                    bullets[1][i].angle += 10
            for i in range(len(bullets[2])):
                if bullets[2][i].y < 0:
                    bullets[2].pop(i)
                    break
                else:
                    bullets[2][i].y -= 10
                    bullets[2][i].x += 10
                    bullets[2][i].angle += 10
        elif char == "uspaps":
            for i in range(len(bullets[0])):
                if bullets[0][i].y <= 15 and bullets[0][i].turn == "up":
                    bullets[0][i].turn = "down"
                elif bullets[0][i].y >= 435 and bullets[0][i].turn == "down":
                    bullets[0][i].turn = "up"
                if bullets[0][i].turn == "down":
                    bullets[0][i].y += 10
                elif bullets[0][i].turn == "up":
                    bullets[0][i].y -= 10
                elif bullets[0][i].turn == "block":
                    bullets[0][i].y = soul.y - 30
                    bullets[0][i].x = soul.x
        elif char == "paps":
            for i in range(len(bullets[0])):
                if bullets[0][i].y < 0:
                    bullets[0].pop(i)
                    break
                else:
                    bullets[0][i].y -= bullets[0][i].speed
        elif char == "dust":
            for i in range(len(bullets[0])):
                bullets[0][i].y -= lifetime / 10
                bullets[0][i].time -= 1
                if bullets[0][i].time <= 0:
                    bullets[0].pop(i)
                    break
            for i in range(len(bullets[1])):
                if bullets[1][i].y < 0:
                    bullets[1].pop(i)
                    break
                else:
                    bullets[1][i].y -= 10
            for i in range(len(bullets[2])):
                if bullets[2][i].y < 0:
                    bullets[2].pop(i)
                    break
                else:
                    bullets[2][i].y -= 10
                    bullets[2][i].angle += 10
        elif char == "snowdust":
            for i in range(len(bullets[0])):
                if bullets[0][i].y < 0:
                    bullets[0].pop(i)
                    break
                else:
                    bullets[0][i].y -= 10
            for i in range(len(bullets[1])):
                bullets[1][i].angle -= 20
        elif char == "dtsans":
            for i in range(len(bullets[0])):
                if bullets[0][i].y < 0:
                    bullets[0].pop(i)
                    break
                else:
                    bullets[0][i].y -= bullets[0][i].speed
        elif char == "frisk":
            for i in range(len(bullets[0])):
                if bullets[0][i].types == "hit":
                    bullets[0][i].anim.pop(0)
                    if len(bullets[0][i].anim) > 0:
                        bullets[0][i].image = bullets[0][i].anim[0]
                    else:
                        bullets[0].pop(i)
                        break
                elif bullets[0][i].types == "slash":
                    bullets[0][i].y -= bullets[0][i].speed
                    bullets[0][i].time -= 1
                    if bullets[0][i].time <= 0:
                        bullets[0].pop(i)
                        break
        if char == "dtsans":
            speed = 6 + hp
        else:
            if stamina >= 0 and charging == False:
                speed = 5
            else:
                speed = 2
        if speedboost:
            speed *= 1.2
        if blink <= 0:
            if keyboard.w and soul.y >= 25:
                if soul.image != "BlueSoul":
                    soul.y -= speed
            elif keyboard.s and soul.y <= 425:
                soul.y += speed
            if keyboard.a and soul.x >= 30:
                if soul.image != "SideSoul":
                    soul.x -= speed
            elif keyboard.d and soul.x <= 570:
                soul.x += speed
            if soul.image == "BlueSoul" and soul.y <= 430:
                soul.y += 10
            if soul.image == "SideSoul" and soul.x <= 580:
                soul.x += 10
def just_a_ghost():
    global ghost
    global d_cd
    ghost -= 1
    if ghost <= 0:
        d_cd = "Призрачная живучесть(пробел)"
    elif ghost == 5:
        d_cd = "Перезарядка: 5 атак"
    elif ghost == 1:
        d_cd = "Перезарядка: 1 атака"
    else:
        d_cd = "Перезарядка: " + str(ghost) + " атаки"
def healing(Heal):
    global heal
    global d_cd
    heal -= Heal
    if heal <= 0:
        d_cd = "Лечение(пробел)"
    else:
        d_cd = "Перезарядка(" + str(heal) + ")"
def Souls():
    global so
    global soul1
    global soul2
    global count
    c = []
    e = soul.x
    r = soul.y
    c.append(e)
    c.append(r)
    so.append(c)
    if len(so) >= 3:
        soul1.pos = (so[len(so) - 2][0], so[len(so) - 2][1])
    if len(so) >= 5:
        soul2.pos = (so[len(so) - 4][0], so[len(so) - 4][1])
    if len(so) > 3:
        so.pop(0)
def on_key_down(key):
    global mode
    global count
    global maxstamina
    global stamina
    global max_stamina
    global b_char
    global blast_char
    global d_char
    global b_st
    global blast_st
    global d_st
    global b_cd
    global b_cd1
    global blast_cd1
    global blast_cd
    global d_cd1
    global d_cd
    global char
    global level
    global diff
    global smin
    global smax
    global bosscount
    global soul
    global modeboss
    global achievments
    global max_hp
    global hp
    global dust
    global password
    global enemies
    global a
    global cod
    global lifetime
    global atkmode
    global lv
    global exp
    global exp_cap
    global cutscene
    global bossphase
    global coins
    global bossrush
    global det
    global boost
    global shield
    global speedboost
    global stamboost
    global cdboost
    global bosses
    global blx
    global bly
    global blast
    global dorge
    global inv
    global bl
    global dor_x
    global enraged
    global notover
    global HYPER
    global codetext
    global bullets
    global attacks
    global bonus
    global boss
    global ghost
    global ghost_hp
    global hyper
    global attacking
    global sans_assist
    global Sans
    global heal
    global charging
    global charge
    global special
    global kill
    global so
    global magic
    global gamemode
    global messages
    global chara
    global codemode
    global difficulty
    global heal
    global weapon
    global weapons
    global attackbuff
    global guide
    global clickguide
    if mode == "menu":
        if keyboard.k_1:
            mode = "char"
            guide = 0
            clickguide = 0
        elif keyboard.k_2:
            mode = "boost"
            guide = 0
            clickguide = 0
        elif keyboard.k_3:
            mode = "code"
            guide = 0
            clickguide = 0
        else:
            guide = 1
    elif mode == "char":
        if keyboard.k_1:
            if stamboost:
                maxstamina = 360
            else:
                maxstamina = 300
            stamina = maxstamina
            max_stamina = maxstamina
            if cdboost:
                b_char = 0.8
                blast_char = 6.4
                d_char = 4
            else:
                b_char = 1
                blast_char = 8
                d_char = 5
            b_st = 10
            blast_st = 10
            d_st = 10
            b_cd = "Кости готовы(лкм)"
            b_cd1 = 0
            blast_cd1 = 0
            blast_cd = "Бластер готов(e)"
            d_cd1 = d_char
            max_hp = 1
            hp = max_hp
            d_cd = "Уворот через:" + str(d_cd1)
            char = "sans"
            mode = "sans"
        elif keyboard.k_2:
            if stamboost:
                maxstamina = 264
            else:
                maxstamina = 220
            stamina = maxstamina
            max_stamina = maxstamina
            if cdboost:
                b_char = 1.2
                blast_char = 12
                d_char = 4
            else:
                b_char = 1.5
                blast_char = 15
                d_char = 5
            b_st = 12
            blast_st = 20
            d_st = 30
            b_cd = "Кости готовы(лкм)"
            b_cd1 = 0
            blast_cd1 = 0
            max_hp = 3
            hp = max_hp
            blast_cd = "Тако (e)"
            d_cd1 = d_char
            d_cd = "Блок через:" + str(d_cd1)
            char = "uspaps"
            mode = "uspaps"
        elif keyboard.k_3 and dust != 0:
            if stamboost:
                maxstamina = 120
            else:
                maxstamina = 100
            stamina = maxstamina
            max_stamina = maxstamina
            if cdboost:
                b_char = 4
                blast_char = 0.4
                d_char = 4
            else:
                b_char = 5
                blast_char = 0.5
                d_char = 5
            b_st = 3
            blast_st = 6
            d_st = 15
            b_cd = "Нож готов(лкм)"
            b_cd1 = 0
            blast_cd1 = 0
            max_hp = 1
            hp = max_hp
            lifetime = 100
            lv = 1
            exp = 0
            exp_cap = 10
            atkmode = False
            blast_cd = "Кости готовы(e)"
            d_cd1 = d_char
            d_cd = "Уворот через:" + str(d_cd1)
            char = "dust"
            mode = "dust"
        elif keyboard.k_4 and chara != 0:
            maxstamina = 0
            stamina = maxstamina
            max_stamina = maxstamina
            if cdboost:
                b_char = 2.4
            else:
                b_char = 3
            blast_char = 0
            d_char = 0
            b_st = 0
            blast_st = 0
            d_st = 0
            max_hp = 2
            hp = max_hp
            lv = 1
            exp = 0
            exp_cap = 10
            heal = 10
            b_cd1 = 0
            attackbuff = 0
            blast_cd1 = -1
            d_cd1 = -1
            weapon = "stick"
            weapons = ["stick"]
            b_cd = "Атака(лкм)"
            blast_cd = "Особая атака(e)"
            d_cd = "Перезарядка(10)"
            char = "frisk"
            mode = "frisk"
        elif keyboard.d:
            if level == "Сложность: лёгкая":
                level = "Сложность: средняя"
                diff = "yellow"
                smin = 5
                smax = 10
                bosscount = 75
                if bossrush:
                    bosscount -= 50
            elif level == "Сложность: средняя":
                level = "Сложность: сложная"
                diff = "red"
                smin = 8
                smax = 12
                bosscount = 100
                if bossrush:
                    bosscount -= 50
            elif level == "Сложность: сложная":
                level = "Сложность: лёгкая"
                diff = "white"
                smin = 2
                smax = 8
                bosscount = 50
                if bossrush:
                    bosscount -= 50
        elif keyboard.a:
            mode = "gamemode"
        elif keyboard.k_5:
            mode = "menu"
    elif mode == "gamemode":
        if keyboard.d:
            if gamemode == "boss":
                gamemode = "enemy"
            elif gamemode == "enemy":
                gamemode = "none"
            elif gamemode == "none":
                gamemode = "boss"
        elif keyboard.a:
            if gamemode == "boss":
                gamemode = "none"
            elif gamemode == "enemy":
                gamemode = "boss"
            elif gamemode == "none":
                gamemode = "enemy"
        elif keyboard.k_1:
            mode = "char"
    elif mode == "boost":
        if keyboard.k_1 and coins >= 10 and boost < 2 and shield == False:
            coins -= 10
            shield = True
            boost += 1
        elif keyboard.k_2 and coins >= 5 and boost < 2 and speedboost == False:
            coins -= 5
            speedboost = True
            boost += 1
        elif keyboard.k_3 and coins >= 7 and boost < 2 and stamboost == False:
            coins -= 7
            stamboost = True
            boost += 1
        elif keyboard.k_4 and coins >= 7 and boost < 2 and cdboost == False:
            coins -= 7
            cdboost = True
            boost += 1
        elif keyboard.k_5 and coins >= 10 and boost < 2 and bossrush == False:
            coins -= 10
            bosscount -= 50
            bossrush = True
            boost += 1
        elif keyboard.k_6 and coins >= 99:
            hyperboost.pop(0)
            if len(hyperboost) == 0:
                coins -= 99
                HYPER = True
                shield = False
                speedboost = False
                stamboost = False
                cdboost = False
                bossrush = False
                boost = 99
                smin = 8
                smax = 14
                level = "Сложность: #@&%$!"
                codetext = "Загляни в код"
                password = ["0", "9", "9", "0"]
        elif keyboard.k_7:
            mode = "menu"
    elif mode == "game":
        if charging == False:
            if keyboard.e:
                if blast_cd == "Бластер готов(e)":
                    blaster.image = "Blaster"
                    if char == "dtsans":
                        a = random.randint(25, 575)
                        blast = 2
                        blaster.x = a
                        blaster.y = 225
                        blast_cd1 = blast_char
                        for i in range(len(enemies)):
                            enemies[i].blast = True
                    else:
                        if stamina > -50:
                            stamina -= blast_st
                            for i in range(len(enemies)):
                                enemies[i].blast = True
                            if stamina < 0:
                                stamina -= 5
                            blast = 2
                            b = random.randint(1, 5)
                            if b == 1 and char == "snowdust":
                                blaster.image = "HyperBlast"
                            blaster.x = soul.x
                            blaster.y = soul.y - 245
                            if stamina > 0:
                                blast_cd1 = blast_char
                            else:
                                blast_cd1 = blast_char * 2
                if blast_cd == "Особая атака(e)":
                    if weapon == "stick":
                        bullet = Actor("SlashAnim1", (soul.x, soul.y - 60))
                        bullet.anim = ["SlashAnim1", "SlashAnim2", "SlashAnim3", "SlashAnim4", "SlashAnim5", "SlashAnim6", "SlashAnim7"]
                        bullet.types = "hit"
                        #bullet.speed = 4.5 + lv * 0.5
                        bullets[0].append(bullet)
                        for i in range(len(enemies)):
                            enemies[i].slash = True
                        blast_cd1 = b_char + 1
                    if weapon == "knife":
                        bullet = Actor("Slash", soul.pos)
                        bullet.time = 10
                        bullet.types = "slash"
                        bullet.speed = 5.5 + lv * 0.5
                        bullets[0].append(bullet)
                        for i in range(len(enemies)):
                            enemies[i].slash = True
                        blast_cd1 = b_char * 2
                    if weapon == "glove":
                        attackbuff = 4
                        blast_cd1 = 0.1
                elif blast_cd == "Кости готовы(e)":
                    if stamina > -50:
                        stamina -= blast_st
                        if stamina < 0:
                            stamina -= 5
                        for i in range(2):
                            a = random.randint(10, 590)
                            bullet = Actor("JumpDustbone", (a, 500))
                            bullets[1].append(bullet)
                        if stamina > 0:
                            blast_cd1 = blast_char
                        else:
                            blast_cd1 = blast_char * 2
                elif blast_cd == "Тако (e)" and sans_assist and magic >= 30:
                    Magic(-30)
                    hp += 1
                    if hp > max_hp:
                        hp = max_hp
                    stamina += 30
                    blast_cd1 = 60
            elif keyboard.space:
                if d_cd == "Уворот готов(space + a или d)":
                    if keyboard.a:
                        dor_x = soul.x - 200
                        if dor_x < 25:
                            dor_x = 25
                    elif keyboard.d:
                        dor_x = soul.x + 200
                        if dor_x > 575:
                            dor_x = 575
                    if dor_x != -50:
                        if stamina > -50:
                            stamina -= d_st
                            if stamina < 0:
                                stamina -= 5
                            animate(soul, tween ='decelerate', duration = 0.5, x = dor_x)
                            dorge = 0
                            dor_x = -50
                            kill = 0
                            so = []
                            b = random.randint(1, 5)
                            if b == 1 and char == "snowdust":
                                kill = 1
                            if stamina > 0:
                                d_cd1 = d_char
                            else:
                                d_cd1 = d_char * 2
                            inv = 0.5
                elif d_cd == "Блок готов(пробел)":
                    bl = "ready"
                    for i in range(len(bullets[0])):
                        if bullets[0][i].turn == "block":
                            bl = "used"
                            break
                    if bl == "ready" and stamina > -50:
                        stamina -= len(bullets[0]) * 1 + d_st
                        if stamina < 0:
                            stamina -= 5
                        bullet = Actor("Bonetest", soul.pos)
                        bullet.turn = "block"
                        bullets[0].append(bullet)
                        if magic >= 150:
                            bullet = Actor("Bonetest", soul.pos)
                            bullet.turn = "block"
                            bullets[0].append(bullet)
                elif d_cd == "Синяя душа готова(пробел)":
                    if stamina > -50:
                        stamina -= d_st
                        if stamina < 0:
                            stamina -= 5
                        for i in range(len(enemies)):
                            if enemies[i].image == "FriskSoul":
                                enemies[i].image = "BlueSoul"
                                enemies[i].angle = 180
                                animate(enemies[i], tween ='decelerate', duration = 1, y = -100)
                elif d_cd == "Отталкивание готово(пробел)":
                    for i in range(len(enemies)):
                        if enemies[i].image == "FriskSoul":
                            animate(enemies[i], tween ='decelerate', duration = 1 - hp * 0.5, y = enemies[i].y - 100 * (6 + hp))
                elif d_cd == "Призрачная живучесть(пробел)" and shield == False:
                    stamina -= d_st
                    hp += 1
                    if hp > max_hp:
                        hp = max_hp
                        shield = True
                    ghost = ghost_hp
                    just_a_ghost()
                elif d_cd == "Лечение(пробел)":
                    hp += 1
                    if hp > max_hp:
                        hp = max_hp
                    heal = 11
                    healing(1)
                if stamina > 0:
                    d_cd1 = d_char
                    if magic >= 50:
                        d_cd1 -= 1
                elif char != "paps" or char != "frisk":
                    d_cd1 = d_char * 2
                    if magic >= 50:
                        d_cd1 -= 2
            elif keyboard.w and soul.image == "BlueSoul" and soul.y >= 425:
                animate(soul, tween ='decelerate', duration = 1, y = soul.y - 135)
            elif keyboard.a and soul.image == "SideSoul" and soul.x >= 575:
                animate(soul, tween ='decelerate', duration = 1, x = soul.x - 135)
            elif keyboard.q:
                if char == "dust":
                    if atkmode == False:
                        atkmode = True
                        if cdboost:
                            b_char = 2
                            blast_char = 4
                            d_char = 6
                        else:
                            b_char = 2.5
                            blast_char = 5
                            d_char = 7.5
                            b_st = 10
                            blast_st = 10
                            d_st = 20
                            if b_cd == "Нож готов(лкм)":
                                b_cd = "Кости готовы(лкм)"
                            if blast_cd == "Кости готовы(e)":
                                blast_cd = "Бластер готов(e)"
                            if d_cd == "Уворот готов(space + a или d)":
                                d_cd = "Синяя душа готова(пробел)"
                    else:
                        atkmode = False
                        if cdboost:
                            b_char = 4.2 - 0.2 * lv
                            blast_char = 0.4
                            d_char = 4
                        else:
                            b_char = 5.2 - 0.2 * lv
                            blast_char = 0.5
                            d_char = 5
                        b_st = 3
                        blast_st = 6
                        d_st = 15
                        if b_cd == "Кости готовы(лкм)":
                            b_cd = "Нож готов(лкм)"
                        if blast_cd == "Бластер готов(e)":
                            blast_cd = "Кости готовы(e)"
                        if d_cd == "Синяя душа готова(пробел)":
                            d_cd = "Уворот готов(space + a или d)"
                elif char == "snowdust" and special >= 50:
                    charging = True
                    charge = 90
                    special = 0
                elif char == "frisk":
                    if weapon == "stick" and lv >= 3:
                        weapon = "knife"
                        if cdboost:
                            b_char = 1.9 - 0.1 * lv
                        else:
                            b_char = 2.3 - 0.1 * lv
                    elif weapon == "knife" and lv >= 6:
                        weapon = "glove"
                        if cdboost:
                            b_char = 1.2
                        else:
                            b_char = 1.5
                    elif weapon == "knife" and lv < 6:
                        weapon = "stick"
                        if cdboost:
                            b_char = 2.5 - 0.1 * lv
                        else:
                            b_char = 3.1 - 0.1 * lv
                    elif weapon == "glove":
                        weapon = "stick"
                        if cdboost:
                            b_char = 2.5 - 0.1 * lv
                        else:
                            b_char = 3.1 - 0.1 * lv
                elif char == "uspaps" and sans_assist == False and blast_cd1 <= 0:
                    sans_assist = True
        if keyboard.k_1 and cutscene != 0:
            dialogs.pop(0)
            if len(dialogs) == 0:
                if cutscene == 1 or cutscene == 9:
                    bossphase = 1
                    d_cd1 = 0.1
                    blast_cd = "Текущий босс - Dusttale Санс"
                    b_cd = "Босс атакует..."
                elif cutscene == 2:
                    count += 10
                    b_cd1 = 0.1
                    blast_cd1 = 0.1
                    d_cd1 = 0.1
                    if level == "Сложность: лёгкая":
                        achiev = "Dusttale Санс на лёгкой сложности побеждён(Код: 0457)"
                    if level == "Сложность: средняя":
                        achiev = "Dusttale Санс на средней сложности побеждён(Код: 1342)"
                    if level == "Сложность: сложная":
                        achiev = "Dusttale Санс на сложной сложности побеждён(Код: 8452)"
                    achievments.append(achiev)
                    enemies = []
                    bosscount += 100
                    if level == "Сложность: средняя":
                        bosscount += 50
                    if level == "Сложность: сложная":
                        bosscount += 100
                    if bossrush:
                        bosscount -= 50
                    bosses += 1
                    modeboss = False
                    for i in range(5):
                        new_enemy()
                elif cutscene == 3:
                    bossphase = 1
                    d_cd1 = 0.1
                    blast_cd = "Текущий босс - Санс?"
                    b_cd = "Босс атакует..."
                elif cutscene == 4:
                    bossphase = 3
                    enraged = True
                    d_cd1 = 0.1
                    blast_cd = "Текущий босс - Решительный Санс"
                    b_cd1 = 0.1
                elif cutscene == 5:
                    count += 25
                    b_cd1 = 0.1
                    blast_cd1 = 0.1
                    d_cd1 = 0.1
                    if level == "Сложность: лёгкая":
                        achiev = "Санс? на лёгкой сложности побеждён(Код: 4692)"
                    if level == "Сложность: средняя":
                        achiev = "Санс? на средней сложности побеждён(Код: 9261)"
                    if level == "Сложность: сложная":
                        achiev = "Санс? на сложной сложности побеждён(Код: 0927)"
                    achievments.append(achiev)
                    enemies = []
                    bosses += 1
                    modeboss = False
                    for i in range(5):
                        new_enemy()
                elif cutscene == 6:
                    bossphase = 3
                    b_cd1 = 0.1
                    blast_cd = "ГИПЕРDUST Санс"
                    ghost += 1
                    just_a_ghost()
                elif cutscene == 7:
                    bossphase = 1
                    b_cd = "Босс атакует..."
                    blast_cd = "ГИПЕРDUST Санс"
                    ghost += 1
                    just_a_ghost()
                elif cutscene == 8:
                    mode = "menu"
                    HYPER = False
                    modeboss = False
                    level = "Сложность: лёгкая"
                    diff = "white"
                    soul.image == "Soul"
                    smin = 2
                    smax = 8
                    bosscount = 50
                    enemies = []
                    for i in range(5):
                        new_enemy()
                elif cutscene == 10:
                    count += 15
                    b_cd1 = 0.1
                    blast_cd1 = 0.1
                    d_cd1 = 0.1
                    if level == "Сложность: лёгкая":
                        achiev = "Dusttale Санс на лёгкой сложности побеждён(Код: 3859)"
                    if level == "Сложность: средняя":
                        achiev = "Dusttale Санс на средней сложности побеждён(Код: 1937)"
                    if level == "Сложность: сложная":
                        achiev = "Dusttale Санс на сложной сложности побеждён(Код: 0602)"
                    achievments.append(achiev)
                    enemies = []
                    bosscount += 100
                    if level == "Сложность: средняя":
                        bosscount += 50
                    if level == "Сложность: сложная":
                        bosscount += 100
                    if bossrush:
                        bosscount -= 50
                    bosses += 1
                    modeboss = False
                    for i in range(5):
                        new_enemy()
                cutscene = 0
    elif mode == "end":
        if keyboard.k_1:
            modeboss = False
            enemies = []
            for i in range(5):
                new_enemy()
            bullets = [[], [], []]
            attacks = []
            messages = []
            count = 0
            special = 0
            magic = 0
            soul.pos = (300, 400)
            b_cd1 = 1
            Blink.image = "Blink"
            blast_cd = 1
            bonus = 0
            d_cd = d_char
            heal = 0
            sans_assist = False
            Sans.hp = 3
            soul.image = "Soul"
            codetext = "Достижения - 3"
            if HYPER:
                mode = "menu?"
                level = "Сложность: ад"
                diff = (255, 0, 255)
                codetext = "Ввести код - 3"
            else:
                mode = "menu"
            if level == "Сложность: лёгкая":
                bosscount = 50
            elif level == "Сложность: средняя":
                bosscount = 75
            elif level == "Сложность: сложная":
                bosscount = 100
            bosses = 0
            atkmode = False
            shield = False
            speedboost = False
            stamboost = False
            cdboost = False
            bossrush = False
            enraged = False
            charging = False
            boost = 0
            for i in range(len(achievments)):
                if achievments[i] == "Dusttale Санс на лёгкой сложности побеждён(Код: 0457)":
                    if dust < 1:
                        dust = 1
                elif achievments[i] == "Dusttale Санс на средней сложности побеждён(Код: 1342)":
                    if dust < 2:
                        dust = 2
                elif achievments[i] == "Dusttale Санс на сложной сложности побеждён(Код: 8452)":
                    if dust < 3:
                        dust = 3
                if achievments[i] == "Dusttale Санс на лёгкой сложности побеждён(Код: 3859)":
                    if dust < 4:
                        dust = 4
                elif achievments[i] == "Dusttale Санс на средней сложности побеждён(Код: 1937)":
                    if dust < 5:
                        dust = 5
                elif achievments[i] == "Dusttale Санс на сложной сложности побеждён(Код: 0602)":
                    if dust < 6:
                        dust = 6
                if achievments[i] == "Санс? на лёгкой сложности побеждён(Код: 4692)":
                    if det < 1:
                        det = 1
                elif achievments[i] == "Санс? на средней сложности побеждён(Код: 9261)":
                    if det < 2:
                        det = 2
                elif achievments[i] == "Санс? на сложной сложности побеждён(Код: 0927)":
                    if det < 3:
                        det = 3
                if achievments[i] == "Storyshift Чара на лёгкой сложности (Код: 1834)":
                    if chara < 1:
                        chara = 1
                elif achievments[i] == "Storyshift Чара на средней сложности (Код: 2536)":
                    if chara < 2:
                        chara = 2
                elif achievments[i] == "Storyshift Чара на сложной сложности (Код: 9374)":
                    if chara < 3:
                        chara = 3
            achievments = []
    elif mode == "fakeend":
        if keyboard.k_1:
            if notover == "GAME OVER!":
                notover = "Вы отказываетесь."
            elif notover == "Вы отказываетесь.":
                if cdboost:
                    b_char = 8
                    blast_char = 2
                    d_char = 8
                else:
                    b_char = 10
                    blast_char = 2.5
                    d_char = 10
                if modeboss == False:
                    b_cd = "Кости готовы(лкм)"
                    blast_cd = "Бластер готов(e)"
                d_cd = "Уворот через:" + str(d_cd1)
                b_cd1 = 0
                blast_cd1 = 0
                d_cd1 = d_char
                stamina = 20
                char = "dtsans"
                mode = "game"
                bullets = [[], [], []]
    elif mode == "code":
        if keyboard.k_1:
            for i in range(4):
                if password[i] == "-":
                    password[i] = "1"
                    break
        if keyboard.k_2:
            for i in range(4):
                if password[i] == "-":
                    password[i] = "2"
                    break
        if keyboard.k_3:
            for i in range(4):
                if password[i] == "-":
                    password[i] = "3"
                    break
        if keyboard.k_4:
            for i in range(4):
                if password[i] == "-":
                    password[i] = "4"
                    break
        if keyboard.k_5:
            for i in range(4):
                if password[i] == "-":
                    password[i] = "5"
                    break
        if keyboard.k_6:
            for i in range(4):
                if password[i] == "-":
                    password[i] = "6"
                    break
        if keyboard.k_7:
            for i in range(4):
                if password[i] == "-":
                    password[i] = "7"
                    break
        if keyboard.k_8:
            for i in range(4):
                if password[i] == "-":
                    password[i] = "8"
                    break
        if keyboard.k_9:
            for i in range(4):
                if password[i] == "-":
                    password[i] = "9"
                    break
        if keyboard.k_0:
            for i in range(4):
                if password[i] == "-":
                    password[i] = "0"
                    break
        if keyboard.backspace:
            for i in range(4):
                if password[i] != "-":
                    a = i
            password[a] = "-"
        if keyboard.enter:
            if password == ["0", "4", "5", "7"]:
                if dust < 1:
                    dust = 1
                    cod = "Код принят"
                else:
                    cod = "Код этого или более сложного достижения уже был введён."
            elif password == ["1", "3", "4", "2"]:
                if dust < 2:
                    dust = 2
                    cod = "Код принят"
                else:
                    cod = "Код этого или более сложного достижения уже был введён."
            elif password == ["8", "4", "5", "2"]:
                if dust < 3:
                    dust = 3
                    cod = "Код принят"
                else:
                    cod = "Код этого или более сложного достижения уже был введён."
            elif password == ["3", "8", "5", "9"]:
                if dust < 4:
                    dust = 4
                    cod = "Код принят"
                else:
                    cod = "Код этого или более сложного достижения уже был введён."
            elif password == ["1", "9", "3", "7"]:
                if dust < 5:
                    dust = 5
                    cod = "Код принят"
                else:
                    cod = "Код этого или более сложного достижения уже был введён."
            elif password == ["0", "6", "0", "2"]:
                if dust < 6:
                    dust = 6
                    cod = "Код принят"
                else:
                    cod = "Код этого или более сложного достижения уже был введён."
            elif password == ["4", "6", "9", "2"]:
                if det < 1:
                    det = 1
                    cod = "Код принят"
                else:
                    cod = "Код этого или более сложного достижения уже был введён."
            elif password == ["9", "2", "6", "1"]:
                if det < 2:
                    det = 2
                    cod = "Код принят"
                else:
                    cod = "Код этого или более сложного достижения уже был введён."
            elif password == ["0", "9", "2", "7"]:
                if det < 3:
                    det = 3
                    cod = "Код принят"
                else:
                    cod = "Код этого или более сложного достижения уже был введён."
            elif password == ["1", "8", "3", "4"]:
                if chara < 1:
                    chara = 1
                    cod = "Код принят"
                else:
                    cod = "Код этого или более сложного достижения уже был введён."
            elif password == ["2", "5", "3", "6"]:
                if chara < 2:
                    chara = 2
                    cod = "Код принят"
                else:
                    cod = "Код этого или более сложного достижения уже был введён."
            elif password == ["9", "3", "7", "4"]:
                if chara < 3:
                    chara = 3
                    cod = "Код принят"
                else:
                    cod = "Код этого или более сложного достижения уже был введён."
            elif password == ["4", "9", "1", "0"]:
                if hyper < 1:
                    hyper = 1
                    cod = "Сколько всего неизвестного..."
                else:
                    cod = "Столько всего недосказанного..."
            elif password == ["0", "9", "9", "0"]:
                if HYPER == False:
                    HYPER = True
                    shield = False
                    speedboost = False
                    stamboost = False
                    cdboost = False
                    bossrush = False
                    boost = 99
                    smin = 8
                    smax = 14
                    level = "Сложность: #@&%$!"
                    cod = "..."
                else:
                    cod = "Это бесполезно."
            else:
                cod = " "
            password = ["-", "-", "-", "-"]
        if keyboard.a:
            codemode -= 1
            if codemode < 1:
                codemode = 3
        if keyboard.d:
            codemode += 1
            if codemode > 3:
                codemode = 1
        if keyboard.e:
            mode = "menu"
            cod = " "
            codemode = 1
    elif mode == "menu?":
        if keyboard.k_1:
            mode = "char?"
        elif keyboard.k_2:
            mode = "boost?"
        elif keyboard.k_3:
            mode = "code?"
    elif mode == "char?":
        if keyboard.k_1:
            mode = "sans?"
        elif keyboard.k_2:
            mode = "uspaps?"
        elif keyboard.k_3 and dust != 0:
            mode = "dust?"
        elif keyboard.k_4 and chara != 0:
            mode = "frisk?"
        elif keyboard.k_5:
            mode = "menu?"
    elif mode == "boost?":
        if keyboard.k_7:
            mode = "menu?"
    elif mode == "code?":
        if keyboard.k_1:
            for i in range(4):
                if password[i] == "-":
                    password[i] = "1"
                    break
        if keyboard.k_2:
            for i in range(4):
                if password[i] == "-":
                    password[i] = "2"
                    break
        if keyboard.k_3:
            for i in range(4):
                if password[i] == "-":
                    password[i] = "3"
                    break
        if keyboard.k_4:
            for i in range(4):
                if password[i] == "-":
                    password[i] = "4"
                    break
        if keyboard.k_5:
            for i in range(4):
                if password[i] == "-":
                    password[i] = "5"
                    break
        if keyboard.k_6:
            for i in range(4):
                if password[i] == "-":
                    password[i] = "6"
                    break
        if keyboard.k_7:
            for i in range(4):
                if password[i] == "-":
                    password[i] = "7"
                    break
        if keyboard.k_8:
            for i in range(4):
                if password[i] == "-":
                    password[i] = "8"
                    break
        if keyboard.k_9:
            for i in range(4):
                if password[i] == "-":
                    password[i] = "9"
                    break
        if keyboard.k_0:
            for i in range(4):
                if password[i] == "-":
                    password[i] = "0"
                    break
        if keyboard.backspace:
            for i in range(4):
                if password[i] != "-":
                    a = i
            password[a] = "-"
        if keyboard.enter:
            if password == ["0", "4", "5", "7"]:
                if dust < 1:
                    dust = 1
                cod = "Он был только на начале пути."
            elif password == ["1", "3", "4", "2"]:
                if dust < 2:
                    dust = 2
                cod = "Такой слабый... Хочет всё и вся."
            elif password == ["8", "4", "5", "2"]:
                if dust < 3:
                    dust = 3
                cod = "Он бежит. Как трус, каким всегда и был."
            elif password == ["3", "8", "5", "9"]:
                if dust < 4:
                    dust = 4
                cod = "Нас связывает только путь."
            elif password == ["1", "9", "3", "7"]:
                if dust < 5:
                    dust = 5
                cod = "Одинаковый путь. Разные цели."
            elif password == ["0", "6", "0", "2"]:
                if dust < 6:
                    dust = 6
                cod = "Печально, что его старания ничего не дали."
            elif password == ["4", "6", "9", "2"]:
                if det < 1:
                    det = 1
                cod = "Он знал много. Слишком много"
            elif password == ["9", "2", "6", "1"]:
                if det < 2:
                    det = 2
                cod = "У него была сила, но он не знал, как ею пользоваться."
            elif password == ["0", "9", "2", "7"]:
                if det < 3:
                    det = 3
                cod = "Ты здесь не случайно, да?."
            elif password == ["1", "8", "3", "4"]:
                if chara < 1:
                    chara = 1
                cod = '"Человек"... Как я ненавижу это слово.'
            elif password == ["2", "5", "3", "6"]:
                if chara < 2:
                    chara = 2
                cod = "Они слишком полагаются на свою силу."
            elif password == ["9", "3", "7", "4"]:
                if chara < 3:
                    chara = 3
                cod = "Их сила... Несравнима с моей."
            elif password == ["0", "9", "9", "0"]:
                cod = "Это бесполезно."
            elif password == ["4", "9", "1", "0"]:
                if hyper < 1:
                    cod = "Так ты здесь не новый? Интересно..."
                    hyper = 1
                else:
                    cod = "Да, да, мы поняли."
            elif password == ["7", "3", "5", "6"]:
                maxstamina = 1 + hyper
                stamina = maxstamina
                max_stamina = maxstamina
                b_char = 5 - hyper
                blast_char = 0
                d_char = 0
                b_st = 1
                blast_st = 0
                d_st = 3
                b_cd1 = 0
                blast_cd1 = -1
                d_cd1 = -1
                b_cd = "Кости готовы(лкм)"
                blast_cd = "..."
                d_cd = "Призрачная живучесть(пробел)"
                max_hp = 2 + hyper
                hp = 1 + hyper
                ghost_hp = 6 - hyper
                char = "paps"
                mode = "paps"
            else:
                cod = " "
            password = ["-", "-", "-", "-"]
        if keyboard.e:
            mode = "menu?"
            cod = " "
    elif mode == "sans" or mode == "uspaps" or mode == "dust" or mode == "paps" or mode == "snowdust" or mode == "frisk":
        if keyboard.k_1:
            if mode == "dust":
                soul.image = "Weakdust"
            elif mode == "snowdust":
                soul.image = "Snowdindust"
            elif mode == "frisk":
                soul.image = "FriskChar"
            elif mode == "paps":
                soul.image = "Phantom"
                boss = Actor("HYPER", (300, -100))
                boss.dorge = 0
                boss.block = 9
                boss.hp = 99
                attacking = ["hyperbonerush", "rushallsides", "hypersidebone"]
                modeboss = True
                boss.speed = 5
                enemies = []
                enemies.append(boss)
                bossphase = 0
                bosses = 99
            mode = "game"
            if level == "Сложность: лёгкая":
                difficulty = 1
            elif level == "Сложность: средняя":
                difficulty = 2
            elif level == "Сложность: сложная":
                difficulty = 3
            if count == bosscount and HYPER == False:
                bosstime()
            if level == "Сложность: #@&%$!":
                for i in range(len(enemies)):
                    enemies.pop(0)
                new_enemy()
        if keyboard.k_2:
            if mode == "paps":
                mode = "char?"
            else:
                mode = "char"
        if keyboard.k_3:
            if mode == "uspaps":
                mode = "mechanics"
            if mode == "frisk":
                mode = "friskmechanics"
            elif mode == "dust" and dust >= 6:
                if stamboost:
                    maxstamina = 156
                else:
                    maxstamina = 130
                stamina = maxstamina
                max_stamina = maxstamina
                if cdboost:
                    b_char = 0.8
                    blast_char = 4
                    d_char = 4.8
                else:
                    b_char = 1
                    blast_char = 5
                    d_char = 6
                b_st = 7
                blast_st = 10
                d_st = 15
                b_cd = "Кости готовы(лкм)"
                b_cd1 = 0
                blast_cd1 = 0
                max_hp = 2
                hp = max_hp
                lv = 6
                exp = 0
                exp_cap = 10
                kill = 0
                blast_cd = "Бластер готов(e)"
                d_cd1 = d_char
                d_cd = "Уворот через:" + str(d_cd1)
                char = "snowdust"
                mode = "snowdust"
            elif mode == "snowdust":
                mode = "dustmechanics"
    elif mode == "mechanics":
        if keyboard.k_1:
            mode = "uspaps"
    elif mode == "friskmechanics":
        if keyboard.k_1:
            mode = "frisk"
    elif mode == "dustmechanics":
        if keyboard.k_1:
            mode = "snowdust"
    elif mode != "yourend":
        if keyboard.k_2:
            mode = "char?"
