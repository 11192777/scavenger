def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal & 1) + binary
        decimal >>= 1
    return binary

if __name__ == '__main__':
    decimal_number = int(input("请输入一个十进制数: "))
    binary_number = decimal_to_binary(decimal_number)
    print("对应的二进制数为:", binary_number)



