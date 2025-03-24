#!/bin/bash

# Create a folder named 'commits' if it doesn't already exist
folder_name='Commits'
if [ ! -d "$folder_name" ]; then
    mkdir -p "$folder_name"
    echo "Folder '$folder_name' created successfully."
fi

# Initialize a counter for report filenames
counter=1

# Read commit hashes from the CSV file
while IFS= read -r line; do
    # Remove leading and trailing whitespace
    line=$(echo "$line" | tr -d '[:space:]')  
    
    if [[ $line =~ ^[a-f0-9]+$ ]]; then
        # Checkout the commit
        git checkout $line
        
        # Run Bandit and generate a report in CSV for this commit
        report_file="Commits/report_${counter}.csv"
        
        # Run Bandit on Python files only, excluding non-Python file types
        bandit -r . -f csv -o $report_file
        
        echo "Bandit report generated for commit $line and saved as report_${counter}.csv"
        
        # Stop after processing 100 commits
        if [ $counter -ge 100 ]; then
            break
        fi
        
        # Increment the counter for the next report
        counter=$((counter + 1))
    fi
done < scikit-learn_commits.csv

echo "All Bandit reports have been generated and saved in the 'Commits' folder."
