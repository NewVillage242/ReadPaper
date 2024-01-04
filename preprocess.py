import os
from dotenv import load_dotenv
from pathlib import Path

def remove_inference(line: str):
    while True:
        left = line.find("[")
        if left == -1:
            break
        right = line.find("]")
        if right == -1:
            break
        line = line[:left] + line[right+1:]

    return line

def remove_parentheses(line):
    #TODO : finish this function
    return line

load_dotenv()

file_path = Path(os.getenv('INPUT')) / os.getenv('ARTICLE')
file_folder : Path = file_path / "raw"
file_folder.mkdir(parents=True, exist_ok=True)
file_folder : Path = file_path / "processed"
file_folder.mkdir(parents=True, exist_ok=True)
files = os.listdir(Path(file_path) / "raw")

for subpath in files:
    with open( Path(file_path) /"processed"/subpath  , "w" ) as output_file:
        with open(Path(file_path) /"raw"/subpath, "r") as input_file:
            processed_line = ""
            for line in input_file:
                processed_line += line
            processed_line = processed_line.replace("\n", "")
        processed_line = remove_inference(processed_line)
        output_file.write(processed_line)