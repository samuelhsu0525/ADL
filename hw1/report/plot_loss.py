import matplotlib.pyplot as plt

# Initialize empty lists to store step numbers and corresponding loss values
steps = []
loss_values = []

# Read the loss values from the "train_loss.txt" file
with open("train_loss.txt", "r") as file:
    for line in file:
        # Extract the loss value from each line and convert it to a float
        loss = float(line.strip())
        
        # Calculate the step number (assuming each line represents 100 steps)
        step = len(loss_values) * 100
        
        # Append the step number and loss value to their respective lists
        steps.append(step)
        loss_values.append(loss)

# Create a plot of step number vs. loss value
plt.figure(figsize=(10, 6))
plt.plot(steps, loss_values, marker='o', linestyle='-', color='b')
plt.title("Learning curve of the loss value")
plt.xlabel("Steps")
plt.ylabel("Loss")
plt.grid(True)

# Display the plot
plt.show()
