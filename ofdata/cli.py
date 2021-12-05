"""Console script for ofdata."""
import argparse
import sys
import json
import os
from pathlib import Path
from ofdata.ofdata import *

def main():
    """Console script for ofdata."""
    parser = argparse.ArgumentParser()
    parser.add_argument("of",help='openfoam path')
    args = parser.parse_args()

    print("Arguments: " + str(args.of))
    # traverse root directory, and list directories as dirs and files as files
    count_runtime_sel = 0
    all_cfiles = 0
    runTimeSelectionDict = {}
    for root, dirs, files in os.walk(os.path.join(args.of,"src")):
        # if (Path(files).suffix == '.C'):
        for file in files:
            if (Path(file).suffix == '.C' and "lnInclude" not in root):
                all_cfiles += 1
                f_path = os.path.join(root,file)
                lines = read_file(f_path)
                
                classify_keyword(lines,runTimeSelectionDict,"addToRunTimeSelectionTable")
                classify_keyword(lines,runTimeSelectionDict,"makePatchTypeField")
                classify_keyword(lines,runTimeSelectionDict,"addNamedToRunTimeSelectionTable")
    
    json_path = os.path.join(Path(__file__).parent,'data','runTimeSelectionDict.json')

    print("json_path",json_path)
    with open(json_path, 'w') as fp:
        json.dump(runTimeSelectionDict, fp,indent=4)

    headers = []
    class_desc = {}
    for k, classes in runTimeSelectionDict.items():
        for cls in classes:
            headers.append(f"{cls}.H")

    for root, dirs, files in os.walk(os.path.join(args.of,"src")):
        for file in files:
            if (file in headers and "lnInclude" not in root):
                f_path = os.path.join(root,file)
                lines = read_file(f_path)
                comment_block = find_block(lines)
                comment = category_comments(comment_block)
                class_desc[file[:-2]] = comment


    json_path = os.path.join(Path(__file__).parent,'data','class_description.json')

    print("json_path",json_path)
    with open(json_path, 'w') as fp:
        json.dump(class_desc, fp,indent=4)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
