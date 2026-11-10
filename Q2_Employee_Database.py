# Employee Database using dictionaries

employees = {
    "E1": {"name": "Kiran", "dept": "IT", "salary": 60000},
    "E2": {"name": "Sara", "dept": "HR", "salary": 45000},
    "E3": {"name": "Dev", "dept": "IT", "salary": 75000},
    "E4": {"name": "Nina", "dept": "Finance", "salary": 52000},
    "E5": {"name": "Omar", "dept": "HR", "salary": 48000}
}

while True:
    print("\n1. Add employee")
    print("2. Update salary")
    print("3. Delete employee")
    print("4. Search by ID")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        emp_id = input("Enter employee ID: ")
        if emp_id in employees:
            print("Employee ID already exists")
        else:
            name = input("Enter name: ")
            dept = input("Enter department: ")
            salary = float(input("Enter salary: "))
            employees[emp_id] = {"name": name, "dept": dept, "salary": salary}
            print("Employee added")

    elif choice == "2":
        emp_id = input("Enter employee ID: ")
        if emp_id in employees:
            employees[emp_id]["salary"] = float(input("Enter new salary: "))
            print("Salary updated")
        else:
            print("Employee not found")

    elif choice == "3":
        emp_id = input("Enter employee ID: ")
        if emp_id in employees:
            del employees[emp_id]
            print("Employee deleted")
        else:
            print("Employee not found")

    elif choice == "4":
        emp_id = input("Enter employee ID: ")
        print(employees.get(emp_id, "Employee not found"))

    elif choice == "5":
        payroll = {}
        count = {}
        highest = {}

        for emp_id, emp in employees.items():
            dept = emp["dept"]
            payroll[dept] = payroll.get(dept, 0) + emp["salary"]
            count[dept] = count.get(dept, 0) + 1
            if dept not in highest or emp["salary"] > highest[dept]["salary"]:
                highest[dept] = emp

        print("Department payroll and headcount:")
        for dept in payroll:
            print(dept, "Payroll:", payroll[dept], "Employees:", count[dept])

        print("Highest paid in each department:")
        for dept, emp in highest.items():
            print(dept, emp["name"], emp["salary"])

        sorted_employees = sorted(employees.items(),
                                  key=lambda x: x[1]["salary"], reverse=True)
        print("Employees sorted by salary:", sorted_employees)

        # A new dictionary keeps the original salary values unchanged.
        new_employees = {
            emp_id: {**emp, "salary": emp["salary"] * 1.10}
            if emp["salary"] < 50000 else emp.copy()
            for emp_id, emp in employees.items()
        }
        print("After 10% raise:", new_employees)

        average = {dept: payroll[dept] / count[dept] for dept in payroll}
        if average:
            dept = max(average, key=average.get)
            print("Highest average salary:", dept, average[dept])

    elif choice == "6":
        break
    else:
        print("Invalid choice")
