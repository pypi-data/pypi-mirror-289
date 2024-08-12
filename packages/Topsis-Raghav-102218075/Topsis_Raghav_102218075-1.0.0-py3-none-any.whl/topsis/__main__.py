import pandas as pd
import numpy as np
import sys

def topsis(input_file, weights, impacts, output_file):
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    if len(df.columns) < 3:
        print("Error: Input file must contain three or more columns.")
        sys.exit(1)

    if not df.iloc[:, 1:].applymap(np.isreal).all().all():
        print("Error: Columns from 2nd to last must contain numeric values only.")
        sys.exit(1)

    weights = list(map(float, weights.split(',')))
    impacts = impacts.split(',')

    if len(weights) != len(impacts) or len(weights) != len(df.columns) - 1:
        print("Error: Number of weights, impacts, and columns (from 2nd to last) must be the same.")
        sys.exit(1)

    if not all(impact in ['+', '-'] for impact in impacts):
        print("Error: Impacts must be either +ve or -ve.")
        sys.exit(1)

    decision_matrix = df.iloc[:, 1:].values
    normalized_matrix = decision_matrix / np.sqrt(np.sum(decision_matrix**2, axis=0))

    weighted_normalized = normalized_matrix * weights
    
    ideal_best = np.max(weighted_normalized, axis=0) * np.array([1 if i == '+' else -1 for i in impacts])
    ideal_worst = np.min(weighted_normalized, axis=0) * np.array([1 if i == '+' else -1 for i in impacts])

    s_best = np.sqrt(np.sum((weighted_normalized - ideal_best)**2, axis=1))
    s_worst = np.sqrt(np.sum((weighted_normalized - ideal_worst)**2, axis=1))

    topsis_score = s_worst / (s_best + s_worst)

    df['Topsis Score'] = topsis_score
    df['Rank'] = df['Topsis Score'].rank(ascending=False, method='dense').astype(int)

    df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    topsis(input_file, weights, impacts, output_file)