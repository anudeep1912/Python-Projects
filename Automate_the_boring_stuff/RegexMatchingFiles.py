#! python3
from pathlib import Path
import re

phone_numbers_reg = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

file = open(Path.cwd()/'dummy.txt', 'a+')
file.seek(0)
content = file.read()
phoneNumbers = phone_numbers_reg.findall(content)
print(phoneNumbers)
matches = []
for groups in phoneNumbers:
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

print(matches)

