"""
This code is part of research paper:
Title: Signal vs Noise in Eye-tracking Data: Biometric Implications and Identity Information Across Frequencies.
Authors: Mehedi Hasan Raju, Lee Friedman, Dillon Lohr, and Oleg V. Komogortsev.
Published: 2024 Symposium on Eye Tracking Research and Applications (ETRA '24).
DOI: https://doi.org/10.1145/3649902.3653353

This work and its accompanying codebase are licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License 
(https://creativecommons.org/licenses/by-nc-sa/4.0/). 

For all other uses, please contact the Office for Commercialization and Industry Relations at Texas State University http://www.txstate.edu/ocir/

Property of Texas State University.

For inquiries and further information, please contact Mehedi Hasan Raju (m.raju@txstate.edu)

"""

import os
import glob
import numpy as np
import pandas as pd
from tqdm import tqdm

def process_gaze_data(input_dir, output_dir):
    """
    Processes gaze data files by setting out-of-bounds gaze positions to NaN,
    rounding the data, and saving the cleaned files to a specified directory.
    
    Parameters:
    - input_dir: Directory containing the raw .csv files.
    - output_dir: Directory where the process files will be saved.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Iterate over all .csv files in the input directory
    for file_name in tqdm(sorted(glob.glob(os.path.join(input_dir, '*.csv')))):
        # Load the data, focusing on the first three columns
        df = pd.read_csv(file_name).iloc[:, :3]
        
        # Set gaze positions outside of a specific boundary to NaN
        boundary_conditions = (df['x'] > 23.3) | (df['x'] < -23.3) | (df['y'] > 11.7) | (df['y'] < -18.5)
        df.loc[boundary_conditions, ['x', 'y']] = np.nan
        
        # Round the data for consistency
        df = df.round(4)
        
        # Construct the full path for the output file
        output_file_path = os.path.join(output_dir, os.path.basename(file_name))
        
        # Save the cleaned data to the output directory
        df.to_csv(output_file_path, index=False, na_rep='NaN')

if __name__ == "__main__":
    # Define the base directory one level up from the script's location
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(base_dir)
    # Define input and output directories relative to the base directory
    input_dir = os.path.join(base_dir, 'data', 'gazebase_v2', 'raw')
    unfiltered_dir = os.path.join(base_dir, 'data', 'gazebase_raw', 'raw')
    
    # Process the gaze data files
    process_gaze_data(input_dir, unfiltered_dir)
