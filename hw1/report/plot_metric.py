import re
import matplotlib.pyplot as plt

# Initialize empty lists to store step numbers and exact_match values
steps = []
exact_match_values = []

# Read the metric values from the "eval_metric.txt" file
with open("eval_metric.txt", "r") as file:
    for line in file:
        # Use regular expressions to extract the step number and exact_match value
        match = re.search(r"(\d+){'exact_match': ([\d.]+)", line)
        if match:
            step = int(match.group(1))
            exact_match = float(match.group(2))
            steps.append(step)
            exact_match_values.append(exact_match)

# Create a plot of step number vs. exact_match value
plt.figure(figsize=(10, 6))
plt.plot(steps, exact_match_values, marker='o', linestyle='-', color='b')
plt.title("Exact Match Metric Over Steps")
plt.xlabel("Number of Steps")
plt.ylabel("Exact Match Value")
plt.grid(True)

# Display the plot
plt.show()
