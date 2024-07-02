
def consonant(strval):
    vowels = ('a','e','i','o','u')
    for c in strval:
        if c.lower() not in vowels:
            yield c



def main():
    strval = 'Python Programming'
    mygen = consonant(strval)

    rlst = list(mygen)
    print(len(rlst))
    for v in rlst:
        print(v, end=' ')
    print()


if __name__ == '__main__':
    main()
