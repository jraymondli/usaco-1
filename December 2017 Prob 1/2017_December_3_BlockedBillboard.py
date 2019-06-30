count = 1
for line in fin:
    if count != 1:
        line = line.strip()
        days, name, amount = line.split(' ')
        days = int(days)
        if "+" in amount:
            n, amount = amount.split('+')
        amount = int(amount)
        recordings.append([days, name, amount])
    else:
        line = line.strip()
    count += 1
fin.close()
recordings.sort()


#print(changes)

fout = open("measurement.out", "w")
fout.write("{}".format(changes))
fout.close()