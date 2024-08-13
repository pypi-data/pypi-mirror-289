import sys
from typing import Callable, Dict, List, Optional, Union

# Import literal type for different versions of Python.
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

from .chars import CHARS

# Colors class.
from .color import color
c = color

# Styling function.
from .utils import style

# Quick styles.
s: Callable[[str, bool], str] = style('s')
d: Callable[[str, bool], str] = style('d')
i: Callable[[str, bool], str] = style('i')
u: Callable[[str, bool], str] = style('u')
k: Callable[[str, bool], str] = style('k')
h: Callable[[str, bool], str] = style('h')
x: Callable[[str, bool], str] = style('x')
du: Callable[[str, bool], str] = style('du')
rev: Callable[[str, bool], str] = style('rev')

# Quick colors.
r: Callable[[str, bool], str] = style('r')
g: Callable[[str, bool], str] = style('g')
y: Callable[[str, bool], str] = style('y')
b: Callable[[str, bool], str] = style('b')
m: Callable[[str, bool], str] = style('m')
cy: Callable[[str, bool], str] = style('c')
w: Callable[[str, bool], str] = style('w')

def available() -> List[str]:
    """ Returns the available styles.

    Returns:
        List[str]: The available styles.
    """

    # Get the available styles.
    ints: Dict[int, str] = {v: '' for v in set(CHARS.values())}
    for sty in CHARS.keys():
        i: int = CHARS[sty]
        if i in ints.keys() and not ints[i]:
            ints[i] = sty
    
    return list(ints.values())

def color(r: int, g: int, b: int, type: Literal['fg', 'bg'] = 'fg') -> str:
    """ Returns the ANSI escape sequence for the given RGB color.
    
    Args:
        r (int): The red value.
        g (int): The green value.
        b (int): The blue value.
        type (str): The type of color. (defaults to 'fg')

    Returns:
        str: The ANSI escape sequence.
    """

    # Check if the type is valid.
    if type not in ['fg', 'bg']:
        raise ValueError("Type must be 'fg' (foreground) or 'bg' (background).")

    # Check if the RGB values are all integers.
    if not all(isinstance(v, int) for v in [r, g, b]):
        raise TypeError("RGB values must be integers.")
    
    # Check if the RGB values are in the range 0-255.
    if not all(0 <= v <= 255 for v in [r, g, b]):
        raise ValueError("RGB values must be in the range 0-255.")

    # Set the type.
    type_: Literal['38', '48'] = '38' if type == 'fg' else '48'
    
    # Generate the ANSI escape sequence.
    code: str = f'CODE{type_};2;{r};{g};{b}'
    
    return code

def prints(
    *values: object,
    s: Optional[Union[List[str], Callable[[str, bool], str]]] = None,
    sep: str = ' ',
    end: str = '\n',
    file = None,
    flush: bool = False
) -> None:
    """ Prints the given values with the given style. Sends the output to Python's print function.

    Args:
        *values (object): The values to print.
        s (Optional[Union[List[str], Callable[[str, bool], str]]]): The style to apply to the text. (defaults to None)
        sep [str]: The separator between the values. (defaults to " ")
        end [str]: The end character. (defaults to '\n')
        file: The file to write to. (defaults to None)
        flush (bool): Whether to flush the output. (defaults to False)
    """

    # Set the style to empty function.
    style_: Callable[[str, bool], str] = style()

    if not s:
        # No style was given.
        pass
    elif type(s) in [list, tuple, set, str]:
        # The style is an array.
        style_ = style(*s)
    elif callable(s):
        # The style is a function.
        style_ = s
    else:
        # Invalid style.
        raise TypeError('Style must be an array or a function.')

    # Apply the style.
    text: str = style_(sep.join([str(v) for v in values]), p=False)

    # Print the text.
    print(text, sep=sep, end=end, file=file, flush=flush)