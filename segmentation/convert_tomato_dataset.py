import os
import shutil

def copy_files_with_extension(file_list_path, input_folder, new_folder, extension):
    # Read the list of filenames from the text file
    with open(file_list_path, 'r') as file:
        filenames = [line.strip() for line in file.readlines()]

    # Create the new folder if it doesn't exist
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    # Copy files with the chosen extension from the input_folder to the new_folder
    for filename in filenames:
        source_file = os.path.join(input_folder, filename + extension)
        if os.path.isfile(source_file):
            destination_file = os.path.join(new_folder, filename + extension)
            shutil.copy2(source_file, destination_file)
            print(f"Copied file: {filename}{extension}")

    print("File copying completed.")

# Example usage
file_list_path = '/mnt/SSD1TB/TACR_TREND/data/tomato_row/tomato360/v2.1/5-fold/fold-0/cut_2042x2042_train_coco.txt'  # Path to the text file containing filenames
input_folder = '/mnt/SSD1TB/TACR_TREND/data/tomato_row/tomato360/mask_2042x2042/'    # Path to the folder where the files are located
new_folder = '/mnt/SSD1TB/TACR_TREND/data/tomato_row/tomato360/segm/ann_dir/train/'        # Path to the folder where the files will be copied
extension = '.png'               # Extension for the files to be copied

copy_files_with_extension(file_list_path, input_folder, new_folder, extension)
