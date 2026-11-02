# app.py
import random
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# ============================================================
# 1. FIXED PARAMETERS (BSD2513 LAB REPORT 2)
# ============================================================
POP_SIZE = 300
CHROM_LEN = 80
TARGET_ONES = 50
MAX_FITNESS = 80
N_GENERATIONS = 50

# Genetic Algorithm settings
TOURNAMENT_K = 3
CROSSOVER_RATE = 0.9
MUTATION_RATE = 1.0 / CHROM_LEN
ELITISM = 1

SELECTION_METHODS = ["Tournament", "Roulette Wheel", "Rank-based"]
CROSSOVER_METHODS = ["One-point", "Two-point", "Uniform"]


# ============================================================
# 2. FITNESS FUNCTION
# ============================================================
def fitness(individual: np.ndarray) -> float:
    """Give the highest score (80) when a chromosome has 50 ones."""
    number_of_ones = int(np.sum(individual))
    return MAX_FITNESS - abs(number_of_ones - TARGET_ONES)


# ============================================================
# 3. POPULATION INITIALISATION
# ============================================================
def init_population(pop_size: int, chromosome_length: int) -> np.ndarray:
    """Generate a population containing random binary chromosomes."""
    return np.random.randint(
        0, 2, size=(pop_size, chromosome_length), dtype=np.int8
    )


# ============================================================
# 4. PARENT SELECTION
# ============================================================
def tournament_selection(population, fitness_values, k=TOURNAMENT_K):
    """Select the fittest chromosome from k randomly selected candidates."""
    candidates = np.random.choice(len(population), size=k, replace=True)
    winner = candidates[np.argmax(fitness_values[candidates])]
    return population[winner].copy()


def calculate_selection_probabilities(fitness_values, method):
    """Calculate selection probabilities for roulette or rank-based selection."""
    if method == "Roulette Wheel":
        return fitness_values / fitness_values.sum()

    if method == "Rank-based":
        order = np.argsort(fitness_values, kind="stable")
        ranks = np.empty(len(fitness_values), dtype=float)
        ranks[order] = np.arange(1, len(fitness_values) + 1)
        return ranks / ranks.sum()

    return None


def select_parent(population, fitness_values, method, probabilities=None):
    if method == "Tournament":
        return tournament_selection(population, fitness_values)

    selected_index = np.random.choice(
        len(population), p=probabilities
    )
    return population[selected_index].copy()


# ============================================================
# 5. CROSSOVER OPERATORS
# ============================================================
def one_point_crossover(parent1, parent2):
    cut = np.random.randint(1, CHROM_LEN)
    child1 = np.concatenate((parent1[:cut], parent2[cut:]))
    child2 = np.concatenate((parent2[:cut], parent1[cut:]))
    return child1, child2


def two_point_crossover(parent1, parent2):
    cut1, cut2 = sorted(
        np.random.choice(np.arange(1, CHROM_LEN), size=2, replace=False)
    )
    child1 = np.concatenate(
        (parent1[:cut1], parent2[cut1:cut2], parent1[cut2:])
    )
    child2 = np.concatenate(
        (parent2[:cut1], parent1[cut1:cut2], parent2[cut2:])
    )
    return child1, child2


def uniform_crossover(parent1, parent2):
    mask = np.random.rand(CHROM_LEN) < 0.5
    child1 = np.where(mask, parent1, parent2)
    child2 = np.where(mask, parent2, parent1)
    return child1, child2


def apply_crossover(parent1, parent2, method, rate):
    if np.random.random() >= rate:
        return parent1.copy(), parent2.copy()

    if method == "Two-point":
        return two_point_crossover(parent1, parent2)
    if method == "Uniform":
        return uniform_crossover(parent1, parent2)

    return one_point_crossover(parent1, parent2)


# ============================================================
# 6. MUTATION
# ============================================================
def mutate(chromosome, mutation_rate):
    """Flip selected bits from 0 to 1 or from 1 to 0."""
    result = chromosome.copy()
    mutation_mask = np.random.random(CHROM_LEN) < mutation_rate
    result[mutation_mask] = 1 - result[mutation_mask]
    return result


