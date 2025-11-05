# gradebook.py
# Name: [Vaibhav Gupta]
# Date: 05-Nov-2025
# Title: Gradebook Analyzer

def print_welcome():
    print("Welcome to Gradebook Analyzer!")
    print("------------------------------")

def print_menu():
    print("\nSelect an option:")
    print("1. Enter student data")
    print("2. Show analysis")
    print("3. Show results table")
    print("4. Exit\n")

def calculate_average(marks_dict):
    values = list(marks_dict.values())
    return sum(values) / len(values) if values else 0

def calculate_median(marks_dict):
    values = sorted(marks_dict.values())
    n = len(values)
    if n == 0:
        return 0
    mid = n // 2
    if n % 2 == 1:
        return values[mid]
    else:
        return (values[mid-1] + values[mid]) / 2

def find_max_score(marks_dict):
    return max(marks_dict.values()) if marks_dict else 0

def find_min_score(marks_dict):
    return min(marks_dict.values()) if marks_dict else 0

def assign_grades(marks_dict):
    grade_dict = {}
    for name, marks in marks_dict.items():
        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        elif marks >= 60:
            grade = "D"
        else:
            grade = "F"
        grade_dict[name] = grade
    return grade_dict

def count_grades(grade_dict):
    summary = {}
    for grade in ["A", "B", "C", "D", "F"]:
        summary[grade] = list(grade_dict.values()).count(grade)
    return summary

def show_statistics(marks_dict):
    print("\n--- Statistical Analysis ---")
    print(f"Average: {calculate_average(marks_dict):.2f}")
    print(f"Median: {calculate_median(marks_dict):.2f}")
    print(f"Max score: {find_max_score(marks_dict)}")
    print(f"Min score: {find_min_score(marks_dict)}")

def show_grade_summary(grade_dict):
    print("\n--- Grade Distribution ---")
    summary = count_grades(grade_dict)
    for grade, count in summary.items():
        print(f"{grade}: {count} student(s)")

def show_pass_fail(marks_dict):
    passed_students = [name for name, m in marks_dict.items() if m >= 40]
    failed_students = [name for name, m in marks_dict.items() if m < 40]
    print("\n--- Pass & Fail List ---")
    print(f"Passed ({len(passed_students)}): {', '.join(passed_students) or 'None'}")
    print(f"Failed ({len(failed_students)}): {', '.join(failed_students) or 'None'}")

def print_results_table(marks_dict, grade_dict):
    print("\nName      Marks   Grade")
    print("--------------------------")
    for name, marks in marks_dict.items():
        print(f"{name:<10}{marks:<8}{grade_dict[name]}")

def main():
    print_welcome()
    marks = {}
    grade_dict = {}
    while True:
        print_menu()
        choice = input("Enter choice (1-4): ").strip()
        if choice == "1":
            marks.clear()  # reset marks if new entry
            n = int(input("How many students? "))
            for i in range(n):
                name = input(f"Enter name of student {i+1}: ")
                mark = int(input(f"Enter marks for {name}: "))
                marks[name] = mark
            grade_dict = assign_grades(marks)
            print("Data entry complete.")
        elif choice == "2":
            if not marks:
                print("No data available. Please enter students first.")
                continue
            show_statistics(marks)
            grade_dict = assign_grades(marks)
            show_grade_summary(grade_dict)
            show_pass_fail(marks)
        elif choice == "3":
            if not marks:
                print("No data available. Please enter students first.")
                continue
            if not grade_dict:
                grade_dict = assign_grades(marks)
            print_results_table(marks, grade_dict)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
