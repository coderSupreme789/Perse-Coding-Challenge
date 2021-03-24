starting, jumps = input(), int(input())
seasons = ["spring", "summer", "autumn", "winter"]
pos = seasons.index(starting)
for i in range(jumps):
    pos += 1
    pos %= 4
print(seasons[pos])
