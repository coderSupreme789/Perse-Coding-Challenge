lemons, sugar = int(input()), int(input())
if lemons >= 20 and sugar >= 3:
    print("A")
elif lemons < 20 and sugar >= 3:
    print("B")
elif lemons >= 20 and sugar < 3:
    print("C")
else:
    print("D")
