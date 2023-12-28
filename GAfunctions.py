import random

ScMap = {'10':['9'],
         '9':['10','17','14'],
         '17':['9','14','8'],
         '14':['9','17','8'],
         '8':['7','17','14','23'],
         '7':['8','23','11','4','6','18'],
         '18':['7','6'],
         '6':['7','18','4','24','22'],
         '22':['6','3','19','5'],
         '5':['22','19'],
         '19':['22','5','2','3'],
         '2':['19','3','16'],
         '16':['2','3','4','21','1'],
         '1':['16','21','11','12','20'],
         '20':['1','12','13'],
         '13':['11','12','15'],
         '15':['13'],
         '11':['23','7','4','21','1','12','13'],
         '23':['8','7','11'],
         '4':['7','6','24','21','3','11'],
         '24':['6','4','3'],
         '3':['24','22','19','2','16','4'],
         '21':['11','4','16','1'],
         '12':['11','1','20','13']}

ScPositions ={'1': (682, 307),
              '2': (705, 188),
              '3': (633, 177),
              '4': (553, 230),
              '5': (682, 80),
              '6': (543, 115),
              '7': (439, 180),
              '8': (326, 194),
              '9': (144, 162),
              '10': (72, 146),
              '11': (518, 333),
              '12': (643, 384),
              '13': (609, 439),
              '14': (268, 221),
              '15': (575, 492),
              '16': (673, 237),
              '17': (241, 155),
              '18': (471, 98),
              '19': (661, 129),
              '20': (691, 390),
              '21': (614, 272),
              '22': (620, 90),
              '23': (384, 262),
              '24': (576, 185)}

ScColors={0 : [65,105,225],
          1 : [255,0,0],
          2 : [0,255,0],
          3 : [255,255,0]}

def adapt(Crom):
    score = 24
    for i in range(1, 25):
        for j in ScMap[str(i)]:
            if Crom[str(i)] == Crom[j]:
                score -= 1
                break
    return score

def generatePop():
    cromList=[]
    for _ in range(0,10):
        Crom = {}
        for i in range(1, 25):
            Crom[str(i)] = random.randrange(0, 4)
        adaptation = adapt(Crom)
        cromList.append((adaptation,Crom))
    return cromList

def Cross(pop):
    cromList =[]
    for i in range(0,5):
        for j in range(0,5):
            if i == j:
                continue
            n = random.randrange(1, 5)
            crossList = random.sample(sorted(ScMap), k=n)
            popCross1= pop[i][1].copy()
            popCross2 = pop[j][1].copy()
            for x in crossList:
                aux = popCross1[x]
                popCross1[x] = popCross2[x]
                popCross2[x] = aux
            adaptation1 = adapt(popCross1)
            cromList.append((adaptation1, popCross1))
            adaptation2 = adapt(popCross2)
            cromList.append((adaptation2, popCross2))
    return cromList

def Mutate(pop):
    cromList = []
    for i in range(0,5):
        n = random.randrange(4,11)
        MutateList = random.sample(sorted(ScMap), k=n)
        popMutate = pop[i][1].copy()
        for x in MutateList:
            colors = [0,1,2,3]
            colors.remove(popMutate[x])
            popMutate[x] = random.choice(colors)
        adaptation = adapt(popMutate)
        cromList.append((adaptation,popMutate))
    return cromList

