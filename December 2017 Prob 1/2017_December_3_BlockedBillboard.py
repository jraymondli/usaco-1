def leftover_area(input_list, changer list):
    pass
# fin = open('billboard.in')
fin = open('ex.txt')
billboard1 = []
billboard2 = []
truck = []
count = 1
for line in fin:
    if count == 1:
        line = line.strip()
        x1, y1, x2, y2 = list(map(lambda x: int(x), line.split(' ')))
        billboard1 = [[x1, y1][x2, y2]]
    if count == 2:
        line = line.strip()
        x1, y1, x2, y2 = list(map(lambda x: int(x), line.split(' ')))
        billboard2 = [[x1, y1][x2, y2]]
    if count == 3:
        line = line.strip()
        x1, y1, x2, y2 = list(map(lambda x: int(x), line.split(' ')))
        truck = [[x1, y1][x2, y2]]
    count += 1
fin.close()
board1 = leftover_area(billboard1, truck)
board2 = leftover_area(billboard2, truck)

print(board1 + board2)
# fout = open("billboard.out", "w")
# fout.write("{}".format(board1 + board2))
# fout.close()
