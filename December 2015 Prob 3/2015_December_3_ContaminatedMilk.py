fin = open('7.in')
# fin = open('ex.txt')
milk_drank = []
sick = []
count = 0
for line in fin:
    line = line.strip()
    if count == 0:
        line = line.split(" ")
        m = int(line[1])
        d = int(line[2])
        s = int(line[3])
    else:
        if count > d:
            person, time = list(map(lambda x: int(x), line.split(" ")))
            sick.append([person, time])
        else:
            person, time, milk = list(map(lambda x: int(x), line.split(" ")))
            milk_drank.append([person, time, milk])
    count += 1
milk_drank.sort()
all_people = {}
possible_candidates = [True for number in range(m)]
for people in milk_drank:                           # Makes the dictionary all_people
    if people[0] in all_people.keys():              #
        all_people[people[0]].append(people[1::])   #
    else:                                           #
        all_people[people[0]] = list()              #
        all_people[people[0]].append(people[1::])   #
for sickly in sick:                                     # Iterates through possible_candidates and selects some to turn
    for milks in all_people[sickly[0]]:                 # into false.
        if milks[1] >= sickly[1]:                       #
            possible_candidates[milks[0]-1] = False     #
max_people = 0
count = 1
for milk in possible_candidates:
    temp = 0
    if milk:
        for person in list(all_people.values()):
            for milks in person:
                if count == milks[0]:
                    temp += 1
                    break
        if temp > max_people:
            max_people = temp
    count += 1
fin.close()
fout = open("badmilk.out", "w")
fout.write("{}".format(max_people))
fout.close()
