import pygame as pg
from random import randint
import time
from screeninfo import get_monitors

#-----------------------------------------------------------------

for m in get_monitors():
    WIDTH = m.width
    HEIGHT = m.height
kDeffh = round((HEIGHT / 17) / 16)
kDeffw = round((WIDTH / 27) / 16)
if kDeffw < kDeffh:
    kDeff = kDeffw
else:
    kDeff = kDeffh
hMap = 16 * kDeff


#-----------------------------------------------------------------

FPS = 60
BLACK = (0, 0, 0)

#-----------------------------------------------------------------

pg.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Подземелья библиотеки СФУ")
clock = pg.time.Clock()
surf = pg.Surface((WIDTH, HEIGHT))

#-----------------------------------------------------------------

data = str(*open("forGame/dataFiles/data.txt", 'r'))
mapBuildingProgress = str(*open("forGame/dataFiles/mapBuildingProgress.txt", 'r')).split(',')
tileMap = str(*open("forGame/dataFiles/tileMap.txt", 'r')).split(';')
kolMap = str(*open("forGame/dataFiles/kolMap.txt", 'r')).split(',')

for i in range(0, 25):
    mapBuildingProgress[i] = mapBuildingProgress[i].split('.')
    tileMap[i] = tileMap[i].split(',')
    kolMap[i] = kolMap[i].split('.')


#-----------------------------------------------------------------

icon = pg.image.load("forGame/images/icon.png")
pg.display.set_icon(icon)

#-----------------------------------------------------------------

heroD = pg.image.load("forGame/images/hero_d.png")
heroD = pg.transform.scale(heroD, (hMap , hMap))
heroD.set_colorkey((255, 255, 255))
heroD1 = pg.image.load("forGame/images/hero_d_1.png")
heroD1 = pg.transform.scale(heroD1, (hMap , hMap))
heroD1.set_colorkey((255, 255, 255))
heroD2 = pg.image.load("forGame/images/hero_d_2.png")
heroD2 = pg.transform.scale(heroD2, (hMap , hMap))
heroD2.set_colorkey((255, 255, 255))
heroU = pg.image.load("forGame/images/hero_u.png")
heroU = pg.transform.scale(heroU, (hMap , hMap))
heroU.set_colorkey((255, 255, 255))
heroU1 = pg.image.load("forGame/images/hero_u_1.png")
heroU1 = pg.transform.scale(heroU1, (hMap , hMap))
heroU1.set_colorkey((255, 255, 255))
heroU2 = pg.image.load("forGame/images/hero_u_2.png")
heroU2 = pg.transform.scale(heroU2, (hMap , hMap))
heroU2.set_colorkey((255, 255, 255))
heroR = pg.image.load("forGame/images/hero_r.png")
heroR = pg.transform.scale(heroR, (hMap , hMap))
heroR.set_colorkey((255, 255, 255))
heroR1 = pg.image.load("forGame/images/hero_r_1.png")
heroR1 = pg.transform.scale(heroR1, (hMap , hMap))
heroR1.set_colorkey((255, 255, 255))
heroR2 = pg.image.load("forGame/images/hero_r_2.png")
heroR2 = pg.transform.scale(heroR2, (hMap , hMap))
heroR2.set_colorkey((255, 255, 255))
heroL = pg.image.load("forGame/images/hero_l.png")
heroL = pg.transform.scale(heroL, (hMap , hMap))
heroL.set_colorkey((255, 255, 255))
heroL1 = pg.image.load("forGame/images/hero_l_1.png")
heroL1 = pg.transform.scale(heroL1, (hMap , hMap))
heroL1.set_colorkey((255, 255, 255))
heroL2 = pg.image.load("forGame/images/hero_l_2.png")
heroL2 = pg.transform.scale(heroL2, (hMap , hMap))
heroL2.set_colorkey((255, 255, 255))


wall_b = pg.image.load("forGame/images/wall_b.png")
wall_b = pg.transform.scale(wall_b, (hMap , hMap))
wall_b.set_colorkey((255, 255, 255))
wall_dop_l = pg.image.load("forGame/images/wall_dop_l.png")
wall_dop_l = pg.transform.scale(wall_dop_l, (hMap , hMap))
wall_dop_l.set_colorkey((255, 255, 255))
wall_dop_r = pg.image.load("forGame/images/wall_dop_r.png")
wall_dop_r = pg.transform.scale(wall_dop_r, (hMap , hMap))
wall_dop_r.set_colorkey((255, 255, 255))
wall_f = pg.image.load("forGame/images/wall_f.png")
wall_f = pg.transform.scale(wall_f, (hMap , hMap))
wall_k = pg.image.load("forGame/images/wall_k.png")
wall_k = pg.transform.scale(wall_k, (hMap , hMap))
wall_l = pg.image.load("forGame/images/wall_l.png")
wall_l = pg.transform.scale(wall_l, (hMap , hMap))
wall_l.set_colorkey((255, 255, 255))
wall_r = pg.image.load("forGame/images/wall_r.png")
wall_r = pg.transform.scale(wall_r, (hMap , hMap))
wall_r.set_colorkey((255, 255, 255))
wall_r_dop = pg.image.load("forGame/images/wall_r_dop.png")
wall_r_dop = pg.transform.scale(wall_r_dop, (hMap , hMap))
wall_r_dop.set_colorkey((255, 255, 255))
wall_l_dop = pg.image.load("forGame/images/wall_l_dop.png")
wall_l_dop = pg.transform.scale(wall_l_dop, (hMap , hMap))
wall_l_dop.set_colorkey((255, 255, 255))
wall_dop_l_r = pg.image.load("forGame/images/wall_dop_l_r.png")
wall_dop_l_r = pg.transform.scale(wall_dop_l_r, (hMap , hMap))
wall_dop_l_r.set_colorkey((255, 255, 255))
wall_book_2 = pg.image.load("forGame/images/wall_book_2.png")
wall_book_2 = pg.transform.scale(wall_book_2, (hMap , hMap))
wall_book_1 = pg.image.load("forGame/images/wall_book_1.png")
wall_book_1 = pg.transform.scale(wall_book_1, (hMap , hMap))
door_1 = pg.image.load("forGame/images/door_1.png")
door_1 = pg.transform.scale(door_1, (hMap , hMap))
door_1.set_colorkey((255, 255, 255))
door_2 = pg.image.load("forGame/images/door_2.png")
door_2 = pg.transform.scale(door_2, (hMap , hMap))
door_2.set_colorkey((255, 255, 255))
door_1_2 = pg.image.load("forGame/images/door_1_2.png")
door_1_2 = pg.transform.scale(door_1_2, (hMap , hMap))
door_1_2.set_colorkey((255, 255, 255))
door_2_2 = pg.image.load("forGame/images/door_2_2.png")
door_2_2 = pg.transform.scale(door_2_2, (hMap , hMap))
door_o_1 = pg.image.load("forGame/images/door_o_1.png")
door_o_1 = pg.transform.scale(door_o_1, (hMap , hMap))
door_o_1.set_colorkey((255, 255, 255))
door_o_2 = pg.image.load("forGame/images/door_o_2.png")
door_o_2 = pg.transform.scale(door_o_2, (hMap , hMap))
door_o_2.set_colorkey((255, 255, 255))
door_o_1_2 = pg.image.load("forGame/images/door_o_1_2.png")
door_o_1_2 = pg.transform.scale(door_o_1_2, (hMap , hMap))
door_o_1_2.set_colorkey((255, 255, 255))
door_o_2_2 = pg.image.load("forGame/images/door_o_2_2.png")
door_o_2_2 = pg.transform.scale(door_o_2_2, (hMap , hMap))


