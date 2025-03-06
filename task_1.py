class HexList(list):
    def __getitem__(self, index):
        return hex(super().__getitem__(index))


my_list = HexList([1, 15, 16, 25])
print(my_list[0])  # 0x1
print(my_list[1])  # 0xf
print(my_list[2])  # 0x10
print(my_list[3])  # 0x19
