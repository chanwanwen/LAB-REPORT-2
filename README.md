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

**RESULTS AND FITNESS CONVERGENCE**
<img width="857" height="269" alt="image" src="https://github.com/user-attachments/assets/71ab6098-0082-4cf0-aae7-78d6bd6aa1ee" />
<img width="839" height="432" alt="image" src="https://github.com/user-attachments/assets/476ea8d7-a234-4f23-80db-38f8e16eaa21" />
<img width="1487" height="773" alt="image" src="https://github.com/user-attachments/assets/08d71171-5229-49b8-8fc9-70af41760ad4" />

<img width="1417" height="725" alt="image" src="https://github.com/user-attachments/assets/a90111ef-f0d6-4eb1-8a7d-afbd0510e35c" />
<img width="1482" height="705" alt="image" src="https://github.com/user-attachments/assets/7e8ba767-8e1d-45d8-9550-727ea25f5600" />
