import sys

infile = "keks.txt"

while True:
    try:
        print("inside TRY")
        myfile = open(infile, mode='r', encoding='ascii')
    except Exception:
        print("inside EXCEPT")
        print("Error found")
        print(sys.exc_info()[1])
        infile = input("Enter Correct file name : ")
    else:
        print("inside else")
        print(myfile.read())
        sys.exit()
    finally:
        print("inside FINALLY")









