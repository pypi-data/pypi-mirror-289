# NonStdOut
*(nonstandard output)*

by Sushii64

library for making printing cooler

haha get it

## Installation

Install using `pip` like so:
```bash
pip install nonstdout
```

Optionally, clone this repository in the folder of the project and import it locally:

```bash
git clone https://github.com/Sushii64/nonstdout
```

## Usage

Import everything from the library:

```python
from nonstdout import *
```

Each command in the library has docstrings, refer to those to learn how to use the library.

### Example Program

```python
from nonstdout import *

clear()

print("-- Text Styling --\n")

print("print()")
print("    normal text")
print("printd()")
printd("    debug text!")
print("printe()")
printe("    error text!")
print("printw()")
printw("    warning text!")
print("prints()")
prints("    success text!")

print()
pause()

clear()

print("-- Loading Bars --\n")

load(15, beg="loading - ")

pause()

load(12, "#", ".", "Loading... [", "]")

pause()

load(5, "O", "o", "im a ghost ", " >:3", 0.3)

pause()

clear()

print("-- Loading Spinners --\n")

spinner(5, before_text="loading ")

pause()

print()

spinner(3, before_text="downloading 'real' drivers ")
spinner(2, before_text="installing 'real' drivers ")
spinner(1, before_text="setting up images ")
spinner(4, before_text="crying in the corner ")
spinner(2, before_text="verifying 'real' drivers ")
spinner(2, before_text="finalising ")

pause()

clear()

print("All done!")
```