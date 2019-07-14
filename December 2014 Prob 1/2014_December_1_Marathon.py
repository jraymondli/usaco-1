def distance_between_two_points(point1, point2):  # Works
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])


def find_dist(points):  # Should work
    last_point = points[0]
    dist = 0
    for x, y in points:
        dist += distance_between_two_points(last_point, [x, y])
        last_point = [x, y]
    return dist


def input_file(file_name):
    fin = open(file_name)
    count = 0
    all_points = []
    for line in fin:
        line = line.strip()
        if count > 0:
            line = list(map(lambda x: int(x), line.split(" ")))
            all_points.append(line)
        count += 1
    fin.close()
    return all_points


def derive_answer(input_points):
    min_length = find_dist(input_points)
    for possible_point_to_skip in input_points[1:-1:]:
        temp = input_points.copy()
        temp.remove(possible_point_to_skip)
        distance = find_dist(temp)
        if distance < min_length:
            min_length = distance
    return min_length


def output_file(input_num):  # Works
    fout = open("marathon.out", "w")
    fout.write("{}".format(input_num))
    fout.close()


output_file(derive_answer(input_file("marathon_bronze/7.in")))
