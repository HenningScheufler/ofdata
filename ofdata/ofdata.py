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

def find_block(lines):
    found_commentblock = False
    startBlock = re.compile(r'\/\*-*\*\\')
    endBlock = re.compile(r'\\\*-*\*\/')
    comment_block = []
    for l in lines:
        if endBlock.search(l):
            break

        if found_commentblock:
            comment_block.append(l)

        if startBlock.search(l):    
            found_commentblock = True

 
    
    return comment_block

def category_comments(lines):
    comment = {}
    keywords = re.compile(r'^[a-zA-Z]+')
    last_keyword = ""
    for l in lines:
        if keywords.search(l):
            comment[l.rstrip()] = ""
            last_keyword = l.rstrip()
        if last_keyword and last_keyword != l.rstrip():
            comment[last_keyword] += l
    comment.pop('License', None)
    return comment

def load_runTimeSelect():
    json_path = os.path.join(Path(__file__).parent,'data','runTimeSelectionDict.json')
    with open(json_path, 'r') as fp:
        runTime_dict = json.load(fp)
    return runTime_dict

def load_class_description():
    json_path = os.path.join(Path(__file__).parent,'data','class_description.json')
    with open(json_path, 'r') as fp:
        runTime_dict = json.load(fp)
    return runTime_dict