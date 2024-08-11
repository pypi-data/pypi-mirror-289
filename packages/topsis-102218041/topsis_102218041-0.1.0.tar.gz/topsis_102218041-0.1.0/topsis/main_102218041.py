import csv
import numpy as np
import sys

def topsis(input_file, weights, impacts, output_file):
    try:

        with open(input_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
        
        headers = data[0]
        if len(headers) < 3:
            raise ValueError("Input file must contain three or more columns.")
        
        for row in data[1:]:
            if len(row) != len(headers):
                raise ValueError("All rows in the input file must have the same number of columns as the header.")
        
        matrix = np.array([list(map(float, row[1:])) for row in data[1:]])
        
        weights = list(map(float, weights.split(',')))
        impacts = impacts.split(',')
        
        if len(weights) != matrix.shape[1] or len(impacts) != matrix.shape[1]:
            raise ValueError("Number of weights, impacts, and columns must be the same.")
        
        if not all(impact in ['+', '-'] for impact in impacts):
            raise ValueError("Impacts must be either + or -.")
        
        norm_matrix = matrix / np.sqrt((matrix**2).sum(axis=0))
        
        weighted_matrix = norm_matrix * weights
        
        ideal_best = np.max(weighted_matrix, axis=0)
        ideal_worst = np.min(weighted_matrix, axis=0)
        
        for i in range(len(impacts)):
            if impacts[i] == '-':
                ideal_best[i], ideal_worst[i] = ideal_worst[i], ideal_best[i]
        
        S_plus = np.sqrt(((weighted_matrix - ideal_best)**2).sum(axis=1))
        S_minus = np.sqrt(((weighted_matrix - ideal_worst)**2).sum(axis=1))
        
        topsis_score = S_minus / (S_plus + S_minus)
        
        ranks = topsis_score.argsort()[::-1] + 1
        
        results = []
        for i in range(len(matrix)):
            row = data[i+1][:1] + list(matrix[i]) + [topsis_score[i], ranks[i]]
            if len(row) != len(headers) + 2: 
                raise ValueError(f"Row length mismatch detected: expected {len(headers) + 2}, but got {len(row)}")
            results.append(row)
        
        # print("TOPSIS Results:")
        # print(f"{headers[0]}, {', '.join(headers[1:])}, Topsis Score, Rank")
        # for result in results:
        #     print(", ".join(map(str, result)))
        
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers + ['Topsis Score', 'Rank'])
            writer.writerows(results)
        
        print(f"Results saved to {output_file}")
    
    except FileNotFoundError:
        print("Input file not found.")
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
    else:
        input_file = sys.argv[1]
        weights = sys.argv[2]
        impacts = sys.argv[3]
        output_file = sys.argv[4]
        topsis(input_file, weights, impacts, output_file)
