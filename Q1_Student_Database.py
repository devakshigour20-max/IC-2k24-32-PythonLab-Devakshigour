# Student Database using nested dictionaries

students = {
    101: {"name": "Asha", "marks": {"Math": 88, "Physics": 76, "Chem": 92}},
    102: {"name": "Ravi", "marks": {"Math": 35, "Physics": 58, "Chem": 64}},
    103: {"name": "Meena", "marks": {"Math": 72, "Physics": 81, "Chem": 69}}
}

while True:
    print("\n1. Add student")
    print("2. Update marks")
    print("3. Delete student")
    print("4. Show student")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = int(input("Enter roll number: "))
        if roll in students:
            print("Roll number already exists")
        else:
            name = input("Enter name: ")
            marks = {}
            n = int(input("Enter number of subjects: "))
            valid = True
            for i in range(n):
                subject = input("Enter subject: ")
                mark = int(input("Enter marks: "))
                if mark < 0 or mark > 100:
                    print("Marks should be between 0 and 100")
                    valid = False
                    break
                marks[subject] = mark
            if valid:
                students[roll] = {"name": name, "marks": marks}
                print("Student added")

    elif choice == "2":
        roll = int(input("Enter roll number: "))
        if roll in students:
            subject = input("Enter subject: ")
            mark = int(input("Enter new marks: "))
            if 0 <= mark <= 100:
                students[roll]["marks"][subject] = mark
                print("Marks updated")
            else:
                print("Invalid marks")
        else:
            print("Student not found")

    elif choice == "3":
        roll = int(input("Enter roll number: "))
        if roll in students:
            del students[roll]
            print("Student deleted")
        else:
            print("Student not found")

    elif choice == "4":
        roll = int(input("Enter roll number: "))
        if roll in students:
            print(students[roll])
        else:
            print("Student not found")

    elif choice == "5":
        averages = {}
        for roll, data in students.items():
            if data["marks"]:
                averages[roll] = round(sum(data["marks"].values()) / len(data["marks"]), 2)

        print("Averages:", averages)
        if averages:
            topper = max(averages, key=averages.get)
            print("Topper:", students[topper]["name"])

        subjects = set()
        for data in students.values():
            subjects.update(data["marks"])

        for subject in subjects:
            scores = [(data["name"], data["marks"][subject])
                      for data in students.values() if subject in data["marks"]]
            if scores:
                print("Highest in", subject, ":", max(scores, key=lambda x: x[1]))

        below_40 = [(data["name"], sub, mark)
                    for data in students.values()
                    for sub, mark in data["marks"].items() if mark < 40]
        print("Below 40:", below_40)

        grades = {"A": [], "B": [], "C": [], "D": [], "F": []}
        for roll, avg in averages.items():
            name = students[roll]["name"]
            if avg >= 90:
                grades["A"].append(name)
            elif avg >= 75:
                grades["B"].append(name)
            elif avg >= 60:
                grades["C"].append(name)
            elif avg >= 40:
                grades["D"].append(name)
            else:
                grades["F"].append(name)
        print("Grades:", grades)

    elif choice == "6":
        break
    else:
        print("Invalid choice")
