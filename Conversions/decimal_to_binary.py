def decimal_to_binary(num):

    if type(num) == float:
        raise TypeError("'float' object cannot be interpreted as an integer")
    if type(num) == str:
        raise TypeError("'str' object cannot be interpreted as an integer")

    if num == 0:
        return "0b0"

    negative = False

    if num < 0:
        negative = True
        num = -num

    binary = []
    while num > 0:
        binary.insert(0, num % 2)
        num >>= 1

    if negative:
        return "".join(str(e) for e in binary)

    return "".join(str(e) for e in binary)


if __name__ == "__main__":
    num=int(input(""))
    print(decimal_to_binary(num))
