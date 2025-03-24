import csv
from pydriller import Repository

repo_path = '.'

# Initialize a list to store commit hashes
Commits = []

# Iterate over commits in the main branch, excluding merges, in reverse order
for commit in Repository(repo_path, only_no_merge=True,order='reverse').traverse_commits():
    
    # Stop once you have 100 commits
    if len(Commits) == 100:
        break

    if (commit.in_main_branch==True):
        Commits.append(commit.hash)

Commits.reverse() # We will run bandit on it to find all vulnerabilities, so it is best to have commit's hashes from oldest to newest for last 100 non-merge commits.

# Save commit hashes in a CSV file
with open('scikit-learn_commits.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Commit Hash"])  # Column name
    for commit in Commits:
        writer.writerow([commit])
