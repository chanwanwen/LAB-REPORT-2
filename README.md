LAB REPORT 2 | CHAN WAN WEN | SD24059

Genetic Algorithm: Binary Pattern Optimisation

GitHub Repository: https://github.com/chanwanwen/LAB-REPORT-2
Live App: https://lab-report-2-6hwucpwohjorxbptkrbzst.streamlit.app/

**About**
***
This project is an interactive Streamlit application that implements a Genetic Algorithm (GA) to solve a binary pattern optimisation problem.

The objective is to find an 80-bit chromosome containing exactly 50 ones. The algorithm follows the assignment requirements, using a population of 300 individuals and evolving them over 50 generations.

The fitness function assigns a maximum score of 80 when a chromosome contains exactly 50 ones. The application allows users to explore different selection and crossover methods and observe how the population evolves over generations.

**Key Features**
***
- Fixed assignment parameters: Population size (300), chromosome length (80), target number of ones (50), maximum fitness (80), and 50 generations.
- Three selection methods: Tournament, Roulette Wheel, and Rank-based selection.
- Three crossover methods: One-point, Two-point, and Uniform crossover.
- Adjustable settings: Users can change the crossover rate, mutation rate, and random seed.
- Best solution display: Shows the best chromosome, its fitness score, and the number of ones and zeros.
- Fitness convergence graph: Visualises best, average, and lowest fitness across generations.
- Final population distribution: Displays a histogram of the number of ones in the final population.
- Generation statistics: Provides a table containing fitness and population information for each generation.
- CSV export: Allows users to download generation statistics for further analysis.

**How to Use the Application**
***
1. Open the Streamlit application.
2. Select a preferred selection method (Tournament, Roulette Wheel, or Rank-based).
3. Select a crossover method (One-point, Two-point, or Uniform).
4. Adjust the crossover rate and mutation rate if needed.
5. Set a random seed to make the experiment reproducible.
6. Click Run Genetic Algorithm to start the optimisation process.
7. Review the best chromosome, fitness convergence graph, and final population distribution.
8. View or download the generation statistics in CSV format.

**How the Genetic Algorithm Works**
***
The application follows these main steps:
1. **Population Initialisation**: Generate 300 random binary chromosomes, each containing 80 bits.
2. **Fitness Evaluation**: Calculate the fitness of each chromosome based on the difference between its number of ones and the target value of 50.
3. **Selection**: Select parent chromosomes using Tournament, Roulette Wheel, or Rank-based selection.
4. **Crossover**: Combine two parent chromosomes using One-point, Two-point, or Uniform crossover.
5. **Mutation**: Randomly flip selected bits from 0 to 1 or from 1 to 0 based on the mutation rate.
6. **Elitism**: Preserve the best chromosome from the current generation by copying it into the next generation.
7. **Termination**: Repeat the process until all 50 generations have been completed and return the best chromosome found.

**Code Overview**
***

The application is organised into several sections, each responsible for a different stage of the Genetic Algorithm and its Streamlit interface.

| Function / Section | Description |
|---|---|
| `fitness()` | Calculates the fitness score based on the difference between the chromosome's number of ones and the target of 50. |
| `init_population()` | Generates the initial population of 300 random binary chromosomes, each containing 80 bits. |
| `tournament_selection()` | Selects the chromosome with the highest fitness from randomly selected candidates. |
| `calculate_selection_probabilities()` | Calculates selection probabilities for Roulette Wheel and Rank-based selection. |
| `select_parent()` | Selects a parent chromosome using the selected selection method. |
| `one_point_crossover()` | Creates offspring by exchanging chromosome segments at one crossover point. |
| `two_point_crossover()` | Creates offspring by exchanging chromosome segments between two crossover points. |
| `uniform_crossover()` | Creates offspring by selecting individual bits from either parent using a random mask. |
| `apply_crossover()` | Applies the selected crossover method according to the crossover rate. |
| `mutate()` | Performs bit-flip mutation by changing selected bits from 0 to 1 or from 1 to 0. |
| `run_genetic_algorithm()` | Executes the GA process, including initialization, fitness evaluation, selection, crossover, mutation, elitism and generation tracking. |

### Streamlit Interface

The Streamlit interface allows users to configure and execute the Genetic Algorithm. It displays the best chromosome, fitness score, number of ones and zeros, fitness convergence graph, and final population distribution. Users can also view generation statistics and download them as a CSV file.

**MAIN APPLICATION**
***
<img width="1068" height="427" alt="image" src="https://github.com/user-attachments/assets/16247628-3a79-484b-9b0e-4406f8efb59e" />

**Installation and Setup**

Follow these steps to run the application locally.

**1. Clone the Repository**
***
git clone https://github.com/chanwanwen/LAB-REPORT-2.git

**Repository Structure**
***

LAB-REPORT-2/
│
├── app.py
├── requirements.txt
├── README.md
│
└── image/
    ├── Main_page.png
    ├── Results.png
    ├── Fitness_Convergence.png
    └── Final_Population.png

**Built With**
***
- Python – Main programming language.
- Streamlit – Interactive web application interface.
- NumPy – Binary chromosome operations and numerical calculations.
- Pandas – Generation statistics and CSV export.
- Matplotlib – Fitness convergence and population distribution visualisations.

**RESULTS AND FITNESS CONVERGENCE**
***
<img width="857" height="269" alt="image" src="https://github.com/user-attachments/assets/71ab6098-0082-4cf0-aae7-78d6bd6aa1ee" />
<img width="839" height="432" alt="image" src="https://github.com/user-attachments/assets/476ea8d7-a234-4f23-80db-38f8e16eaa21" />

**FINAL POPULATION DISTRIBUTION**
***
<img width="1487" height="773" alt="image" src="https://github.com/user-attachments/assets/08d71171-5229-49b8-8fc9-70af41760ad4" />


<img width="1417" height="725" alt="image" src="https://github.com/user-attachments/assets/a90111ef-f0d6-4eb1-8a7d-afbd0510e35c" />
<img width="1482" height="705" alt="image" src="https://github.com/user-attachments/assets/7e8ba767-8e1d-45d8-9550-727ea25f5600" />

**Complexity Analysis**

Let:
- G = Number of generations (50)
- P = Population size (300)
- L = Chromosome length (80)

**Time Complexity:**

The time complexity is approximately:

O(G × P × L)

Fitness evaluation requires examining each chromosome's bits across all generations.
Based on the assignment parameters:
50 × 300 × 80 = 1,200,000 bit evaluations

**Space Complexity:**

O(P × L + G)

The population requires O(P × L) space, while generation statistics require additional O(G) space.

For this experiment, the population contains 300 chromosomes with 80 bits each.

**Reproducibility**

A random seed is used to control the random number generation process. Running the application with the same seed and identical algorithm settings produces the same results.

The application also allows users to experiment with different selection methods, crossover methods, crossover rates, and mutation rates to observe their effects on the optimisation process.
