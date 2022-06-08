
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    t = line.split()
    lst.append(t)

lst1 = []
for i in lst:
    lst1 = lst1+ i
lst1 = list(set(lst1))
lst1.sort()        
print(lst1)       