fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh :
    line = line.strip()
    line = line.split()
    if 'From' in line:
        for word in line:
            if '@' in word:
                print(word)
                count +=1

print("There were", count, "lines in the file with From as the first word")
