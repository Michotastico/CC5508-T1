import matplotlib.pyplot as plt
from skimage import io
import Algorithm.Watermark as wm
import Algorithm.TamperDetection as td
import Algorithm.Recovery as rc


def test1():
    Original = io.imread('Images/Test1.jpg')
    Watermarked = wm.apply_watermark('Images/Test1.jpg')
    fig, (ax_original, ax_watermarked) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    ax_original.imshow(Original, cmap=plt.cm.gray)
    ax_original.axis('off')
    ax_original.set_title('Original', fontsize=10)
    ax_watermarked.imshow(Watermarked, cmap=plt.cm.gray)
    ax_watermarked.axis('off')
    ax_watermarked.set_title('Watermarked', fontsize=10)

    fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                         bottom=0.02, left=0.02, right=0.98)

    io.imsave('Images/Test1W.jpg', Watermarked)
    plt.show()

def test2():
    Watermarked = wm.apply_watermark('Images/Test1.jpg')
    level1 = Watermarked.copy()
    level1 = td.level1(level1)
    fig, (ax_original, ax_watermarked) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    ax_original.imshow(level1, cmap=plt.cm.gray)
    ax_original.axis('off')
    ax_original.set_title('level1', fontsize=10)
    ax_watermarked.imshow(Watermarked, cmap=plt.cm.gray)
    ax_watermarked.axis('off')
    ax_watermarked.set_title('Watermarked', fontsize=10)

    fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                         bottom=0.02, left=0.02, right=0.98)

    io.imsave('Images/Test2L1.jpg', level1)
    plt.show()


def test3():
    Watermarked = wm.apply_watermark('Images/Test1.jpg')
    level2 = Watermarked.copy()
    level2 = td.level1(level2)
    fig, (ax_original, ax_watermarked) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    ax_original.imshow(level2, cmap=plt.cm.gray)
    ax_original.axis('off')
    ax_original.set_title('level2', fontsize=10)
    ax_watermarked.imshow(Watermarked, cmap=plt.cm.gray)
    ax_watermarked.axis('off')
    ax_watermarked.set_title('Watermarked', fontsize=10)

    fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                         bottom=0.02, left=0.02, right=0.98)

    io.imsave('Images/Test2L2.jpg', level2)
    plt.show()


def test4():
    Watermarked = wm.apply_watermark('Images/Test1.jpg')
    level3 = Watermarked.copy()
    level3 = td.level1(level3)
    fig, (ax_original, ax_watermarked) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    ax_original.imshow(level3, cmap=plt.cm.gray)
    ax_original.axis('off')
    ax_original.set_title('level3', fontsize=10)
    ax_watermarked.imshow(Watermarked, cmap=plt.cm.gray)
    ax_watermarked.axis('off')
    ax_watermarked.set_title('Watermarked', fontsize=10)

    fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                         bottom=0.02, left=0.02, right=0.98)

    io.imsave('Images/Test2L3.jpg', level3)
    plt.show()


def test5():
    Watermarked = wm.apply_watermark('Images/Test1.jpg')
    Recovered = rc.recovery(Watermarked)
    fig, (ax_original, ax_watermarked) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    ax_original.imshow(Recovered, cmap=plt.cm.gray)
    ax_original.axis('off')
    ax_original.set_title('Recovered', fontsize=10)
    ax_watermarked.imshow(Watermarked, cmap=plt.cm.gray)
    ax_watermarked.axis('off')
    ax_watermarked.set_title('Watermarked', fontsize=10)

    fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                         bottom=0.02, left=0.02, right=0.98)

    io.imsave('Images/TestRecovery1.jpg', Recovered)
    plt.show()


def test6():
    Watermarked = wm.apply_watermark('Images/Test1.jpg')
    h, w = Watermarked.shape
    for i in range(0, w):
        for o in range(0, h/4):
            Watermarked[i, o] = 255
    Recovered = rc.recovery(Watermarked)
    fig, (ax_original, ax_watermarked) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    ax_original.imshow(Recovered, cmap=plt.cm.gray)
    ax_original.axis('off')
    ax_original.set_title('Recovered', fontsize=10)
    ax_watermarked.imshow(Watermarked, cmap=plt.cm.gray)
    ax_watermarked.axis('off')
    ax_watermarked.set_title('Watermarked', fontsize=10)

    fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                         bottom=0.02, left=0.02, right=0.98)

    io.imsave('Images/TestRecovery2.jpg', Recovered)
    plt.show()


def test_levels():
    Watermarked = wm.apply_watermark('Images/Test1.jpg')
    Watermarked = drawImage(Watermarked)
    Level1 = td.level1(Watermarked)
    Level2 = td.level2(Watermarked)
    Level3 = td.level3(Watermarked)

    fig, ((ax_1, ax_2), (ax_3, ax_4)) = plt.subplots(nrows=2, ncols=2, figsize=(10, 5))
    ax_1.imshow(Watermarked, cmap=plt.cm.gray)
    ax_1.axis('off')
    ax_1.set_title('Watermarked', fontsize=10)

    ax_2.imshow(Level1, cmap=plt.cm.gray)
    ax_2.axis('off')
    ax_2.set_title('Level1', fontsize=10)

    ax_3.imshow(Level2, cmap=plt.cm.gray)
    ax_3.axis('off')
    ax_3.set_title('Level2', fontsize=10)

    ax_4.imshow(Level3, cmap=plt.cm.gray)
    ax_4.axis('off')
    ax_4.set_title('Level3', fontsize=10)

    plt.savefig('Images/levels.jpg', bbox_inches='tight')
    plt.show()


def drawImage(image):
    a, b = image.shape
    aa = 0
    bb = 0
    while aa != a and bb != b:
        image[aa][bb] = 255
        image[a - aa - 1][bb] = 255
        aa += 1
        bb += 1
    for i in range(0, a):
        image[i][b/2] = 255
    for j in range(0, b):
        image[a/2][j] = 255
    return image