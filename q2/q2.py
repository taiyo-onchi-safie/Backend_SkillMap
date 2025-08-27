def converting_from_binary_to_decimal(binary: str) -> int:
    decimal = 0
    digit_count = len(binary)

    if int(binary) == 0:
        return 0

    for i in range(digit_count):
        if binary[i] == "1":
            decimal += pow(2, (digit_count - 1) - i)

    return decimal
