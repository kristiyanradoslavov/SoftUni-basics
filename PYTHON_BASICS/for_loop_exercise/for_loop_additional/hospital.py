period = int(input())

treated_patients = 0
untreated_patients = 0
doctors = 7

for days in range(1, period + 1):
    current_patients = int(input())
    if days % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    if current_patients <= doctors:
        treated_patients += current_patients
    elif current_patients > doctors:
        untreated_patients = untreated_patients + (current_patients - doctors)
        treated_patients += current_patients - (current_patients - doctors)

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
