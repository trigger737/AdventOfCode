with open("input.txt", "r") as input_file:
    data = input_file.readlines()
data_upravena = [int(i.replace("\n", "")) for i in data]
for i in data_upravena:
    for n in data_upravena:
        for x in data_upravena:
            if i + n + x == 2020:
                print(i * n * x)
