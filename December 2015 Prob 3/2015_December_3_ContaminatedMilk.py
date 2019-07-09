def add_person(input_person, input_dict):
    if input_person[0] in input_dict.keys():
        input_dict[input_person[0]].append(input_person[1::])
    else:
        input_dict[input_person[0]] = list()
        input_dict[input_person[0]].append(input_person[1::])


fin = open('7.in')
# fin = open('ex.txt')
people_drank_milk = []
sick_people = []
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
            sick_people.append([person, time])
        else:
            person, time, milk = list(map(lambda x: int(x), line.split(" ")))
            people_drank_milk.append([person, time, milk])
    count += 1
fin.close()
people_drank_milk.sort()
all_people = {}
possible_milk_candidates = [True for number in range(m)]
for persons_milk_drank in people_drank_milk:
    add_person(persons_milk_drank, all_people)
for person in sick_people:
    for milk_drank in all_people[person[0]]:
        if milk_drank[1] >= person[1]:
            possible_milk_candidates[milk_drank[0]-1] = False
max_sick_people = 0
count = 1
for milk_candidate in possible_milk_candidates:
    temp = 0
    if milk_candidate:
        for person in list(all_people.values()):
            for milk_drank in person:
                if count == milk_drank[0]:
                    temp += 1
                    break
        if temp > max_sick_people:
            max_sick_people = temp
    count += 1

fout = open("badmilk.out", "w")
fout.write("{}".format(max_sick_people))
fout.close()
