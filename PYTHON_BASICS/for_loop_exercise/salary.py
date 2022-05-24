tab_count = int(input())
salary = int(input())

fine = 0

for tabs in range(1, tab_count + 1):
    website = input()
    if website == "Facebook":
        fine = fine + 150
    elif website == "Instagram":
        fine = fine + 100
    elif website == "Reddit":
        fine = fine + 50
    if fine >= salary:
        break


final_salary = salary - fine

if final_salary <= 0:
    print("You have lost your salary.")
else:
    print(final_salary)