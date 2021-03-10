def count_bits(n):
    binary = '';
    find_ones = 0;
    while n // 2 != 0:
        binary = str(n%2) + binary;
        n = n //2;
    binary = str(n) + binary;
    for i in binary:
        if(i=='1'):
            find_ones = find_ones + 1;
    return find_ones;
