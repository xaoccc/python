import os


def find_extensions(dir_name, first_level=False):
    # Traverse all files and folders in the directory
    for file_folder in os.listdir(dir_name):
        # Store full path in a variable and check if this is a file or a folder
        file = os.path.join(dir_name, file_folder)
        if os.path.isfile(file):
            # If it is file, we store it in a dictionary
            if file_folder.split(".")[-1] not in filenames:
                filenames[file_folder.split(".")[-1]] = []
            filenames[file_folder.split(".")[-1]].append(file_folder)
        # If the file/folder is directory, we call the function recursively for each sub-folder
        # if we need several levels down, we write first_level + 1 when calling the function recursively
        # and define parameter first_level when creating the function, the recursion ends when first_level==n
        # where n is the number of levels down we have to search
        # Remove "and not first_level" if you want to find all files in all sub-folders
        elif os.path.isdir(file) and not first_level:
            find_extensions(file, first_level=True)


filenames = {}
result = ""
find_extensions(input("Enter dir name (./ for current dir): "))

filenames = dict(sorted(filenames.items(), key=lambda x: x[0]))

for extension, filename in filenames.items():
    filenames[extension] = sorted(filename)
    result += f".{extension}\n"
    for i in filename:
        result += f"- - - {i}\n"

with open("report.txt", "w") as log:
    log.write(result)