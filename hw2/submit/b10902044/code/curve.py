import matplotlib.pyplot as plt
import json

# Initialize lists to store the data
steps = []
rouge_1_scores = []
rouge_2_scores = []
rouge_l_scores = []

# Read and parse the data from the file
with open('curve_data.txt', 'r') as file:
    for line in file:
        data = line.split()
        step = int(data[0])
        scores = json.loads(' '.join(data[1:]))
        
        steps.append(step)
        rouge_1_scores.append(scores["rouge-1"])
        rouge_2_scores.append(scores["rouge-2"])
        rouge_l_scores.append(scores["rouge-l"])

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(steps, rouge_1_scores, label='Rouge-1')
plt.plot(steps, rouge_2_scores, label='Rouge-2')
plt.plot(steps, rouge_l_scores, label='Rouge-L')

plt.xlabel('Step')
plt.ylabel('Score')
plt.legend()
plt.title('Rouge Scores Over Steps')
plt.grid(True)

# Show the plot or save it to a file
plt.show()
