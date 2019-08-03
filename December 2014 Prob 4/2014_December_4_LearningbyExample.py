def input_file(file_name):
    fin = open(file_name)
    count = 0
    all_existing_cows = []
    cows_coming_in = []
    for line in fin:
        line = line.strip()
        if count > 0:
            has_spots, lbs = line.split(" ")
            all_existing_cows.append([int(lbs), has_spots == "S"])
        else:
            cows, start, finish = line.split(" ")
            cows_coming_in = range(int(start), int(finish)+1)
        count += 1
    fin.close()
    all_existing_cows.sort()
    return all_existing_cows, cows_coming_in


def find_all_spots(all_cows):
    all_spots = 0
    existing_cows = all_cows[0]
    existing_cows_weights = [i[0] for i in existing_cows]
    incoming_cows = all_cows[1]
    passed_checkpoint = False
    current_checkpoint = 0
    for cow in incoming_cows:
        if passed_checkpoint:
            current_checkpoint += 1
            passed_checkpoint = False
        if cow != incoming_cows[0] and cow != incoming_cows[-1]:
            if cow == existing_cows[current_checkpoint+1][0]:
                passed_checkpoint = True
                if existing_cows[current_checkpoint+1][1]:
                    all_spots += 1
            else:
                if abs(existing_cows[current_checkpoint][0] - cow) == abs(existing_cows[current_checkpoint+1][0] - cow):
                    if existing_cows[current_checkpoint][1] or existing_cows[current_checkpoint+1][1]:
                        all_spots += 1
                else:
                    possible_close_weights = [existing_cows[current_checkpoint][0], existing_cows[current_checkpoint+1][0]]
                    closest_existing_weight = min(possible_close_weights, key=lambda x: abs(x-cow))
                    index_value = existing_cows_weights.index(closest_existing_weight)
                    if existing_cows[index_value][1]:
                        all_spots += 1
        else:
            if cow == incoming_cows[-1]:
                current_checkpoint += 1
            if existing_cows[current_checkpoint][1]:
                all_spots += 1
    return all_spots


def output_file(input_num):
    fout = open("learning.out", "w")
    fout.write("{}".format(input_num))
    fout.close()


output_file(find_all_spots(input_file("learning.in")))
