from random import randint

tileMap = open("forGame/dataFiles/tileMap.txt", "w")
mapBuildingProgress = open("forGame/dataFiles/mapBuildingProgress.txt", "w")
kolMap = open("forGame/dataFiles/kolMap.txt", "w")
data = open("forGame/dataFiles/data.txt", "w")
mapColor = str(*open("forGame/dataFiles/mapColor.txt", "r")).split('.')

Map = [ [ [] ] ] * 25
for i in range(0, 25):
    Map[i] = [ [] ] * 17
    for ii in range(0, 17):
        Map[i][ii] = [0] * 27

for i in range(0, 25):
    mapColor[i] = mapColor[i].split(',')

forTileMap = [ [ [] ] ] * 25
for i in range(0, 25):
    forTileMap[i] = [ [] ] * 17
    for ii in range(0, 17):
        forTileMap[i][ii] = [''] * 27

for n in range(0, 25):
    for y in range(0, 17):
        for x in range(0, 27):
            
            forM = mapColor[n][(y * 27) + x]

            if y == 0:
                if x == 0:
                    forTileMap[n][y][x] += 'wall_r.'
                    Map[n][y][x] = 0
                elif x == 26:
                    forTileMap[n][y][x] += 'wall_l.'
                    Map[n][y][x] = 0
                elif forM == '000000':
                    if mapColor[n][((y + 1) * 27) + x] == '000000' or mapColor[n][((y + 1) * 27) + x] == 'e6000a':
                        forTileMap[n][y][x] += 'wall_r.wall_l.'
                        Map[n][y][x] = 0
                    else:
                        if randint(1, 4) == 4:
                            forTileMap[n][y][x] += 'wall_k.'
                        else:
                            forTileMap[n][y][x] += 'wall_f.'
                    Map[n][y][x] = 0
                elif forM == 'ff006e':
                    forTileMap[n][y][x] += 'door_1.'
                    Map[n][y][x] = 3
                elif forM == '00ffff':
                    if randint(1, 2) == 2:
                        forTileMap[n][y][x] += 'wall_book_1.'
                    else:
                        forTileMap[n][y][x] += 'wall_book_2.'
                    Map[n][y][x] = 0
            elif y == 16:
                if x == 0:
                    forTileMap[n][y][x] += 'wall_r.'
                    Map[n][y][x] = 0
                elif x == 26:
                    forTileMap[n][y][x] += 'wall_l.'
                    Map[n][y][x] = 0
                elif forM == 'ff006e':
                    forTileMap[n][y][x] += 'door_1.'
                    forTileMap[n][y - 1][x] += 'door_2.'
                    Map[n][y][x] = 3
                else:
                    forTileMap[n][y][x] += 'wall_f.'
                    Map[n][y][x] = 0
            elif x == 0:
                if mapColor[n][((y + 1) * 27) + x + 1] == '000000' or mapColor[n][((y + 1) * 27) + x + 1] == 'e6000a' or mapColor[n][((y + 1) * 27) + x + 1] == '00ffff':
                    forTileMap[n][y][x] += 'wall_r_dop.'
                else:
                    forTileMap[n][y][x] += 'wall_r.'
                Map[n][y][x] = 0
                    
            elif x == 26:
                if mapColor[n][((y + 1) * 27) + x - 1] == '000000' or mapColor[n][((y + 1) * 27) + x - 1] == 'e6000a' or mapColor[n][((y + 1) * 27) + x - 1] == '00ffff':
                    forTileMap[n][y][x] += 'wall_l_dop.'
                else:
                    forTileMap[n][y][x] += 'wall_l.'
                Map[n][y][x] = 0
            else:
                if forM == 'b6ff00':
                    forTileMap[n][y][x] += 'obelisk.'
                    Map[n][y][x] = 0
                elif forM == '00ffff':
                    if randint(1, 2) == 2:
                        forTileMap[n][y][x] += 'wall_book_1.'
                    else:
                        forTileMap[n][y][x] += 'wall_book_2.'
                    Map[n][y][x] = 0
                elif forM == 'e6000a':
                    if mapColor[n][((y + 1) * 27) + x] == '000000':
                        forTileMap[n][y][x] += 'floor_1.door_1_2.'
                    else:
                        forTileMap[n][y][x] += 'door_1.'
                        forTileMap[n][y - 1][x] += 'door_2.'
                    Map[n][y][x] = 3
                elif forM == 'ffffff' or forM == '7f0000' or forM == '404040' or forM == 'ffd800' or forM == 'ff6a00':
                    if forM == 'ffffff':
                        a = randint(1, 8)
                        if a == 1:
                            forTileMap[n][y][x] += 'floor_1.'
                        elif a > 1 and a < 5:
                            forTileMap[n][y][x] += 'floor_2.'
                        elif a > 4 and a < 8:
                            forTileMap[n][y][x] += 'floor_3.'
                        elif a == 8:
                            forTileMap[n][y][x] += 'floor_4.'
                        Map[n][y][x] = 1
                    elif forM == '7f0000':
                        forTileMap[n][y][x] += 'floor_w.'
                        Map[n][y][x] = 1
                    elif forM == '404040':
                        if mapColor[n][((y - 1) * 27) + x] == '000000':
                            forTileMap[n][y][x] += 'floor_d.'
                        elif mapColor[n][((y - 1) * 27) + x] == '7f0000':
                            forTileMap[n][y][x] += 'floor_w_2.'
                        elif mapColor[n][((y - 1) * 27) + x] == 'ffffff' or mapColor[n][((y - 1) * 27) + x] == '00ffff':
                            forTileMap[n][y][x] += 'floor_f.'
                        else:
                            forTileMap[n][y][x] += 'floor_b.'
                        Map[n][y][x] = 2
                    elif forM == 'ffd800':
                        forTileMap[n][y][x] += 'floor_e.'
                        Map[n][y][x] = 1
                    elif forM == 'ff6a00':
                        forTileMap[n][y][x] += 'floor_s.'
                        Map[n][y][x] = 1
                    if mapColor[n][((y + 1) * 27) + x] == '000000' or mapColor[n][((y + 1) * 27) + x] == '00ffff':
                        if (mapColor[n][((y + 1) * 27) + x + 1] == '000000' or mapColor[n][((y + 1) * 27) + x + 1] == '00ffff')\
                           and (mapColor[n][((y + 1) * 27) + x - 1] == '000000' or mapColor[n][((y + 1) * 27) + x - 1] == '00ffff'):
                            forTileMap[n][y][x] += 'wall_b.'
                        elif mapColor[n][((y + 1) * 27) + x + 1] == '000000' or mapColor[n][((y + 1) * 27) + x + 1] == '00ffff':
                            forTileMap[n][y][x] += 'wall_dop_l.'
                        elif mapColor[n][((y + 1) * 27) + x - 1] == '000000' or mapColor[n][((y + 1) * 27) + x - 1] == '00ffff':
                            forTileMap[n][y][x] += 'wall_dop_r.'
                        else:
                            forTileMap[n][y][x] += 'wall_dop_l_r.'
                if forM == '000000':
                    if (mapColor[n][((y + 1) * 27) + x] == '000000' or mapColor[n][((y + 1) * 27) + x] == '00ffff')\
                        and (mapColor[n][((y + 1) * 27) + x + 1] == '000000' or mapColor[n][((y + 1) * 27) + x + 1] == '00ffff')\
                        and (mapColor[n][((y + 1) * 27) + x - 1] == '000000' or mapColor[n][((y + 1) * 27) + x - 1] == '00ffff'):
                        forTileMap[n][y][x] += 'wall_r_dop.wall_l_dop.'
                    elif (mapColor[n][((y + 1) * 27) + x] == '000000' or mapColor[n][((y + 1) * 27) + x] == '00ffff')\
                        and (mapColor[n][((y + 1) * 27) + x + 1] == '000000' or mapColor[n][((y + 1) * 27) + x + 1] == '00ffff'):
                        forTileMap[n][y][x] += 'wall_r_dop.wall_l.'
                    elif (mapColor[n][((y + 1) * 27) + x] == '000000' or mapColor[n][((y + 1) * 27) + x] == '00ffff')\
                        and (mapColor[n][((y + 1) * 27) + x - 1] == '000000' or mapColor[n][((y + 1) * 27) + x - 1] == '00ffff'):
                        forTileMap[n][y][x] += 'wall_r.wall_l_dop.'
                    elif mapColor[n][((y + 1) * 27) + x] == '000000' or mapColor[n][((y + 1) * 27) + x] == '00ffff':
                        forTileMap[n][y][x] += 'wall_r.wall_l.'
                    elif mapColor[n][((y + 1) * 27) + x] == 'e6000a':
                        forTileMap[n][y][x] += 'door_2_2.'
                    elif (mapColor[n][(y * 27) + x + 1] == '000000' or mapColor[n][(y * 27) + x + 1] == '00ffff')\
                        and (mapColor[n][(y * 27) + x - 1] == '000000' or mapColor[n][(y * 27) + x - 1] == '00ffff'):
                        if randint(1, 4) == 4:
                            forTileMap[n][y][x] += 'wall_k.'
                        else:
                            forTileMap[n][y][x] += 'wall_f.'
                    else:
                        if randint(1, 4) == 4:
                            forTileMap[n][y][x] += 'wall_k.'
                        else:
                            forTileMap[n][y][x] += 'wall_f.'
                    Map[n][y][x] = 0
                if forM == '808080':
                    forTileMap[n][y][x] += 'peper.'
                    Map[n][y][x] = 8

s = ''
for n in range(0, 25):
    for y in range(0, 17):
        for x in range(0, 27):
            s += forTileMap[n][y][x] + ','
    s += ';'
tileMap.write(s)
tileMap.close()
    
s = ''
for n in range(0, 25):
    for y in range(0, 17):
        for x in range(0, 27):
            s += str(Map[n][y][x]) + '.'
    s += ','
s = s.replace('.,', ',')
kolMap.write(s)
kolMap.close()

s = ''
for n in range(0, 25):
    for y in range(0, 17):
        for x in range(0, 27):
            s += '0.'
    s = s[:(918 * (n + 1)) - 1] + ','
mapBuildingProgress.write(s)
mapBuildingProgress.close()

data.write('')
data.close()
