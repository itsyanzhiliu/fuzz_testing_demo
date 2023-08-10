import subprocess
import random
import sys

# Mock function that simulates code coverage
def evaluate_coverage(input_string):
    # Simulate coverage measurement (randomly generate some coverage)
    return set(random.sample(range(1, 1001), random.randint(1, 201)))

# Function to mutate an input string
def mutate_input(input_string):
    # Simulate simple mutation
    return input_string + random.choice(["a", "b", "c"])

def main():
    if len(sys.argv) < 2:
        print("Usage: python fuzzer.py <path_to_executable> [-show]")
        return

    executable_path = sys.argv[1]
    show_output = "-show" in sys.argv

    seed_inputs = ["initial_input"]
    covered_lines = set()

    num_iterations = 10
    consecutive_no_new_coverage = 3

    for iteration in range(num_iterations):
        if show_output:
            print(f"Iteration {iteration + 1}:")

        new_seeds = []
        for seed_input in seed_inputs:
            # Generate and evaluate mutated input
            mutated_input = mutate_input(seed_input)
            new_coverage = evaluate_coverage(mutated_input)

            # Check if there is new coverage
            if new_coverage - covered_lines:
                new_seeds.append(mutated_input)
                covered_lines.update(new_coverage)

                if show_output:
                    print(f"Generated input: {mutated_input}")
                    print(f"New coverage: {new_coverage}")

        # If no new seeds, increase the count
        if not new_seeds:
            consecutive_no_new_coverage += 1
        else:
            consecutive_no_new_coverage = 0

        # If no new coverage for consecutive iterations, stop
        if consecutive_no_new_coverage >= 3:
            if show_output:
                print("No new coverage for consecutive iterations. Stopping.")
            break

        # Update seed inputs with new seeds
        seed_inputs = new_seeds

    print(len(covered_lines))
    print(", ".join(sorted(map(lambda x: f"test.c:{x}", covered_lines))))

if __name__ == "__main__":
    main()
