def hex_ouput(hex_num):
    dec_num = 0
    hex_num = input("Enter a hex number to convert: ")
    # for index, digit in enumerate(hex_num):
    #     if index > 1:
    #         dec_num += int(digit) * 16 ** (len(hex_num) - index - 1)
    for power, digit in enumerate(reversed(hex_num)):
        dec_num += int(digit, 16) * (16 ** power)
    print(dec_num)

hex_ouput("0x50")
