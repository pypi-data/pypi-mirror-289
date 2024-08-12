import sys
import pandas as pd
import numpy as np
import os


def validate_inputs(weights, impacts, num_of_columns):
    weights = weights.replace(" ", "").split(',')
    impacts = impacts.replace(" ", "").split(',')

    if len(weights) != num_of_columns or len(impacts) != num_of_columns:
        raise ValueError(
            "Number of weights and impacts must be equal to the number of  (columns from 2nd to last).")

    try:
        weights = [float(w) for w in weights]
    except ValueError:
        raise ValueError("All weights must be numeric values.")
    
    if any(w <= 0 for w in weights):
        raise ValueError("All weights must be positive values.")

    for impact in impacts:
        if impact not in ['+', '-']:
            raise ValueError("Impacts must be either '+' or '-'.")

    return weights, impacts


def topsis(input_file, weights, impacts, result_file):
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{input_file}' not found.")
    
    if df.empty:
        raise ValueError("Input file is empty.")

    if df.shape[1] < 3:
        raise ValueError("Input file must contain at least three columns.")
    
    if df.columns.duplicated().any():
        raise ValueError("Input file contains duplicate column names.")
    
    if df.shape[0] < 2:
        raise ValueError("Input file must contain at least two rows of data.")

    data = df.iloc[:, 1:].values
    if not np.issubdtype(data.dtype, np.number):
        raise ValueError("From 2nd to last columns must contain numeric values only.")
    
    if np.isnan(data).any() or np.isinf(data).any():
        raise ValueError("Data contains NaN or infinite values.")
    num_of_columns = data.shape[1]
    weights, impacts = validate_inputs(weights, impacts, num_of_columns)

    
    norm_data = data / np.sqrt((data ** 2).sum(axis=0))

    weighted_data = norm_data * weights

    
    ideal_best = np.max(weighted_data, axis=0)
    ideal_worst = np.min(weighted_data, axis=0)

    for i, impact in enumerate(impacts):
        if impact == '-':
            ideal_best[i], ideal_worst[i] = ideal_worst[i], ideal_best[i]

    separation_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
    separation_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

    
    topsis_score = separation_worst / (separation_best + separation_worst)


    df['Topsis Score'] = topsis_score
    df['Rank'] = df['Topsis Score'].rank(method='max', ascending=False).astype(int)

    if os.path.exists(result_file):
        confirmation = input(f"'{result_file}' already exists. Overwrite? (y/n): ")
        if confirmation.lower() != 'y':
            sys.exit("Operation aborted by the user.")
    
    df.to_csv(result_file, index=False)
    print(f"Results saved to '{result_file}'.")


def main():
    if len(sys.argv) != 5:
        print("Usage: topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    result_file = sys.argv[4]

    if not input_file.endswith('.csv'):
        raise ValueError("Input file must be a CSV file.")
    
    if not result_file.endswith('.csv'):
        raise ValueError("Result file must have a '.csv' extension.")

    try:
        topsis(input_file, weights, impacts, result_file)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()