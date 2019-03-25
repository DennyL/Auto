######################
#      RENAMER       #
# by Denys Lozinskyi #
######################
import os

"""
    NOTE! Source is a folder that containes files to be renamed with addition of "(translation)" word.
    Dest is a folder that contains files, names of which are being taken for renaming files in a source folder.
    Files in both the folders share corresponding IDs, like:
    \dest\21. Ivan Ivanov.pdf and \source\21. Иван Иванов.docx.
    Here the first is an original file and the second is the translation of the first.
    An output of the script is to make a pair of those files with the same name,
    marking the one that contains a translation:
    So that "21. Иван Иванов.docx" became "21. Ivan Ivanov (translation).docx",
    keeping an original extension of the file.
    NOTE! For correct output of the script the files MUST have same IDs separated from the rest of a name by a dot.
"""

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
        # initiating iteration over files in source folder
        # picking id of a file
        fractals_of_name = name.split(".")
        name_id = fractals_of_name[0]

        for i in range(len(files_in_dest)):
            # now, iterating over the files in dest folder to figure out,
            # if we have there a file with same id.
            if name_id == files_in_dest[i].split(".")[0]:
                # if a pair is found, extract an extension of the file to be renamed
                extension = fractals_of_name[-1]
                # and building its new name based on a name from dest folder
                # leaving aside its extension (because we need to preserve the original one)

                '''OPTIONS / ADJUSTMENTS'''
                ###new_file = os.path.join(path2source, files_in_dest[i].rpartition(".")[0] + " (translation)." + extension)
                ###new_file = os.path.join(path2source, files_in_dest[i].rpartition(".")[0] + " (original)." + extension)
                '''this one we use, if a name to rename with already containes "(original/translation)" part'''
                new_file = os.path.join(path2source, files_in_dest[i].rpartition(".")[0].split("(")[0] + "(original)." + extension)
                
                old_file = os.path.join(path2source, name)
                '''ENABLING RENAMING'''
                ####os.rename(old_file, new_file)
                print(old_file, "   --->   ", new_file)
                break
        else:
            # if a file with such ID was not found
            print("\nCannot find a pair for: " + name + "\n")
    print("Process is over")


if __name__ == '__main__':
    main()
