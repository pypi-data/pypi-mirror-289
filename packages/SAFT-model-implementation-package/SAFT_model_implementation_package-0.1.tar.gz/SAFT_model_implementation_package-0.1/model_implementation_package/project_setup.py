
import os

def greeeetings():
    print("Hello from project setup!")

def setup_project_structure():
    # get relevant information 
    project_name = input("Enter the project name: ")

    # make project structure
    try:
        os.makedirs(project_name)
        print(f"Directory '{project_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{project_name}' already exists.")

    model_file_path = os.path.join(project_name, 'model.py')
    
    with open(model_file_path, 'w') as model_file:
        model_file.write("# model.py\n")
        print(f"File 'model.py' created successfully in '{project_name}'.")