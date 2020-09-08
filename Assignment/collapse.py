def collapse(value):   
    total = 0
    remainingDigits = len(value)
    
    if remainingDigits == 1:
        return value
    
    if remainingDigits < 1 or remainingDigits > 50:
        return None
    
    try:
        valueTest = int(value)
        if valueTest < 0:
            return None
    except:
        return None
    
    while remainingDigits > 1:
        total = 0
        for i in value:
            total += int(i)
        value = str(total)
        remainingDigits = len(str(total))
    
    return value