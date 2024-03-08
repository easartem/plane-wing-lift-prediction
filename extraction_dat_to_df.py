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