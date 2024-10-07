import re
import matplotlib.pyplot as plt

# Initialize empty lists to store step numbers and loss/exact_match values
train_steps = []
train_loss_values = []
eval_steps = []
eval_exact_match_values = []

# Read the loss values from the "train_loss.txt" file
with open("train_loss.txt", "r") as file:
    for line in file:
        loss = float(line.strip())
        step = len(train_loss_values) * 100  # Assuming each line represents 100 steps
        train_steps.append(step)
        train_loss_values.append(loss)

# Read the "Exact Match" metric values from the modified "eval_metric.txt" file
with open("eval_metric.txt", "r") as file:
    for line in file:
        match = re.search(r"(\d+) {'exact_match': ([\d.]+)", line)
        if match:
            step = int(match.group(1))
            exact_match = float(match.group(2))
            eval_steps.append(step)
            eval_exact_match_values.append(exact_match)

# Create a plot with two y-axes
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot the training loss values on the left y-axis (ax1)
ax1.plot(train_steps, train_loss_values, label="Train Loss", marker='o', linestyle='-', color='b')
ax1.set_xlabel("Number of Steps")
ax1.set_ylabel("Loss", color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Create a second y-axis (ax2) on the right for the Exact Match values
ax2 = ax1.twinx()

# Plot the evaluation "Exact Match" metric values on the right y-axis (ax2)
ax2.plot(eval_steps, eval_exact_match_values, label="Exact Match", marker='o', linestyle='-', color='r')
ax2.set_ylabel("Exact Match", color='r')
ax2.tick_params(axis='y', labelcolor='r')

plt.title("curve of loss value and Exact Match metric value over Steps")
plt.grid(True)

# Display the plot
plt.show()
