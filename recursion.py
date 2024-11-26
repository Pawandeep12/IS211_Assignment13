def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def compareTo(s1, s2):
    # Base cases
    if not s1 and not s2:  # Both strings are empty
        return 0
    elif not s1:  # s1 is empty, so it's smaller
        return -1
    elif not s2:  # s2 is empty, so s1 is larger
        return 1
    elif s1[0] != s2[0]:  # First characters differ
        return ord(s1[0]) - ord(s2[0])
    else:  # First characters are the same, compare the rest
        return compareTo(s1[1:], s2[1:])

if __name__ == "__main__":
    # Test Fibonacci
    print("Fibonacci Sequence:")
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")
    
    # Test GCD
    print("\nGCD Tests:")
    print(f"gcd(48, 18) = {gcd(48, 18)}")  # Should return 6
    print(f"gcd(101, 103) = {gcd(101, 103)}")  # Should return 1
    
    # Test String Comparison
    print("\nString Comparison:")
    print(f"compareTo('apple', 'apple') = {compareTo('apple', 'apple')}")  # Should return 0
    print(f"compareTo('apple', 'banana') = {compareTo('apple', 'banana')}")  # Should return negative
    print(f"compareTo('banana', 'apple') = {compareTo('banana', 'apple')}")  # Should return positive