floor_1 = pg.image.load("forGame/images/floor_1.png")
floor_1 = pg.transform.scale(floor_1, (hMap , hMap))
floor_2 = pg.image.load("forGame/images/floor_2.png")
floor_2 = pg.transform.scale(floor_2, (hMap , hMap))
floor_3 = pg.image.load("forGame/images/floor_3.png")
floor_3 = pg.transform.scale(floor_3, (hMap , hMap))
floor_w = pg.image.load("forGame/images/floor_w.png")
floor_w = pg.transform.scale(floor_w, (hMap , hMap))
floor_w_2 = pg.image.load("forGame/images/floor_w_2.png")
floor_w_2 = pg.transform.scale(floor_w_2, (hMap , hMap))
floor_d = pg.image.load("forGame/images/floor_d.png")
floor_d = pg.transform.scale(floor_d, (hMap , hMap))
floor_f = pg.image.load("forGame/images/floor_f.png")
floor_f = pg.transform.scale(floor_f, (hMap , hMap))
floor_4 = pg.image.load("forGame/images/floor_4.png")
floor_4 = pg.transform.scale(floor_4, (hMap , hMap))
floor_e = pg.image.load("forGame/images/floor_e.png")
floor_e = pg.transform.scale(floor_e, (hMap , hMap))
floor_s = pg.image.load("forGame/images/floor_s.png")
floor_s = pg.transform.scale(floor_s, (hMap , hMap))
floor_b = pg.image.load("forGame/images/floor_b.png")
floor_b = pg.transform.scale(floor_b, (hMap , hMap))


IfonPad = pg.image.load("forGame/images/fonPad.png")
IfonPad = pg.transform.scale(IfonPad, (432 * kDeff , 272 * kDeff))
screen_home = pg.image.load("forGame/images/screen_home.png")
screen_home = pg.transform.scale(screen_home, (432 * kDeff , 272 * kDeff))
for_screen_home_pad = pg.image.load("forGame/images/for_screen_home_pad.png")
for_screen_home_pad = pg.transform.scale(for_screen_home_pad, (432 * kDeff , 284 * kDeff))
forFonPad = pg.image.load("forGame/images/forFonPad.png")
forFonPad = pg.transform.scale(forFonPad, (238 * kDeff , 16 * kDeff))
forFonPad.set_colorkey((0, 0, 0))
forFonSpusk = pg.image.load("forGame/images/forFonSpusk.png")
forFonSpusk = pg.transform.scale(forFonSpusk, (220 * kDeff , 16 * kDeff))
forFonSpusk.set_colorkey((0, 0, 0))
forFonPod = pg.image.load("forGame/images/forFonPod.png")
forFonPod = pg.transform.scale(forFonPod, (234 * kDeff , 16 * kDeff))
forFonPod.set_colorkey((0, 0, 0))

forInfoExit = pg.image.load("forGame/images/forInfoExit.png")
forInfoExit = pg.transform.scale(forInfoExit, (304 * kDeff , 144 * kDeff))
forInfoExit.set_colorkey((255, 255, 254))
forInfoDead = pg.image.load("forGame/images/forInfoDead.png")
forInfoDead = pg.transform.scale(forInfoDead, (304 * kDeff , 144 * kDeff))
forInfoDead.set_colorkey((255, 255, 254))
forInfoWin = pg.image.load("forGame/images/forInfoWin.png")
forInfoWin = pg.transform.scale(forInfoWin, (304 * kDeff , 144 * kDeff))
forInfoWin.set_colorkey((255, 255, 254))
forInfoSett = pg.image.load("forGame/images/forInfoSett.png")
forInfoSett = pg.transform.scale(forInfoSett, (304 * kDeff , 144 * kDeff))
forInfoSett.set_colorkey((255, 255, 254))
forInfoStart = pg.image.load("forGame/images/forInfoStart.png")
forInfoStart = pg.transform.scale(forInfoStart, (304 * kDeff , 144 * kDeff))
forInfoStart.set_colorkey((255, 255, 254))
fonProlog = pg.image.load("forGame/images/fonProlog.png")
fonProlog = pg.transform.scale(fonProlog, (432 * kDeff , 284 * kDeff))
fonKey = pg.image.load("forGame/images/fonKey.png")
fonKey = pg.transform.scale(fonKey, (432 * kDeff , 284 * kDeff))
fonEnd = pg.image.load("forGame/images/fonEnd.png")
fonEnd = pg.transform.scale(fonEnd, (432 * kDeff , 284 * kDeff))


v0 = pg.image.load("forGame/images/v0.png") 
v0 = pg.transform.scale(v0, (64 * kDeff , 24 * kDeff))
v25 = pg.image.load("forGame/images/v25.png")
v25 = pg.transform.scale(v25, (64 * kDeff , 24 * kDeff))
v50 = pg.image.load("forGame/images/v50.png")
v50 = pg.transform.scale(v50, (64 * kDeff , 24 * kDeff))
v75 = pg.image.load("forGame/images/v75.png")
v75 = pg.transform.scale(v75, (64 * kDeff , 24 * kDeff))
v100 = pg.image.load("forGame/images/v100.png")
v100 = pg.transform.scale(v100, (64 * kDeff , 24 * kDeff))


unTerr = pg.image.load("forGame/images/unTerr.png")
unTerr = pg.transform.scale(unTerr, (hMap , hMap))

peper = pg.image.load("forGame/images/peper.png")
peper = pg.transform.scale(peper, (hMap , hMap))
peper.set_colorkey((255, 255, 255))

obelisk = pg.image.load("forGame/images/obelisk.png")
obelisk = pg.transform.scale(obelisk, (hMap , hMap))
obelisk.set_colorkey((0, 0, 0))

#-----------------------------------------------------------------

