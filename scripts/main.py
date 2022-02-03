import os
from posixpath import abspath
import sys

def init():
    '''
    Collect information from the user
    -Name
    -Author
    -Description
    '''


    project_name = input(" > What is the name of the project?\n")
    project_author = input(" > Who is the author of this project?\n")
    project_desc = input(" > How do you describe this project?\n")

    #Check if the project name contains illegal characters
    project_name = check_name(project_name)

    
    #Print the detatils back to the user
    print("\n\n > ### PROJECT DETAILS ###")
    print(f" > Project Name : {project_name}")
    print(f" > Author : {project_author}")
    print(f" > Project Description : {project_desc}")


    #Create the project folder
    
    dir_path = "../../" + project_name
    abs_path = os.path.abspath(dir_path)
    if create_dir(dir_path):
        print(f"\n\n > Project folder created at {abs_path}\n")
    else:
        sys.exit(" ** The folder already exists")

    #Create the README.md file

    readme_filename = abs_path + "\README.md"
    readme_content = f"# {project_name}\n\n## Description \n{project_desc}\n\n## How to install the project\n\nTODO\n\n## How to run the project\n\nTODO\n\n## Author\n\n{project_author}"
    if create_file(readme_filename, readme_content):
        print(f" > README.md created at {readme_filename}\n")
    else:
        sys.exit(" ** The file already exists")

def check_name(name):

    '''
    Check if the name contains any illegal characters
    '''

    for char in name:
        if not char.isalnum():
            if char == '-':
                continue
            else:
                print(f" > The character {char} is not supported")
                print(" > Please enter new project name")
                name = check_name(input())
                break
    return name

def create_dir(dir_path):

    '''
    To crete a directory in the name provided through the dir_path argument.

    '''
    #create dir

    try:
        os.mkdir(dir_path)
    except OSError as error:
        print(error)
        return False
    return True


def create_file(file_name, contents=""):

    try:
        with open(file_name, 'w') as f:
            f.write(contents)
    except FileExistsError as error:
        print(error)
        return False
    return True


if __name__ == "__main__":

    init()