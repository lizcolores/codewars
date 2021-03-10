def digital_root(n):
    suma = 0
    exterior_num = 0
    while n != 0:
        exterior_num = n % 10
        n //= 10;
        suma += exterior_num;
        if(len(str(suma))>1) and n%10 ==0 and n//10 == 0:
            n = suma;
            suma = 0
    return suma
