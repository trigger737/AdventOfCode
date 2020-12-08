def main():
    fin = open("input.txt", "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    p1, p2 = 0, 0
    for line in lines:
        a, b, c = line.split()
        b = b[0]
        lo, hi = map(int, a.split("-"))
        p1 += lo <= c.count(b) <= hi
        p2 += sum(c[x - 1] == b for x in (lo, hi)) == 1
    print(p1)
    print(p2)

if __name__ == "__main__":
    main()