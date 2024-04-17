# Signal vs Noise in Eye-tracking Data: Biometric Implications and Identity Information Across Frequencies

## Citation
Mehedi Hasan Raju, Lee Friedman, Dillon J. Lohr, and Oleg V. Komogortsev.
2024. Signal vs Noise in Eye-tracking Data: Biometric Implications and Identity Information Across Frequencies. In 2024 Symposium on Eye Tracking Re-
search and Applications (ETRA ’24), June 4–7, 2024, Glasgow, United Kingdom. ACM, New York, NY, USA, 7 pages. 
https://doi.org/10.1145/3649902.3653353


## License
This work and its accompanying codebase are licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License ([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)).

For all other uses, please contact the Office for Commercialization and Industry Relations at Texas State University http://www.txstate.edu/ocir/

Property of Texas State University.

## Contact
For inquiries and further information, please contact:
Mehedi Hasan Raju  
Email: [m.raju@txstate.edu](mailto:m.raju@txstate.edu)

## Instructions

1. Create a new Conda environment by running the following command with the provided `biometric.yml` file:
    ```bash
    conda env create -f biometric.yml
    ```

2. Navigate to the code directory:

    ```bash
    cd code
    ```

3. Run the run.py script to download and process the GazeBase dataset. This will classify the data into 'signal' and 'noise' categories and store it in a new folder named data in the same parent directory:

    ```bash
    python run.py
    ```

4. Train your model using the 'gazebase_signal' and 'gazebase_noise' datasets.

5. For instructions on how to use the Eye Know You Too (EKYT) model, visit the following link for the source code and detailed setup instructions: https://git.txstate.edu/oklab/ekyt-release

    ```bash
    # Train a full ensemble to enable evaluation for signal data
    python train_and_test.py --mode=train --fold=0 --gazebase_dir=data/gazebase_signal  --batch_classes=8 --batch_samples=8 --map_at_r
    python train_and_test.py --mode=train --fold=1 --gazebase_dir=data/gazebase_signal  --batch_classes=8 --batch_samples=8 --map_at_r
    python train_and_test.py --mode=train --fold=2 --gazebase_dir=data/gazebase_signal  --batch_classes=8 --batch_samples=8 --map_at_r
    python train_and_test.py --mode=train --fold=3 --gazebase_dir=data/gazebase_signal  --batch_classes=8 --batch_samples=8 --map_at_r

    # Test a full ensemble to enable evaluation for signal data
    python train_and_test.py --mode=test --fold=0 --gazebase_dir=data/gazebase_signal  --batch_classes=8 --batch_samples=8 --map_at_r
    python train_and_test.py --mode=test --fold=1 --gazebase_dir=data/gazebase_signal  --batch_classes=8 --batch_samples=8 --map_at_r
    python train_and_test.py --mode=test --fold=2 --gazebase_dir=data/gazebase_signal  --batch_classes=8 --batch_samples=8 --map_at_r
    python train_and_test.py --mode=test --fold=3 --gazebase_dir=data/gazebase_signal  --batch_classes=8 --batch_samples=8 --map_at_r

    # We evaluate under the short term evaluation by following intruction.
    python evaluate.py --model= 'model_name_needs to be replaced' --n_seq=12 --round=1 --bootstrap

    # We evaluate under the long term evaluation by following intruction.
    python evaluate.py --model= 'model_name_needs to be replaced' --n_seq=12 --round=6 --bootstrap


    # Train a full ensemble to enable evaluation for noise data
    python train_and_test.py --mode=train --fold=0 --gazebase_dir=data/gazebase_noise  --batch_classes=8 --batch_samples=8 --map_at_r
    python train_and_test.py --mode=train --fold=1 --gazebase_dir=data/gazebase_noise  --batch_classes=8 --batch_samples=8 --map_at_r
    python train_and_test.py --mode=train --fold=2 --gazebase_dir=data/gazebase_noise  --batch_classes=8 --batch_samples=8 --map_at_r
    python train_and_test.py --mode=train --fold=3 --gazebase_dir=data/gazebase_noise  --batch_classes=8 --batch_samples=8 --map_at_r

    # Test a full ensemble to enable evaluation for noise data
    python train_and_test.py --mode=test --fold=0 --gazebase_dir=data/gazebase_noise  --batch_classes=8 --batch_samples=8 --map_at_r
    python train_and_test.py --mode=test --fold=1 --gazebase_dir=data/gazebase_noise  --batch_classes=8 --batch_samples=8 --map_at_r
    python train_and_test.py --mode=test --fold=2 --gazebase_dir=data/gazebase_noise  --batch_classes=8 --batch_samples=8 --map_at_r
    python train_and_test.py --mode=test --fold=3 --gazebase_dir=data/gazebase_noise  --batch_classes=8 --batch_samples=8 --map_at_r

    # We evaluate under the short term evaluation by following intruction.
    python evaluate.py --model= 'model_name_needs_to_be_replaced' --n_seq=12 --round=1 --bootstrap

    # We evaluate under the long term evaluation by following intruction.
    python evaluate.py --model= 'model_name_needs_to_be_replaced' --n_seq=12 --round=6 --bootstrap
    ```
