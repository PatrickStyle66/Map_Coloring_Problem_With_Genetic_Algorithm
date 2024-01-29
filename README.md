## The map coloring problem
The map coloring problem( or the four color theorem ) states that no more than four colors are required to color the regions of any map so that no two adjacent regions have the same color. While this seems to be a (not so) simple task to do manually, doing it using an algorithm can be very time-consuming considering that this is an NP-complete problem.

## Genetic Algorithm
There's some interesting algorithms that solve the map coloring problem and their complexity depends on the number of vertices and/or edges of the graph, but with the genetic algorithm the only factor that counts for the result is the **randomness**. But the beautiful part about it is that such randomness is directed to a goal, by using crossover and mutation techniques found in the genetic algorithms we can control the random fact by measuring how good the samples are and selecting the best ones generated randomly and continue to evolve them eventually achieveing the answer to the problem!

In this scenario, I applied the crossover technique on the best samples and the mutation on the worst samples. This way, we can get better samples for each generation.

## Visualization
In this example, I used a map from a brazilian state called 'Santa Catarina' and built a graph representing it.

### It can achieve the answer really fast:
![GoodScore](https://github.com/PatrickStyle66/Map_Coloring_Problem_With_Genetic_Algorithm/assets/30088774/b3e528d1-e141-4643-a32f-264943aa2137)

### Or it can struggle to find the answer:
![NotGoodScore](https://github.com/PatrickStyle66/Map_Coloring_Problem_With_Genetic_Algorithm/assets/30088774/77316848-25b5-4f61-b509-73f68d5817fe)
## Step by Step function
You can use this option to see only the major changes to the map and which generation this changes occurred
![Step By Step](https://github.com/PatrickStyle66/Map_Coloring_Problem_With_Genetic_Algorithm/assets/30088774/64721944-9f45-49fc-8c3c-68deeb0f5b03)
