import numpy as np
import pandas as pd
import sys
import os

def topsis(input_file, weights, impacts, output_file):
    try:
        # Check if the file exists
        if not os.path.isfile(input_file):
            raise FileNotFoundError(f"File '{input_file}' not found.")
        
        # Reading the input file
        df = pd.read_csv(input_file)

        # Validating the input CSV format
        if df.shape[1] < 3:
            raise ValueError("Input file must have at least three columns.")
        
        # Extracting data and headers
        headers = df.columns.tolist()
        data = df.iloc[:, 1:].values  # Excluding the first column

        # Converting weights and impacts to lists
        weights = list(map(float, weights.split(',')))
        impacts = impacts.split(',')

        # Validating weights and impacts
        if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
            raise ValueError("Number of weights and impacts must match the number of criteria columns.")

        if not all(i in ['+', '-'] for i in impacts):
            raise ValueError("Impacts must be either '+' or '-'.")

        # Check if all data are numeric
        if not np.issubdtype(data.dtype, np.number):
            raise ValueError("From the 2nd to last columns must contain numeric values only.")

        # Normalize the decision matrix
        norm_data = data / np.sqrt(np.sum(data**2, axis=0))

        # Multiply by weights
        weighted_data = norm_data * weights

        # Calculate ideal best and worst
        ideal_best = np.max(weighted_data, axis=0) * np.array([1 if i == '+' else -1 for i in impacts])
        ideal_worst = np.min(weighted_data, axis=0) * np.array([1 if i == '-' else -1 for i in impacts])

        # Calculate the distance to ideal best and worst
        dist_best = np.sqrt(np.sum((weighted_data - ideal_best)**2, axis=1))
        dist_worst = np.sqrt(np.sum((weighted_data - ideal_worst)**2, axis=1))

        # Calculate the TOPSIS score
        topsis_score = dist_worst / (dist_best + dist_worst)

        # Add the scores and rank them
        df['TOPSIS Score'] = topsis_score
        df['Rank'] = df['TOPSIS Score'].rank(ascending=False).astype(int)

        # Save the result to the output file
        df.to_csv(output_file, index=False)
        print(f"Results saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 5:
        print("Usage: topsis-nikhil-102218082 <input_file> <weights> <impacts> <output_file>")
    else:
        input_file, weights, impacts, output_file = sys.argv[1:]
        topsis(input_file, weights, impacts, output_file)

if __name__ == "__main__":
    main()
