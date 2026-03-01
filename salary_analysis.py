from data.employees_data import employees

dept_totals = {}
dept_counts = {}

for emp in employees:
    dept = emp["dept"]

    if dept not in dept_totals:
        dept_totals[dept] = emp["salary"]
        dept_counts[dept] = 1
    else:
        dept_totals[dept] += emp["salary"]
        dept_counts[dept] += 1

print("Average Salary by Department\n")

for dept in dept_totals:
    avg_salary = dept_totals[dept] / dept_counts[dept]
    print(dept, ":", avg_salary)