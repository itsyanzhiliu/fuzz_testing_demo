import subprocess
import random
import matplotlib.pyplot as plt

# Function to mutate input
def mutate_input(input_string):
    # Implement your mutation logic here
    # For simplicity, let's just add a random character
    index = random.randint(0, len(input_string))
    new_char = chr(random.randint(32, 126))  # ASCII printable characters
    mutated_input = input_string[:index] + new_char + input_string[index:]
    return mutated_input

# Function to evaluate coverage
def evaluate_coverage(program, input_string):
    # Run the program and capture coverage
    # You might need to adjust this based on how coverage is collected in your program
    result = subprocess.run([program, input_string],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True)
    # Parse the coverage data from result
    coverage_data = result.stdout  # Adjust this based on how your program outputs coverage data
    return coverage_data

# Main fuzzing loop
def fuzz(program, seed_inputs, max_iterations):
    explored_statements = set()
    input_strings = seed_inputs.copy()

    for iteration in range(max_iterations):
        new_input_strings = []
        for seed_input in input_strings:
            # Generate and evaluate mutated input
            mutated_input = mutate_input(seed_input)
            new_coverage = evaluate_coverage(program, mutated_input)

            # Update explored statements
            new_statements = set(new_coverage.split(',')) - explored_statements
            explored_statements.update(new_statements)

            # Add promising inputs to new_input_strings
            if len(new_statements) > 0:
                new_input_strings.append(mutated_input)

        input_strings = new_input_strings

    return len(explored_statements), sorted(list(explored_statements))

# Main program
if __name__ == "__main__":
    program_path = "/path/to/your/program"  # Adjust this to the actual path
    seed_inputs = ["http://example.com"]  # Seed inputs
    max_iterations = 10

    explored_statements, covered_lines = fuzz(program_path, seed_inputs, max_iterations)
    
    # Print the results
    print(explored_statements)
    print(','.join(covered_lines))

    # Add code to generate the graph

    plt.plot(iteration_numbers, explored_statement_numbers, label="Explored Statements")
    plt.plot(iteration_numbers, coverage_numbers, label="Coverage")
    plt.xlabel("Iterations")
    plt.ylabel("Metrics")
    plt.legend()
    plt.savefig("graph.png")  # Save the graph as an image
    

