import csv

# Part (a): Create a CSV file called stud.csv with student records.
def create_csv():
    students = [
        ["Reg.No", "Name", "Section", "Mark1", "Mark2", "Mark3"],
        ["1001", "Alice", "A", 85, 90, 88],
        ["1002", "Bob", "B", 78, 82, 80],
        ["1003", "Charlie","A", 92, 88, 94],
        ["1004", "David", "B", 76, 85, 78],
        ["1005", "Eva", "A", 89, 92, 87],
        ["1006", "Frank", "B", 80, 76, 88],
        ["1007", "Grace", "A", 95, 89, 91],
    ]
    
    with open("stud.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(students)
    print("stud.csv created successfully.")

# Part (b): Read the CSV file and print details of students from a specific section.
def print_students_by_section(section):
    print(f"\nDetails of students in section {section}:")
    with open("stud.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)  # Read and store header
        print(header)
        for row in reader:
            if row[2] == section:
                print(row)

# Part (c): Print details of the first three toppers.
def print_top_three_toppers():
    students = []
    with open("stud.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            reg_no = row[0]
            name = row[1]
            section = row[2]
            marks = list(map(int, row[3:6]))  # Convert Mark1, Mark2, Mark3 to integers
            total = sum(marks)  # Calculate total marks
            students.append({"Reg.No": reg_no, "Name": name, "Section": section, "Total": total})
    
    # Sort students by total marks in descending order to find the top 3
    top_students = sorted(students, key=lambda x: x["Total"], reverse=True)[:3]

    print("\nTop 3 Toppers:")
    print(["Reg.No", "Name", "Section", "Total Marks"])
    for student in top_students:
        print([student["Reg.No"], student["Name"], student["Section"], student["Total"]])

# Run all parts of the program
create_csv()
print_students_by_section("A")
print_top_three_toppers()
