import pygame
from generative import SC_COLORS, SC_MAP, SC_POSITIONS, generate_pop, cross, mutate
from buttons import button, std_button
from colors import Colors

WIDTH, HEIGHT = 818, 622

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Map Coloring Problem')

bg = pygame.image.load('SCMap.jpg').convert()

pygame.init()
font = pygame.font.SysFont('comicsans', 30)


def handle_step_buttons(event, pos, buttons, current_map, right_limit):
    left_button, right_button, back_button = buttons
    if left_button.hover(pos) and event.type == pygame.MOUSEBUTTONDOWN and current_map >= 0:
        current_map -= 1
    if right_button.hover(pos) and event.type == pygame.MOUSEBUTTONDOWN and current_map < right_limit:
        current_map += 1
    if back_button.hover(pos) and event.type == pygame.MOUSEBUTTONDOWN:
        return False, current_map

    return True, current_map


def draw_step_map(maps_list, scores_list, generations_list, current_map):
    for i in range(1, 25):
        for j in SC_MAP[str(i)]:
            pygame.draw.line(WIN, Colors.BLACK, SC_POSITIONS[(str(i))], SC_POSITIONS[(str(j))], width=4)
    for position in SC_POSITIONS:
        pygame.draw.circle(WIN, Colors.BLACK, SC_POSITIONS[position], 12)
        pygame.draw.circle(WIN, SC_COLORS[maps_list[current_map][1][position]], SC_POSITIONS[position], 10)
    generation = font.render(f'Generation: {generations_list[current_map]}', 1, Colors.BLACK)
    genscore = font.render(f'Best Chromossome score: {scores_list[current_map]}', 1, Colors.BLACK)
    WIN.blit(generation, (50, 375))
    WIN.blit(genscore, (50, 425))


def step_func(maps_list, scores_list, generations_list):
    run = True
    current_map = 0
    left_button = button(Colors.DARK_GREEN, 235, 550, 50, 50, std_button('<',0))
    right_button = button(Colors.DARK_GREEN, 460, 550, 50, 50, std_button('>', 0))
    back_button = button(Colors.DARK_GREEN, 320, 550, 100, 50, std_button('back',0))
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
        left_button.draw(WIN,Colors.BLACK)
        right_button.draw(WIN,Colors.BLACK)
        back_button.draw(WIN,Colors.BLACK)
        pygame.display.update()


def end_processing(startingscore, iteration, score, regen, step_by_step):
    startscore = font.render(f'Starting score: {startingscore}', 1, Colors.BLACK)
    generation = font.render(f'Generation: {iteration - 1}', 1, Colors.BLACK)
    genscore = font.render(f'Best Chromossome score: {score}', 1, Colors.BLACK)
    bestgen = font.render(f'Best Generation: {iteration - 1} ', 1, Colors.BLACK)
    regen.draw(WIN, Colors.BLACK)
    step_by_step.draw(WIN,Colors.BLACK)
    WIN.blit(startscore, (50, 335))
    WIN.blit(generation, (50, 375))
    WIN.blit(genscore, (50, 425))
    WIN.blit(bestgen, (50,475))


def display_gen_info(iteration, score, startingscore):
    generation = font.render(f'Generation: {iteration}',1,Colors.BLACK)
    genscore = font.render(f'Best Chromossome score: {score}',1,Colors.BLACK)
    startscore = font.render(f'Starting score: {startingscore}',1,Colors.BLACK)
    WIN.blit(startscore, (50, 325))
    WIN.blit(generation, (50, 375))
    WIN.blit(genscore, (50, 425))


def new_generation(population):
    best5 = population[:5]
    worst5 = population[5:]
    population.extend(cross(best5))
    population.extend(mutate(worst5))
    population.sort(key=lambda x: x[0], reverse=True)
    best = population[0]
    print(best)
    return population[:10], best


def draw_map(iteration, best):
    for i in range(1, 25):
        for j in SC_MAP[str(i)]:
            pygame.draw.line(WIN,Colors.BLACK,SC_POSITIONS[(str(i))],SC_POSITIONS[(str(j))],width=4)
    for position in SC_POSITIONS:
        if iteration < 2:
            pygame.draw.circle(WIN, Colors.BLACK, SC_POSITIONS[position], 12)
            pygame.draw.circle(WIN, Colors.WHITE, SC_POSITIONS[position], 10)
        else:
            pygame.draw.circle(WIN, Colors.BLACK, SC_POSITIONS[position], 12)
            pygame.draw.circle(WIN, SC_COLORS[best[1][position]], SC_POSITIONS[position], 10)


def handle_main_buttons(event, pos, buttons, show_button, maps_list, scores_list, generation_list):
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
    regen = button(Colors.DARK_GREEN, 159, 550, 200, 50, std_button('Generate again',0))
    step_by_step = button(Colors.DARK_GREEN, 434, 550, 200, 50, std_button('Step By Step',0))
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
