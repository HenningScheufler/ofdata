import os, re
from pathlib import Path
import json

def read_file(f_path):
    with open(f_path,"r") as f:
        return f.readlines()


def get_classes(expression):
    # make one line
    str = expression.replace(' ','')
    str = str.replace('\n','')
    str = str.replace('\t','')

    #find arguements
    str_args = str[str.find("(")+1:str.find(")")]
    args = str_args.split(",")
    return args[0], args[1]

def find_keyword(keyword):
    return re.compile(r"\b{}\b(?!\.)".format(keyword))

def classify_keyword(lines,runTimeSelectionDict,keyword):
    match = find_keyword(keyword)
    foundTable = False
    flat_expression = ""
    for l in lines:

        if foundTable:
           flat_expression += l
           if ";" in l:
               foundTable=False

        if match.search(l):
            flat_expression += l
            foundTable=True
            if ";" in l:
               foundTable=False
    
    found = flat_expression != ""
    if found:
        cls_base, cls_dervied = get_classes(flat_expression)
        if cls_base not in runTimeSelectionDict:
            runTimeSelectionDict[cls_base] = []
        runTimeSelectionDict[cls_base].append(cls_dervied)
  
    return found


# traverse root directory, and list directories as dirs and files as files
count_runtime_sel = 0
all_cfiles = 0
runTimeSelectionDict = {}
for root, dirs, files in os.walk("src"):
    # if (Path(files).suffix == '.C'):
    for file in files:
        if (Path(file).suffix == '.C' and "lnInclude" not in root):
            all_cfiles += 1
            f_path = os.path.join(root,file)
            lines = read_file(f_path)
            
            classify_keyword(lines,runTimeSelectionDict,"addToRunTimeSelectionTable")
            classify_keyword(lines,runTimeSelectionDict,"makePatchTypeField")
            classify_keyword(lines,runTimeSelectionDict,"addNamedToRunTimeSelectionTable")


print("count_runtime_sel",count_runtime_sel)
print("all_cfiles",all_cfiles)
print(runTimeSelectionDict)


with open('runTimeSelectionDict.json', 'w') as fp:
    json.dump(runTimeSelectionDict, fp,indent=4)
