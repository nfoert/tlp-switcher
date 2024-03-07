import colorama

COLOR_BLACK = colorama.Fore.BLACK
COLOR_BLUE = colorama.Fore.BLUE
COLOR_CYAN = colorama.Fore.CYAN
COLOR_GREEN = colorama.Fore.GREEN
COLOR_MAGENTA = colorama.Fore.MAGENTA
COLOR_RED = colorama.Fore.RED
COLOR_WHITE = colorama.Fore.WHITE
COLOR_YELLOW = colorama.Fore.YELLOW
COLOR_RESET = colorama.Fore.RESET

NERD_FONTS = True

if NERD_FONTS:
    SYMBOL_CHECK = ""
    SYMBOL_X = ""
    SYMBOL_LOADING = "󱍸"
    SYMBOL_WARNING = ""
    SYMBOL_STAR = ""

else:
    SYMBOL_CHECK = "✔"
    SYMBOL_X = "✘"
    SYMBOL_LOADING = "ⵔ"
    SYMBOL_WARNING = "⚠"
    SYMBOL_STAR = "☆"

DEFAULT_CONFIG = {
        "tlp_conf_path": "/etc/tlp.conf",
    }

MESSAGE_WELCOME = f'''
{COLOR_GREEN}tlp-switcher{COLOR_RESET} by {COLOR_MAGENTA}nfoert{COLOR_RESET}
    - {COLOR_CYAN}github.com/nfoert/tlp-switcher{COLOR_RESET}
'''

MESSAGE_HELP = f'''
Avaliable commands:
    - list
    - add
    - set
    - remove
    - help

{COLOR_YELLOW}list{COLOR_RESET}
    List all profiles avaliable to use

{COLOR_YELLOW}add <name>{COLOR_RESET}
    Save a new profile using the current tlp configs

{COLOR_YELLOW}set <name>{COLOR_RESET}
    Set the current profile to one that you've already created

{COLOR_YELLOW}remove <name>{COLOR_RESET}
    Delete a saved profile

{COLOR_YELLOW}help{COLOR_RESET}
    Display this message


First, you'll want to modify your tlp configs to match a profile you'd like to create
Then, use {COLOR_MAGENTA}tlp-switcher add <name>{COLOR_RESET} to save that profile
You can use {COLOR_MAGENTA}tlp-switcher set <name>{COLOR_RESET} to switch to that profile at any time
And use {COLOR_MAGENTA}tlp-switcher list{COLOR_RESET} to list all saved profiles
Then, you can use {COLOR_MAGENTA}tlp-switcher remove <name>{COLOR_RESET} to remove that profile
'''

MESSAGE_HOW_TO_HELP = f'''
You can use {COLOR_MAGENTA}tlp-switcher help{COLOR_RESET} for help
'''

MESSAGE_COMMAND_NOT_FOUND = f"{COLOR_RED}{SYMBOL_X} That command is not found!{COLOR_RESET}"