x = hMap
y = hMap
xst = 0
yst = 0
speed = kDeff
running = True
fullExit = False
right = False
left = False
up = False
down = False
step = 4
kill = False
flag = 1
wM = 27
hM = 17
n = 0
Map = [''] * hM
xs = 0
ys = 0
xe = 0
ye = 0
o = 2
xu=0
yu=0
xd=0
yd=0
wFW = 27 * hMap
hFW = 17 * hMap
forStart = True
hp = 2
nBooks = 25

vol = float(str(*open("forGame/dataFiles/settings.txt", 'r')))
pg.mixer.music.set_volume(vol)

if len(data) == 0:
    lvly = 1
    lvlx = 1
else:
    data = data.split(',')
    lvlx = int(data[0])
    lvly = int(data[1])
    hp = int(data[4])
    nBooks = int(data[5])

#-----------------------------------------------------------------

def read():
    
    global data, mapBuildingProgress, tileMap, kolMap, lvly, lvlx, hp, nBooks
    
    data = str(*open("forGame/dataFiles/data.txt", 'r'))
    mapBuildingProgress = str(*open("forGame/dataFiles/mapBuildingProgress.txt", 'r')).split(',')
    tileMap = str(*open("forGame/dataFiles/tileMap.txt", 'r')).split(';')
    kolMap = str(*open("forGame/dataFiles/kolMap.txt", 'r')).split(',')
    
    for i in range(0, 25):
        mapBuildingProgress[i] = mapBuildingProgress[i].split('.')
        tileMap[i] = tileMap[i].split(',')
        kolMap[i] = kolMap[i].split('.')

    if len(data) == 0:
        lvly = 1
        lvlx = 1
        hp = 2
    else:
        data = data.split(',')
        lvlx = int(data[0])
        lvly = int(data[1])
        hp = int(data[4])
        nBooks = int(data[5])

#-----------------------------------------------------------------

def forPadKod():
    
    global lvlx, lvly, hp, x, y, flag, step, xst, yst, hp
    
    hp -= 1
    if hp < 0:
        kills()
    else:
        while True:
            x = randint(1, 25)
            y = randint(1, 15)
            forKolMap = kolMap[((lvly - 1) * 5) + (lvlx - 1)]
            a = int(forKolMap[(y * 27) + x])
            if a == 1:
                x = x * hMap
                y = y * hMap
                break
        xst = x
        yst = y

#-----------------------------------------------------------------

