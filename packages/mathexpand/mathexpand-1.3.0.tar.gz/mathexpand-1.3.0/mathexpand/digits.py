def take_digits(number, return_type="l"):
    digits_list = list()
    digits_dict = {}
    temp = number

    for _ in range(len(str(number)) - 1):
        divisor = int("1" + (len(str(temp))-1) * "0")
        digits_list.append(int((temp - temp % divisor) / divisor))
        digits_dict[divisor] = int((temp - temp % divisor) / divisor)

        temp = temp % divisor

    digits_list.append(temp)
    digits_dict[1] = temp

    if return_type=="l":
        return digits_list
    elif return_type=="d":
        return digits_dict
    else:
        raise ValueError("Unkdown return type \"{}\"".format(return_type))
