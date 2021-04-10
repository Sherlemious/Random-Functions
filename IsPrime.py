def is_prime(num):
    flag = True
    if num % 2 != 0:
        for f in range(3, num//2, 2):
            if num % f == 0:
                flag = False
                break
    else:
        flag = False
        
    return flag
