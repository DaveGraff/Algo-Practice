def reverse(self, x: int) -> int:
    MIN_INT = -2147483648
    MAX_INT = 2147483647
    negative = x < 0

    if negative:
        x *= -1

    new_num = 0

    while x != 0:
        val = x % 10
        new_num *= 10
        
        if new_num > MAX_INT or new_num < MIN_INT:
            return 0
        
        new_num += val
        x -= val
        x /= 10
        
    if negative:
        new_num *= -1
        
    return int(new_num)