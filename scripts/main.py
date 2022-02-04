import os
from posixpath import abspath
import sys
from jinja2 import Template

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
    template_path = os.path.abspath("../templates/README.md.template")

    rendered_readme = load_template(template_path,
    {
        "project_name" : project_name,
        "author_name" : project_author
    }
    )
    
    if create_file(readme_filename, rendered_readme):
        print(f" > README.md created at {readme_filename}\n")
    else:
        sys.exit(" ** The file already exists")

    #Create the TODO.md file and main.py file

    filename = abs_path + "\TODO.md"
    template_path = os.path.abspath("../templates/TODO.md.template")

    rendered = load_template(template_path,
    {
        "project_name" : project_name
    }
    )
    
    if create_file(filename, rendered):
        print(f" > TODO.md created at {filename}\n")
    else:
        sys.exit(" ** The file already exists")


    filename = abs_path + "\main.py"
    template_path = os.path.abspath("../templates/main.py.template")

    rendered = load_template(template_path,
    {
        "project_name" : project_name
    }
    )
    
    if create_file(filename, rendered):
        print(f" > main.py created at {filename}\n")
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

def load_template(template_loc,params):

    '''
    Loads the template and render it with the params and returns the string
    '''

    rendered_string = ""
    with open(template_loc,'r') as f:

        temp = Template(f.read())
        rendered_string = temp.render(params)

    return rendered_string

if __name__ == "__main__":

    init()