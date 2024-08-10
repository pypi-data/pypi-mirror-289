import pandas as pd
import numpy as np
import sys

def topsis(input_file, weights, impacts, result_file):
    # Read the input file
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: An error occurred while reading the file: {e}")
        sys.exit(1)

    # Validate the input file
    if df.shape[1] < 3:
        print("Error: Input file must contain three or more columns.")
        sys.exit(1)

    # Parse weights and impacts
    try:
        weights = [float(i) for i in weights.split(',')]
        impacts = impacts.split(',')
    except ValueError:
        print("Error: Weights must be numeric and separated by commas.")
        sys.exit(1)

    if len(weights) != len(impacts) or len(weights) != df.shape[1] - 1:
        print("Error: Number of weights, impacts, and columns (from 2nd to last) must be the same.")
        sys.exit(1)

    if not all(i in ['+', '-'] for i in impacts):
        print("Error: Impacts must be either '+' or '-'.")
        sys.exit(1)

    # Extracting the data for analysis (from 2nd to last column)
    data = df.iloc[:, 1:].values

    # Check if all values are numeric
    if not np.issubdtype(data.dtype, np.number):
        print("Error: Columns from 2nd to last must contain numeric values only.")
        sys.exit(1)

    # Normalize the data
    norm_data = data / np.sqrt((data ** 2).sum(axis=0))

    # Multiply by weights
    weighted_data = norm_data * weights

    # Calculate ideal best and worst
    ideal_best = np.max(weighted_data, axis=0) * (np.array(impacts) == '+') + np.min(weighted_data, axis=0) * (
                np.array(impacts) == '-')
    ideal_worst = np.min(weighted_data, axis=0) * (np.array(impacts) == '+') + np.max(weighted_data, axis=0) * (
                np.array(impacts) == '-')

    # Calculate distances from ideal best and worst
    dist_ideal_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
    dist_ideal_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

    # Calculate the TOPSIS score
    score = dist_ideal_worst / (dist_ideal_best + dist_ideal_worst)

    # Add the score to the dataframe
    df['Topsis Score'] = score

    # Rank the scores
    df['Rank'] = df['Topsis Score'].rank(ascending=False)

    # Save the result to a file
    try:
        df.to_csv(result_file, index=False)
        print(f"Results saved to '{result_file}'")
    except Exception as e:
        print(f"Error: Could not save results to '{result_file}': {e}")
        sys.exit(1)
