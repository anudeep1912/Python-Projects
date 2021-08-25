from pathlib import Path
import os

print(str(Path('spam', 'bacon', 'eggs')))  # Path forms a path with the given arguments
Path('spam') / 'bacon' / 'eggs'            # / operator can be used to join paths just as in '+' for strings
# / evaluates from left to right do the first expression should be a path object

Path.cwd()  # Gives the current working directory
os.chdir('C:\\Windows\\System32')    # changes the current working directory

Path.home()    # Gives the home directory
os.makedirs('E:\\delicious\\walnut\\waffles')    # Creates the directories
Path(r'C:\Users\Al\spam').mkdir()                # Creates a directory

Path.cwd().is_absolute()    # Returns True if the path given is a absolute path
os.path.abspath('path')     # will return a string of the absolute path of the argument

os.path.isabs(path)         # will return True if the argument is an absolute path and False if it is a relative path.
os.path.relpath(path, start)    # will return a string of a relative path from the start path to path.\
#                               # If start is not provided, the current working directory is used as the start \
#                               # path.


p = Path('C:/Users/Al/spam.txt')
p.parent    # # This is a Path object, not a string. remaining all are strings
p.anchor    # C:/
p.name      # spam.txt
p.stem      # spam
p.suffix    # .txt
p.drive     # C:

os.path.getsize(path)    # will return the size in bytes of the file in the path argument
os.listdir(path)         # will return a list of filename strings for each file in the path argument. (Note that this function is in the os module, not os.path.)

p = Path('C:/Users/Al/Desktop')
list(p.glob('*'))        # glob is a special method on a path object. it returns a generator which needs to be given to a list.

p.glob('*.txt')              # Here * stands for multiples of any character with extension of text.
p.glob('tex?.txt')           # Here ? matches exactly one character.

p.exists()                # p is a path object. returns True if the path exists or returns False if it doesn’t exist.
p.is_file()               # returns True if the path exists and is a file, or returns False otherwise.
p.is_dir()                # returns True if the path exists and is a directory, or returns False otherwise.


helloFile = open(Path.home() / 'hello.txt', 'r')  # open opens the file and it only takes path objects as input and returns a file object
helloContent = helloFile.read()              # will return the contents as one long string
helloContentLine = helloFile.readlines()     # will give a list containing all lines.
open(Path.home(), 'w')      # r mode for read only, w for write mode replaces existing and a for append mode.
helloFile.close()           # closes the file

