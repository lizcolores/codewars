def binary_array_to_number(arr):
    decimal = 0
    for indice, value in enumerate(arr[::-1]):
        decimal += value * 2 ** indice;
    return decimal
