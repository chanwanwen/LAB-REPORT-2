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
