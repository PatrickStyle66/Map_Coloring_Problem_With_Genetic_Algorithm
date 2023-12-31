import  pygame
from  GAfunctions import *
W, H = 818, 622

win = pygame.display.set_mode((W, H))

pygame.display.set_caption('GA_Visualization')

bg = pygame.image.load('SCMap.jpg').convert()

pygame.init()
font = pygame.font.SysFont('comicsans', 30)
run = True
InitialPop = generatePop()
InitialPop.sort(key=lambda x: x[0],reverse=True)
population = InitialPop[:]
score = 0
iter = 1
while run:
    win.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    for i in range(1, 25):
        for j in ScMap[str(i)]:
            pygame.draw.line(win,[0,0,0],ScPositions[(str(i))],ScPositions[(str(j))],width=4)
    for position in ScPositions:
        if iter < 2:
            pygame.draw.circle(win, [0, 0, 0], ScPositions[position], 12)
            pygame.draw.circle(win, [255, 255, 255], ScPositions[position], 10)
        else:
            pygame.draw.circle(win, [0, 0, 0], ScPositions[position], 12)
            pygame.draw.circle(win, ScColors[best[1][position]], ScPositions[position], 10)
    if score != 24:
        Best5 = population[:5]
        Worst5 = population[5:]
        population.extend(Cross(Best5))
        population.extend(Mutate(Worst5))
        population.sort(key=lambda x: x[0], reverse=True)
        NextGen = population[:10]
        best = population[0]
        print(best)
        score = best[0]
        if iter == 1:
            startingscore = score
        population = NextGen[:]
        generation = font.render(f'Generation: {iter}',1,(0,0,0))
        genscore = font.render(f'Best Chromossome score: {score}',1,(0,0,0))
        startscore = font.render(f'Starting score: {startingscore}',1,(0,0,0))
        win.blit(startscore, (50, 325))
        win.blit(generation, (50, 375))
        win.blit(genscore, (50, 425))
        iter = iter + 1
    else:
        startscore = font.render(f'Starting score: {startingscore}', 1, (0, 0, 0))
        generation = font.render(f'Generation: {iter}', 1, (0, 0, 0))
        genscore = font.render(f'Best Chromossome score: {score}', 1, (0, 0, 0))
        bestgen = font.render(f'Best Generation: {iter}', 1, (0, 0, 0))
        win.blit(startscore,(50,335))
        win.blit(generation, (50, 375))
        win.blit(genscore, (50, 425))
        win.blit(bestgen,(50,475))
    pygame.display.update()