import os
import json
import shutil
from subprocess import PIPE, run
import sys


GAME_DIR_PATTERN = "game"

def find_all_game_dirs(source):
    game_paths = []
    
    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)
        break
    return game_paths

def get_name_from_path(paths, to_strip):
    new_names = []
    for path in paths:
        _, dir_name = os.path.split(path)
        new_dir_name = dir_name.replace(to_strip, "")
        new_names.append(new_dir_name)
    return new_names


def create_directory(path):
    if not os.path.exists(path):
        os.mkdir(path)

def main(source, target):
    pwd = os.getcwd()
    source_path = os.path.join(pwd, source)
    target_path = os.path.join(pwd, target)

    game_paths = find_all_game_dirs(source_path)
    create_directory(target_path)
    new_game_dirs = get_name_from_path(game_paths, "_game")
    print(new_game_dirs)
    print(f"Found {len(game_paths)} game directories.")



if __name__ == "__main__": # Only Run the Main file 
    args = sys.argv 
    if len(args) != 3:
        raise Exception("Usage: python get_game_data.py <input_file> <output_directory>")
    
    source, target = args[1:]
    main(source, target)
        
