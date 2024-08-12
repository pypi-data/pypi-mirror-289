import sys
from .hamlang import HamLang

def main():
    if len(sys.argv) != 2:
        print("\nUsage: hamlang <filename.ham>\n")
        sys.exit(1)
    
    filename = sys.argv[1]
    with open(filename, "r", encoding="UTF-8") as file:
        if filename.endswith(r'.ham'):
            code = file.read()
        else:
            print("\nUsage: hamlang <filename.ham>")
            print("(Invalid FileExtension) hamlang only read '.ham'\n")

            sys.exit(1)


    interpreter = HamLang()
    interpreter.compile(code)

if __name__ == "__main__":
    main()