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


def test4():
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