import random
import string
from typing import Optional, Literal


def f_up(txt: str):
    """Capitalize first letter of string"""
    return txt[0].upper() + txt[1:]


Case = Literal['upper', 'lower', 'both']


def ascii_code(length: Optional[int] = 6,
               case: Optional[Case] = 'both',
               digits: Optional[bool] = True
               ):
    pools = {
        'both': string.ascii_letters,
        'lower': string.ascii_lowercase,
        'upper': string.ascii_uppercase
    }
    return ''.join(random.choices(pools[case] + string.digits if digits else [], k=length))


class TextColor:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

