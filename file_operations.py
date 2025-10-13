import os

def read_data() -> list[str]:
    try:
        with open('data/collatz_data.csv', 'r') as file:
            lines = file.readlines()
            for line in lines:
                line.split(',')
            return [line.strip() for line in lines]
    except FileNotFoundError:
        print("File not found. No Data written yet.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def save_data(num: int, count: int) -> str:
    try:
        with open('data/collatz_data.csv', 'a') as file:
            file.write(f"{num},{count}\n")
        with open('data/backup_data/collatz_data_backup.csv', 'a') as backup_file:
            backup_file.write(f"{num},{count}\n")  
        return "Data saved successfully."
    except Exception as e:
        return f"An error occurred while saving data: {e}"
    
if __name__ == "__main__":
    print(read_data())
    