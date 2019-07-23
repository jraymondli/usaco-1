def input_file(file_name):
    fin = open(file_name)
    count = 0
    cows_positions = []
    cows_speed = []
    for line in fin:
        line = line.strip()
        if count > 0:
            pos, spd = line.split(" ")
            cows_positions.append(int(pos))
            cows_speed.append(int(spd))
        count += 1
    fin.close()
    return cows_positions, cows_speed


def jog_once(input_cows):
    input_cows = list(map(lambda x: [x[0]+x[1], x[1]], input_cows))
    print(input_cows)
    for cow in range(len(input_cows)-2):
        print(input_cows, cow)
        if input_cows[cow][0] == input_cows[cow+1][0]:
            input_cows.remove(input_cows[cow])


def cows_are_jogging(cows_pos_and_spd):
    cows_positions = cows_pos_and_spd[0]
    cows_speed = cows_pos_and_spd[1]
    same_pace = False
    while not same_pace:
        jog_once(input_cows)
        pace = input_cows[0][1]
        all_same_pace = True
        for cow in input_cows:
            if cow[1] != pace:
                all_same_pace = False
        same_pace = all_same_pace
    return len(input_cows)


def output_file(input_num):
    fout = open("cowjog.out", "w")
    fout.write("{}".format(input_num))
    fout.close()


output_file(cows_are_jogging(input_file("cowjog_bronze/1.in")))
