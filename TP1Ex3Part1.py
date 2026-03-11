# ==================== Exercise 3: Sorting & Difference ====================

print("=" * 93)
print(" " * 33 + "Part 1: Sort Values by Sign")
print("=" * 93)

classeur = {'negatives': [], 'positives': []}

def trier(classeur, valeur):
    if valeur < 0:
        classeur['negatives'].append(valeur)
    elif valeur > 0:
        classeur['positives'].append(valeur)
    return classeur

print("Enter numbers to sort (enter 0 to stop):\n")

i = 1
while True:
    valeur = float(input(f"Step {i} - Enter a number: "))

    if valeur == 0:
        print("\nZero detected — stopping.")
        break

    trier(classeur, valeur)

    print(f"  Positives : {classeur['positives']}")
    print(f"  Negatives : {classeur['negatives']}")
    print()
    i += 1

print("-" * 93)
print(f"  Final Positives : {classeur['positives']}")
print(f"  Final Negatives : {classeur['negatives']}")
print("=" * 93)
print()