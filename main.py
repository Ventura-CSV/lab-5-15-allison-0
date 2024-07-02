
def consonant(strval):
    vowels = ('a','e','i','o','u')
    for c in strval:



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
