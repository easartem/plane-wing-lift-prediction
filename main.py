# init project 


# extraction_json_to_csv.py-------------------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import json

with open('data\\ailes_avion.json') as f:
    data = json.load(f)

# Use pd.json_normalize to convert the JSON to a DataFrame
df = pd.json_normalize(data)

# Rename the columns for clarity
df.columns = ['Name', 'Link', 'Family', 'Thickness(%)', 'x-Location_of_Max_Thk(%)', 'Camber(%)', 'Data_Sources', 'Cl_Max', 'Cl/Cd_Max', 'Cd@Cl=0.1', 'Cd@Cl=0.4', 'Cd@Cl=0.6']

# Create a csv file
df.to_csv("data\\ailes_avion.csv", index=False)

# Display the DataFrame
df.head(5)


# extraction_dat_to_df.py---------------------------------------------------------------------------------------------------------------------------------------------------
import os
import pandas as pd

directory = 'BIGFOIL_DAT'
winglist_name = []
winglist_size = []

# iterate over files in that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        #print(f)
        with open(f, 'r') as f:
            content = f.read()
            #print(filename, len(content))
            winglist_name.append(filename)
            winglist_size.append(len(content))

df_index = pd.DataFrame({'name':winglist_name, 'size':winglist_size})
df_index.to_csv('dat_files_index.csv')