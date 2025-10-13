######################################################################
############ Variables #########################################
name = "Fatma"
surname = "Göven"
print("Adım:", name, "Soyadım:", surname) #okunabilirlik -
# s: string
# d: decimal
# f: float
print("Adım: %s Soyadım: %s" %(name,surname)) #okunabilirlik +
print(f"Adım: {name} Soyadım: {surname}")
#f --> formatter



######################################################################
############ EscapeCharacter #########################################

#EscapeCharacter: \n Çıkış karakteri

print("""1.satır
2.satır
3.satır
""")

print("""\n\r\t4.satır
5.satır
6.satır
""")