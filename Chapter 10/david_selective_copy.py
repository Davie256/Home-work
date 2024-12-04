import os, shutil
from pathlib import Path

def search_file(start_dir, file_extension):

    for folderName, subfolders, filenames in os.walk(start_dir):
        for file in filenames:
            if file.endswith(file_extension):

                source_file = os.path.join(f'{start_dir}',f'{folderName}',f'{file}')
                destination_folder = Path.home()/ f'{New_folder_name}'

                if os.path.exists(source_file):
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)
                    shutil.copy(source_file, destination_folder)

            else:
                print('No files with the above extension found')
                break

    print('\nFiles copied successfully')


start_dir = input('Please specify the folder path containing the files in this format, C:\\....\\... \n')
file_extension = input('\nPlease specify the file extension you want to look for: formart; .txt, .pdf etc\n')
New_folder_name = input('\nPlease specify the destination folder where the files are to be pasted in home path: \n')


search_file(start_dir, file_extension)



