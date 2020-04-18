values={
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

def decimal_to_hexadecimal(num):
    assert type(num) in (int, float) and num==int(num)
    hexadecimal=""
    negative=False
    if num<0:
        negative=True
        num *= -1
    while num>0:
        num, remainder = divmod(num, 16)
        hexadecimal = values[remainder]+hexadecimal
    if negative:
        hexadecimal="-"+hexadecimal
    return hexadecimal

if __name__ == "__main__":
    num=int(input(""))
    print(decimal_to_hexadecimal(num))