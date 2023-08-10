import subprocess
import random
import matplotlib.pyplot as plt

# Mutation function
def mutate_input(input_string):
    mutation_type = random.choice(["delete", "insert", "swap", "replace"])
    
    if mutation_type == "delete":
        index = random.randint(0, len(input_string) - 1)
        mutated_input = input_string[:index] + input_string[index+1:]
    elif mutation_type == "insert":
        index = random.randint(0, len(input_string))
        new_char = chr(random.randint(32, 126))
        mutated_input = input_string[:index] + new_char + input_string[index:]
    elif mutation_type == "swap":
        index1 = random.randint(0, len(input_string) - 1)
        index2 = random.randint(0, len(input_string) - 1)
        mutated_input = list(input_string)
        mutated_input[index1], mutated_input[index2] = mutated_input[index2], mutated_input[index1]
        mutated_input = ''.join(mutated_input)
    elif mutation_type == "replace":
        index = random.randint(0, len(input_string) - 1)
        new_char = chr(random.randint(32, 126))
        mutated_input = input_string[:index] + new_char + input_string[index+1:]
    else:
        mutated_input = input_string
    
    return mutated_input

# Function to evaluate coverage
def evaluate_coverage(program, input_string):
    result = subprocess.run([program, input_string],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True)
    # Extract and return coverage data from the result
    coverage_data = result.stdout  # Adjust based on your program's output
    return coverage_data

# Main fuzzing loop
def fuzz(program, seed_inputs, max_iterations):
    explored_statements = set()
    input_strings = seed_inputs.copy()
    coverage_history = []

    for iteration in range(max_iterations):
        new_input_strings = []
        coverage_iteration = set()

        for seed_input in input_strings:
            mutated_input = mutate_input(seed_input)
            new_coverage = evaluate_coverage(program, mutated_input)
            new_statements = set(new_coverage.split(',')) - explored_statements

            explored_statements.update(new_statements)
            coverage_iteration.update(new_statements)

            if len(new_statements) > 0:
                new_input_strings.append(mutated_input)

        input_strings = new_input_strings
        coverage_history.append(len(explored_statements))

    return explored_statements, coverage_history

# Main program
if __name__ == "__main__":
    program_path = "/path/to/your/program"  # Adjust this to the actual path
    seed_inputs = ["http://example.com"]  # Seed inputs
    max_iterations = 10
    
    # Run fuzzing
    explored_statements, coverage_history = fuzz(program_path, seed_inputs, max_iterations)

    # Print results
    print("Explored Statements:", len(explored_statements))
    print("Coverage History:", coverage_history)

    # Generate and save the graph
    plt.plot(range(1, max_iterations + 1), coverage_history)
    plt.xlabel("Iterations")
    plt.ylabel("Explored Statements")
    plt.title("Fuzzing Progress")
    plt.savefig("fuzzer_graph.png")
