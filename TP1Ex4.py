# ==================== Exercise 4: List Indexing ====================

print("=" * 93)
print(" " * 34 + "Exercise 4: List Indexing")
print("=" * 93)

def index_list(L1, L2):
    result = []
    for i in L2:
        if -len(L1) <= i < len(L1):
            result.append(L1[i])
        else:
            result.append(None)
    return result

L1 = input("Enter elements of L1 (separated by spaces): ").split()
L2 = list(map(int, input("Enter indices  of L2 (separated by spaces): ").split()))

print()
print(f"  L1      : {L1}")
print(f"  L2      : {L2}")
print()

result = index_list(L1, L2)

print(f"  Result  : {result}")
print("-" * 93)
print(" " * 42 + "Finished!")
print("=" * 93)