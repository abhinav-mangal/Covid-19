import string
import random


def PassGen():
    s1 = string.ascii_uppercase

    s2 = string.ascii_lowercase

    s3 = string.punctuation

    s4 = string.ascii_letters

    s5 = string.digits

    passlen = int(input('Enter the Length of your Password\n '))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    s.extend(list(s5))

    random.shuffle(s)
    gen = ("".join(s[0:passlen]))
    print(gen)


PassGen()
