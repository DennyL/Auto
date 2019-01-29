import os

path2source = "D:\\workflow\\source\\"
path2dest = "D:\workflow\dest\\"

files_in_source = os.listdir(path2source)
files_in_dest = os.listdir(path2dest)

def main():
    '''
       renames files in one folder with names of
       the files in another folder if they have same IDs
    '''
    for name in files_in_source:
        name_id = name.partition(".")[0]
        print(name_id)
        for i in range(len(files_in_dest)):
            if name_id == files_in_dest[i].partition(".")[0]:
                new_file = os.path.join(path2source, (files_in_dest[i])[:-4] + " (μετάφραση).docx")
                old_file = os.path.join(path2source, name)
                print(old_file, "   --->   ", new_file)
                os.rename(old_file, new_file)
    print("Process is over")

main()
