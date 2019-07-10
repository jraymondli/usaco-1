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


def derive_answer(input_dict, input_list, input_len):
    possible_milk_candidates = [True for num in range(input_len)]
    max_sick_people = 0
    milk_id = 1
    for person in input_list:
        for milk_drank in input_dict[person[0]]:
            if milk_drank[1] >= person[1]:
                possible_milk_candidates[milk_drank[0] - 1] = False
    for milk_candidate in possible_milk_candidates:
        temp = 0
        if milk_candidate:
            for persons_milks_and_times in list(input_dict.values()):
                for milk_drank in persons_milks_and_times:
                    print(milk_drank)
                    if milk_id == milk_drank[0]:
                        temp += 1

                        break
            if temp > max_sick_people:
                max_sick_people = temp
    milk_id += 1
    return max_sick_people


def output_file(input_num):
    fout = open("badmilk.out", "w")
    fout.write("{}".format(input_num))
    fout.close()


total_milks, all_sick_people, amount_milks = input_file()
total_milks.sort()
output_file(derive_answer(create_people_dict(total_milks), all_sick_people, amount_milks))
