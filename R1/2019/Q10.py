val = 0
while True:
    coin = int(input())
    if coin == -1:
        break
    val += coin
    
print(30*(val//60))
