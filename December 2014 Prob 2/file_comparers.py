def compare2files(file1, file2):
    fin1 = open(file1)
    fin2 = open(file2)
    file1_cont = []
    file2_cont = []
    for line in fin1:
        line = line.strip()
        file1_cont.append(line)
    for line in fin2:
        line = line.strip()
        file2_cont.append(line)
    for i in range(len(file1)):
        if not file1_cont[i] == file2_cont[i]:
            print(i+1)


compare2files("8.out", "crosswords.out")
