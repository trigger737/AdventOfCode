#day 2/input.txt
with open("input.txt", "r") as input:
    data = input.read().splitlines()

counter = 0
result = 0
for idx, item in enumerate(data):
    splited = item.split(" ")
    splited[0] = splited[0]. split("-")
    letter = splited[1].replace(":", "")
    min = int(splited[0][0])
    max = int(splited[0][1])
    pwd = splited[2]
    count = pwd.count(letter)
    if count >= min and count <=max:
        counter += 1
    else:
        pass

    if letter == pwd[min-1] and letter == pwd[max-1]:
        pass
    elif letter == pwd[min-1]:
        result += 1
    elif letter == pwd[max-1]:
        result += 1
    else:
        pass
    print(str(min) + "-"+ str(max) ,letter, pwd, result)
print("pocet validnich hesel: ", counter)
print(result)





