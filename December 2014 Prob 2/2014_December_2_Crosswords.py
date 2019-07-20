def input_file(file_name):
    fin = open(file_name)
    count = 0
    all_points = []
    for line in fin:
        line = line.strip()
        if count > 0:
            line = list(line)
            all_points.append(line)
        count += 1
    fin.close()
    return all_points


def in_area(index, lst):
    return index in range(0, len(lst))


def check_if_horizontal(input_list, line, cell):
    if in_area(line + 2, input_list) or in_area(cell + 2, input_list):
        if input_list[line][cell] != "#":
            if not in_area(cell - 1, input_list[line]) and input_list[line][cell + 1] == "." and input_list[line][cell + 2] == ".":
                input_list[line][cell] = "!"
            try:
                if input_list[line][cell - 1] == "#" and input_list[line][cell + 1] == "." and input_list[line] \
                        [cell + 2] == ".":
                    input_list[line][cell] = "!"
            except:
                pass


def check_if_vertical(input_list, line, cell):
    if in_area(line + 2, input_list) or in_area(cell + 2, input_list):
        if input_list[line][cell] != "#":

            if not in_area(line - 1, input_list) and input_list[line + 1][cell] == "." and input_list[line + 2][cell] == ".":
                input_list[line][cell] = "!"
            try:

                if input_list[line - 1][cell] == "#" and input_list[line + 1][cell] == "." and \
                        input_list[line + 2][cell] == ".":
                    input_list[line][cell] = "!"
            except:
                pass


def if_starter(input_list):
    for line in range(len(input_list)):
        for cell in range(len(input_list[line])):
            check_if_horizontal(input_list, line, cell)
            check_if_vertical(input_list, line, cell)
    return input_list


def output_lines(input_list):
    all_lines = [0]
    for line in range(len(input_list)):
        for cell in range(len(input_list[line])):
            if input_list[line][cell] == "!":
                all_lines[0] += 1
                all_lines.append([line+1, cell+1])
    return all_lines


def output_file(input_list):
    fout = open("crosswords.out", "w")
    count = 1
    for line in input_list:
        if count == 1:
            fout.write("{}\n".format(line))
        else:
            fout.write("{} {}\n".format(line[0], line[1]))
        count += 1
    fout.close()


output_file(output_lines(if_starter(input_file("crosswords.in"))))
