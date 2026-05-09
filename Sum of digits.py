def recursive_sum(n):
    if n == 0: return 0
    return (n % 10) + recursive_sum(n // 10)

def iterative_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

num = 12345
print(f"Recursive: {recursive_sum(num)}")
print(f"Iterative: {iterative_sum(num)}")
# Output: Recursive: 15 | Iterative: 15