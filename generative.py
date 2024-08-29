from random import randrange, sample, choice
from constants import Constants


def adapt(crom) -> int:
    score = 24
    for i in range(1, 25):
        for j in Constants.SC_MAP[str(i)]:
            if crom[str(i)] == crom[j]:
                score -= 1
                break
    return score


def generate_pop() -> list[tuple[int, dict[str, int]]]:
    crom_list = list()
    for _ in range(0, 10):
        crom = {}
        for i in range(1, 25):
            crom[str(i)] = randrange(0, 4)
        adaptation = adapt(crom)
        crom_list.append((adaptation,crom))
    crom_list.sort(key=lambda x: x[0],reverse=True)
    return crom_list


def cross(pop) -> list[tuple[int, dict[str, int]]]:
    crom_list = list()
    for i in range(0,5):
        for j in range(0,5):
            if i == j:
                continue
            n = randrange(1, 5)
            cross_list = sample(sorted(Constants.SC_MAP), k=n)
            pop_cross1= pop[i][1].copy()
            pop_cross2 = pop[j][1].copy()
            for x in cross_list:
                aux = pop_cross1[x]
                pop_cross1[x] = pop_cross2[x]
                pop_cross2[x] = aux
            adaptation1 = adapt(pop_cross1)
            crom_list.append((adaptation1, pop_cross1))
            adaptation2 = adapt(pop_cross2)
            crom_list.append((adaptation2, pop_cross2))
    return crom_list


def mutate(pop) -> list[tuple[int, dict[str, int]]]:
    crom_list = list()
    for i in range(0,5):
        n = randrange(4,11)
        mutate_list = sample(sorted(Constants.SC_MAP), k=n)
        pop_mutate = pop[i][1].copy()
        for x in mutate_list:
            colors = [0,1,2,3]
            colors.remove(pop_mutate[x])
            pop_mutate[x] = choice(colors)
        adaptation = adapt(pop_mutate)
        crom_list.append((adaptation,pop_mutate))
    return crom_list
