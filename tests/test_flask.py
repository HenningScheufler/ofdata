from flask import Flask, render_template, request, render_template_string
from ofdata.ofdata import load_runTimeSelect, load_class_description
app = Flask(__name__)

d_rs = load_runTimeSelect()
d_cd = load_class_description()

def parse_table(text):
    lines = text.split("\n")
    tableFound = False
    modl = ""
    for l in lines:
        if "\\endtable" in l:
            tableFound = False
            modl += "</table>\n"

        if tableFound:
            table = l.split("|")
            modl += "<tr>\n"
            for t in table:
                modl += f"<td>{t}</td>\n"
            modl += "</tr>\n"
        else:
            if "table" not in l:
                modl += f"{l}\n"

        if "\\table" in l:
            tableFound = True
            modl += "<table>\n"
    return modl

@app.route("/func/<string:functionObj>/", methods=['GET'])
def functionObj(functionObj):
    func_objs = d_rs["functionObject"]
    obj_desc = " "
    obj_use = " "
    if "Description" in d_cd[functionObj]:
        obj_desc = d_cd[functionObj]["Description"]
        obj_desc = parse_table(obj_desc)
        obj_desc = obj_desc.replace("\\verbatim","<pre><code>")
        obj_desc = obj_desc.replace("\\endverbatim","</code></pre>")
    if "Usage" in d_cd[functionObj]:
        obj_use = d_cd[functionObj]["Usage"]
        obj_use = parse_table(obj_use)
        print(obj_use)
        obj_use = obj_use.replace("\\verbatim","<pre><code>")
        obj_use = obj_use.replace("\\endverbatim","</code></pre>")


    return render_template('test.html', func_objs=func_objs,obj_desc=obj_desc,obj_use=obj_use)
  

@app.route('/select_table/<table>', methods=['GET', 'POST'])
def select_table(table):
    return table

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)