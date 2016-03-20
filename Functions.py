import numpy

def mapping(X, k, N):
    '''
    Block-mapping sequence.
    :param X: Position of block [0, N - 1]
    :param k: Prime secret key in [0 , N - 1]
    :param N: Number of blocks
    :return: Mapping of X
    '''
    return ((k * X) % N) + 1


def removeLSB(pixel):
    '''
    Function who removes the two LSBs of a pixel.
    :param pixel: The pixel
    :return: The pixel with zeroes in the wto LSBs
    '''
    return (pixel >> 2) << 2


def primesfrom3to(n):
    """
    Credits for this function to Robert William Hanks
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
    Returns a array of primes, 3 <= p < n
    """
    sieve = numpy.ones(n/2, dtype=numpy.bool)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1


def get_biggest_prime(N):
    '''
    Get the biggest prime number in [0, N]
    :param N: Number > prime
    :return: Primer number
    '''
    primes = primesfrom3to(N)
    return primes[len(primes) - 1]


def average(block):
    '''
    Calculate the average of a block
    :param block: Matrix
    :return: Average of block
    '''
    h, w = block.shape
    value = 0
    counter = 0
    for x in range(0, w - 1):
        for y in range(0, h - 1):
            value += block[x, y]
            counter += 1
    return value/counter


def ones_in_sixMSB(n):
    '''
    Counter of ones of six MSB of n
    :param n: Number
    :return: The number of ones in the six MSBs of the number n
    '''
    number = removeLSB(n)
    return bin(number).count("1")


def split_binary_sixMSB(n):
    '''
    Function who return the six MSB of a number in a array of int
    :param n: Number to be splitted
    :return: list of int
    '''
    shifted = n >> 2
    binary = bin(shifted)
    binary = binary[2:]
    size = len(binary)
    for i in range(0, 6 - size):
        binary = '0' + binary
    splitted = []
    for c in binary:
        splitted.append(int(c))
    return splitted