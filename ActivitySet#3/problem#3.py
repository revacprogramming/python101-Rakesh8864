def get_cs():
    a=input()
    return(a)
    #"""get string input"""


def cs_to_lot(cs):
      l=[]
    cs = cs.split(";")
    for i in cs:
        l.append(tuple(i.split("=")))
    return (l)

    #"""convert connected string to list of strings"""


def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()