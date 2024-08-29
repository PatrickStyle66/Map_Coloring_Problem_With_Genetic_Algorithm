import pygame
from generative import generate_pop, cross, mutate
from buttons import Button, StdButton
from constants import Constants

WIDTH, HEIGHT = 818, 622
pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Map Coloring Problem')

bg = pygame.image.load('SCMap.jpg').convert()
font = pygame.font.SysFont('comicsans', 30)


def handle_step_buttons(event, pos, buttons, current_map, right_limit) -> tuple[bool, int]:
    left_button, right_button, back_button = buttons
    if left_button.hover(pos) and event.type == pygame.MOUSEBUTTONDOWN and current_map >= 0:
        current_map -= 1
    if right_button.hover(pos) and event.type == pygame.MOUSEBUTTONDOWN and current_map < right_limit:
        current_map += 1
    if back_button.hover(pos) and event.type == pygame.MOUSEBUTTONDOWN:
        return False, current_map

    return True, current_map


def draw_step_map(maps_list, scores_list, generations_list, current_map) -> None:
    for i in range(1, 25):
        for j in Constants.SC_MAP[str(i)]:
            pygame.draw.line(WIN, Constants.BLACK, Constants.SC_POSITIONS[(str(i))], Constants.SC_POSITIONS[(str(j))], width=4)
    for position in Constants.SC_POSITIONS:
        pygame.draw.circle(WIN, Constants.BLACK, Constants.SC_POSITIONS[position], 12)
        pygame.draw.circle(WIN, Constants.SC_COLORS[maps_list[current_map][1][position]], Constants.SC_POSITIONS[position], 10)
    generation = font.render(f'Generation: {generations_list[current_map]}', 1, Constants.BLACK)
    genscore = font.render(f'Best Chromossome score: {scores_list[current_map]}', 1, Constants.BLACK)
    WIN.blit(generation, (50, 375))
    WIN.blit(genscore, (50, 425))


def step_func(maps_list, scores_list, generations_list) -> None:
    run = True
    current_map = 0
    left_button = Button(Constants.DARK_GREEN, 235, 550, 50, 50, StdButton('<',0))
    right_button = Button(Constants.DARK_GREEN, 460, 550, 50, 50, StdButton('>', 0))
    back_button = Button(Constants.DARK_GREEN, 320, 550, 100, 50, StdButton('back',0))
    buttons = [left_button, right_button, back_button]
    right_limit = len(maps_list) - 1
    while run:
        WIN.blit(bg, (0, 0))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            run, current_map = handle_step_buttons(event, pos, buttons, current_map, right_limit)
        
        draw_step_map(maps_list, scores_list, generations_list, current_map)
        left_button.draw(WIN,Constants.BLACK)
        right_button.draw(WIN,Constants.BLACK)
        back_button.draw(WIN,Constants.BLACK)
        pygame.display.update()


def end_processing(startingscore, iteration, score, regen, step_by_step) -> None:
    startscore = font.render(f'Starting score: {startingscore}', 1, Constants.BLACK)
    generation = font.render(f'Generation: {iteration - 1}', 1, Constants.BLACK)
    genscore = font.render(f'Best Chromossome score: {score}', 1, Constants.BLACK)
    bestgen = font.render(f'Best Generation: {iteration - 1} ', 1, Constants.BLACK)
    regen.draw(WIN, Constants.BLACK)
    step_by_step.draw(WIN,Constants.BLACK)
    WIN.blit(startscore, (50, 335))
    WIN.blit(generation, (50, 375))
    WIN.blit(genscore, (50, 425))
    WIN.blit(bestgen, (50,475))


def display_gen_info(iteration, score, startingscore) -> None:
    generation = font.render(f'Generation: {iteration}',1,Constants.BLACK)
    genscore = font.render(f'Best Chromossome score: {score}',1,Constants.BLACK)
    startscore = font.render(f'Starting score: {startingscore}',1,Constants.BLACK)
    WIN.blit(startscore, (50, 325))
    WIN.blit(generation, (50, 375))
    WIN.blit(genscore, (50, 425))


def new_generation(population) -> tuple[list[tuple[int, dict[str, int]]], tuple[int, dict[str, int]]]:
    best5 = population[:5]
    worst5 = population[5:]
    population.extend(cross(best5))
    population.extend(mutate(worst5))
    population.sort(key=lambda x: x[0], reverse=True)
    best = population[0]
    print(best)
    return population[:10], best


def draw_map(iteration, best) -> None:
    for i in range(1, 25):
        for j in Constants.SC_MAP[str(i)]:
            pygame.draw.line(
                WIN,
                Constants.BLACK,
                Constants.SC_POSITIONS[(str(i))],
                Constants.SC_POSITIONS[(str(j))],
                width=4
            )
    for position in Constants.SC_POSITIONS:
        if iteration < 2:
            pygame.draw.circle(WIN, Constants.BLACK, Constants.SC_POSITIONS[position], 12)
            pygame.draw.circle(WIN, Constants.WHITE, Constants.SC_POSITIONS[position], 10)
        else:
            pygame.draw.circle(WIN, Constants.BLACK, Constants.SC_POSITIONS[position], 12)
            pygame.draw.circle(WIN, Constants.SC_COLORS[best[1][position]], Constants.SC_POSITIONS[position], 10)


def handle_main_buttons(event, pos, buttons, show_button, maps_list, scores_list, generation_list) -> None:
    regen, step_by_step = buttons
    if regen.hover(pos) and show_button and event.type == pygame.MOUSEBUTTONDOWN:
        main()
        exit()
    if step_by_step.hover(pos) and show_button:
        if event.type == pygame.MOUSEBUTTONDOWN:
            step_func(maps_list,scores_list,generation_list)


def main() -> None:
    run = True
    initial_pop = generate_pop()
    population = initial_pop[:]
    score = 0
    iteration = 1
    regen = Button(Constants.DARK_GREEN, 159, 550, 200, 50, StdButton('Generate again',0))
    step_by_step = Button(Constants.DARK_GREEN, 434, 550, 200, 50, StdButton('Step By Step',0))
    buttons = [regen, step_by_step]
    show_button = False
    maps_list = []
    scores_list = []
    generation_list = []
    while run:
        WIN.blit(bg,(0,0))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            handle_main_buttons(event, pos, buttons, show_button, maps_list, scores_list, generation_list)

        if score != 24:
            next_gen, best = new_generation(population)
            previous_score = score
            score = best[0]
            if score > previous_score:
                maps_list.append(best)
                scores_list.append(score)
                generation_list.append(iteration)
            if iteration == 1:
                startingscore = score
            population = next_gen[:]
            display_gen_info(iteration, score, startingscore)
            iteration = iteration + 1
            show_button = False
        else:
            end_processing(startingscore, iteration, score, regen, step_by_step)
            show_button = True
        draw_map(iteration, best)

        pygame.display.update()


if __name__ == '__main__':
    main()