def writePep():

    global lxlx, lvly, tileMap, nBooks, data, x, y, hp

    tileMap = str(*open("forGame/dataFiles/tileMap.txt", 'r')).split(';')
    tileMap[((lvly - 1) * 5) + (lvlx - 1)] = tileMap[((lvly - 1) * 5) + (lvlx - 1)].replace('peper', 'floor_1', 1)
    nBooks -= 1
    s = ''
    for n in range(0, 25):
        s += tileMap[n] + ';'
    tileMap = open("forGame/dataFiles/tileMap.txt", 'w')
    tileMap.write(s)
    tileMap.close() 
    tileMap = str(*open("forGame/dataFiles/tileMap.txt", 'r')).split(';')
    for n in range(0, 25):
        tileMap[n] = tileMap[n].split(',')
    data = open("forGame/dataFiles/data.txt", 'w')
    data.write(str(lvlx) + ',' + str(lvly) + ',' + str(x // hMap) + ',' + str(y // hMap) + ',' + str(hp) + ',' + str(nBooks))
    data = str(*open("forGame/dataFiles/data.txt", 'r')).split(',')

    if nBooks == 0:
        info(3)
    

def kills():

    global runing, x, y, n, data, fullExit
    
    exec(open("forGame/skripts/genMap.py").read())
    info(2)
    read()
    menu()
    if not(fullExit): 
        runing = True
        genMap(1)
        if not(len(data) == 0):
            x = int(data[2]) * hMap
            y = int(data[3]) * hMap
        sc.blit(heroD, (x, y - kDeff * 4))
        pg.display.update()
        running = True
        n = 4

#-----------------------------------------------------------------

def info(o):
    
    global runing, x, y, n, data, fullExit, nBooks, right, left, up, down

    mx = 0
    my = 0
    xst = x
    yst = y

    if o == 1:
        if nBooks > 0:
            sc.blit(forInfoExit, ((wFW // 2) - (152 * kDeff), (hFW // 2) - (72 * kDeff)))
            pg.display.update()
            pg.time.delay(2000)
            genMap(-1)
            pg.display.update()
        else:
            nBooks = 25
            '''if (int(str(*open("forGame/dataFiles/skore.txt", 'r')))) < ((len(str(*open("forGame/dataFiles/mapBuildingProgress.txt", 'r')).split('1'))) * (int((str(*open("forGame/dataFiles/data.txt", 'r')).split(','))[5])) * 0.5):
                f = open("forGame/dataFiles/skore.txt", 'w')
                f.write(str(int((len(str(*open("forGame/dataFiles/mapBuildingProgress.txt", 'r')).split('1'))) * (int((str(*open("forGame/dataFiles/data.txt", 'r')).split(','))[5])) * 0.5)))
                f.close()'''
            
            sc.blit(fonEnd, (0, 0))
            pg.display.update()
            flag = True
            while flag == True:
                for event in pg.event.get():
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if int(event.button) == 1:
                            if mx > 146 and mx < 285 and my > 194 and my < 223:
                                flag = False
                                exec(open("forGame/skripts/genMap.py").read())
                                read()
                                menu()
                                if not(fullExit): 
                                    runing = True
                                    genMap(1)
                                    if not(len(data) == 0):
                                        x = int(data[2]) * hMap
                                        y = int(data[3]) * hMap
                                    sc.blit(heroD, (x, y - kDeff * 4))
                                    pg.display.update()
                                    running = True
                                    n = 4
                    elif event.type == pg.MOUSEMOTION:
                        mx = int(event.pos[0]) // kDeff
                        my = int(event.pos[1]) // kDeff

    elif o == 2:
        sc.blit(forInfoDead, ((wFW // 2) - (152 * kDeff), (hFW // 2) - (72 * kDeff)))
        pg.display.update()
        pg.time.delay(2000)
        genMap(-1)
        pg.display.update()
    elif o == 3:
            sc.blit(forInfoWin, ((wFW // 2) - (152 * kDeff), (hFW // 2) - (72 * kDeff)))
            pg.display.update()
            pg.time.delay(2000)
            genMap(-1)
            pg.display.update()
    x = xst
    y = yst
    right = False
    left = False
    up = False
    down = False
    
#-----------------------------------------------------------------
    
def fonPad():
    pg.mixer.music.pause()
    for i in range(0, 16 * kDeff, kDeff // 2):
        sc.blit(IfonPad, (0, (-1 * i) // 2))
        sc.blit(forFonPad, ((wFW // 2) - (119 * kDeff), (hFW // 2) - (8 * kDeff)))
        pg.display.update()
        clock.tick(FPS)
        
def fonSpusk():
    pg.mixer.music.pause()
    for i in range(0, 16 * kDeff, speed // 2):
        sc.blit(IfonPad, (0, (-1 * i) // 2))
        sc.blit(forFonSpusk, ((wFW // 2) - (110 * kDeff), (hFW // 2) - (8 * kDeff)))
        pg.display.update()
        clock.tick(FPS)
        
def fonPod():
    pg.mixer.music.pause()
    for i in range(0, 16 * kDeff, speed // 2):
        sc.blit(IfonPad, (0, (-30 + i) // 2))
        sc.blit(forFonPod, ((wFW // 2) - (117 * kDeff), (hFW // 2) - (8 * kDeff)))
        pg.display.update()
        clock.tick(FPS)

#-----------------------------------------------------------------

def vek(mapVek):
    visMap = [[0, 1, 1, 1, 1, 1, 0],
              [1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1],
              [0, 1, 1, 1, 1, 1, 0]]
    if (mapVek[2][2] == 0 or mapVek[2][2] == 3) and (mapVek[2][3] == 0 or mapVek[2][3] == 3):
        visMap[0][1] = 0; visMap[0][2] = 0; visMap[1][2] = 0
    if (mapVek[2][4] == 0 or mapVek[2][4] == 3) and (mapVek[2][3] == 0 or mapVek[2][3] == 3):
        visMap[1][4] = 0; visMap[0][4] = 0; visMap[0][5] = 0
    if (mapVek[2][4] == 0 or mapVek[2][4] == 3) and (mapVek[3][4] == 0 or mapVek[3][4] == 3):
        visMap[2][5] = 0; visMap[2][6] = 0; visMap[1][6] = 0
    if (mapVek[3][4] == 0 or mapVek[3][4] == 3) and (mapVek[4][4] == 0 or mapVek[4][4] == 3):
        visMap[4][5] = 0; visMap[4][6] = 0; visMap[5][6] = 0
    if (mapVek[4][3] == 0 or mapVek[4][3] == 3) and (mapVek[4][4] == 0 or mapVek[4][4] == 3):
        visMap[5][4] = 0; visMap[6][4] = 0; visMap[6][5] = 0
    if (mapVek[4][3] == 0 or mapVek[4][3] == 3) and (mapVek[4][2] == 0 or mapVek[4][2] == 3):
        visMap[5][2] = 0; visMap[6][2] = 0; visMap[6][1] = 0
    if (mapVek[3][2] == 0 or mapVek[3][2] == 3) and (mapVek[4][2] == 0 or mapVek[4][2] == 3):
        visMap[4][1] = 0; visMap[4][0] = 0; visMap[5][0] = 0
    if (mapVek[2][2] == 0 or mapVek[2][2] == 3) and (mapVek[3][2] == 0 or mapVek[3][2] == 3):
        visMap[2][1] = 0; visMap[2][0] = 0; visMap[1][0] = 0
    if mapVek[2][2] == 0 or mapVek[2][2] == 3:
        visMap[0][0] = 0; visMap[0][1] = 0; visMap[1][0] = 0; visMap[1][1] = 0
    if mapVek[1][1] == 0 or mapVek[1][1] == 3:
        visMap[0][0] = 0
    if mapVek[2][4] == 0 or mapVek[2][4] == 3:
        visMap[1][5] = 0; visMap[0][5] = 0; visMap[1][6] = 0; visMap[0][6] = 0
    if mapVek[1][5] == 0 or mapVek[1][5] == 3:
        visMap[0][6] = 0
    if mapVek[4][4] == 0 or mapVek[4][4] == 3:
        visMap[5][5] = 0; visMap[5][6] = 0; visMap[6][5] = 0; visMap[6][6] = 0
    if mapVek[5][5] == 0 or mapVek[5][5] == 3:
        visMap[6][6] = 0
    if mapVek[4][2] == 0 or mapVek[4][2] == 3:
        visMap[5][0] = 0; visMap[5][1] = 0; visMap[6][0] = 0; visMap[6][1] = 0
    if mapVek[5][1] == 0 or mapVek[5][1] == 3:
        visMap[6][0] = 0
    if mapVek[2][3] == 0 or mapVek[2][3] == 3:
        visMap[1][3] = 0; visMap[0][3] = 0; visMap[0][2] = 0; visMap[0][4] = 0
    if mapVek[1][3] == 0 or mapVek[1][3] == 3:
        visMap[0][3] = 0
    if mapVek[3][2] == 0 or mapVek[3][2] == 3:
        visMap[3][1] = 0; visMap[3][0] = 0; visMap[2][0] = 0; visMap[4][0] = 0
    if mapVek[3][1] == 0 or mapVek[3][1] == 3:
        visMap[3][0] = 0
    if mapVek[4][3] == 0 or mapVek[4][3] == 3:
        visMap[5][3] = 0; visMap[6][3] = 0; visMap[6][2] = 0; visMap[6][4] = 0
    if mapVek[5][3] == 0 or mapVek[5][3] == 3:
        visMap[6][3] = 0
    if mapVek[3][4] == 0 or  mapVek[3][4] == 3:
        visMap[3][5] = 0; visMap[3][6] = 0; visMap[2][6] = 0; visMap[4][6] = 0
    if mapVek[3][5] == 0 or mapVek[3][5] == 3:
        visMap[3][6] = 0
    if mapVek[1][2] == 0 or mapVek[1][2] == 3:
        visMap[0][1] = 0
        visMap[0][2] = 0
    if mapVek[1][4] == 0 or mapVek[1][4] == 3:
        visMap[0][4] = 0
        visMap[0][5] = 0
    if mapVek[2][1] == 0 or mapVek[2][1] == 3:
        visMap[2][0] = 0
        visMap[1][0] = 0
    if mapVek[4][1] == 0 or mapVek[4][1] == 3:
        visMap[4][0] = 0
        visMap[5][0] = 0
    if mapVek[5][2] == 0 or mapVek[5][2] == 3:
        visMap[6][2] = 0
        visMap[6][1] = 0
    if mapVek[5][4] == 0 or mapVek[5][4] == 3:
        visMap[6][4] = 0
        visMap[6][5] = 0
    if mapVek[2][5] == 0 or mapVek[2][5] == 3:
        visMap[2][6] = 0
        visMap[1][6] = 0
    if mapVek[4][5] == 0 or mapVek[4][5] == 3:
        visMap[4][6] = 0
        visMap[5][6] = 0
    return visMap

#-----------------------------------------------------------------

def genMap(o):

    global xu, yu, xd, yd, x, y, xst, yst, xs, ys, xe, ye

    xu=0; yu=0; xd=0; yd=0; x = hMap; y = hMap; xst = x; yst = y; xs = 0; ys = 0; xe = 0; ye = 0

    if not(o == -1):
        a = randint(1, 3)
        if a == 1:
            pg.mixer.music.load('forGame/tracks/track_1.mp3')
            pg.mixer.music.play(-1)
        elif a == 2:
            pg.mixer.music.load('forGame/tracks/track_2.mp3')
            pg.mixer.music.play(-1)
        elif a == 3:
            pg.mixer.music.load('forGame/tracks/track_3.mp3')
            pg.mixer.music.play(-1)
    
    for my in range(0, 17):
        for mx in range(0, 27):
            sc.blit(unTerr, (mx * hMap, my * hMap))
            a = tileMap[((lvly - 1) * 5) + (lvlx - 1)][(my * 27) + mx].split('.')
            b = int(mapBuildingProgress[((lvly - 1) * 5) + (lvlx - 1)][(my * 27) + mx])
            for i in range(0, len(a)):
                if a[i] == 'floor_1':
                    if b == 1:
                        sc.blit(floor_1, (mx * hMap, my * hMap))
                elif a[i] =='floor_2':
                    if b == 1:
                        sc.blit(floor_2, (mx * hMap, my * hMap))
                elif a[i] == 'floor_3':
                    if b == 1:
                        sc.blit(floor_3, (mx * hMap, my * hMap))
                elif a[i] == 'floor_4':
                    if b == 1:
                        sc.blit(floor_4, (mx * hMap, my * hMap))
                elif a[i] == 'floor_w':
                    if b == 1:
                        sc.blit(floor_w, (mx * hMap, my * hMap))
                elif a[i] == 'floor_s':
                    if b == 1:
                        sc.blit(floor_s, (mx * hMap, my * hMap))
                    xs = mx * hMap
                    ys = my * hMap
                elif a[i] == 'floor_e':
                    if b == 1:
                        sc.blit(floor_e, (mx * hMap, my * hMap))
                    xe = mx * hMap
                    ye = my * hMap
                elif a[i] == 'floor_b':
                    if b == 1:
                        sc.blit(floor_b, (mx * hMap, my * hMap))
                elif a[i] == 'door_1':
                    if b == 1:
                        sc.blit(door_1, (mx * hMap, my * hMap))
                    if my == 0:
                        xu = mx * hMap
                        yu = my * hMap
                    elif my == 16:
                        xd = mx * hMap
                        yd = (my - 1) * hMap
                elif a[i] == 'door_1_2':
                    if b == 1:
                        sc.blit(door_1_2, (mx * hMap, my * hMap))
                elif a[i] == 'door_2_2':
                    if b == 1:
                        sc.blit(door_2_2, (mx * hMap, my * hMap))
                elif a[i] == 'floor_d':
                    if b == 1:
                        sc.blit(floor_d, (mx * hMap, my * hMap))
                elif a[i] == 'floor_f':
                    if b == 1:
                        sc.blit(floor_f, (mx * hMap, my * hMap))
                elif a[i] == 'floor_w_2':
                    if b == 1:
                        sc.blit(floor_w_2, (mx * hMap, my * hMap))
                elif a[i] == 'obelisk':
                    if b == 1:
                        sc.blit(obelisk, (mx * hMap, my * hMap))
                elif a[i] == 'wall_book_1':
                    if b == 1:
                        sc.blit(wall_book_1, (mx * hMap, my * hMap))
                elif a[i] == 'wall_book_2':
                    if b == 1:
                        sc.blit(wall_book_2, (mx * hMap, my * hMap))
                elif a[i] == 'wall_f':
                    if b == 1:
                        sc.blit(wall_f, (mx * hMap, my * hMap))
                elif a[i] == 'wall_k':
                    if b == 1:
                        sc.blit(wall_k, (mx * hMap, my * hMap))
                elif a[i] == 'door_2':
                    if b == 1:
                        sc.blit(door_2, (mx * hMap, my * hMap))
                elif a[i] == 'wall_b':
                    if b == 1:
                        sc.blit(wall_b, (mx * hMap, my * hMap))
                elif a[i] == 'wall_dop_l':
                    if b == 1:
                        sc.blit(wall_dop_l, (mx * hMap, my * hMap))
                elif a[i] == 'wall_dop_r':
                    if b == 1:
                        sc.blit(wall_dop_r, (mx * hMap, my * hMap))
                elif a[i] == 'wall_dop_l_r':
                    if b == 1:
                        sc.blit(wall_dop_l_r, (mx * hMap, my * hMap))
                elif a[i] == 'wall_l':
                    if b == 1:
                        sc.blit(wall_l, (mx * hMap, my * hMap))
                elif a[i] == 'wall_l_dop':
                    if b == 1:
                        sc.blit(wall_l_dop, (mx * hMap, my * hMap))
                elif a[i] == 'wall_r_dop':
                    if b == 1:
                        sc.blit(wall_r_dop, (mx * hMap, my * hMap))
                elif a[i] == 'wall_r':
                    if b == 1:
                        sc.blit(wall_r, (mx * hMap, my * hMap))
                elif a[i] == 'peper':
                    if b == 1:
                        sc.blit(peper, (mx * hMap, my * hMap))

    pg.display.update()

    if o == 1:
        x = xs
        y = ys
    elif o == 2:
        x = xe
        y = ye
    elif o == 3:
        x = xu
        y = yu
    elif o == 4:
        x = xd
        y = yd

#-----------------------------------------------------------------

def forPlay():
    sc.blit(forInfoStart, ((wFW // 2) - (152 * kDeff), (hFW // 2) - (72 * kDeff)))
        

def settings():

    global vol

    sc.blit(forInfoSett, ((wFW // 2) - (152 * kDeff), (hFW // 2) - (72 * kDeff)))
    
    if vol == 0:
        sc.blit(v0, (184 * kDeff, 121 * kDeff))
    elif vol == 0.25:
        sc.blit(v25, (184 * kDeff, 121 * kDeff))
    elif vol == 0.5:
        sc.blit(v50, (184 * kDeff, 121 * kDeff))
    elif vol == 0.75:
        sc.blit(v75, (184 * kDeff, 121 * kDeff))
    else:
        sc.blit(v100, (184 * kDeff, 121 * kDeff))
    

def menu():

    global running, x, y, n, fullExit, vol
    
    pg.mixer.music.load('forGame/tracks/track_home.mp3')
    pg.mixer.music.play(-1)
    
    fullExit = True
    setting = False
    information = False
    rekords = False
    play = False
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                fullExit = True
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if int(event.button) == 1:
                    if setting == False and information == False and rekords == False and play == False:
                        if x > 72 and x < 213 and y > 158 and y < 189:
                            play = True
                            b = False
                        #elif x > 218 and x < 359 and y > 158 and y < 189:
                        #    rekords = True
                        elif x > 72 and x < 213 and y > 194 and y < 225:
                            setting = True
                        #elif x > 218 and x < 359 and y > 194 and y < 225:
                        #    information = True
                        #    forMenu = 0
                        elif x > 145 and x < 286 and y > 230 and y < 261:
                            fullExit = True
                            running = False
                            pg.mixer.music.pause()
                    elif setting == True:
                        if x > 146 and x < 175 and y > 118 and y < 147:
                            vol -= 0.25
                            if vol < 0:
                                vol = 0
                            pg.mixer.music.set_volume(vol)
                        elif x > 256 and x < 285 and y > 118 and y < 147:
                            vol += 0.25
                            if vol > 1:
                                vol = 1
                            pg.mixer.music.set_volume(vol)
                        elif x > 146 and x < 285 and y > 153 and y < 182:
                            f = open("forGame/dataFiles/settings.txt", 'w')
                            f.write(str(vol))
                            f.close()
                            setting = False
                    elif play == True:
                        if x > 131 and x < 300 and y > 127 and y < 156:
                            running = False
                            fullExit = False
                            play = False
                            pg.mixer.music.pause()
                        elif x > 131 and x < 300 and y > 160 and y < 189:
                            sc.blit(fonProlog, (0, 0))
                            pg.display.update()
                            flag = True
                            while flag == True:
                                for event in pg.event.get():
                                    if event.type == pg.QUIT:
                                        fullExit = True
                                        running = False
                                        flag = False
                                    elif event.type == pg.MOUSEBUTTONDOWN:
                                        if int(event.button) == 1:
                                            if x > 146 and x < 285 and y > 194 and y < 223:
                                                flag = False
                                                pg.time.delay(100)
                                    elif event.type == pg.MOUSEMOTION:
                                        x = int(event.pos[0]) // kDeff
                                        y = int(event.pos[1]) // kDeff
                            running = False
                            fullExit = False
                            play = False
                            sc.blit(fonKey, (0, 0))
                            pg.display.update()
                            flag = True
                            while flag == True:
                                for event in pg.event.get():
                                    if event.type == pg.QUIT:
                                        fullExit = True
                                        running = False
                                        flag = False
                                    elif event.type == pg.MOUSEBUTTONDOWN:
                                        if int(event.button) == 1:
                                            if x > 146 and x < 285 and y > 194 and y < 223:
                                                flag = False
                                    elif event.type == pg.MOUSEMOTION:
                                        x = int(event.pos[0]) // kDeff
                                        y = int(event.pos[1]) // kDeff
                                                    
                            pg.mixer.music.pause()
                            exec(open("forGame/skripts/genMap.py").read())
                            read()
                            
            elif event.type == pg.MOUSEMOTION:
                x = int(event.pos[0]) // kDeff
                y = int(event.pos[1]) // kDeff
        sc.blit(for_screen_home_pad, (0, n))
        n -= 1
        if n < -12 * kDeff:
            n = 0
        sc.blit(screen_home, (0, 0))
        if setting == True:
            settings()
        elif play == True:
            forPlay()
        pg.display.update()
        clock.tick(FPS)
    running = True



#-----------------------------------------------------------------

menu()
if not(fullExit):
    genMap(1)
    if not(len(data) == 0):
        x = int(data[2]) * hMap
        y = int(data[3]) * hMap
    sc.blit(heroD, (x, y - kDeff * 4))
    pg.display.update()
    running = True
    n = 4
    
#-----------------------------------------------------------------

while running and not(fullExit):
    keys = pg.key.get_pressed()

    xOnMap = round(x / hMap)
    yOnMap = round(y / hMap)
    
    forKolMap = kolMap[((lvly - 1) * 5) + (lvlx - 1)]
    
    if yOnMap > 0:
        k6 = int(forKolMap[((yOnMap - 1) * 27) + xOnMap - 1])
        k7 = int(forKolMap[((yOnMap - 1) * 27) + xOnMap])
        k8 = int(forKolMap[((yOnMap - 1) * 27) + xOnMap + 1])
    else:
        k6 = 0
        k7 = 0
        k8 = 0
    if yOnMap < 16:
        k2 = int(forKolMap[((yOnMap + 1) * 27) + xOnMap + 1])
        k3 = int(forKolMap[((yOnMap + 1) * 27) + xOnMap])
        k4 = int(forKolMap[((yOnMap + 1) * 27) + xOnMap - 1])
    else:
        k2 = 0
        k3 = 0
        k4 = 0 
    k1 = int(forKolMap[(yOnMap * 27) + xOnMap + 1])
    k5 = int(forKolMap[(yOnMap * 27) + xOnMap - 1])

    if keys[pg.K_RIGHT] == True and right == False and left == False and k1 > 0:
        if k1 == 2:
            lvly += 1
            if lvly > 5:
                kill = True
                kills()
            fonPad()
            genMap(0)
            left = False; right = False; up = False; down = False
            forPadKod()
            forStart = True
        elif up == True and k8 == 1 and k7 == 1:
            right = True
            xst = x
            n = 1
            step = 1
            flag = 1
        elif down == True and k2 == 1 and k3 == 1:
            right = True
            xst = x
            n = 1
            step = 1
            flag = 1
        elif down == False and up == False:
            right = True
            xst = x
            n = 1
            step = 1
            flag = 1
    elif keys[pg.K_LEFT] == True and right == False and left == False and k5 > 0:
        if k5 == 2:
            lvly += 1
            if lvly > 5:
                kill = True
                kills()
            fonPad()
            genMap(0)
            left = False; right = False; up = False; down = False
            forPadKod()
            forStart = True
        elif up == True and k6 == 1 and k7 == 1:
            left = True
            xst = x
            n = 2
            step = 1
            flag = 1
        elif down == True and k4 == 1 and k3 == 1:
            left = True
            xst = x
            n = 2
            step = 1
            flag = 1
        elif down == False and up == False:
            left = True
            xst = x
            n = 2
            step = 1
            flag = 1
            
    if keys[pg.K_UP] == True and up == False and down == False and k7 > 0:
        if k7 == 2:
            lvly += 1
            if lvly > 5:
                kill = True
                kills()
            fonPad()
            genMap(0)
            left = False; right = False; up = False; down = False
            forPadKod()
            forStart = True
        elif right == True and k8 == 1 and k1 == 1:
            up = True
            yst = y
            n = 3
            step = 1
            flag = 1
        elif left == True and k6 == 1 and k5 == 1:
            up = True
            yst = y
            n = 3
            step = 1
            flag = 1
        elif left == False and right == False:
            up = True
            yst = y
            n = 3
            step = 1
            flag = 1
    elif keys[pg.K_DOWN] == True and up == False and down == False and k3 > 0:
        if k3 == 2:
            lvly += 1
            if lvly > 5:
                kill = True
                kills()
            fonPad()
            genMap(0)
            left = False; right = False; up = False; down = False
            forPadKod()
            forStart = True
        elif left == True and k4 == 1 and k5 == 1:
            down = True
            yst = y
            n = 4
            step = 1
            flag = 1
        elif right == True and k1 == 1 and k2 == 1:
            down = True
            yst = y
            n = 4
            step = 1
            flag = 1
        elif left == False and right == False:
            down = True
            yst = y
            n = 4
            step = 1
            flag = 1

    if x == xu and y == yu and up == True:
        lvlx -= 1
        genMap(4)
        left = False; right = False; up = False; down = False
    elif x == xd and y == yd and down == True:
        lvlx += 1
        genMap(3)
        left = False; right = False; up = False; down = False
        forStart = True
    
    if right == True or left == True or up == True or down == True:
        flag += 1
        if flag > 5:
            flag = 1
            step += 1
            if step > 4:
                step = 1
                    
        if right == True:
            if x - xst < hMap:
                x += speed
            else:
                right = False
        elif left == True:
            if xst - x < hMap:
                x -= speed
            else:
                left = False
        if up == True:
            if yst - y < hMap:
                y -= speed
            else:
                up = False
        elif down == True:
            if y - yst < hMap:
                y += speed
            else:
                down = False

    if x < 0:
        x = 0
        left = False
        step = 4
    elif x > WIDTH - hMap:
        x = WIDTH - hMap
        right = False
        step = 4
    if y < 0:
        y = 0
        up = False
        step = 4
    elif y > HEIGHT - hMap:
        y = HEIGHT - hMap
        down = False
        step = 4

    if True:

        visMap = [ [] ] * 7
        for i in range(0, 7):
            visMap[i] = [0] * 7
        for my in range(-3, 4):
            for mx in range(-3, 4):
                formx = (x // hMap) + mx
                formy = (y // hMap) + my
                if formy < hM and formy >= 0 and formx < wM and formx >= 0:
                    visMap[my + 3][mx + 3] = int(forKolMap[(formy * 27) + formx])
                else:
                    visMap[my + 3][mx + 3] = 0

        visMap = vek(visMap)
        forMapBP = mapBuildingProgress[((lvly - 1) * 5) + (lvlx - 1)]


        for my in range(-3, 4):
            for mx in range(-3, 4):
                formx = int((x / hMap) + mx)
                formy = int((y / hMap) + my)
                if formy < 17 and formy >= 0 and formx < 27 and formx >= 0 and visMap[my + 3][mx + 3] == 1:
                    a = tileMap[((lvly - 1) * 5) + (lvlx - 1)][(formy * 27) + formx].split('.')
                    b = int(mapBuildingProgress[((lvly - 1) * 5) + (lvlx - 1)][(formy * 27) + formx])
                    for i in range(0, len(a)):
                        if a[i] == 'floor_1':
                            if b == 1:
                                sc.blit(floor_1, (formx * hMap, formy * hMap))
                        elif a[i] =='floor_2':
                            if b == 1:
                                sc.blit(floor_2, (formx * hMap, formy * hMap))
                        elif a[i] == 'floor_3':
                            if b == 1:
                                sc.blit(floor_3, (formx * hMap, formy * hMap))
                        elif a[i] == 'floor_4':
                            if b == 1:
                                sc.blit(floor_4, (formx * hMap, formy * hMap))
                        elif a[i] == 'floor_w':
                            if b == 1:
                                sc.blit(floor_w, (formx * hMap, formy * hMap))
                        elif a[i] == 'floor_s':
                            if b == 1:
                                sc.blit(floor_s, (formx * hMap, formy * hMap))
                        elif a[i] == 'floor_e':
                            if b == 1:
                                sc.blit(floor_e, (formx * hMap, formy * hMap))
                        elif a[i] == 'floor_b':
                            if b == 1:
                                sc.blit(floor_b, (formx * hMap, formy * hMap))
                        elif a[i] == 'door_1':
                            if b == 1:
                                if (mx == 0 and my == 0) or  (mx == 0 and ((formy * hMap) - hMap < y) and ((formy * hMap) + hMap > y)):
                                    sc.blit(door_o_1, (formx * hMap, formy * hMap))
                                        
                                else:
                                    sc.blit(door_1, (formx * hMap, formy * hMap))
                                    sc.blit(door_2, (formx * hMap, (formy - 1) * hMap))
                        elif a[i] == 'door_2_2':
                            if b == 1:
                                if (mx == 0 and my == -1) or (my == -1 and ((formx * hMap) - hMap < x) and ((formx * hMap) + hMap > x)):
                                    sc.blit(door_o_2_2, (formx * hMap, formy * hMap))
                                else:
                                    sc.blit(door_2_2, (formx * hMap, formy * hMap))
                        elif a[i] == 'floor_d':
                            if b == 1:
                                sc.blit(floor_d, (formx * hMap, formy * hMap))
                        elif a[i] == 'floor_f':
                            if b == 1:
                                sc.blit(floor_f, (formx * hMap, formy * hMap))
                        elif a[i] == 'floor_w_2':
                            if b == 1:
                                sc.blit(floor_w_2, (formx * hMap, formy * hMap))
                        elif a[i] == 'obelisk':
                            if b == 1:
                                sc.blit(obelisk, (formx * hMap, formy * hMap))
                        elif a[i] == 'wall_book_1':
                            if b == 1:
                                sc.blit(wall_book_1, (formx * hMap, formy * hMap))
                        elif a[i] == 'wall_book_2':
                            if b == 1:
                                sc.blit(wall_book_2, (formx * hMap, formy * hMap))
                        elif a[i] == 'wall_f':
                            if b == 1:
                                sc.blit(wall_f, (formx * hMap, formy * hMap))
                        elif a[i] == 'wall_k':
                            if b == 1:
                                sc.blit(wall_k, (formx * hMap, formy * hMap))
                        elif a[i] == 'wall_l':
                            if b == 1:
                                sc.blit(wall_l, (formx * hMap, formy * hMap))
                        elif a[i] == 'wall_l_dop':
                            if b == 1:
                                sc.blit(wall_l_dop, (formx * hMap, formy * hMap))
                        elif a[i] == 'wall_r_dop':
                            if b == 1:
                                sc.blit(wall_r_dop, (formx * hMap, formy * hMap))
                        elif a[i] == 'wall_r':
                            if b == 1:
                                sc.blit(wall_r, (formx * hMap, formy * hMap))
                        elif a[i] == 'peper':
                            if b == 1:
                                if mx == 0 and my == 0:
                                    sc.blit(floor_1, (formx * hMap, formy * hMap))
                                    writePep()
                                else:
                                    sc.blit(peper, (formx * hMap, formy * hMap))
                    forMapBP[formx + (formy * wM)] = '1'
        mapBuildingProgress[((lvly - 1) * 5) + (lvlx - 1)] = forMapBP
        
        if right == True:
            if step == 1:
                sc.blit(heroR1, (x, y - kDeff * 4))
            elif step == 2:
                sc.blit(heroR, (x, y - kDeff * 4))
            elif step == 3:   
                sc.blit(heroR2, (x, y - kDeff * 4))
            else:
                sc.blit(heroR, (x, y - kDeff * 4))
        elif left == True:
            if step == 1:
                sc.blit(heroL1, (x, y - kDeff * 4))
            elif step == 2:
                sc.blit(heroL, (x, y - kDeff * 4))
            elif step == 3:
                sc.blit(heroL2, (x, y - kDeff * 4))
            else:
                sc.blit(heroL, (x, y - kDeff * 4))
        elif up == True:
            if step == 1:
                sc.blit(heroU1, (x, y - kDeff * 4))
            elif step == 2:
                sc.blit(heroU, (x, y - kDeff * 4))
            elif step == 3:
                sc.blit(heroU2, (x, y - kDeff * 4))
            else:
                sc.blit(heroU, (x, y - kDeff * 4))
        elif down == True:
            if step == 1:
                sc.blit(heroD1, (x, y - kDeff * 4))
            elif step == 2:
                sc.blit(heroD, (x, y - kDeff * 4))
            elif step == 3:
                sc.blit(heroD2, (x, y - kDeff * 4))
            else:
                sc.blit(heroD, (x, y - kDeff * 4))
        else:
            if n == 1:
                sc.blit(heroR, (x, y - kDeff * 4))
            elif n == 2:
                sc.blit(heroL, (x, y - kDeff * 4))
            elif n == 3:
                sc.blit(heroU, (x, y - kDeff * 4))
            elif n == 4:
                sc.blit(heroD, (x, y - kDeff * 4))

        for my in range(-3, 4):
            for mx in range(-3, 4):
                formx = int((x / hMap) + mx)
                formy = int((y / hMap) + my)
                if formy < 17 and formy >= 0 and formx < 27 and formx >= 0 and visMap[my + 3][mx + 3] == 1:
                    a = tileMap[((lvly - 1) * 5) + (lvlx - 1)][(formy * 27) + formx].split('.')
                    b = int(mapBuildingProgress[((lvly - 1) * 5) + (lvlx - 1)][(formy * 27) + formx])
                    for i in range(0, len(a)):
                        if a[i] == 'door_2':
                            if b == 1:
                                if (mx == 0 and my == -1) or  (mx == 0 and (((formy + 1) * hMap) - hMap < y) and (((formy + 1) * hMap) + hMap > y)):
                                    sc.blit(door_o_2, (formx * hMap, formy * hMap))
                                else:
                                    sc.blit(door_2, (formx * hMap, formy * hMap))
                        elif a[i] == 'wall_b':
                            if b == 1:
                                sc.blit(wall_b, (formx * hMap, formy * hMap))
                        elif a[i] == 'wall_dop_l':
                            if b == 1:
                                sc.blit(wall_dop_l, (formx * hMap, formy * hMap))
                        elif a[i] == 'wall_dop_r':
                            if b == 1:
                                sc.blit(wall_dop_r, (formx * hMap, formy * hMap))
                        elif a[i] == 'wall_dop_l_r':
                            if b == 1:
                                sc.blit(wall_dop_l_r, (formx * hMap, formy * hMap))
                        elif a[i] == 'door_1_2':
                            if b == 1:
                                if (mx == 0 and my == 0) or (my == 0 and ((formx * hMap) - hMap < x) and ((formx * hMap) + hMap > x)):
                                    sc.blit(door_o_1_2, (formx * hMap, formy * hMap))
                                else:
                                    sc.blit(door_1_2, (formx * hMap, formy * hMap))


        if x == xs and y == ys and (up == True or down == True or right == True or left == True):
            lvly -= 1
            if lvly < 1:
                lvly = 1
                if forStart == False:
                    info(1)
            else:
                fonPod()
                genMap(2)
                left = False; right = False; up = False; down = False
                forStart = True
                x = xe
                y = ye
                xst = x
                yst = y
        elif x == xe and y == ye and (up == True or down == True or right == True or left == True):
            lvly += 1
            if lvly > 5:
                lvly = 5
            else:
                fonSpusk()
                genMap(1)
                left = False; right = False; up = False; down = False
                forStart = True
        elif kill == True:
            kills()
            
        forStart = False

        pg.display.update()

    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            data = open("forGame/dataFiles/data.txt", 'w')
            data.write(str(lvlx) + ',' + str(lvly) + ',' + str(x // hMap) + ',' + str(y // hMap) + ',' + str(hp) + ',' + str(nBooks))
            data.close()
            f = ''
            for i in range(0, 25):
                for k in range(0, 459):
                    f += str(int(mapBuildingProgress[i][k])) + '.'
                f = f[:(918 * (i + 1))] + ','
            mapBuildingProgress = open("forGame/dataFiles/mapBuildingProgress.txt", 'w')
            mapBuildingProgress.write(f)
            mapBuildingProgress.close()
            menu()
            if not(fullExit):
                data = str(*open("forGame/dataFiles/data.txt", 'r')).split(',')
                mapBuildingProgress = str(*open("forGame/dataFiles/mapBuildingProgress.txt", 'r')).split(',')
                tileMap = str(*open("forGame/dataFiles/tileMap.txt", 'r')).split(';')
                kolMap = str(*open("forGame/dataFiles/kolMap.txt", 'r')).split(',')

                for i in range(0, 25):
                    mapBuildingProgress[i] = mapBuildingProgress[i].split('.')
                    tileMap[i] = tileMap[i].split(',')
                    kolMap[i] = kolMap[i].split('.')
                genMap(1)
                if len(data) == 6:
                    x = int(data[2]) * hMap
                    y = int(data[3]) * hMap
                sc.blit(heroD, (x, y - kDeff * 4))
                pg.display.update()
                running = True
                n = 4
    
    clock.tick(FPS)


pg.mixer.music.pause()
pg.quit()


        
