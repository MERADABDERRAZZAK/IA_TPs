# ==================== Exercise 1: Fibonacci Sequence ====================

print("=" * 93)
print(" " * 40 + "Fibonacci Sequence")
print("=" * 93)

a, b = 0, 1
n = int(input("Enter n (print Fibonacci numbers up to n): "))

print(f"\nStarting values: a = {a}, b = {b}")
print(f"Print all Fibonacci numbers where a <= {n}")
print("-" * 60)

i = 1
while a <= n:
    print(f"Step {i}:")
    print(f"  Current value  : a = {a}")
    print(f"  Operation      : a, b = b, a+b")
    a, b = b, a + b
    print(f"  New values     : a = {a}, b = {b}")
    print()
    i += 1

print("-" * 93)
print(" " * 17 + "Finished! All Fibonacci numbers up to n have been printed.")
print("=" * 93)
print()