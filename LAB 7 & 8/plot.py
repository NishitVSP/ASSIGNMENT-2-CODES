import pandas as pd
import matplotlib.pyplot as plt

# Load the summary CSV file
summary_csv = "bandit_summary.csv"
df = pd.read_csv(summary_csv)

# Aggregate Data Across Commits
total_high_severity = df["High Severity Count"].sum()
total_medium_severity = df["Medium Severity Count"].sum()
total_low_severity = df["Low Severity Count"].sum()

# Analyze Vulnerability Patterns
df["Severity Total"] = df["High Severity Count"] + df["Medium Severity Count"] + df["Low Severity Count"]

# HIGH Severity Trends Line Chart
plt.figure(figsize=(12, 6))
plt.plot(df.index, df["High Severity Count"], label="High Severity", color="red", marker="o")
plt.xlabel("Commit Number")
plt.ylabel("High Severity Count")
plt.title("High Severity Trends Across Commits")
plt.legend()
plt.grid()
plt.show()

# MEDIUM Severity Trends Line Chart
plt.figure(figsize=(12, 6))
plt.plot(df.index, df["Medium Severity Count"], label="Medium Severity ", color="blue", marker="o")
plt.xlabel("Commit Number")
plt.ylabel("Medium Severity Count")
plt.title("Medium Severity Trends Across Commits")
plt.legend()
plt.grid()
plt.show()

# LOW Severity Trends Line Chart
plt.figure(figsize=(12, 6))
plt.plot(df.index, df["Low Severity Count"], label="Low Severity", color="green", marker="o")
plt.xlabel("Commit Number")
plt.ylabel("LOW Severity Count")
plt.title("LOW Severity Trends Across Commits")
plt.legend()
plt.grid()
plt.show()

# Compare Severity Levels
severity_counts = {
    "High": total_high_severity,
    "Medium": total_medium_severity,
    "Low": total_low_severity,
}

# Analyze CWE Coverage
cwe_series = df["Unique CWEs"].str.split(", ").explode().dropna()
cwe_counts = cwe_series.value_counts()


# Top CWEs bar chart
top_cwes = cwe_counts.head(10)
plt.figure(figsize=(12, 8))
top_cwes.plot(kind="barh", color="purple")
plt.title("Top 10 CWEs Across All Commits")
plt.xlabel("Occurrences")
for i, val in enumerate(top_cwes):
    plt.text(val + 1, i, str(val), va="center", fontsize=10)
plt.gca().invert_yaxis()  # Invert y-axis for better readability
plt.show()

# Define colors for the labels
colors = ["red", "orange", "green"]

# Compute percentages
total = sum(severity_counts.values())
percentages = {key: (val / total) * 100 for key, val in severity_counts.items()}

# Pie chart for severity levels (without percentage labels)
plt.figure(figsize=(8, 8))
wedges, _ = plt.pie(
    severity_counts.values(), 
    labels=severity_counts.keys(), 
    colors=colors, 
    startangle=140, 
    wedgeprops={"edgecolor": "black", "linewidth": 1.5},
    explode=[0.1 if val / total < 0.05 else 0 for val in severity_counts.values()]  # Explode small slices
)

# Create a legend outside the pie chart with percentages
legend_labels = [f"{key}: {val:.1f}%" for key, val in percentages.items()]
plt.legend(wedges, legend_labels, loc="upper right", fontsize=12, title="Severity Distribution")

plt.title("Severity Levels Distribution Across All Commits", fontsize=14)
plt.show()
