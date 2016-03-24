import Functions


def extract_LSB(pixel, pos):
    tmp = bin(pixel)
    tmp = tmp[2:]
    v = int(tmp[len(tmp)-pos])
    return v


def level1(_block):
    matrix = _block.copy()
    height, width = matrix.shape
    hor_block = height / 4
    ver_block = width / 4
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
