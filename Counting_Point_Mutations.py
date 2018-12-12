import sys

f = open(sys.argv[1])
lines = f.readlines()

ref = lines[0].rstrip()
alt = lines[1].rstrip()

f.close()

count = 0
for i in range(len(ref)):
    if ref[i] != alt[i]:
        count += 1

print count
