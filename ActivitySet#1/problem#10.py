name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

email = dict()

for line in handle :
    if 'From:' in line:
        line = line.strip()
        line = line.split()
        for word in line:
            if '@' in word:
                if word in email:
                    email[word] = email[word] + 1
                else:
                    email[word] = 1

largest = 0
email_large = None

for m in email :
    if email[m] > largest:
        largest = email[m]
        email_large = m
print(email_large, largest)
