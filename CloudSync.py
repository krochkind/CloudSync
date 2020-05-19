import os
import pprint
import shutil

pp = pprint.PrettyPrinter(indent=2)

folder_name = "MyFolder"
source_dir = fr"D:\MySource\{folder_name}"
destination_dir = fr"D:\Dropbox\Destination\{folder_name}"

source_files = {}
destination_files = {}
differences = {}
num_files_coppied = 0

def copy_file(key):
    shutil.copy2(source_dir + key, destination_dir + key)
    return 1

for subdir, dirs, files in os.walk(source_dir):
    for file in files:
        filepath = subdir + os.sep + file
        modification_date = os.stat(filepath).st_mtime
        filepath = filepath.replace(source_dir, "")
        source_files[filepath] = modification_date

for subdir, dirs, files in os.walk(destination_dir):
    for file in files:
        filepath = subdir + os.sep + file
        modification_date = os.stat(filepath).st_mtime
        filepath = filepath.replace(destination_dir, "")
        destination_files[filepath] = modification_date

differences = source_files.items() - destination_files.items()

if len(differences) > 0:
    keys = [i[0] for i in differences]
    for key in keys:
        #print(source_dir + key + " -- to -- " + destination_dir + key)
        folder = key.rsplit('\\', 1)[0]
        file_name = key.rsplit('\\', 1)[1]
        
        if not os.path.exists(destination_dir + folder):
            os.makedirs(destination_dir + folder)

        if os.path.isfile(source_dir + key):
            if not file_name.startswith("~"):
                print("Updating {0}".format(source_dir + key))
                if ((key in destination_files) and (destination_files[key] > source_files[key])):
                    print("  The Destination is more recent than the Source.  Are you sure you want to overwrite? ", end="")
                    overwrite = input("[Y/N] ").upper()
                    if overwrite == "Y":
                        num_files_coppied += copy_file(key)
                else:
                    num_files_coppied += copy_file(key)

    plural = "s"
    if num_files_coppied == 1:
        plural = ""
    
    if num_files_coppied > 0:
        print("\nUpdated {0} file{1}".format(num_files_coppied, plural))
    else:
        print("No files to update")
else:
    print("No files to update")

prompt_quit = input('\nPress any key to quit... ')