flowerbed = [1,0,0,0,0,1]
print(flowerbed[0])
n = 2
x = 0

for i in range(len(flowerbed)):
    if flowerbed[i] == 0:
        if i == 0 or flowerbed[i-1] == 0:
            if i+1 < len(flowerbed) and (flowerbed[i+1] == 0 or i== len(flowerbed)-1):
                x = x + 1
            elif len(flowerbed) == 1 and flowerbed[i] == 0:
                x = x + 1



print(n==x)