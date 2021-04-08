def common_factors(num1, num2):
    divisors = []
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == num2 % i == 0:
            divisors.append(i)
    return divisors
