import matplotlib.pyplot as plt

checkpoints = [32, 64, 96, 128, 159]
mean_perplexities = [4.0206313886642455, 3.797881936073303, 3.713958703517914, 3.6286749324798584, 3.623328058719635]

# Plotting the graph
plt.plot(checkpoints, mean_perplexities, marker='o')
plt.title('learning curve')
plt.xlabel('Checkpoint')
plt.ylabel('Mean Perplexity')
plt.grid(True)
plt.show()
