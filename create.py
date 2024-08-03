import csv
import requests

def read_numbers_from_csv(file_path, column_name):
    numbers = []
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                numbers.append(row[column_name])
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except KeyError:
        print(f"Error: The column name '{column_name}' does not exist in the CSV file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return numbers

def get_numbers_from_user():
    numbers = []
    print("Enter phone numbers (type 'done' to finish):")
    while True:
        number = input("Phone number: ")
        if number.lower() == 'done':
            break
        numbers.append(number)
    return numbers

def create_group(group_name, numbers):
    url = "https://gate.whapi.cloud/groups"
    payload = {
        "subject": group_name,
        "participants": numbers
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer Va0lyJ3tzroqFvDXCj68d8EEjJBmzsn6"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.text

def main():
    print("Choose an option:")
    print("1. Make Group Using CSV File")
    print("2. Enter Numbers Manually")
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        file_path = input("Enter the path to the CSV file: ").strip()
        column_name = input("Enter the column name to use for contact numbers: ").strip()
        numbers = read_numbers_from_csv(file_path, column_name)
        if not numbers:
            print("No numbers were read from the CSV file. Please check the file path and column name.")
            return
    elif choice == '2':
        numbers = get_numbers_from_user()
    else:
        print("Invalid choice.")
        return

    group_name = input("Enter the group name: ").strip()
    response_text = create_group(group_name, numbers)
    print(response_text)

if __name__ == "__main__":
    main()
