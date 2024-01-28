from  GAfunctions import *
from PygameClasses import *
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
regen = button((0, 100, 0), 159, 550, 200, 50, std_button('Generate again',0))
step_by_step = button((0, 100, 0), 434, 550, 200, 50, std_button('Step By Step',0))
show_button = False
MapsList = []
scoresList = []
generationList = []

def StepFunc(MapsList,scoresList,generationsList):
    run = True
    currentMap = 0
    leftButton = button((0, 100, 0), 235, 550, 50, 50, std_button('<',0))
    rightButton = button((0, 100, 0), 460, 550, 50, 50, std_button('>', 0))
    backButton = button((0, 100, 0), 320, 550, 100, 50, std_button('back',0))
    while run:
        win.blit(bg, (0, 0))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if leftButton.isOver(pos):
                leftButton.color = (0,255,0)
                if event.type == pygame.MOUSEBUTTONDOWN and currentMap != 0:
                    currentMap = currentMap - 1
            else:
                leftButton.color = (0,100,0)
            if rightButton.isOver(pos):
                rightButton.color = (0, 255, 0)
                if event.type == pygame.MOUSEBUTTONDOWN and currentMap < len(MapsList) - 1:
                    currentMap = currentMap + 1
            else:
                rightButton.color= (0,100,0)
            if backButton.isOver(pos):
                backButton.color = (0,255,0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    run = False
            else:
                backButton.color = (0,100,0)
        for i in range(1, 25):
            for j in ScMap[str(i)]:
                pygame.draw.line(win, [0, 0, 0], ScPositions[(str(i))], ScPositions[(str(j))], width=4)
        for position in ScPositions:
            pygame.draw.circle(win, [0, 0, 0], ScPositions[position], 12)
            pygame.draw.circle(win, ScColors[MapsList[currentMap][1][position]], ScPositions[position], 10)
        generation = font.render(f'Generation: {generationsList[currentMap]}', 1, (0, 0, 0))
        genscore = font.render(f'Best Chromossome score: {scoresList[currentMap]}', 1, (0, 0, 0))
        win.blit(generation, (50, 375))
        win.blit(genscore, (50, 425))
        leftButton.draw(win,(0,0,0))
        rightButton.draw(win,(0,0,0))
        backButton.draw(win,(0,0,0))
        pygame.display.update()


while run:
    win.blit(bg,(0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if regen.isOver(pos) and show_button:
            regen.color = (0,255,0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                InitialPop = generatePop()
                InitialPop.sort(key=lambda x: x[0], reverse=True)
                population = InitialPop[:]
                score = 0
                iter = 1
                MapsList = []
                scoresList = []
                generationList = []
        else:
            regen.color = (0, 100, 0)
        if step_by_step.isOver(pos) and show_button:
            step_by_step.color = (0,255,0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                StepFunc(MapsList,scoresList,generationList)

        else:
            step_by_step.color = (0, 100, 0)
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
        previous_score = score
        score = best[0]
        if score > previous_score:
            MapsList.append(best)
            scoresList.append(score)
            generationList.append(iter)
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
        show_button = False
    else:
        startscore = font.render(f'Starting score: {startingscore}', 1, (0, 0, 0))
        generation = font.render(f'Generation: {iter}', 1, (0, 0, 0))
        genscore = font.render(f'Best Chromossome score: {score}', 1, (0, 0, 0))
        bestgen = font.render(f'Best Generation: {iter}', 1, (0, 0, 0))
        show_button = True
        regen.draw(win, (0, 0, 0))
        step_by_step.draw(win,(0,0,0))
        win.blit(startscore,(50,335))
        win.blit(generation, (50, 375))
        win.blit(genscore, (50, 425))
        win.blit(bestgen,(50,475))

    pygame.display.update()