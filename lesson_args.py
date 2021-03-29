import sys
import os


x = len(sys.argv)

if x > 1:
    if sys.argv[1] == "/?":
        print("HELP")
        print(")")
    print("Arguments: " + str(sys.argv[1:]))
else:
    print("there is no args")


os.system("dir > file.txt")

sys.exit(2)