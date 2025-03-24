import matplotlib.pyplot as plt

# Configurations
configs = [
    'pytest', #sequential execution
    '-n auto --dist load --parallel-threads auto',
    '-n auto --dist load --parallel-threads 1',
    '-n auto --dist no --parallel-threads auto',
    '-n auto --dist no --parallel-threads 1',
    '-n 1 --dist load --parallel-threads auto',
    '-n 1 --dist load --parallel-threads 1',
    '-n 1 --dist no --parallel-threads auto',
    '-n 1 --dist no --parallel-threads 1'
]

# Speedup ratios (replace these with your actual values later)
speedups = [1.0, 0.14, 1.05, 0.186, 1.151, 0.145, 1.177, 0.141, 1.24]

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Create the bar plot
bars = ax.bar(range(len(configs)), speedups, align='center', alpha=0.8)

# Customize the plot
ax.set_ylabel('Speedup Ratio (Tseq/Tpar)')
ax.set_title('Speedup Ratios for Different pytest Configurations')
ax.set_xticks(range(len(configs)))
ax.set_xticklabels(configs, rotation=45, ha='right')

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.2f}',
            ha='center', va='bottom')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
