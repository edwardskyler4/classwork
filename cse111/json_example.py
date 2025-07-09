import json

def main():
    student_data = {
        "name": "Alex",
        "id": 12345,
        "courses": [
            {"title": "Intro to Python", "credits": 3},
            {"title": "Web Development", "credits": 3},
        ],
        "is_active": True
    }

    print(student_data)

    with open('student.json', 'w') as file:
        json.dump(student_data, file, indent = 4)
        
    print()
    print("Successfully wrote data to student.json")
    print()

    with open('student.json', 'r') as file:
        loaded_data = json.load(file)
    
    print("Successfully read data from student.json")

    print()
    print(loaded_data)

    print(f"\nStudent Name: {loaded_data['name']}")

if __name__ == "__main__":
    main()