# ==================== Part 2: Difference Between Two Lists ====================

print("=" * 93)
print(" " * 30 + "Part 2: Difference Between Two Lists")
print("=" * 93)

def difference(L1, L2):
    only_in_L1 = [x for x in L1 if x not in L2]
    only_in_L2 = [x for x in L2 if x not in L1]
    return (only_in_L1, only_in_L2)

L1 = input("Enter elements of L1 (separated by spaces): ").split()
L2 = input("Enter elements of L2 (separated by spaces): ").split()

print()
print(f"  L1           : {L1}")
print(f"  L2           : {L2}")
print()

result = difference(L1, L2)

print(f"  In L1 not L2 : {result[0]}")
print(f"  In L2 not L1 : {result[1]}")
print(f"  Result tuple : {result}")
print("-" * 93)
print(" " * 42 + "Finished!")
print("=" * 93)