## string ##

# Tek Tırnak, çift tırnak ile string tanımlanabilir.
# Ayrıca 3 tırnak ile de docstring oluşturabilir. Bu birden fazla satırdan metin oluşturmayı sağlar okunabilirliği arttırır

metinData = 'metin1'
metinData2 = "metin2"
metinData3 = ''' Bu,
birden
fazla satırdan oluşan 
bir metindir.
'''
print(f"1-->{metinData}, 2-->{metinData2}, 3-->{metinData3}")
print("##########################################")

# 1-) Immutability (Değişmezlik): String karakterinin doğrudan değiştirilmesine izin vermez
metin1 = "metin4"
# metin1[0] = "J" --> Hatalıdır izin verilmez
print(metin1)
print("##########################################")

# 2-) Karakter Dizisi (Sequence): stringler bir karakter dizisidir, indeks ile istenilen karaktere ulaşılabilir
# indeks 0'dan başlar pozitif indeksle düzden, negatif indeksle tersten erişim sağlanır

metin2 = "metin5"
print(metin2[0]) #m
print(metin2[5]) #5
print(metin2[-1]) #5
print("##########################################")

# 3-) len() ile harf sayısı bulunabilir
metin3 = "Fatma Göven"
print(f"{metin3} harf sayısı, {len(metin3)} ") #boşlukta karakter olarak sayılır
print("##########################################")

# 4-) * operatörü string tekrarlanabilir
metin4= "Şanslı"
print(f"{metin4}'ün 4 kez çoğaltılmış hali", metin4*4, sep=" - ")
print("##########################################")

# 5-) Python Unicode desteği sağlar uluslarası metinler kolaylıkla gösterilebilir
metin6 = "こんにちは"  # Japonca
print(f"{metin6}")
print("##########################################")

# 6-) + operatörü ile birleştirme yapılabilir (Concatenation)
metin43 = "Ümit"
metin44 = "Göven"
sonuc = metin43 + " - " + metin44
print(sonuc)
print("##########################################")

# 7-) join(iterable) Iterable (liste,tuple vb) içindeki elemanları br stringle birleştirir
liste =["Python", "Java"]
print(liste)
print(liste[0] + " * " + liste[1])
print(" ".join(liste))
print("##########################################")

# 8-) Slicing: string'in belirli parçasını alma
metin89 = "Elektrik Elektronik Mühendisliği"
print(metin89[0:8])
print(metin89[:8])
print(metin89[9:20])
print(metin89[20:])
print("##########################################")

# 9-) Arama --> find(): Alt stringin ana string içinde ilk geçtiği indeksi döner, yoksa -1 döner
print(metin89.find("Elektronik"))
print(metin89.find("Fatma"))
print("##########################################")

# 10-) Değiştirme --> replace(): Belirtilen alt stringi başka bir stringle değiştirme
metin89 = metin89.replace("Elektronik","Haberleşme")
print(metin89.replace("Elektrik","Elektronik"))
print("##########################################")

# 11-) upper(): Karakterlerin hepsi büyük olur, isupper(): Hepsi büyük mü kontrol eder (bool)
metin11 = "Python programming language"
print(f"Büyük Harfli hali: {metin11.upper()}")
print(f"metin11 harfleri büyük mü? {metin11.isupper()}")
print(f"Şimdi Nasıl? {metin11.upper().isupper()}")
print("##########################################")

# 12-) lower(): Karakterlerin hepsi küçük olur, islower(): Hepsi küçük mü kontrol eder (bool)
print(f"Büyük Harfli hali: {metin11.lower()}")
print(f"metin11 harfleri büyük mü? {metin11.islower()}")
print(f"Şimdi Nasıl? {metin11.lower().islower()}")
print("##########################################")

# 13-) casefold(): Karakterlerin hepsi küçük olur, unicode için daha avantajlı
metin122 = "ß"
print(metin122.casefold())
print("##########################################")

# 14-) capitalize(): stringin sadece ilk harfleri büyük olur diğerleri küçük kalır. Cümlelerde kullanılır
metin34 = "programlama datası x ..."
print(f"{metin34.capitalize()}")
print("##########################################")

# 15-) title(): Her kelimenin ilk harfini büyük yapar, başlıklarda kullanılır.
metin23 ="her kelimenin baş harfi büyük olsun"
print(f"{metin23.title()}")
print("##########################################")

# 16-) endswith(suffix, start, end): stringin belirtilen alt stringle bitip bitmediğine bakar (bool)
metin122 = "Artık bitti."
print(f"{metin122.endswith("Artık")}")
print(f"{metin122.endswith("bitti.")}")
print("##########################################")

