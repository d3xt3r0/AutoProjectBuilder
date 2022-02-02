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

    #Print the detatils back to the user

    print("### PROJECT DETAILS ###")
    print(f"Project Name : {project_name}")
    print(f"Author : {project_author}")
    print(f"Project Description : {project_desc}")



if __name__ == "__main__":

    init()