import os
import zipfile
import shutil
import argparse

ALLOWED_EXTENSIONS = ['.cpp', '.c' ,'.py']
EXCLUDED_ITEMS = ['op.py', 'op2.py', '.DS_Store']

def extract_zip():
    current_directory = os.getcwd()
    for folder_name in os.listdir(current_directory):
        folder_path = os.path.join(current_directory, folder_name)
        if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                if file_name.endswith('.zip'):
                    zip_file_path = os.path.join(folder_path, file_name)
                    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                        zip_ref.extractall(folder_path)
                    print(f'Extracted {zip_file_path} to {folder_path}')


def filter_conditions(file_name, num_questions):
    for i in range(1, num_questions + 1):
        if (f"q{i}" in file_name or f"Q{i}" in file_name or f"_{i}" in file_name) and any(file_name.endswith(ext) for ext in ALLOWED_EXTENSIONS):
            return i - 1 
    return -1


def recursive_traverse(folder, num_questions):
    for each_folder in os.listdir(folder):
        full_path = os.path.join(folder, each_folder)
        if each_folder in folders or each_folder in EXCLUDED_ITEMS or each_folder.endswith('.zip'):
            continue
        elif os.path.isdir(full_path):
            recursive_traverse(full_path, num_questions)
        else:
            print("\t", each_folder)
            cat_folders = filter_conditions(each_folder, num_questions)
            if cat_folders != -1:
                target_folder = folders[cat_folders]
                target_path = os.path.join(target_folder, each_folder)  
                shutil.copy2(full_path, target_path)  


def main(no_of_questions):
    global folders
    global NO_OF_QUESTIONS
    NO_OF_QUESTIONS = no_of_questions
    
    folders = [f'q{i + 1}' for i in range(no_of_questions)]
    
    extract_zip()
    all_folders = os.listdir()
    
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
               
    for each_folder in all_folders:
        if each_folder in folders or each_folder in EXCLUDED_ITEMS:
            continue
        else:
            print("Folder Name: ", each_folder)
            recursive_traverse(each_folder, NO_OF_QUESTIONS)


def wrapper():
    parser = argparse.ArgumentParser(description='Extract Moodle files and organize them.')
    parser.add_argument('--noofqs', type=int, required=True, help='Number of questions')  # Make sure this is required
    args = parser.parse_args()

    if args.noofqs is None or args.noofqs <= 0:
        print("Please provide a valid number of questions greater than 0.")
    else:
        main(args.noofqs)
        
if __name__ == "__main__":
    wrapper()