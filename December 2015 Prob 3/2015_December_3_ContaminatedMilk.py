def input_file():
    fin = open('badmilk.in')
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
        else:
            if count > d:
                person, time = list(map(lambda x: int(x), line.split(" ")))
                sick_people.append([person, time])
            else:
                person, time, milk = list(map(lambda x: int(x), line.split(" ")))
                people_drank_milk.append([person, time, milk])
        count += 1
    fin.close()
    return [people_drank_milk, sick_people, m]


def create_people_dict(input_list):
    all_people = {}
    for persons_milk_drank in input_list:
        if persons_milk_drank[0] in all_people.keys():
            all_people[persons_milk_drank[0]].append(persons_milk_drank[1::])
        else:
            all_people[persons_milk_drank[0]] = list()
            all_people[persons_milk_drank[0]].append(persons_milk_drank[1::])
    return all_people


def derive_answer(input_dict):
    possible_milk_candidates = [True for num in range(m)]
    max_sick_people = 0
    count = 1
    for person in sick_people:
        for milk_drank in input_dict[person[0]]:
            if milk_drank[1] >= person[1]:
                possible_milk_candidates[milk_drank[0] - 1] = False
    for milk_candidate in possible_milk_candidates:
        temp = 0
        if milk_candidate:
            for person in list(input_dict.values()):
                for milk_drank in person:
                    if count == milk_drank[0]:
                        temp += 1
                        break
            if temp > max_sick_people:
                max_sick_people = temp
        count += 1
    return max_sick_people


def output_file(input_num):
    fout = open("badmilk.out", "w")
    fout.write("{}".format(input_num))
    fout.close()


people_drank_milk = input_file()[0]
sick_people = input_file()[1]
m = input_file()[2]
people_drank_milk.sort()
output_file(derive_answer(create_people_dict(people_drank_milk)))