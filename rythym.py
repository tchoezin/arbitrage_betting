dank = [650, -1150, -145, 115, 215, -265, 600, -900, 320, -425, -120, 100, -135, 115]
fank = [111150, -1150, -145, 115, 215, -265, 600, -900, 320, -425, -120, 100, -135, 115]
dank1 = ['ATL Hawks', 650, 'MIA Heat', -950, 'MIN Timberwolves', -145, 'MEM Grizzlies', 195, 'NO Pelicans', 215, 'PHO Suns', -255, 'CHI Bulls', 600, 'MIL Bucks', -500, 'DEN Nuggets', 360, 'GS Warriors', -425, 'PHI 76ers', -120, 'TOR Raptors', 100, 'DAL Mavericks', -100, 'UTA Jazz', 115]
dank2 = ['ATL Hawks', 750, 'MIA Heat', -1250, 'MIN Timberwolves', -65, 'MEM Grizzlies', 115, 'NO Pelicans', 315, 'PHO Suns', -265, 'CHI Bulls', 700, 'MIL Bucks', -900, 'DEN Nuggets', 220, 'GS Warriors', -225, 'PHI 76ers', -100, 'TOR Raptors', 170, 'DAL Mavericks', -135, 'UTA Jazz', 125]

list = []
list2 = []
twolist = []

#print(list)
#print(list2)

def daSorter(needlist):
    newfriend = []
    for i in range(0, len(needlist), 2):
        newList = []
        newList.append(needlist[i])
        if needlist[i+1] < 0:
            needlist[i+1] = -100/needlist[i+1]+1
        else:
            needlist[i+1] = needlist[i+1]/100+1
        newList.append(needlist[i+1])
        newfriend.append(newList)
    return newfriend

bdank = daSorter(dank1)
rdank = daSorter(dank2)
print(bdank)
#print(rdank)


def maxOdds(uno, dos):
    bestfriend = []
    for e in uno:
        for w in dos:
            if e[0] == w[0]:
                dude = []
                dude.append(e[0])
                q = max(e[1],w[1])
                dude.append(q)
                bestfriend.append(dude)
    return bestfriend
    
k = maxOdds(bdank, rdank)
#print(k)

def marginbeast(damax):
    final = []
    for z in range(0, len(damax),2):
        v = damax[z]
        b = damax[z+1]
        final.append(v[0])
        final.append(b[0])
        k = (((1/v[1])+(1/b[1]))*100)/100
        final.append(k)
    return final

print(marginbeast(k))



for i in range(0, len(list), 2):
        gameList = []
        gameList.append(list[i])
        gameList.append(list[i+1])
        twolist.append(gameList)

##print(twolist)

for j in twolist: 
    k = (((1/j[0])+(1/j[1]))*100)/100
  
 

##for y in range(0, len(twolist), 1):
   # k=twolist[y]
   #k = (((1/y(0))+(1/y(1)))*100)/100
   # print(k)


 

   

