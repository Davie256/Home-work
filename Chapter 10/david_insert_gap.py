import os, re, shutil

def insert_gap(folder_path, prefix):

    gap_position = 1

    pattern = re.compile(rf'^{prefix}(\d+)\.txt$')

    files = os.listdir(folder_path)
    existing_numbers = set()

    for file_name in files:
        match = pattern.match(file_name)
        if match:
            number = int(match.group(1))
            existing_numbers.add(number)

    for i in range(max(existing_numbers), gap_position, -1): #range(5,1,-1)
        old_file = f'{prefix}{i:d}.txt'
        new_file = f'{prefix}{i+1:d}.txt'

        if old_file in files:
            shutil.move(os.path.join(folder_path, old_file), os.path.join(folder_path, new_file))
            print (f'Inserted gap : Renamed {old_file} to {new_file}.')

def main():
    folder_path = 'C://Users//david//ddddd'
    prefix = 'spam'
    insert_gap(folder_path, prefix)

main()

