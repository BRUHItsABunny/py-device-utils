def luhn_checksum(n: int) -> int:
    i = 0
    luhn = 0
    while n > 0:
        cur = n % 10
        if i % 2 == 0:
            cur = cur * 2
            if cur > 9:
                cur = cur % 10 + cur / 10

        luhn += cur
        n = n / 10
        i += 1
    return luhn


def luhn_calculate(n: int) -> int:
    luhn = luhn_checksum(n)
    if luhn == 0:
        return 0
    return 10 - luhn


def luhn_valid(n: int) -> int:
    return (n % 10 + luhn_checksum(int(n / 10))) % 10 == 0
