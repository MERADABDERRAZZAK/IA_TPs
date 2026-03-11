notes = []

while True:
    note = float(input("Enter a grade (negative value to stop): "))
    
    if note < 0:
        print("Program stopped.")
        break
    
    notes.append(note)
    
    print(f"Number of grades : {len(notes)}")
    print(f"Highest grade    : {max(notes):.2f}")
    print(f"Lowest grade     : {min(notes):.2f}")
    print(f"Average          : {sum(notes) / len(notes):.2f}")
    print("-" * 90)