from pathlib import Path as path

user_directory = input('Please enter your directory: ')
# destination_directory = input('To what destination you want to move the renamed Files: ')
user_directory = user_directory.replace('\\', '/')
# destination_directory = destination_directory.replace('\\', '/')
our_files = path(user_directory)

for file in our_files.iterdir():
    directory = file.parent

    for file1 in file.iterdir():

        for file2 in file1.iterdir():
            file_name = file2.stem

            for file3 in file2.iterdir():
                date = file3.stem

                for file4 in file3.iterdir():
                    if 'PASS' in file4.stem:
                        new_name = file_name + '_PASSED.zip'
                        print(new_name)
                    else:
                        new_name = file_name + '_FAILED.zip'
                        print(new_name)
                    for file5 in file4.iterdir():
                        file5.rename(path(directory, new_name))
                        print(file5)
