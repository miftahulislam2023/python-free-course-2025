import csv
students = [
    {
        "ID": 1, 
        "Name": "Abdur Rahim",
        "Grade": "A+"
    },
    {
        "ID": 2, 
        "Name": "Abdul Karim", 
        "Grade": "A"
    }
]
with open("grades.csv", "w", newline='') as file:
    columns = ["ID", "Name", "Grade"]
    writer = csv.DictWriter(file, fieldnames=columns)

    writer.writeheader() # হেডার (কলামের নাম) লেখা
    writer.writerows(students) # সব ডেটা লেখা