# 17-) startswith(suffix, start, end): stringin belirtilen alt stringle başlayıp başlamadığına bakar (bool)
print(f"{metin122.startswith("Artık")}")
print(f"{metin122.startswith("bitti.")}")
print("##########################################")

# 18-) index(substring, start, end): ana string içinde belirtiln alt string'in başladığı indelsi döner. Bulunamazsa ValueError verir
metin324 = " Hiçbir şeye benzemez bir şeye inanmanın tadı... "
print(f"{metin324.index("şeye")}")
#print(f"{metin324.index("tadi")}") Hatalı kod ValueError: substring not found :)
print("##########################################")

# 19-) strip(): baş ve sondaki boşlukları kaldırır
print(f"Trimsiz: {metin324}, boyutu {len(metin324)}")
print(f"Trimli: {metin324.strip()}, boyutu {len(metin324.strip())}")
print("##########################################")

#20-) split(): stringi ayırıcıya göre böler
metin32 = []
metin324_2 = metin324.strip().replace(" ","*")
metin32 = metin324_2.split("*")
print(metin324_2)
print(metin32)
print(metin32[0])
print(metin32[1])
print(metin32[2])
print(metin32[3])
print(metin32[4])
print(metin32[5])
print(metin32[6])
print("##########################################")

# 21-) string ve döngüler: döngü ile stringdeki karakterlere erişilebilir
for temp in metin324_2:
    print(temp)
print("##########################################")

# 22-) ord(): stringlerin Unicode değerine erişmek için kullanıır
# chr(): sayı değerleri ile string oluşturur
print(ord('Ü'))
print(chr(70))
print("##########################################")

# 23-) id(): Stringlerin bellekte temsili (her yeni string yeni bir yer kaplar)
metin78 = "Merhaba "
metin781 = metin78 + "Televole"
print(f"metin78'in bellekteki yeri: {id(metin78)}")
print(f"metin781'in bellekteki yeri: {id(metin781)}")
print("##########################################")

# 24-) import re kütüphanesi ile stringler üzerinde düzenli ifadelerle güçlü arama ve değiştirme yapılabilir

import re
metin = "Python 101 Course, 404 Not Found"
pattern = r"\d+"
sonuc = re.findall(pattern, metin)
print(sonuc) # ['101']

## pattern = r"\d+"
# \d: rakamı ifade eder [0-9]
# +: bir veya birden fazla rakam eşleşmesi sağlar
# r: raw string literal (ham string) tanımı
## re.findall(pattern, metin)
# findall(): verilen metindeki regx desenine ugun tüm eşleşmeleri bulur ve liste olarak döndürür
print("##########################################")

# 25-) İleri Düzey Formatlama:
# Raw String: r"metin" şeklinde tanımlanır, kaçış karakterlerini yok sayar.
print(r"C:\kullanıcı\dosya")  # Kaçış karakteri işlenmez
print(r"C:\kullanıcı\dosya\naltsatır")   # Kaçış karakteri işlenmez
print("C:\kullanıcı\dosya\naltsatır")  # Kaçış karakteri işlenir
print("##########################################")

# 26-) center(width, char): stringi ortalar ve etrafını verilen karakterle doldurur
metin = "Simurg5478"
print(metin.center(25,'+'))
print("##########################################")

# 27-) count(substring,start,end): alt stringin string içinde kaç kez geçtiğini döner
## İsteğe bağlı başlangıç ve bitiş indeksi de belirtilebilir
metin231 = "Python, öğren. Python uygula. Python kazan"
search231 = "Python"
print(f"{search231} kelimesi, '{metin231}''da {metin231.count(search231)} kez geçer")
print("##########################################")

# 28-) encode(encoding, errors): string'i belirtilen kodlamaya dönüştürür. errors hata işleme yöntemini belirler
print(metin231.encode("utf8"))
print("##########################################")

# 29-) expandtabs(tabsize): stringdeki tab karakterlerini belirtilen sayıda boşlukla değiştirir
metin3211 = "Python\tYaşa\t654"
print(metin3211.expandtabs(15))
print("##########################################")

# 30-) isalnum(): string harf ve rakamdan mı oluşuyor kontrolü yapar (özel karakter kabul etmez sadece harf ve sayı olmalı) (bool)
print(metin.isalnum())
print("##########################################")

# 31-) isalpha(): string sadece harften mi oluşuyor kontrolü yapar (bool)
print(search231.isalpha())
print("##########################################")

# 32-) isdigit(): string sadece rakamdan mı oluşuyor kontrolü yapar (bool)
metin78 = "827737730"
print(metin78.isdigit())
print("##########################################")

# 33-) Metot() dir: Fonksiyon okur yazarlığı için
print(dir("java"))
print(dir("python"))

## Üyelik operatörleri --> in, not in
## Kimlik operatörleri --> is, is not