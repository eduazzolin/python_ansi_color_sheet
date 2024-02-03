class Colors:
    # Variables for ANSI escape codes for font colors
    F_RED = '\033[38;2;255;0;0m'
    F_GREEN = '\033[38;2;0;255;0m'
    F_BLUE = '\033[38;2;0;0;255m'
    F_YELLOW = '\033[38;2;255;255;0m'
    F_PURPLE = '\033[38;2;128;0;128m'
    F_ORANGE = '\033[38;2;255;165;0m'
    F_CYAN = '\033[38;2;0;255;255m'
    F_PINK = '\033[38;2;255;192;203m'
    F_BROWN = '\033[38;2;139;69;19m'
    F_GRAY = '\033[38;2;128;128;128m'
    F_BLACK = '\033[38;2;0;0;0m'
    F_WHITE = '\033[38;2;255;255;255m'
    F_MAROON = '\033[38;2;128;0;0m'
    F_OLIVE = '\033[38;2;128;128;0m'
    F_TEAL = '\033[38;2;0;128;128m'
    F_NAVY = '\033[38;2;0;0;128m'
    F_SILVER = '\033[38;2;192;192;192m'
    F_GOLD = '\033[38;2;255;215;0m'
    F_INDIGO = '\033[38;2;75;0;130m'
    F_ORCHID = '\033[38;2;218;112;214m'
    F_DARKGREEN = '\033[38;2;0;100;0m'
    F_TURQUOISE = '\033[38;2;64;224;208m'
    F_FIREBRICK = '\033[38;2;178;34;34m'
    F_SEASHELL = '\033[38;2;255;245;238m'

    # Variables for ANSI escape codes for background colors
    B_RED = '\033[48;2;255;0;0m'
    B_GREEN = '\033[48;2;0;255;0m'
    B_BLUE = '\033[48;2;0;0;255m'
    B_YELLOW = '\033[48;2;255;255;0m'
    B_PURPLE = '\033[48;2;128;0;128m'
    B_ORANGE = '\033[48;2;255;165;0m'
    B_CYAN = '\033[48;2;0;255;255m'
    B_PINK = '\033[48;2;255;192;203m'
    B_BROWN = '\033[48;2;139;69;19m'
    B_GRAY = '\033[48;2;230;230;230m'
    B_BLACK = '\033[48;2;0;0;0m'
    B_WHITE = '\033[48;2;255;255;255m'
    B_MAROON = '\033[48;2;128;0;0m'
    B_OLIVE = '\033[48;2;128;128;0m'
    B_TEAL = '\033[48;2;0;128;128m'
    B_NAVY = '\033[48;2;0;0;128m'
    B_SILVER = '\033[48;2;192;192;192m'
    B_GOLD = '\033[48;2;255;215;0m'
    B_INDIGO = '\033[48;2;75;0;130m'
    B_ORCHID = '\033[48;2;218;112;214m'
    B_DARKGREEN = '\033[48;2;0;100;0m'
    B_TURQUOISE = '\033[48;2;64;224;208m'
    B_FIREBRICK = '\033[48;2;178;34;34m'
    B_SEASHELL = '\033[48;2;255;245;238m'

    # Variables for ANSI escape codes for text effects
    E_ITALIC = '\033[3m'
    E_BOLD = '\033[1m'
    E_UNDERLINE = '\033[4m'
    E_BLINK = '\033[5m'
    E_REVERSE = '\033[7m'
    RESET = '\033[0m'


if __name__ == '__main__':
    backgounds = [i for i in dir(Colors) if i.startswith("B_")]
    font_colors = [i for i in dir(Colors) if i.startswith("F_")]
    effects = [i for i in dir(Colors) if i.startswith("E_")]

    print("\n-------------------\nBackgrounds:")
    for i in backgounds:
        print(f"{getattr(Colors, i)}{i}{Colors.RESET}")

    print("\n-------------------\nFont colors:")
    for i in font_colors:
        print(f"{getattr(Colors, i)}{i}{Colors.RESET}")

    print("\n-------------------\nEffects:")
    for i in effects:
        print(f"{getattr(Colors, i)}{i}{Colors.RESET}")
