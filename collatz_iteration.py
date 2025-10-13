from helper_modules.get_input import get_input
from helper_modules.cls import cls
from file_operations import read_data, save_data

def get_processed_numbers() -> set[int]:
    # Extract the starting numbers that have already been processed
    collatz_data = read_data()
    processed_numbers = set()
    
    for line in collatz_data:
        if line and ',' in line:
            try:
                # Extract the first number (starting number) from each line
                number = int(line.split(',')[0])
                processed_numbers.add(number)
            except ValueError:
                continue  # Skip invalid lines    
    return processed_numbers

def iterate_num_range(number_range):
    processed_numbers = get_processed_numbers()
    # Only show the count and highest processed number
    if processed_numbers:
        highest_processed = max(processed_numbers)
        print(f"Found {len(processed_numbers)} processed numbers. Highest: {highest_processed}")
    else:
        print("No processed numbers found - starting fresh")

    for i in range(1, number_range + 1):
        if i in processed_numbers:
            print(f"Skipping {i} - already processed")
            continue  # Skip if already processed
            
        num: int = i
        count: int = 0
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num * 3 + 1
            count += 1
        print(f"Processing {i}: {count} steps")
        save_data(i, count)
    cls()
    print(f"Saved data to /data/collatz_data.csv and /data/backup_data/collatz_data_backup.csv")

def run_iteration() -> None:
    number_range = get_input('Enter a number-range to iterate over: ', int, 1)
    iterate_num_range(number_range)
