def input_file(file_name):  # correct
    fin = open(file_name)
    count = 0
    all_existing_cows = []
    cows_coming_in = []
    for line in fin:
        line = line.strip()
        if count > 0:
            has_spots, lbs = line.split(" ")
            all_existing_cows.append([has_spots == "S", int(lbs)])
        else:
            cows, start, finish = line.split(" ")
            cows_coming_in = range(int(start), int(finish)+1)
        count += 1
    fin.close()
    return all_existing_cows, cows_coming_in


def find_closest_number(input_num, input_list):
    weights = []
    temp = list(map(lambda x: abs(x - input_num), input_list))
    minimum = min(temp)
    count = 0
    for i in temp:
        if i == minimum:
            weights.append(input_list[count])
        count += 1
    return weights


def find_all_spots(all_cows):
    all_spots = 0
    existing_cows_weight = [i[1] for i in all_cows[0]]
    existing_cows_spots = [i[0] for i in all_cows[0]]
    incoming_cows = all_cows[1]
    for cow in incoming_cows:
        for weight in find_closest_number(cow, existing_cows_weight):
            if existing_cows_spots[existing_cows_weight.index(weight)]:
                all_spots += 1
                break
    return all_spots


def output_file(input_num):
    fout = open("learning.out", "w")
    fout.write("{}".format(input_num))
    fout.close()


output_file(find_all_spots(input_file("learning_bronze/3.in")))
