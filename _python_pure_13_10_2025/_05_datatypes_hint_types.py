
#int, str, float, bool, list, tuple, set, dict

# Type Hint:

number: int = 10
PI: float = 3.14
value: str = "Merhabalar"
is_login: bool = True
list_data:list[int] = [1,2,3]
tuple_data:tuple[int,int] = (1,2)
dict_data:dict[str, int] = {"Merhabalar":44}

data:bytes=b"\x00\xff" #byte ve bytearray işlemleri
data_byte_array:bytearray = bytearray(b"abc")

nothing:None | str = None #None veya str olabilir