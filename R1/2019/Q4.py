terms = [int(input()) for i in range(4)]

if terms[3] - terms[2] == terms[2] - terms[1] and terms[2] - terms[1] == terms[1] - terms[0]:
    print(str(terms[3]-terms[2]))
else:
    print("NO")
