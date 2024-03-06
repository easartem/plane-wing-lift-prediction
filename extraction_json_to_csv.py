import pandas as pd
import json

with open('ailes_avion.json') as f:
    data = json.load(f)

# Use pd.json_normalize to convert the JSON to a DataFrame
df = pd.json_normalize(data)

# Rename the columns for clarity
df.columns = ['Name', 'Link', 'Family', 'Thickness(%)', 'x-Location_of_Max_Thk(%)', 'Camber(%)', 'Data_Sources', 'Cl_Max', 'Cl/Cd_Max', 'Cd@Cl=0.1', 'Cd@Cl=0.4', 'Cd@Cl=0.6']

# Create a csv file
df.to_csv("ailes_avion.csv", index=False)
# Display the DataFrame
df.head(5)
