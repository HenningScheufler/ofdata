#%%
from ofdata.ofdata import read_file, find_block, category_comments
import re, json
lines = read_file("forces.H")
# print(lines)
# def find_block(lines):
#     found_commentblock = False
#     startBlock = re.compile(r'\/\*-*\*\\')
#     endBlock = re.compile(r'\\\*-*\*\/')
#     comment_block = []
#     for l in lines:
#         if found_commentblock:
#             comment_block.append(l)

#         if startBlock.search(l):
            
#             found_commentblock = True

#         if endBlock.search(l):
#             break
    
#     return comment_block

# def find_keywords(lines):
#     comment = {}
#     keywords = re.compile(r'^[a-zA-Z]+')
#     last_keyword = ""
#     for l in lines:
#         if keywords.search(l):
#             comment[l.rstrip()] = ""
#             last_keyword = l.rstrip()
#             print("keywords",l.rstrip())
#         if last_keyword and last_keyword != l.rstrip():
#             comment[last_keyword] += l
#     return comment

comment_block = find_block(lines)
comment = category_comments(comment_block)
print(comment)
with open("test.json", 'w') as fp:
    json.dump(comment, fp,indent=4)

# %%
str ="forces.H"

print(str[:-2])
# %%
