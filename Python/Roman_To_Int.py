def romanToInt(self, s: str) -> int:
    switcher = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
        
    total = 0
    lastchar = 1001
    
    for i, char in enumerate(s):
        if i != 0:
            if lastchar < switcher.get(char):
                total += switcher.get(char) - (2 * lastchar)
                continue
        lastchar = switcher.get(char)
        total += lastchar
            
    return total