# ============================================================
# 7. GENETIC ALGORITHM
# ============================================================
def run_genetic_algorithm(seed, selection_method, crossover_method,
                          crossover_rate, mutation_rate):
    random.seed(seed)
    np.random.seed(seed)

    population = init_population(POP_SIZE, CHROM_LEN)
    records = []
    best_chromosome = None
    best_score = -1

    for generation in range(1, N_GENERATIONS + 1):
        scores = np.array([fitness(chromosome) for chromosome in population])
        ones_counts = population.sum(axis=1)

        best_index = int(np.argmax(scores))
        generation_best_score = float(scores[best_index])
        generation_best = population[best_index].copy()

        if generation_best_score > best_score:
            best_score = generation_best_score
            best_chromosome = generation_best.copy()

        records.append({
            "Generation": generation,
            "Best Fitness": generation_best_score,
            "Average Fitness": float(np.mean(scores)),
            "Lowest Fitness": float(np.min(scores)),
            "Average Ones": float(np.mean(ones_counts)),
            "Optimal Individuals": int(np.sum(scores == MAX_FITNESS))
        })

        # Stop after recording generation 50.
        if generation == N_GENERATIONS:
            break

        # Preserve the best chromosome in the next generation.
        elite_index = int(np.argmax(scores))
        next_population = [population[elite_index].copy()]

        probabilities = calculate_selection_probabilities(
            scores, selection_method
        )

        # Produce the remaining chromosomes.
        while len(next_population) < POP_SIZE:
            parent1 = select_parent(
                population, scores, selection_method, probabilities
            )
            parent2 = select_parent(
                population, scores, selection_method, probabilities
            )

            child1, child2 = apply_crossover(
                parent1, parent2, crossover_method, crossover_rate
            )

            next_population.append(mutate(child1, mutation_rate))

            if len(next_population) < POP_SIZE:
                next_population.append(mutate(child2, mutation_rate))

        population = np.asarray(next_population, dtype=np.int8)

    return best_chromosome, best_score, pd.DataFrame(records), population


