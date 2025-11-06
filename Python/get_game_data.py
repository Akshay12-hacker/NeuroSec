import os
import json
import shutil
from subprocess import PIPE, run
import sys


GAME_DIR_PATTERN = "game"

def find_all_game_dirs(source):
    pass


def main(source, target):
    pwd = os.getcwd()
    source_path = os.path.join(pwd, source)
    target_path = os.path.join(pwd, target)


if __name__ == "__main__": # Only Run the Main file 
    args = sys.argv 
    if len(args) != 3:
        raise Exception("Usage: python get_game_data.py <input_file> <output_directory>")
    
    source, target = args[1:]
    main(source, target)
        
