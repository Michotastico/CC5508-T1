import matplotlib.pyplot as plt
from skimage import io
import Algorithm.Watermark as wm


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

    plt.show()