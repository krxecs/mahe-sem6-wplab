#!/usr/bin/env python3
# Q3: Write a python program to multiply two matrices

def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        return None

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(rows_B):
                result[i][j] += A[i][k] * B[k][j]

    return result

def input_matrix(name):
    while True:
        try:
            rows = int(input(f"Enter number of rows for Matrix {name}: "))
            cols = int(input(f"Enter number of columns for Matrix {name}: "))
            if rows <= 0 or cols <= 0:
                print("Rows and columns must be positive integers.")
                continue
            break
        except ValueError:
            print("Please enter valid integers for rows and columns.")

    matrix = []
    print(f"Enter each row of Matrix {name} as {cols} space-separated integers:")
    for i in range(rows):
        while True:
            line = input(f"Row {i+1}: ").strip()
            parts = line.split()
            if len(parts) != cols:
                print(f"Expected {cols} values but got {len(parts)}. Try again.")
                continue
            try:
                row = [int(x) for x in parts]
            except ValueError:
                print("Please enter only integers.")
                continue
            matrix.append(row)
            break
    return matrix

if __name__ == "__main__":
    try:
        print("--- Matrix A Input ---")
        matrix_a = input_matrix("A")

        print("\n--- Matrix B Input ---")
        matrix_b = input_matrix("B")

        result_matrix = multiply_matrices(matrix_a, matrix_b)

        if result_matrix:
            print("\nResultant Matrix:")
            for row in result_matrix:
                print(row)
        else:
            print("\nError: Matrices cannot be multiplied. Columns of A must equal Rows of B.")

    except ValueError:
        print("Error: Please provide valid integers.")
