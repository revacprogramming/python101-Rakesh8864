
def add(a, b):
    s=a+b # ...\
    return s

def output(a, b, sum):
    print(a,"+",b,"=",sum)

def main():
    a, b = map(int,input("input?").split())
    sum = add(a, b)
    output(a, b, sum)


if __name__ == '__main__':
    main()