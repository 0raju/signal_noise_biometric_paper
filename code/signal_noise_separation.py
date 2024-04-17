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

import os, glob
import numpy as np
import pandas as pd
from tqdm import tqdm
from scipy.signal import firwin, filtfilt


def zero_phase_digital_filter(data, filter_type):

    """
    Apply a zero-phase digital filter (highpass or lowpass) to the input data.
    
    Parameters are taken from:
    Mehedi Hasan Raju, Lee Friedman, Troy M. Bouman, and Oleg V. Komogortsev. 2023.
    Filtering Eye-Tracking Data From an EyeLink 1000: Comparing Heuristic, Savitzky-Golay,
    IIR and FIR Digital Filters. Journal of Eye Movement Research, 14(3):6.
    https://doi.org/10.16910/jemr.14.3.6

    """
    
    SAMPLING_FREQUENCY = 1000
    NYQUIST_FREQUENCY = 0.5 * SAMPLING_FREQUENCY
    NTAPS = 79
    CUTOFF = 84 / NYQUIST_FREQUENCY
    
    b = firwin(NTAPS, CUTOFF, pass_zero=(filter_type == 'lowpass'))
    return filtfilt(b, 1, data)


def process_file(file_path, output_dir, filter_type):
    """
    Process a single file: Load, filter, and save the filtered data.
    """
    df = pd.read_csv(file_path).iloc[:, :3]
    df['n'] = df['n'].astype(int)

    # Handle missing values
    nan_mask = df['x'].isna() & df['y'].isna()
    df.interpolate(inplace=True)

    # Applying zerophase filter
    df['x'] = zero_phase_digital_filter(df['x'], filter_type).round(4)
    df['y'] = zero_phase_digital_filter(df['y'], filter_type).round(4)

    # Reapply NaNs to match original missing data
    df.loc[nan_mask, ['x', 'y']] = np.nan

    # Save the filtered data
    df.to_csv(os.path.join(output_dir, os.path.basename(file_path)), index=False, na_rep='NaN')


if __name__ == "__main__":

    # Define the base directory paths for data processing
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    unfiltered_dir = os.path.join(base_dir, 'data', 'gazebase_raw', 'raw')
    signal_dir = os.path.join(base_dir, 'data', 'gazebase_signal', 'raw')
    noise_dir = os.path.join(base_dir, 'data', 'gazebase_noise', 'raw')

    # Create directories for processed signal and noise data if they don't exist
    os.makedirs(signal_dir, exist_ok=True)
    os.makedirs(noise_dir, exist_ok=True)

    # Process all files in the unfiltered directory and apply filtering
    file_paths = sorted(glob.glob(os.path.join(unfiltered_dir, '*.csv')))
    for file_path in tqdm(file_paths):
        process_file(file_path, signal_dir, 'lowpass')
        process_file(file_path, noise_dir, 'highpass')

