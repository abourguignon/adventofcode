from itertools import groupby

from data import input


vowels = list('aeiou')
bad_strings = ['ab', 'cd', 'pq', 'xy']

def has_at_least_three_vowels(s):
    """
    It contains at least three vowels (`aeiou` only), like `aei`, `xazegov`, or
    `aeiouaeiouaeiou`.
    """
    string_vowels = filter(lambda c: c in vowels, list(s))
    print 'Vowels (%s): %s \t=> %s' % (
        len(string_vowels),
        (', '.join(string_vowels) or 'none'),
        ('OK' if bool(len(string_vowels) >= 3) else 'not OK')
    )
    return bool(len(string_vowels) >= 3)

def has_twin_letters(s):
    """
    It contains at least one letter that appears twice in a row, like `xx`,
    `abcdde` (`dd`), or `aabbccdd` (`aa`, `bb`, `cc`, or `dd`).
    """
    grouped_letters = [(c, len(list(g))) for c, g in groupby(s)]
    twin_letters = filter(lambda t: t[1] > 1, grouped_letters)
    print 'Twin letters: %s \t=> %s' % (
        (', '.join(['%s*%s' % (c, i) for c, i in twin_letters]) or 'none'),
        ('OK' if bool(twin_letters) else 'not OK')
    )
    return bool(twin_letters)

def has_no_bad_strings(s):
    """
    It does not contain the strings `ab`, `cd`, `pq`, or `xy`, even if they are
    part of one of the other requirements.
    """
    any_bad_string = any(bad_string in s for bad_string in bad_strings)
    print 'Bad strings: %s \t=> %s' % (
        any_bad_string,
        ('OK' if bool(not any_bad_string) else 'not OK')
    )
    return bool(not any_bad_string)


nice_strings = 0

for string in input.splitlines():
    string = string.lower()  # Just in case of vicious trap...
    print '\n>>>', string
    if has_at_least_three_vowels(string) and has_twin_letters(string) and has_no_bad_strings(string):
        print 'Nice string !'
        nice_strings += 1
    else:
        print 'Bad string :('

print '\n\n\nNice strings: %s/%s' % (nice_strings, len(input.splitlines()))
