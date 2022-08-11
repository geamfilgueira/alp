a = int(input())

i = 1

while i <= a:
    j = 0
    print(f"Tabuada do {i}")
    while j <= 10:
        print(f"{i} x {j} = {i * j}")
        j = j + 1
    print("")
    i = i + 1

