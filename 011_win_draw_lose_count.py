n = int(input())
maxpoint = 0
topteam  = 0
wincount = []
drawcount = []
losecount = []
winpoint = []
for i in range(n):
    wincount.append(0)
    drawcount.append(0)
    losecount.append(0)
    winpoint.append(0)
    for j in input():
        if j == '-':
            continue
        elif j == 'W':
            wincount[i] += 1
            winpoint[i] += 2
        elif j == 'D':
            drawcount[i] += 1
            winpoint[i]  += 1
        elif j == 'L':
            losecount[i] += 1
        if winpoint[i] > maxpoint:
            maxpoint = winpoint[i]
            topteam = i
print('{} {} {} {} {}'.format(topteam + 1,winpoint[topteam],wincount[topteam],drawcount[topteam],losecount[topteam]))
