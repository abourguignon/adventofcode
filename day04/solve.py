from hashlib import md5

from data import input


def mine_advent_coin(key, leading_sequence):
    i = 0
    md5hash = ''
    while not md5hash.startswith(leading_sequence):
        i+=1
        key = input + str(i)
        md5hash = str(md5(key).hexdigest())

    print 'Answer: %s, because md5(%s).hexdigest() => %s' % (i, key, md5hash)

    return i

mine_advent_coin(input, 5*'0')
mine_advent_coin(input, 6*'0')
