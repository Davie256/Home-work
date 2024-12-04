import os, re, shutil

def fillling_gaps(folder_path, prefix):

    pattern = re.compile(rf'^{re.escape(prefix)}(\d+)\.txt$', re.IGNORECASE)

    files = os.listdir(folder_path)
    existing_numbers = set()

    for file_name in files:
        match = pattern.match(file_name)
        if match:
            number = int(match.group(1))
            existing_numbers.add(number)

    expected_numbers = set(range(1, max(existing_numbers)+1))
    missing_numbers = expected_numbers - existing_numbers

    for number in missing_numbers:
        old_file = f'{prefix}{number+1:d}.txt'
        new_file = f'{prefix}{number:d}.txt'

        if old_file in files:
            shutil.move(os.path.join(folder_path, old_file), os.path.join(folder_path, new_file))
            print(f'Renamed {old_file} to {new_file} to close the gap.')

def main():
    folder_path = input('Enter the folder path in this format; C:/..../....\n')
    prefix = input('\nEnter the file prefix ie. spam \n')
    fillling_gaps(folder_path, prefix)

main()


