import os

# Get the directory where this script is located (the project directory)
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
# Define data directory paths within the project
DATA_DIR = os.path.join(PROJECT_DIR, "data")
BACKUP_DIR = os.path.join(DATA_DIR, "backup_data")
MAIN_CSV_PATH = os.path.join(DATA_DIR, "collatz_data.csv")
BACKUP_CSV_PATH = os.path.join(BACKUP_DIR, "collatz_data_backup.csv")

def ensure_data_directories():
    """Create data directories if they don't exist"""
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(BACKUP_DIR, exist_ok=True)

def read_data() -> list[str]:
    try:
        # Ensure directories exist before reading
        ensure_data_directories()
        
        with open(MAIN_CSV_PATH, 'r') as file:
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
        # Ensure directories exist before saving
        ensure_data_directories()
        
        with open(MAIN_CSV_PATH, 'a') as file:
            file.write(f"{num},{count}\n")
        with open(BACKUP_CSV_PATH, 'a') as backup_file:
            backup_file.write(f"{num},{count}\n")  
        return "Data saved successfully."
    except Exception as e:
        return f"An error occurred while saving data: {e}"
    
if __name__ == "__main__":
    print(read_data())
    