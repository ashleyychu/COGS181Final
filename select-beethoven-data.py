import os
import shutil
import pandas as pd


# Path to the directory containing the data divided into year folders
data_directory = 'maestro-v3.0.0'

# Path to the CSV file containing information about Beethoven files
csv_file = 'maestro-v3.0.0/maestro-v3.0.0.csv'

# Path to the directory where you want to copy the Beethoven files
output_directory = 'beethoven'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Read the CSV file containing information about Beethoven files
beethoven_df = pd.read_csv(csv_file)
# Iterate through each row in the DataFrame
for index, row in beethoven_df.iterrows():
    # Extract year and filename from the DataFrame
    if row['canonical_composer'] == 'Ludwig van Beethoven':
        filename = row['midi_filename']
    
        # Construct the full path to the source file
        source_file = os.path.join(data_directory, filename)
        
        # Construct the full path to the destination file
        destination_file = os.path.join(output_directory, filename[5:])
        # Copy the file to the output directory if it exists
        if os.path.exists(source_file):
            shutil.copyfile(source_file, destination_file)
            print(f"Copied {filename} to {output_directory}")