## Date ##

from datetime import date, datetime
from time import strftime

#bugünün tarihi
bugun: date = date.today()
print(f"bugun: {bugun}")
print(f"bugun yıl: {bugun.year}")
print(f"bugun ay: {bugun.month}")
print(f"bugun gün: {bugun.day}")
print(f"bugun haftası: {bugun.weekday()}") #0:Monday

# sabit tarih
tarih:date= date(2025, 2, 28)
print(f"tarih: {tarih}")

simdiki_zaman:datetime=datetime.now()
simdiki_zaman_2 = datetime.strftime(simdiki_zaman,"%Y-%m-%d")
print(f"simdiki_zaman: {simdiki_zaman}")    # saat dahil

#Formatter
formatter_date = datetime.strptime(simdiki_zaman_2,"%Y-%m-%d")
print(f"Güncel yıl: {formatter_date}")

date_format = date(2025,2,16)
print(f"{date_format}")

tr_date_format = date_format.strftime("%A.%B.%Y / %d.%m.%y")
print(f"{tr_date_format}")

