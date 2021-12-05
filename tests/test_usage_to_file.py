from ofdata.ofdata import load_runTimeSelect, load_class_description


d_rs = load_runTimeSelect()
d_cd = load_class_description()

# print(d_rs["functionObject"])

print(d_cd["probes"]["Description"])
print(d_cd["probes"]["Usage"])#,end='\n')
with open("forces.txt","w") as f:
    f.write(d_cd["forces"]["Usage"])