from tabnanny import check


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
    project_name = check_project_name(project_name)


    #Print the detatils back to the user
    print("### PROJECT DETAILS ###")
    print(f"Project Name : {project_name}")
    print(f"Author : {project_author}")
    print(f"Project Description : {project_desc}")


def check_project_name(name):

    for char in name:
        if not char.isalnum():
            if char == '-':
                continue
            else:
                print(f" > The character {char} is not supported")
                print(" > Please enter new project name")
                name = check_project_name(input())
                break
    return name



if __name__ == "__main__":

    init()