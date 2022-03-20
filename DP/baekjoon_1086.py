
'''

백준 문제

https://www.acmicpc.net/problem/1086

'''

def factorial(n: int) -> int:
    return 1 if n == 1 else factorial(n - 1) * n

def gcd(a: int, b: int) -> int:
    if not a or not b: return 0
    if a < b:
        a, b = b, a
    return gcd(b, a % b) if a % b else b

def permutation(bit: int, remainder: int) -> int:
    if bit == (1 << n) - 1:
        if remainder: return 0
        else: return 1
        
    if dp[bit][remainder] != -1: return dp[bit][remainder]
    
    temp = 0
    for i in range(n): 
        if not bit & (1 << i):
            re = (mod_numbers[i] + remainder * mod_digits[digits[i]]) % k
            temp += permutation(bit | (1 << i), re)

    dp[bit][remainder] = temp
    return dp[bit][remainder]
        
if __name__ == "__main__":
    n = int(input())
    numbers = [int(input()) for i in range(n)]
    k = int(input())

    digits = [len(str(number)) for number in numbers]
    mod_numbers = [number % k for number in numbers]
    mod_digits = [10 ** i % k for i in range(51)]
    dp = [[-1]*k for i in range(1 << n)]
    numerator = permutation(0, 0)
    denominator = factorial(n)
    greatest_common_divisor = gcd(numerator, denominator)
    if greatest_common_divisor:
        numerator //= greatest_common_divisor
        denominator //= greatest_common_divisor
        print(f"{numerator}/{denominator}")
    else:
        print("0/1")
