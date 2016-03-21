from skimage import io
import Functions


def apply_watermark(filename):
    img = io.imread(filename) # Image in gray scale
    image = img.copy()
    blocks = []
    height, width = image.shape
    hor_block = width / 4
    ver_block = height / 4
    for x in range(0, hor_block):
        for y in range(0, ver_block):
            x_coor = x * 4
            y_coor = y * 4
            block = image[x_coor: x_coor + 4, y_coor: y_coor + 4]
            blocks.append(block)
    n = len(blocks)
    k = Functions.get_biggest_prime(n)

    for index in range(0, n):
        block_B = blocks[index]
        block_A = (blocks[Functions.mapping(index + 1, k, n) - 1]).copy()
        for x in range(0, 4):
            for y in range(0, 4):
                block_B[x, y] = Functions.removeLSB(block_B[x, y])
        avg_B = Functions.average(block_B)
        for i in range(0, 2):
            for j in range(0, 2):
                i_coor = i * 2
                j_coor = j * 2
                blockBS = block_B[i_coor: i_coor+2, j_coor: j_coor+2]
                average = Functions.average(blockBS)
                v = 0
                if average >= avg_B:
                    v = 1
                p = 1
                if Functions.ones_in_sixMSB(average) % 2 == 0:
                    p = 0
                subblock_a = block_A[i_coor: i_coor+2, j_coor: j_coor+2].copy()
                avg_as = Functions.average(subblock_a)
                r = Functions.split_binary_sixMSB(avg_as)
                if v == 1:
                    v = 2
                if p == 1:
                    p = 2
                if r[2] == 1:
                    r[2] = 2
                if r[4] == 1:
                    r[4] = 2
                blockBS[0][0] = (blockBS[0][0] + v + r[0])
                blockBS[0][1] = (blockBS[0][1] + p + r[1])
                blockBS[1][0] = (blockBS[1][0] + r[2] + r[3])
                blockBS[1][1] = (blockBS[1][1] + r[4] + r[5])
    return image




