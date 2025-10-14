
# Dynamics Type
# Değişken İsimlendirme ==>  (_ snake_case)

## sayılar Number ##

number1 = 10
number2 = -20
PI= 3.14159
number4 = None
print(f"number1: {number1} number2:{number2} PI:{PI}")
print(f"Boş değer: {number4} type:{type(number4)}")

## types ##

print(f"number1: {number1} ==> Türü: {type(number1)}")
print(f"PI: {PI} ==> Türü: {type(PI)}")
## string ##
name = "Fatma"
surname = "Göven"

print(f"Adım: {name}, Soyadım: {surname}")

## boolean True/False ##
is_login = True
print(f"Login mi? {is_login} ==> Türü: {type(is_login)}")

## List ##

my_list = [1, 2, 3, 4, 5, 6, True, "Malatya", 51.56]
print(f"Liste: {my_list}, ==> Türü: {type(my_list)}")

## Tuple ##
# Tuple'daki değerler değiştirilemez, immutable
my_tuple = (1, 2, 3, 4, 5, 6, True,"Malatya", 51.56)
print(f"Tuple: {my_tuple}, ==> Türü: {type(my_tuple)}")

## Set ##
# unique yapı her eleman benzersizdir

my_set = { 2, 3, 4, 5, 6,"Malatya", "Malatya", 51.56, 2, 6, 5, 4, 2, 3, True, True, "Malatya", False}
print(f"Set: {my_set}, ==> Türü: {type(my_set)}")

## Dictionary

my_dict = {
    "name": "Fatma",
    "surname": "Göven",
    "is_login":True
}
print(f"Dict: {my_dict}, ==> Türü: {type(my_dict)}")