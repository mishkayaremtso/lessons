import re

inputf = "file.txt"
result = "result.txt"


inpf = open(inputf, mode='r', encoding='Latin-1')
resultfile = open(result, mode='w', encoding='Latin-1')
text = inpf.read()

lookfor = r"[\w.-]+@(?!tortordic)[A-Za-z-]+\.[\w.]+"

results = re.findall(lookfor, text)

for item in results:
    print(item)

print("Len: " + str(len(results)))