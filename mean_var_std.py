import numpy as np

def calculate(input_list):
    """
    Validates input and calculates statistics on 3x3 NumPy array.
    """
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Reshape input list into 3x3 NumPy array
    matrix = np.array(input_list).reshape(3, 3)

    # Perform calculations
    calculations = {
        'mean': [
            np.mean(matrix, axis=0).tolist(),
            np.mean(matrix, axis=1).tolist(),
            np.mean(matrix).item()
        ],
        'variance': [
            np.var(matrix, axis=0).tolist(),
            np.var(matrix, axis=1).tolist(),
            np.var(matrix).item()
        ],
        'standard deviation': [
            np.std(matrix, axis=0).tolist(),
            np.std(matrix, axis=1).tolist(),
            np.std(matrix).item()
        ],
        'max': [
            np.max(matrix, axis=0).tolist(),
            np.max(matrix, axis=1).tolist(),
            np.max(matrix).item()
        ],
        'min': [
            np.min(matrix, axis=0).tolist(),
            np.min(matrix, axis=1).tolist(),
            np.min(matrix).item()
        ],
        'sum': [
            np.sum(matrix, axis=0).tolist(),
            np.sum(matrix, axis=1).tolist(),
            np.sum(matrix).item()
        ]
    }

    return calculations
