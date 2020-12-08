with open('input.txt', 'r') as input:
    data = input.read().strip().split('\n\n')

data = [i.replace('\n', " ") for i in data]

for i, x in enumerate(data):
    data[i] = x.split()
    aaa = {}
    for n, y in enumerate(data[i]):
        a, b = y.split(':')
        #data[i][n] = {a:b}
        aaa[a] = b
    data[i] = aaa

    #print(data[i])

valid = 0

#print(data)
exps = ["pid", "ecl", "hcl", "hgt", "eyr", "iyr", "byr"]
for i in data:
    if "pid" in i and "ecl" in i and "hcl" in i and "hgt" in i and "eyr" in i and "iyr" in i and "byr" in i:
        valid += 1
    else:
        print("nok")

print(valid)