import os
import sys

def rename_files(old, new, src_dir, dest_dir):

    file_list = os.listdir(src_dir)

    # for each file, rename filename
    for file_name in file_list:

        new_filename = file_name.replace(old, new)

        print("Old Name - " + file_name,end=" --> ")
        os.rename(src_dir + "/" + file_name, dest_dir + "/" + new_filename)
        print("New Name - " + new_filename)
        
    #os.chdir(saved_path)




source_directory = ""
dest_directory = ""

old = "" 
new = ""

old = str(sys.argv[1])
new = str(sys.argv[2])

try:
    source_directory = str(sys.argv[3])
except:
    print("No source directory specified. Using current working directory as source directory.")
    source_directory = os.getcwd()

try:
    dest_directory = str(sys.argv[4])
except:
    print("No destination directory specified. Using source directory as destination directory.")
    dest_directory = source_directory


rename_files(old, new, source_directory, dest_directory)
print("input format:   pythonfile.py old new source_directory destination_directory")
# example: .\File_rename-old-new-src-dest.exe "04" "07" "D:\ExtraFiles\Files"

# pyinstaller --onefile -w 'filename.py'pip 
# python -m PyInstaller  script.py

