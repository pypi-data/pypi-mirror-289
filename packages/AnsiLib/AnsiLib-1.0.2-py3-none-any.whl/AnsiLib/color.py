from typing import Callable
from .utils import style

class color:
    # Text colors.
    class t:
        k: Callable[[str, bool], str] = style('kt0')
        r: Callable[[str, bool], str] = style('rt0')
        g: Callable[[str, bool], str] = style('gt0')
        y: Callable[[str, bool], str] = style('yt0')
        b: Callable[[str, bool], str] = style('bt0')
        m: Callable[[str, bool], str] = style('mt0')
        c: Callable[[str, bool], str] = style('ct0')
        w: Callable[[str, bool], str] = style('wt0')
        d: Callable[[str, bool], str] = style('dt0')

    # Background colors.
    class b:
        k: Callable[[str, bool], str] = style('kb0')
        r: Callable[[str, bool], str] = style('rb0')
        g: Callable[[str, bool], str] = style('gb0')
        y: Callable[[str, bool], str] = style('yb0')
        b: Callable[[str, bool], str] = style('bb0')
        m: Callable[[str, bool], str] = style('mb0')
        c: Callable[[str, bool], str] = style('cb0')
        w: Callable[[str, bool], str] = style('wb0')
        d: Callable[[str, bool], str] = style('db0')

    # Bright text colors.
    class t_:
        k: Callable[[str, bool], str] = style('kt1')
        r: Callable[[str, bool], str] = style('rt1')
        g: Callable[[str, bool], str] = style('gt1')
        y: Callable[[str, bool], str] = style('yt1')
        b: Callable[[str, bool], str] = style('bt1')
        m: Callable[[str, bool], str] = style('mt1')
        c: Callable[[str, bool], str] = style('ct1')
        w: Callable[[str, bool], str] = style('wt1')

    # Bright background colors.
    class b_:
        k: Callable[[str, bool], str] = style('kb1')
        r: Callable[[str, bool], str] = style('rb1')
        g: Callable[[str, bool], str] = style('gb1')
        y: Callable[[str, bool], str] = style('yb1')
        b: Callable[[str, bool], str] = style('bb1')
        m: Callable[[str, bool], str] = style('mb1')
        c: Callable[[str, bool], str] = style('cb1')
        w: Callable[[str, bool], str] = style('wb1')