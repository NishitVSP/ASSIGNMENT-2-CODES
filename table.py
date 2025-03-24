import pandas as pd
import glob
import csv

# Function to analyze Bandit reports and generate a summary CSV
def generate_summary_csv_with_cwe_count(reports_dir, output_csv):
    # Open the output CSV file for writing
    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow([
            "CSV File Name",
            "High Severity Count",
            "Medium Severity Count",
            "Low Severity Count",
            "High Confidence Count",
            "Medium Confidence Count",
            "Low Confidence Count",
            "Unique CWEs",
            "Unique CWE Count"
        ])
        
        # Process each report in the directory
        for report_file in sorted(glob.glob(f"{reports_dir}/*.csv")):  # Sort files to maintain order
            df = pd.read_csv(report_file)
            
            # Skip empty files
            if df.empty:
                continue
            
            # Get counts for severity levels
            high_severity_count = len(df[df['issue_severity'] == 'HIGH'])
            medium_severity_count = len(df[df['issue_severity'] == 'MEDIUM'])
            low_severity_count = len(df[df['issue_severity'] == 'LOW'])
            
            # Get counts for confidence levels
            high_confidence_count = len(df[df['issue_confidence'] == 'HIGH'])
            medium_confidence_count = len(df[df['issue_confidence'] == 'MEDIUM'])
            low_confidence_count = len(df[df['issue_confidence'] == 'LOW'])
            
            # Get unique CWEs (excluding NaN values)
            unique_cwes = df['issue_cwe'].dropna().unique()
            
            # Count unique CWEs
            unique_cwe_count = len(unique_cwes)
            
            # Write the data to the CSV file
            writer.writerow([
                report_file.split('/')[-1],  # Extract just the filename
                high_severity_count,
                medium_severity_count,
                low_severity_count,
                high_confidence_count,
                medium_confidence_count,
                low_confidence_count,
                ", ".join(map(str, unique_cwes)),  # Join CWEs into a single string
                unique_cwe_count  # Add unique CWE count column
            ])

# Example usage
reports_dir = 'Commits'  # Path to the folder containing Bandit reports
output_csv = 'bandit_summary.csv'  # Output summary CSV file name

generate_summary_csv_with_cwe_count(reports_dir, output_csv)
