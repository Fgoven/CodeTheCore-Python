## Loop

### for
## Loop Over

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for temp in my_list:
    print(f"{temp}", end=" ")
print("\n****************************************\n")

# range() --> belirli aralıkta sayı üretir
for temp in range(16):
    print(f"{temp}", end=" ")
print("\n****************************************\n")
# range(start,stop,step): aralıklı sayı üretme

for temp in range(1,17,3):
    print(f"{temp}", end=" ")
print("\n*****************************************\n")

# 10'a kadar (10 dahil) olan sayıların toplamı
# 1.YOL
sum1 = 0
for i in range(11):
    #sum1 += i
    sum1 = sum1 + i
print(f"10 a kadar olan sayıların toplamı: {sum1}")
# 2.YOL
sum_data = sum(range(1,11))
print(f"10 a kadar olan sayıların toplamı: {sum_data}")
print("\n*****************************************\n")

### while
data:int = 1
while data < 6:
    print(f"{data}")
    data += 1
print("\n*****************************************\n")

# while, break, continue,pass
## step 1: 1 ile 10 arasındaki sayıların toplamı
## step 2: Eğer 10'dan sonra devam ediyorsa dur
## step 3: Eğer döngüde 5 varsa toplama yapma
## step 4: Eğer döngüde 6 varsa bir şey yapma
## step 5: 1-10 arasındaki tek sayıları göster ve topla
## step 6: 1-10 arasındaki çift sayıları göster ve topla
## step 7:başlangıç ve bitiş kullanıcıdan alınsın ve toplansın

# step1,step2:
data:int = 0
sum_all, sum_even, sum_odd = 0, 0, 0
while data < 11:
    sum_all = sum(range(data))
    data += 1
print(f"Toplam: {sum_all}")

# step3:
sum_all = 0
data = 0
while data < 11:
    if data == 5:
        data += 1
    else:
        sum_all = sum(range(data))
        data += 1
print(f"Toplam: {sum_all}")

# step4:
sum_all = 0
data = 0
while data < 11:
    if data == 6:
        pass
    print(f"Data: {data}", end=" ")
    data += 1
print("\n*****************************************\n")
# step5:
data = 0
sum_all, sum_even, sum_odd = 0, 0, 0
while data < 11:
    if data % 2 == 0:
        data += 1
        continue
    else:
        print(f"Tek sayılar: {data}", end=" ")
        sum_odd += data
        data += 1
print(f"\nTek Toplam: {sum_odd}")
print("\n*****************************************\n")
# step 6:
data = 0
sum_even  = 0
while data < 11:
    if data % 2 == 0:
        print(f"Çift sayılar: {data}", end=" ")
        sum_even += data
        data += 1
    else:
        data += 1
        continue
print(f"\nÇift Toplam: {sum_even}")
print("\n*****************************************\n")

# step 7:
start = int(input("Start: "))
stop = int(input("Stop: "))

sum2 = sum(range(start, stop))
print(f"{start} ve {stop} arasındaki sayıların toplamı: {sum2}")
