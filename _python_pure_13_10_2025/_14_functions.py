## Functions

# 1-) function --> parametresiz, return'süz
def account_sum():
    sayi1 = 10
    sayi2 = 20
    sayi12_sum = sayi1 + sayi2
    print(f"1: {sayi1} + {sayi2} =  {sayi12_sum}")
account_sum()

# 2-) function --> parametreli, return'süz
def account_sum2(sayi1, sayi2):
    sayi12_sum = sayi1 + sayi2
    print(f"2: {sayi1} + {sayi2} =  {sayi12_sum}")
account_sum2(10, 20)

# 3-) fucntion --> parametresiz, return'lü
def account_sum3():
    sayi1 = 10
    sayi2 = 20
    sayi12_sum = sayi1 + sayi2
    return sayi12_sum
result = account_sum3()
print(f"3: {result}")

# 4-) function --> parametreli, return'lü
def account_sum2(sayi1, sayi2):
    sayi12_sum = sayi1 + sayi2
    return sayi12_sum
result = account_sum2(10, 20)
print(f"4: {result}")