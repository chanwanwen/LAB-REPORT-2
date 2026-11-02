LAB REPORT 2 | CHAN WAN WEN | SD24059

Genetic Algorithm: Binary Pattern Optimisation

GitHub Repository: https://github.com/chanwanwen/LAB-REPORT-2
Live App: https://lab-report-2-6hwucpwohjorxbptkrbzst.streamlit.app/

**About**

This project is an interactive Streamlit application that implements a Genetic Algorithm (GA) to solve a binary pattern optimisation problem.

The objective is to find an 80-bit chromosome containing exactly 50 ones. The algorithm follows the assignment requirements, using a population of 300 individuals and evolving them over 50 generations.

The fitness function assigns a maximum score of 80 when a chromosome contains exactly 50 ones. The application allows users to explore different selection and crossover methods and observe how the population evolves over generations.

**Key Features**

- Fixed assignment parameters: Population size (300), chromosome length (80), target number of ones (50), maximum fitness (80), and 50 generations.
- Three selection methods: Tournament, Roulette Wheel, and Rank-based selection.
- Three crossover methods: One-point, Two-point, and Uniform crossover.
- Adjustable settings: Users can change the crossover rate, mutation rate, and random seed.
- Best solution display: Shows the best chromosome, its fitness score, and the number of ones and zeros.
- Fitness convergence graph: Visualises best, average, and lowest fitness across generations.
- Final population distribution: Displays a histogram of the number of ones in the final population.
- Generation statistics: Provides a table containing fitness and population information for each generation.
- CSV export: Allows users to download generation statistics for further analysis.

**MAIN APPLICATION**
<img width="1068" height="427" alt="image" src="https://github.com/user-attachments/assets/16247628-3a79-484b-9b0e-4406f8efb59e" />

**How to Use the Application**

1. Open the Streamlit application.
2. Select a preferred selection method (Tournament, Roulette Wheel, or Rank-based).
3. Select a crossover method (One-point, Two-point, or Uniform).
4. Adjust the crossover rate and mutation rate if needed.
5. Set a random seed to make the experiment reproducible.
6. Click Run Genetic Algorithm to start the optimisation process.
7. Review the best chromosome, fitness convergence graph, and final population distribution.
8. View or download the generation statistics in CSV format.

**How the Genetic Algorithm Works**

The application follows these main steps:
1. **Population Initialisation**: Generate 300 random binary chromosomes, each containing 80 bits.
2. **Fitness Evaluation**: Calculate the fitness of each chromosome based on the difference between its number of ones and the target value of 50.
3. **Selection**: Select parent chromosomes using Tournament, Roulette Wheel, or Rank-based selection.
4. **Crossover**: Combine two parent chromosomes using One-point, Two-point, or Uniform crossover.
5. **Mutation**: Randomly flip selected bits from 0 to 1 or from 1 to 0 based on the mutation rate.
6. **Elitism**: Preserve the best chromosome from the current generation by copying it into the next generation.
7. **Termination**: Repeat the process until all 50 generations have been completed and return the best chromosome found.

**RESULTS AND FITNESS CONVERGENCE**
<img width="857" height="269" alt="image" src="https://github.com/user-attachments/assets/71ab6098-0082-4cf0-aae7-78d6bd6aa1ee" />
<img width="839" height="432" alt="image" src="https://github.com/user-attachments/assets/476ea8d7-a234-4f23-80db-38f8e16eaa21" />

**FINAL POPULATION DISTRIBUTION**
<img width="1487" height="773" alt="image" src="https://github.com/user-attachments/assets/08d71171-5229-49b8-8fc9-70af41760ad4" />


<img width="1417" height="725" alt="image" src="https://github.com/user-attachments/assets/a90111ef-f0d6-4eb1-8a7d-afbd0510e35c" />
<img width="1482" height="705" alt="image" src="https://github.com/user-attachments/assets/7e8ba767-8e1d-45d8-9550-727ea25f5600" />
