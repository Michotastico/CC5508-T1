import Functions


def extract_LSB(pixel, pos):
    tmp = bin(pixel)
    tmp = tmp[2:]
    if len(tmp) == 1 and pos > 1:
        return 0
    v = int(tmp[len(tmp)-pos])
    return v


def level1(_block):
    matrix = _block.copy()
    width, height = matrix.shape
    hor_block = width / 4
    ver_block = height / 4
    for x in range(0, hor_block):
        for y in range(0, ver_block):
            x_coor = x * 4
            y_coor = y * 4
            block = matrix[x_coor: x_coor + 4, y_coor: y_coor + 4]
            copy_block = block.copy()
            for k in range(0, 4):
                for l in range(0, 4):
                    copy_block[k, l] = Functions.removeLSB(copy_block[k, l])
            avg_B = Functions.average(copy_block)
            for i in range(0, 2):
                for j in range(0, 2):
                    i_coor = i * 2
                    j_coor = j * 2
                    bs = block[i_coor: i_coor+2, j_coor: j_coor+2]
                    v = extract_LSB(bs[0, 0], 2)
                    p = extract_LSB(bs[0, 1], 2)
                    for a in range(0, 2):
                        for b in range(0, 2):
                            bs[a, b] = Functions.removeLSB(bs[a, b])
                    average = Functions.average(bs)
                    ns = Functions.ones_in_sixMSB(average)
                    pp = 1
                    if ns % 2 == 0:
                        pp = 0
                    if p != pp:
                        bs.fill(False)
                        continue
                    vv = 0
                    if average >= avg_B:
                        vv = 1
                    if v == vv:
                        bs.fill(255)
                    else:
                        bs.fill(False)
    return matrix


def level2(_block):
    matrix = level1(_block)
    width, height = matrix.shape
    hor_block = width / 4
    ver_block = height / 4
    for x in range(0, hor_block):
        for y in range(0, ver_block):
            x_coor = x * 4
            y_coor = y * 4
            block = matrix[x_coor: x_coor + 4, y_coor: y_coor + 4]
            isInvalid = False
            for i in range(0, 4):
                for j in range(0, 4):
                    if block[i][j] == False:
                        isInvalid = True
                        break
                if isInvalid:
                    break
            if isInvalid:
                block.fill(False)
    return matrix


def level3(_block):
    matrix = level2(_block)
    width, height = matrix.shape
    hor_block = width / 4
    ver_block = height / 4
    for x in range(0, hor_block):
        for y in range(0, ver_block):
            x_coor = x * 4
            y_coor = y * 4
            block = matrix[x_coor: x_coor + 4, y_coor: y_coor + 4]
            if block[0][0] == False:
                continue
            neighborhood = []
            counter = 0
            if x == 0:
                if y == 0 or y == (ver_block - 1):
                    continue
                else:
                    neighborhood.append(matrix[x_coor: x_coor + 4, y_coor + 4: y_coor + 8])  # UM
                    neighborhood.append(matrix[x_coor + 4: x_coor + 8, y_coor + 4: y_coor + 8])  # UR
                    neighborhood.append(matrix[x_coor + 4: x_coor + 8, y_coor: y_coor + 4])  # MR
                    neighborhood.append(matrix[x_coor: x_coor + 4, y_coor - 4: y_coor])  # BM
                    neighborhood.append(matrix[x_coor + 4: x_coor + 8, y_coor - 4: y_coor])  # BR
            elif x == (hor_block - 1):
                if y == 0 or y == (ver_block - 1):
                    continue
                else:
                    neighborhood.append(matrix[x_coor - 4: x_coor, y_coor + 4: y_coor + 8])  # UL
                    neighborhood.append(matrix[x_coor: x_coor + 4, y_coor + 4: y_coor + 8])  # UM
                    neighborhood.append(matrix[x_coor - 4: x_coor, y_coor: y_coor + 4])  # ML
                    neighborhood.append(matrix[x_coor - 4: x_coor, y_coor - 4: y_coor])  # BL
                    neighborhood.append(matrix[x_coor: x_coor + 4, y_coor - 4: y_coor])  # BM
            elif y == 0:
                neighborhood.append(matrix[x_coor - 4: x_coor, y_coor + 4: y_coor + 8])  # UL
                neighborhood.append(matrix[x_coor: x_coor + 4, y_coor + 4: y_coor + 8])  # UM
                neighborhood.append(matrix[x_coor + 4: x_coor + 8, y_coor + 4: y_coor + 8])  # UR
                neighborhood.append(matrix[x_coor - 4: x_coor, y_coor: y_coor + 4])  # ML
                neighborhood.append(matrix[x_coor + 4: x_coor + 8, y_coor: y_coor + 4])  # MR
            elif y == (ver_block - 1):
                neighborhood.append(matrix[x_coor - 4: x_coor, y_coor: y_coor + 4])  # ML
                neighborhood.append(matrix[x_coor + 4: x_coor + 8, y_coor: y_coor + 4])  # MR
                neighborhood.append(matrix[x_coor - 4: x_coor, y_coor - 4: y_coor])  # BL
                neighborhood.append(matrix[x_coor: x_coor + 4, y_coor - 4: y_coor])  # BM
                neighborhood.append(matrix[x_coor + 4: x_coor + 8, y_coor - 4: y_coor])  # BR
            else:
                neighborhood.append(matrix[x_coor - 4: x_coor, y_coor + 4: y_coor + 8])  # UL
                neighborhood.append(matrix[x_coor: x_coor + 4, y_coor + 4: y_coor + 8])  # UM
                neighborhood.append(matrix[x_coor + 4: x_coor + 8, y_coor + 4: y_coor + 8])  # UR
                neighborhood.append(matrix[x_coor - 4: x_coor, y_coor: y_coor + 4])  # ML
                neighborhood.append(matrix[x_coor + 4: x_coor + 8, y_coor: y_coor + 4])  # MR
                neighborhood.append(matrix[x_coor - 4: x_coor, y_coor - 4: y_coor])  # BL
                neighborhood.append(matrix[x_coor: x_coor + 4, y_coor - 4: y_coor])  # BM
                neighborhood.append(matrix[x_coor + 4: x_coor + 8, y_coor - 4: y_coor])  # BR

            for n in neighborhood:
                if n[0][0] == False:
                    counter += 1
            if counter >= 5:
                block.fill(False)
    return matrix

