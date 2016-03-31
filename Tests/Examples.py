import matplotlib.pyplot as plt
from skimage import io
import Algorithm.Watermark as wm
import Algorithm.TamperDetection as td
import Algorithm.Recovery as rc


def scratch_image(image):
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


def erase_image(image, percentage):
    h, w = image.shape
    w = int(w*percentage)
    for i in range(0, h):
        for o in range(0, w):
            image[i, o] = 0
    return image


def watermarking_examples():
    image1 = io.imread('Images/Watermarking/Example1.jpg')
    image2 = io.imread('Images/Watermarking/Example2.png')
    image3 = io.imread('Images/Watermarking/Example3.jpg')
    water1 = wm.apply_watermark('Images/Watermarking/Example1.jpg')
    water2 = wm.apply_watermark('Images/Watermarking/Example2.png')
    water3 = wm.apply_watermark('Images/Watermarking/Example3.jpg')
    fig, ((im1, w1), (im2, w2), (im3, w3)) = plt.subplots(nrows=3, ncols=2, figsize=(10, 5))

    im1.imshow(image1, cmap=plt.cm.gray)
    im2.imshow(image2, cmap=plt.cm.gray)
    im3.imshow(image3, cmap=plt.cm.gray)

    w1.imshow(water1, cmap=plt.cm.gray)
    w2.imshow(water2, cmap=plt.cm.gray)
    w3.imshow(water3, cmap=plt.cm.gray)

    im1.axis('off')
    im2.axis('off')
    im3.axis('off')
    w1.axis('off')
    w2.axis('off')
    w3.axis('off')

    fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                         bottom=0.02, left=0.02, right=0.98)

    io.imsave('Images/Tampered/water1.png', water1)
    io.imsave('Images/Tampered/water2.png', water2)
    io.imsave('Images/Tampered/water3.png', water3)

    plt.savefig('Images/Watermarking/Examples1-3.png', bbox_inches='tight')
    plt.show()


def tampered_examples():
    image1 = scratch_image(io.imread('Images/Tampered/water1.png'))
    image2 = scratch_image(io.imread('Images/Tampered/water2.png'))
    image3 = scratch_image(io.imread('Images/Tampered/water3.png'))

    level1a = td.level1(image1)
    level1b = td.level1(image2)
    level1c = td.level1(image3)

    level2a = td.level2(image1)
    level2b = td.level2(image2)
    level2c = td.level2(image3)

    level3a = td.level3(image1)
    level3b = td.level3(image2)
    level3c = td.level3(image3)

    fig, (im1, l1, l2, l3) = plt.subplots(nrows=1, ncols=4, figsize=(10, 5))

    im1.imshow(image1, cmap=plt.cm.gray)
    l1.imshow(level1a, cmap=plt.cm.gray)
    l2.imshow(level2a, cmap=plt.cm.gray)
    l3.imshow(level3a, cmap=plt.cm.gray)

    im1.axis('off')
    l1.axis('off')
    l2.axis('off')
    l3.axis('off')

    fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                         bottom=0.02, left=0.02, right=0.98)

    plt.savefig('Images/Tampered/Example4.png', bbox_inches='tight')
    plt.show()

    fig, (im1, l1, l2, l3) = plt.subplots(nrows=1, ncols=4, figsize=(10, 5))

    im1.imshow(image2, cmap=plt.cm.gray)
    l1.imshow(level1b, cmap=plt.cm.gray)
    l2.imshow(level2b, cmap=plt.cm.gray)
    l3.imshow(level3b, cmap=plt.cm.gray)

    im1.axis('off')
    l1.axis('off')
    l2.axis('off')
    l3.axis('off')

    fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                         bottom=0.02, left=0.02, right=0.98)

    plt.savefig('Images/Tampered/Example5.png', bbox_inches='tight')
    plt.show()

    fig, (im1, l1, l2, l3) = plt.subplots(nrows=1, ncols=4, figsize=(10, 5))

    im1.imshow(image3, cmap=plt.cm.gray)
    l1.imshow(level1c, cmap=plt.cm.gray)
    l2.imshow(level2c, cmap=plt.cm.gray)
    l3.imshow(level3c, cmap=plt.cm.gray)

    im1.axis('off')
    l1.axis('off')
    l2.axis('off')
    l3.axis('off')

    fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                         bottom=0.02, left=0.02, right=0.98)

    plt.savefig('Images/Tampered/Example6.png', bbox_inches='tight')
    plt.show()


def recovery_examples():
    image1 = erase_image(io.imread('Images/Tampered/water1.png'), 0.25)
    image2 = erase_image(io.imread('Images/Tampered/water1.png'), 0.50)
    image3 = erase_image(io.imread('Images/Tampered/water2.png'), 0.33)
    image4 = erase_image(io.imread('Images/Tampered/water3.png'), 0.75)

    reco1 = rc.recovery(image1)
    reco2 = rc.recovery(image2)
    reco3 = rc.recovery(image3)
    reco4 = rc.recovery(image4)

    fig, (img1, r1) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

    img1.imshow(image1, cmap=plt.cm.gray)
    r1.imshow(reco1, cmap=plt.cm.gray)

    img1.axis('off')
    r1.axis('off')

    fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                         bottom=0.02, left=0.02, right=0.98)

    plt.savefig('Images/Recovery/Example7.png', bbox_inches='tight')
    plt.show()

    fig, (img1, r1) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

    img1.imshow(image2, cmap=plt.cm.gray)
    r1.imshow(reco2, cmap=plt.cm.gray)

    img1.axis('off')
    r1.axis('off')

    fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                         bottom=0.02, left=0.02, right=0.98)

    plt.savefig('Images/Recovery/Example8.png', bbox_inches='tight')
    plt.show()

    fig, (img1, r1) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

    img1.imshow(image3, cmap=plt.cm.gray)
    r1.imshow(reco3, cmap=plt.cm.gray)

    img1.axis('off')
    r1.axis('off')

    fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                         bottom=0.02, left=0.02, right=0.98)

    plt.savefig('Images/Recovery/Example9.png', bbox_inches='tight')
    plt.show()

    fig, (img1, r1) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

    img1.imshow(image4, cmap=plt.cm.gray)
    r1.imshow(reco4, cmap=plt.cm.gray)

    img1.axis('off')
    r1.axis('off')

    fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                         bottom=0.02, left=0.02, right=0.98)

    plt.savefig('Images/Recovery/Example10.png', bbox_inches='tight')
    plt.show()
