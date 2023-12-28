## The map coloring problem
The map coloring problem( or the four color theorem ) states that no more than four colors are required to color the regions of any map so that no two adjacent regions have the same color. While this seems to be a (not so) simple task to do manually, doing it using an algorithm can be very time-consuming considering that this is an NP-complete problem.

## Genetic Algorithm
There's some interesting algorithms that solve the map coloring problem and their complexity depends on the number of vertices and/or edges of the graph, but with the genetic algorithm the only factor that counts for the result is the **randomness**. But the beautiful part about it is that such randomness is directed to a goal, by using crossover and mutation techniques found in the genetic algorithms we can control the random fact by measuring how good the samples are and selecting the best ones generated randomly and continue to evolve them eventually achieveing the answer to the problem!

In this scenario, I applied the crossover technique on the best samples and the mutation on the worst samples. This way, we can get better samples for each generation.

## Visualization
In this example, I used a map from a brazilian state called 'Santa Catarina' and built a graph representing it.

### It can achieve the answer really fast:
![GoodScore](https://github.com/PatrickStyle66/FootbalExtension/assets/30088774/92650ac7-c2be-4d31-bc5c-13be877f7f16)

### Or it can struggle to find the answer:
![NotGoodScore](https://github.com/PatrickStyle66/FootbalExtension/assets/30088774/ad411ef2-6488-45ce-9081-eb32e08d7a76)
