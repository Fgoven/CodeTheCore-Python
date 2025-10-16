from pip._internal.resolution.resolvelib import requirements


#default değer kullanımı

def account_sum4(sayi1, sayi2=10):
    sayi12_sum = sayi1 + sayi2
    return sayi12_sum
result = account_sum4(10, 20)
print(f"5: {result}")
result = account_sum4(10)
print(f"6: {result}")

# Function beartype

# 1. YOL
# python -m pip install beartype --> Windows

# 2. YOL
# cat requrement.txt
# pip install -r requirements.txt

# bearype kullanım sebebi tanımladığım dışında ben değer girilmesini istemiyorum demekmiş
# Runtime'da hata yakalamayı kolaylaştırır

from beartype import beartype
@beartype
def account_sum5(sayi1:int=0, sayi2:int=0) -> int:
    return sayi1 + sayi2
result = account_sum5()
print(f"5: {result}")
result = account_sum5(3,6)
print(f"5: {result}")
result = account_sum5(3)
print(f"5: {result}")
#result = account_sum5(3,"6") ## hata verir str giremem int olmalı
#print(f"5: {result}")
