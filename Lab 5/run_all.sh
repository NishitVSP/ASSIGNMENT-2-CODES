project_path="./algorithms"
output_path="./algorithms/pynguin-results"
excel_file="./algorithms/module_names.xlsx" 

mkdir -p "$output_path"

# Export PYNGUIN_DANGER_AWARE
export PYNGUIN_DANGER_AWARE=1

# Use Python to read the Excel file and print module names
module_names=$(python3 - <<END
import pandas as pd
df = pd.read_excel('$excel_file')
for module in df['File']:
    print(module)
END
)
 
# Loop through each module name
echo "$module_names" | while read -r module_name; do
  # Trim leading and trailing whitespace
  module_name=$(echo "$module_name" | xargs)

  # Check if module_name is empty after trimming whitespace
  if [[ -z "$module_name" ]]; then
      continue
  fi

  echo "Generating tests for module: $module_name"

  # Run Pynguin for the module
  pynguin --project-path "$project_path" --output-path "$output_path" --module-name "$module_name" --maximum-iterations 2500 --maximum-search-time 500 --maximum-test-execution-timeout 700 -v

  echo "Finished generating tests for module: $module_name"
done