# ============================================================
# 8. STREAMLIT INTERFACE
# ============================================================
st.set_page_config(
    page_title="Genetic Algorithm - Lab Report 2",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 Genetic Algorithm: Binary Pattern Optimisation")
st.write(
    "This application uses a Genetic Algorithm to find an 80-bit "
    "chromosome containing exactly 50 ones."
)

with st.sidebar:
    st.header("Problem Requirements")
    st.write(f"**Population size:** {POP_SIZE}")
    st.write(f"**Chromosome length:** {CHROM_LEN}")
    st.write(f"**Target number of ones:** {TARGET_ONES}")
    st.write(f"**Maximum fitness:** {MAX_FITNESS}")
    st.write(f"**Generations:** {N_GENERATIONS}")

    st.divider()
    st.subheader("Fitness Function")
    st.code("f(x) = 80 - abs(number_of_ones - 50)")
    st.caption("The maximum fitness is 80 when the chromosome has exactly 50 ones.")

st.subheader("Genetic Algorithm Settings")

col1, col2, col3 = st.columns(3)

with col1:
    selection_method = st.selectbox(
        "Selection method", SELECTION_METHODS, index=0
    )

with col2:
    crossover_method = st.selectbox(
        "Crossover method", CROSSOVER_METHODS, index=0
    )

with col3:
    seed = st.number_input(
        "Random seed", min_value=0, value=42, step=1
    )

col4, col5 = st.columns(2)

with col4:
    crossover_rate = st.slider(
        "Crossover rate", 0.0, 1.0, CROSSOVER_RATE, 0.05
    )

with col5:
    mutation_rate = st.slider(
        "Mutation rate per bit", 0.0, 0.10,
        float(MUTATION_RATE), 0.0025, format="%.4f"
    )

run_button = st.button(
    "Run Genetic Algorithm", type="primary", use_container_width=True
)

if run_button:
    best_chromosome, best_score, history, final_population = (
        run_genetic_algorithm(
            int(seed),
            selection_method,
            crossover_method,
            crossover_rate,
            mutation_rate
        )
    )

    # Store the result so it remains visible after Streamlit reruns.
    st.session_state["ga_result"] = (
        best_chromosome, best_score, history, final_population
    )

if "ga_result" in st.session_state:
    best_chromosome, best_score, history, final_population = (
        st.session_state["ga_result"]
    )

    number_of_ones = int(np.sum(best_chromosome))
    number_of_zeros = CHROM_LEN - number_of_ones
    bit_pattern = "".join(str(int(bit)) for bit in best_chromosome)

    st.divider()
    st.header("Results")

    metric1, metric2, metric3 = st.columns(3)
    metric1.metric("Best Fitness", f"{best_score:.0f} / {MAX_FITNESS}")
    metric2.metric("Number of Ones", number_of_ones)
    metric3.metric("Number of Zeros", number_of_zeros)

    st.write(f"**Chromosome length:** {CHROM_LEN} bits")
    st.write("**Best chromosome found:**")
    st.code(bit_pattern, language="text")

    if best_score == MAX_FITNESS and number_of_ones == TARGET_ONES:
        st.success("Optimal solution found: 50 ones and fitness 80.")
    else:
        st.info(
            "The optimal solution was not found in this run. "
            "Try another random seed or operator setting."
        )

    # Convergence graph
    st.subheader("Fitness Convergence")
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(
        history["Generation"], history["Best Fitness"],
        label="Best fitness", linewidth=2
    )
    ax.plot(
        history["Generation"], history["Average Fitness"],
        label="Average fitness", linestyle="--"
    )
    ax.plot(
        history["Generation"], history["Lowest Fitness"],
        label="Lowest fitness", alpha=0.7
    )
    ax.axhline(
        MAX_FITNESS, linestyle=":", label=f"Maximum fitness = {MAX_FITNESS}"
    )
    ax.set_xlabel("Generation")
    ax.set_ylabel("Fitness")
    ax.set_title("Fitness Across Generations")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.legend()
    st.pyplot(fig)
    plt.close(fig)

    # Final population distribution
    st.subheader("Final Population Distribution")
    final_ones = final_population.sum(axis=1)

    fig2, ax2 = plt.subplots(figsize=(9, 4))
    ax2.hist(
        final_ones,
        bins=np.arange(final_ones.min(), final_ones.max() + 2) - 0.5,
        edgecolor="black"
    )
    ax2.axvline(
        TARGET_ONES, linestyle="--",
        label=f"Target = {TARGET_ONES}"
    )
    ax2.set_xlabel("Number of ones in a chromosome")
    ax2.set_ylabel("Number of individuals")
    ax2.set_title("Distribution of Ones in the Final Population")
    ax2.legend()
    st.pyplot(fig2)
    plt.close(fig2)

    optimal_count = int(np.sum(final_ones == TARGET_ONES))
    st.write(
        f"**Optimal individuals in final population:** "
        f"{optimal_count} out of {POP_SIZE}"
    )

    with st.expander("View generation statistics"):
        st.dataframe(history, hide_index=True, use_container_width=True)
        st.download_button(
            "Download generation statistics (CSV)",
            data=history.to_csv(index=False),
            file_name="generation_statistics.csv",
            mime="text/csv"
        )

# Explanation section
with st.expander("How the Genetic Algorithm works"):
    st.markdown(
        """
        1. **Initialization:** Generate 300 random chromosomes, each containing 80 bits.
        2. **Fitness evaluation:** Calculate the fitness of every chromosome.
           A chromosome with exactly 50 ones receives a fitness of 80.
        3. **Selection:** Select parent chromosomes using the chosen selection method.
        4. **Crossover:** Combine parent chromosomes to produce offspring.
        5. **Mutation:** Randomly flip bits to maintain population diversity.
        6. **Elitism:** Preserve the best chromosome when creating the next generation.
        7. **Termination:** Repeat the process for 50 generations and return the best chromosome.
        """
    )

with st.expander("Genetic Algorithm complexity"):
    st.markdown(
        """
        Let P represent population size, L represent chromosome length,
        and G represent the number of generations.

        - **Time complexity:** O(G × P × L). Fitness evaluation examines the bits
          of every chromosome in each generation.
        - **Space complexity:** O(P × L) for storing the population, with
          additional O(G) space for generation statistics.
        - **Assignment values:** G = 50, P = 300, L = 80.
        - Fitness evaluation examines approximately 1,200,000 bits over the run.
        """
    )

st.caption(
    "BSD2513 Artificial Intelligence | Lab Report 2 | Genetic Algorithm"
)
