import pygame
from GAfunctions import SC_COLORS, SC_MAP, SC_POSITIONS, generate_pop, cross, mutate
from PygameClasses import button, std_button

W, H = 818, 622

win = pygame.display.set_mode((W, H))

pygame.display.set_caption('GA_Visualization')

bg = pygame.image.load('SCMap.jpg').convert()

pygame.init()
font = pygame.font.SysFont('comicsans', 30)


def step_func(maps_list, scores_list, generations_list):
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
            if leftButton.is_over(pos):
                leftButton.color = (0,255,0)
                if event.type == pygame.MOUSEBUTTONDOWN and currentMap != 0:
                    currentMap = currentMap - 1
            else:
                leftButton.color = (0,100,0)
            if rightButton.is_over(pos):
                rightButton.color = (0, 255, 0)
                if event.type == pygame.MOUSEBUTTONDOWN and currentMap < len(maps_list) - 1:
                    currentMap = currentMap + 1
            else:
                rightButton.color= (0,100,0)
            if backButton.is_over(pos):
                backButton.color = (0,255,0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    run = False
            else:
                backButton.color = (0,100,0)
        for i in range(1, 25):
            for j in SC_MAP[str(i)]:
                pygame.draw.line(win, [0, 0, 0], SC_POSITIONS[(str(i))], SC_POSITIONS[(str(j))], width=4)
        for position in SC_POSITIONS:
            pygame.draw.circle(win, [0, 0, 0], SC_POSITIONS[position], 12)
            pygame.draw.circle(win, SC_COLORS[maps_list[currentMap][1][position]], SC_POSITIONS[position], 10)
        generation = font.render(f'Generation: {generations_list[currentMap]}', 1, (0, 0, 0))
        genscore = font.render(f'Best Chromossome score: {scores_list[currentMap]}', 1, (0, 0, 0))
        win.blit(generation, (50, 375))
        win.blit(genscore, (50, 425))
        leftButton.draw(win,(0,0,0))
        rightButton.draw(win,(0,0,0))
        backButton.draw(win,(0,0,0))
        pygame.display.update()


def main():
    run = True
    InitialPop = generate_pop()
    InitialPop.sort(key=lambda x: x[0],reverse=True)
    population = InitialPop[:]
    score = 0
    iteration = 1
    regen = button((0, 100, 0), 159, 550, 200, 50, std_button('Generate again',0))
    step_by_step = button((0, 100, 0), 434, 550, 200, 50, std_button('Step By Step',0))
    show_button = False
    maps_list = []
    scores_list = []
    generationList = []
    while run:
        win.blit(bg,(0,0))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if regen.is_over(pos) and show_button:
                regen.color = (0,255,0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    InitialPop = generate_pop()
                    InitialPop.sort(key=lambda x: x[0], reverse=True)
                    population = InitialPop[:]
                    score = 0
                    iteration = 1
                    maps_list = []
                    scores_list = []
                    generationList = []
            else:
                regen.color = (0, 100, 0)
            if step_by_step.is_over(pos) and show_button:
                step_by_step.color = (0,255,0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    step_func(maps_list,scores_list,generationList)

            else:
                step_by_step.color = (0, 100, 0)
        for i in range(1, 25):
            for j in SC_MAP[str(i)]:
                pygame.draw.line(win,[0,0,0],SC_POSITIONS[(str(i))],SC_POSITIONS[(str(j))],width=4)
        for position in SC_POSITIONS:
            if iteration < 2:
                pygame.draw.circle(win, [0, 0, 0], SC_POSITIONS[position], 12)
                pygame.draw.circle(win, [255, 255, 255], SC_POSITIONS[position], 10)
            else:
                pygame.draw.circle(win, [0, 0, 0], SC_POSITIONS[position], 12)
                pygame.draw.circle(win, SC_COLORS[best[1][position]], SC_POSITIONS[position], 10)
        if score != 24:
            Best5 = population[:5]
            Worst5 = population[5:]
            population.extend(cross(Best5))
            population.extend(mutate(Worst5))
            population.sort(key=lambda x: x[0], reverse=True)
            NextGen = population[:10]
            best = population[0]
            print(best)
            previous_score = score
            score = best[0]
            if score > previous_score:
                maps_list.append(best)
                scores_list.append(score)
                generationList.append(iteration)
            if iteration == 1:
                startingscore = score
            population = NextGen[:]
            generation = font.render(f'Generation: {iteration}',1,(0,0,0))
            genscore = font.render(f'Best Chromossome score: {score}',1,(0,0,0))
            startscore = font.render(f'Starting score: {startingscore}',1,(0,0,0))
            win.blit(startscore, (50, 325))
            win.blit(generation, (50, 375))
            win.blit(genscore, (50, 425))
            iteration = iteration + 1
            show_button = False
        else:
            startscore = font.render(f'Starting score: {startingscore}', 1, (0, 0, 0))
            generation = font.render(f'Generation: {iteration - 1}', 1, (0, 0, 0))
            genscore = font.render(f'Best Chromossome score: {score}', 1, (0, 0, 0))
            bestgen = font.render(f'Best Generation: {iteration - 1} ', 1, (0, 0, 0))
            show_button = True
            regen.draw(win, (0, 0, 0))
            step_by_step.draw(win,(0,0,0))
            win.blit(startscore,(50,335))
            win.blit(generation, (50, 375))
            win.blit(genscore, (50, 425))
            win.blit(bestgen,(50,475))

        pygame.display.update()


if __name__ == '__main__':
    main()
