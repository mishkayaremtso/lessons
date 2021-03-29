import re

myText = "  Celeste| 2123 |justo.faucibus.lectus@duiCum.edu \
            Jayme| 2123|quis@quamvel.edu                             \
            Bryar| 2123|Nunc.ut.erat@pedePraesenteu.co.uk            \
            Zenia| 2123|sit@velitdui.net                              \
            Summer|2123|in.lobortis.tellus@arcuiaculisenim.ca       \
            Isabella|2123|Nam.interdum.enim@arcu.ca "
"""
\d = Any Digit 0-9
\D = Any NON digit
\w = Any alphabet symbol [A-Z, a-z]
\W = any non Alphabet symbol
\s = breakspace
\S = non breakspace

"""


textLookFor = r"@\w+\.\w+"
result = re.findall(textLookFor, myText)
print(result)
