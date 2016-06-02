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

def has_non_overlapping_pair(s):
    """
    It contains a pair of any two letters that appears at least twice in the
    string without overlapping, like `xyxy` (`xy`) or `aabcdefgaa` (`aa`),
    but not like `aaa` (`aa`, but it overlaps).
    """
    has_non_overlapping_pair = False

    for i, c in enumerate(s):
        try:
            pair = s[i] + s[i+1]
            if len(s.replace(pair, '')) <= len(s) - 4:
                has_non_overlapping_pair = True
                break
        except IndexError:  # We've reached the end of the string
            pass

    print 'Non overlapping pair: %s \t=> %s' % (
        has_non_overlapping_pair,
        ('OK' if has_non_overlapping_pair else 'not OK')
    )

    return has_non_overlapping_pair

def has_separated_twin_letters(s):
    """
    It contains at least one letter which repeats with exactly one letter
    between them, like `xyx`, `abcdefeghi` (`efe`), or even `aaa`.
    """
    has_separated_twin_letters = False
    try:
        has_separated_twin_letters = any(s[i] == s[i+2] for i, c in enumerate(s))
    except IndexError:  # We've reached the end of the string
        pass

    print 'Separated twin letters: %s \t=> %s' % (
        has_separated_twin_letters,
        ('OK' if has_separated_twin_letters else 'not OK')
    )

    return has_separated_twin_letters



nice_strings = 0
really_nice_strings = 0

for string in input.splitlines():
    string = string.lower()  # Just in case of vicious trap...

    print '\n>>>', string

    if has_at_least_three_vowels(string) and has_twin_letters(string) and has_no_bad_strings(string):
        print 'Nice string ! (step one)'
        nice_strings += 1
    else:
        print 'Bad string :( (step one)'

    if has_non_overlapping_pair(string) and has_separated_twin_letters(string):
        print 'Really nice string ! (step two)'
        really_nice_strings += 1
    else:
        print 'Really bad string :((( (step two)'

print '\n\n\n'
print 'Nice strings (step one): %s/%s' % (nice_strings, len(input.splitlines()))
print 'Really nice strings (step two): %s/%s' % (really_nice_strings, len(input.splitlines()))
