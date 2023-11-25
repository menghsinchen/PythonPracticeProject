mystring = "1.有大量點子可以選,就能做出更好的選擇。2.不論要解決什麼問題,千萬別碰到第一個解決方案就選了。"

def replacestrings(mystring):
    replacestrings = {
        " ":"",
        ",":"，",
        "(":"（",
        ")":"）",
        "——":"——",
        ":":"："
        }
    for before, after in replacestrings.items():
        mystring = mystring.replace(before, after)
    print(mystring)

def binary_to_hexadecimal(binary):
    ten = int(str(binary), 2)
    sixteen = hex(ten)
    print(ten)

binary_to_hexadecimal(1010111)