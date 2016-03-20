import matplotlib.pyplot as plt
from skimage import feature, io, filters, data
import Functions


def apply_watermark(filename):
    image = io.imread(filename) # Image in gray scale
    blocks = []
    height, width = image.shape
    hor_block = height / 4
    ver_block = width / 4
    for x in range(0, hor_block - 1):
        for y in range(0, ver_block - 1):
            x_coor = x * 4
            y_coor = y * 4
            block = image[x_coor: x_coor + 4, y_coor: y_coor + 4]
            blocks.append(block)
    n = len(blocks)
    k = Functions.get_biggest_prime(n)

    for index in range(0, n - 1):
        block_B = blocks[index]
        block_A = (blocks[Functions.mapping(index + 1, k, n) - 1]).copy()
        for x in range(0, 4):
            for y in range(0, 4):
                block_B[x, y] = Functions.removeLSB(block_B[x, y])
        avg_B = Functions.average(block_B)
        for x in range(0, 2):
            for y in range(0, 2):
                x_coor = x * 2
                y_coor = y * 2
                block = block_B[x_coor: x_coor+2, y_coor: y_coor+2]
                average = Functions.average(block)
                v = 0
                if average >= avg_B:
                    v = 1
                p = 1
                if Functions.ones_in_sixMSB(average) % 2 == 0:
                    p = 0
                subblock_a = block_A[x_coor: x_coor+2, y_coor: y_coor+2]
                avg_as = Functions.average(subblock_a)
                r = Functions.split_binary_sixMSB(avg_as)
                block[0][0] = block[0][0] + v + r[0]
                block[0][1] = block[0][1] + p + r[1]
                block[1][0] = block[1][0] + r[2] + r[3]
                block[1][1] = block[1][1] + r[4] + r[5]
    return image




