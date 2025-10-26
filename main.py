def PrimeList(N):
    primes = []
    # 小于2的数没有质数，直接返回
    if N <= 2:
        return ""
    # 遍历2到N-1的每个数
    for num in range(2, N):
        is_prime = True
        # 试除判断是否为质数，只需试除到sqrt(num)
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    return " ".join(primes)

