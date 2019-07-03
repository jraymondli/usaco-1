fin = open('cowsignal.in')
# fin = open('ex.txt')
count = 1
message = []
lw = []
multiply = 0
all_letter = {}
for line in fin:
    line = line.strip()
    if count == 1:
        length, width, multiplier = list(map(lambda x: int(x), line.split(' ')))
        lw = [length, width]
        multiply = multiplier
    else:
        lines.append(list(line.split(" ")))
    count += 1
for lines in range(lw[0]):
    for chars in range(lw[1]):
        message[lines][chars] *= 2
for lines in range(lw[0]):
    "".join(message[lines])
fin.close()
fout = open("cowsignal.out", "w")
for line in message:
    fout.write("{}\n".format(line)
fout.close()
