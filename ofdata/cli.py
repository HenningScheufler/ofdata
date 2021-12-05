"""Console script for ofdata."""
import argparse
import sys


def main():
    """Console script for ofdata."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
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
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
