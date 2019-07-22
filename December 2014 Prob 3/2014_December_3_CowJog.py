def input_file(file_name):
    fin = open(file_name)
    count = 0
    all_cows = []
    for line in fin:
        line = line.strip()
        if count > 0:
            line = list(map(lambda x: int(x), line.split(" ")))
            all_cows.append(line)
        count += 1
    fin.close()
    return all_cows


def jog_once(input_cows):
    input_cows = list(map())



def cows_are_jogging(input_cows):
    same_pace = False
    while not same_pace:

        pace = input_cows[0][1]
        all_same_pace = True
        for cow in input_cows:
            if cow[1] != pace:
                all_same_pace = False
        same_pace = all_same_pace


def output_file(input_num):
    fout = open("cowjog.out", "w")
    fout.write("{}".format(input_num))
    fout.close()


output_file(input_file("cowjog.in"))
