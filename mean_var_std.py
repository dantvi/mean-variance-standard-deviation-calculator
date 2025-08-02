def calculate(input_list):
    """
    Validates input and reshapes into a 3x3 NumPy array.
    """
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Reshape input list into 3x3 NumPy array
    matrix = np.array(input_list).reshape(3, 3)

    # TODO: Perform statistical calculations
