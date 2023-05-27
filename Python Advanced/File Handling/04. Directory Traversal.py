import os


def find_extensions(dir_name, first_level=True):
    for file_folder in dir_name:
        if os.path.isfile(file_folder):
            if file_folder.split(".")[-1] not in filenames:
                filenames[file_folder.split(".")[-1]] = []
            filenames[file_folder.split(".")[-1]].append(file_folder)

        elif os.path.isdir(file_folder):
            sub_directory = os.listdir(f"./{file_folder}")
            for file in sub_directory:
                if "." in file:
                    if file.split(".")[-1] not in filenames:
                        filenames[file.split(".")[-1]] = []
                    filenames[file.split(".")[-1]].append(file)


filenames = {}
result = ""
directory = os.listdir(input("Enter dir name (./ for current dir): "))
find_extensions(directory)
for extension, filename in filenames.items():
    result += f".{extension}\n"
    for i in filename:
        result += f"- - - {i}\n"


with open("report.txt", "w") as log:
    log.write(result)