from hashlib import md5

from data import input


i = 0
md5hash = ''
while not md5hash.startswith('00000'):
    i+=1
    key = input + str(i)
    md5hash = str(md5(key).hexdigest())

print 'Answer: %s, because md5(%s).hexdigest() => %s' % (i, key, md5hash)
