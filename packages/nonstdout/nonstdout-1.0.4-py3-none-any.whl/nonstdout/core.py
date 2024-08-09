import time
import threading
from colorama import *
from getpass import getpass

def clear() -> None: 
    '''
Clears the terminal screen.
    '''
    print("\033[H\033[2J\033[3J", end="")

def pause(prompt: str | None = "Press Enter to continue...") -> None:
    '''
Pauses execution until Enter is pressed.

prompt
  the text to display as the prompt, default "Press Enter to continue..."
    '''
    getpass(prompt)

def printd(*values: object, sep: str | None = " ", end: str | None = "\n", file: str | None = None, flush: bool = False) -> None:
    '''
Prints the values to a stream, or to sys.stdout by default.

Text is shown usually in some sort of grey, technically BLACK.

sep
  string inserted between values, default a space.
end
  string appended after the last value, default a newline.
file
  a file-like object (stream); defaults to the current sys.stdout.
flush
  whether to forcibly flush the stream.
    '''
    content = Fore.BLACK
    for value in values:
        content += value
        content += " " if values[::-1][0] != value else Fore.RESET
    print(content, sep=sep, end=end, file=file, flush=flush)

def printe(*values: object, sep: str | None = " ", end: str | None = "\n", file: str | None = None, flush: bool = False) -> None:
    '''
Prints the values to a stream, or to sys.stdout by default.

Text is shown in RED.

sep
  string inserted between values, default a space.
end
  string appended after the last value, default a newline.
file
  a file-like object (stream); defaults to the current sys.stdout.
flush
  whether to forcibly flush the stream.
    '''
    content = Fore.RED
    for value in values:
        content += value
        content += " " if values[::-1][0] != value else Fore.RESET
    print(content, sep=sep, end=end, file=file, flush=flush)

def printw(*values: object, sep: str | None = " ", end: str | None = "\n", file: str | None = None, flush: bool = False) -> None:
    '''
Prints the values to a stream, or to sys.stdout by default.

Text is shown in YELLOW.

sep
  string inserted between values, default a space.
end
  string appended after the last value, default a newline.
file
  a file-like object (stream); defaults to the current sys.stdout.
flush
  whether to forcibly flush the stream.
    '''
    content = Fore.YELLOW
    for value in values:
        content += value
        content += " " if values[::-1][0] != value else Fore.RESET
    print(content, sep=sep, end=end, file=file, flush=flush)

def prints(*values: object, sep: str | None = " ", end: str | None = "\n", file: str | None = None, flush: bool = False) -> None:
    '''
Prints the values to a stream, or to sys.stdout by default.

Text is shown in GREEN.

sep
  string inserted between values, default a space.
end
  string appended after the last value, default a newline.
file
  a file-like object (stream); defaults to the current sys.stdout.
flush
  whether to forcibly flush the stream.
    '''
    content = Fore.GREEN
    for value in values:
        content += value
        content += " " if values[::-1][0] != value else Fore.RESET
    print(content, sep=sep, end=end, file=file, flush=flush)

def load(count: int, block: str | None = f"{Back.WHITE} {Back.RESET}", nada: str | None = " ", beg: str | None = "", end: str | None = "", pause: float | None = 0.1):
    '''
Creates a loading bar with specified text.

count
  number of blocks to load, required parameter
block
  the character to use as the block, default solid white box
nada
  the character to use as the lack of a block, default whitespace
beg
  what to put before the loading bar, e.g. "loading [", default nothing
end
  what to put after the loading bar, e.g. "]", default nothing
pause
  how long to wait in seconds before loading the next block, default 0.1
    '''
    blocks = ""
    nadacount = count
    blockcount = 0
    for _ in range(count):
        blocks += nada
    print(f"{beg}{blocks}{end}", end="\r")
    for _ in range(count):
        blocks = ""
        nadacount -= 1
        blockcount += 1
        for _ in range(blockcount): 
            blocks += block
        for _ in range(nadacount): 
            blocks += nada
        print(f"{beg}{blocks}{end}", end="\r")
        time.sleep(pause)
    print(f"{beg}{blocks}{end}")

spinner_active = False
spinner_thread = None

def start_spinner(symbols: list[str] | None = ["|", "/", "-", "\\"], before_text: str | None = "", after_text: str | None = ""):
    '''
Creates a loading spinner that lasts forever until stopped.

symbols
  the symbols that the spinner goes through to animate, default spinner
finished_symbol
  the symbol that shows up when the spinner is done, default ✓
before_text
  what to put before the spinner, e.g. "loading... [", default nothing
after_text
  what to put after the spinner, e.g. "]", default nothing
    '''
    global spinner_active, spinner_thread

    spinner_active = True

    def spin():
        elapsed = 0
        while spinner_active:
            print(f"{before_text}{symbols[int((elapsed * 10) % len(symbols))]}{after_text}", end="\r")
            elapsed += 0.1
            time.sleep(0.1)

    spinner_thread = threading.Thread(target=spin)
    spinner_thread.start()

def stop_spinner(finished_symbol: str | None = "✓", before_text: str | None = "", after_text: str | None = ""):
    '''
Stops the currently running spinner, if any.
Note: for the best results, use the same parameters you put on the start_spinner function, if any.

finished_symbol
  the symbol that shows up when the spinner is done, default ✓
before_text
  what to put before the spinner, e.g. "loading... [", default nothing
after_text
  what to put after the spinner, e.g. "]", default nothing
    '''
    global spinner_active, spinner_thread

    spinner_active = False
    if spinner_thread:
        spinner_thread.join()
        print(f"{before_text}{finished_symbol}{after_text}")