import Functions
import TamperDetection as td


def recovery(block):
    recovered = block.copy()
    recovered.fill(0)
    image = block.copy()
    blocks = []
    blocks2 = []
    height, width = image.shape
    hor_block = width / 4
    ver_block = height / 4
    for x in range(0, hor_block):
        for y in range(0, ver_block):
            x_coor = x * 4
            y_coor = y * 4
            block = image[x_coor: x_coor + 4, y_coor: y_coor + 4]
            blocks.append(block)
            block2 = recovered[x_coor: x_coor + 4, y_coor: y_coor + 4]
            blocks2.append(block2)

    n = len(blocks)
    k = Functions.get_biggest_prime(n)

    for index in range(0, n):
        block_B = blocks[index]
        block_C = blocks2[Functions.mapping(index + 1, k, n) - 1]
        for i in range(0, 2):
            for j in range(0, 2):
                i_coor = i * 2
                j_coor = j * 2
                blockBS = block_B[i_coor: i_coor+2, j_coor: j_coor+2]
                r0 = td.extract_LSB(blockBS[0,0], 1)<< 7
                r1 = td.extract_LSB(blockBS[0,1], 1)<< 6
                r2 = td.extract_LSB(blockBS[1,0], 1)<< 5
                r3 = td.extract_LSB(blockBS[1,0], 2)<< 4
                r4 = td.extract_LSB(blockBS[1,1], 1)<< 3
                r5 = td.extract_LSB(blockBS[1,1], 2)<< 2
                r = r0 + r1 + r2+ r3 + r4 + r5
                blockAS = block_C[i_coor: i_coor+2, j_coor: j_coor+2]
                blockAS.fill(r)
    return recovered