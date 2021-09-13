colorSet = True

PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
DBLUE = "\033[1;34m"
GREEN = '\033[92m'
DGREEN = "\033[0;32m"
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

def noColors(toggler):
    global colorSet
    global PURPLE
    global CYAN
    global DARKCYAN
    global BLUE
    global DBLUE
    global GREEN
    global DGREEN
    global YELLOW
    global RED
    global BOLD
    global UNDERLINE
    global END
    if toggler == "True":
        colorSet = True
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        DBLUE = "\033[1;34m"
        GREEN = '\033[92m'
        DGREEN = "\033[0;32m"
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'
    else:
        print("     All colors turned off!")
        colorSet = False
        PURPLE = ''
        CYAN = ''
        DARKCYAN = ''
        BLUE = ''
        DBLUE = ""
        GREEN = ''
        DGREEN = ""
        YELLOW = ''
        RED = ''
        BOLD = ''
        UNDERLINE = ''
        END = ''
