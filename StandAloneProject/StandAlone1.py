import os

FILE_NAME = 'Customer.txt'


def create_record():
    while True:
        name = input("Enter your name: ").strip()

        try:
            age = int(input("Enter your age (18-60): "))
            if age < 18 or age > 60:
                print("Age must be between 18 and 60.")
                continue
        except ValueError:
            print("Invalid age. Enter a number.")
            continue

        designation = input("Enter your designation (P25/M30/T20): ").strip().upper()
        if designation not in ['P25', 'M30', 'T20']:
            print("Invalid designation. Choose from P25, M30, or T20.")
            continue

        if designation == 'P25':
            salary = 25000
        elif designation == 'M30':
            salary = 30000
        elif designation == 'T20':
            salary = 20000

        print("\nEntered Details:")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Designation: {designation}")
        print(f"Salary: {salary}")

        choice = input("\nType 'yes' to confirm or 'no' to re-enter: ").strip().lower()

        if choice == 'yes':
            with open(FILE_NAME, 'a') as f:
                f.write(f"{name},{age},{designation},{salary}\n")
            print("Record saved successfully.\n")
            break
        elif choice == 'no':
            print("Please re-enter the details.\n")
        else:
            print("Invalid input. Please type 'yes' or 'no'.\n")


def display_records():
    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    with open(FILE_NAME, 'r') as f:
        lines = f.readlines()

    if not lines:
        print("No records found.\n")
        return

    print("\n----- Records -----")
    for line in lines:
        name, age, designation, salary = line.strip().split(',')
        salary = float(salary)
        hike = min(salary * 0.30, salary)  # 30% hike max
        print(f"Name: {name}, Age: {age}, Designation: {designation}, "
              f"Salary: {salary}, Max Possible Hike: {hike}")
    print("-------------------\n")


def raise_salary():
    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    name_to_raise = input("Enter the name of the person whose salary is to be raised: ").strip()

    with open(FILE_NAME, 'r') as f:
        lines = f.readlines()

    found = False
    updated_lines = []

    for line in lines:
        name, age, designation, salary = line.strip().split(',')
        if name.lower() == name_to_raise.lower():
            try:
                percent = float(input(f"Enter raise percentage for {name} (Max 30%): "))
                if percent > 30:
                    print("Hike cannot be more than 30%.")
                    percent = 30
                salary = float(salary)
                salary += salary * (percent / 100)
                print(f"Updated salary for {name}: {salary}")
                found = True
            except ValueError:
                print("Invalid percentage.")
                salary = float(salary)

            updated_line = f"{name},{age},{designation},{salary}\n"
        else:
            updated_line = line

        updated_lines.append(updated_line)

    if not found:
        print(f"No record found for {name_to_raise}.\n")
    else:
        with open(FILE_NAME, 'w') as f:
            f.writelines(updated_lines)
        print("Salary updated successfully.\n")


def main():
    while True:
        print("===== Choices =====")
        print("1. Create")
        print("2. Display")
        print("3. Raise Salary")
        print("4. Exit")
        print("================")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            create_record()
        elif choice == '2':
            display_records()
        elif choice == '3':
            raise_salary()
        elif choice == '4':
            print("Thank you for using the application!")
            break
        else:
            print("Invalid choice. Please enter 1-4.\n")


if __name__ == "__main__":
    main()
