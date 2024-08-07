"""
**TensePy Extensions** \n
\\@since 0.3.24 \\
\\@author Aveyzan
```ts \\
module tense.extensions
```
Providing TensePy extensions, including `ANSIColor` and NennɅI classes. \\
This submodule imports `tense.primary` module.
"""
import sys

if sys.version_info < (3, 9):
    err, s = (RuntimeError, "Use 'tense_eight' module for Python versions below 3.9.")
    raise err(s)

import warnings, uuid, random
from tense.primary import *

from typing import Callable
import re

# between @since and @author there is unnecessarily long line spacing
# hence this warning is being thrown; it is being disabled.
filterwarnings("ignore", category = SyntaxWarning)

_var = TypeVar
_uni = Union
_lit = Literal
_opt = Optional
_cal = Callable
_cm = classmethod
_sm = staticmethod
_p = property

_T = _var("_T")
_T1 = _var("_T1")
_T2 = _var("_T2")
_T3 = _var("_T3")

_T_co = _var("_T_co", covariant = True)

_V1 = _var("_V1")
_V2 = _var("_V2")
_M = _var("_M")

_ColorType = tcs.ColorType[_T]
_ReckonNGT = tcs.ReckonNGT
_AbroadValue1 = _uni[tcs.AbroadValue1[_T], ModernString]
_AbroadValue2 = _uni[tcs.AbroadValue2[_T], ModernString]
_AbroadModifier = _uni[tcs.AbroadModifier[_T], ModernString]
_AbroadPackType = tcs.AbroadPackType[_T]
_AbroadConvectType = tcs.AbroadConvectType[_T]
_AbroadLiveType = tcs.AbroadLiveType[_T]
_AbroadVividType = tcs.AbroadVividType[_V1, _V2, _M]
_RandomizeType = tcs.PickSequence[_T]

_AbroadInitializer = tcs.AbroadInitializer[int]
_AbroadStringInitializer = tcs.AbroadInitializer[str]
_AbroadFloatyInitializer = tcs.AbroadInitializer[float]
_AbroadMultiInitializer = tcs.AbroadInitializer[tcs.AbroadInitializer[int]]
_AbroadImmutableInitializer = tuple[int, ...]
_AbroadIntFloatInitializer = list[_T]

def _disassign(self, array: list[_T], *items: _T):
    """Since 0.3.17, unavailable for 0.3.24"""
    a: list[_T] = []
    for i1 in abroad(array):
        for i2 in abroad(items):
            if array[i1] != items[i2]: a.append(array[i1])
    return a

class ANSIColor:
    """
    \\@since 0.3.24 \\
    \\@author Aveyzan
    ```ts \\
    in module tense.extensions
    ```
    This class is basing on ANSI escape code. Note that not only colorization \\
    is implemented here, there are also other font styles. For more read this \\
    article's description: https://en.wikipedia.org/wiki/ANSI_escape_code.

    Warning: all of its methods won't change any background or foreground \\
    color where `tkinter` and `livewires` are used. 
    """
    __local_changer = 24
    def __init__(self) -> None:
        pass
    @_sm
    def setBits(bits: _lit[3, 4, 8, 24] = 24, /):
        """
        \\@since 0.3.26a2 (in code since 0.3.25) \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class ANSIColor
        ```
        This static method simply bases on representative colors via ANSI 
        escape code: 3-bit and 4-bit (16 colors, 8 normal and 8 bright), 8-bit \\
        (256 colors) and 24-bit (16777216 colors). Values in brackets are allowed \\
        values. Default `bits` value is 24, what means you can use RGB color picker. \\
        Using tuple for other ones (16 and 256) is liable for errors, since code awaits
        3 items, hence you should use integer value instead. For 4-bit it would be: \\
        30-37 (normal) and 90-97 (bright) for foreground, 40-47 (normal) and 100-107 \\
        (bright) for background. In the code you will only need to specify either \\
        color name in string or one integer from range 1-16 (3-bit - 1-8).
        """
        if not isinstance(bits, int):
            err, s = (TypeError, "Parameter 'bits' is not an integer")
            raise err(s)
        elif bits not in (3, 4, 8, 24):
            err, s = (ValueError, "Parameter 'bits' does not have one of the following possible values: 3, 4, 8 and 24")
            raise err(s)
        ANSIColor.__local_changer = bits
        return __class__
    @_sm
    def toRgb(hex: str, /):
        """
        \\@since 0.3.24 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class ANSIColor
        ```
        Converts a hexadecimal string to RGB tuple. \\
        Issue patched on 0.3.26a2
        """
        HEX = "0123456789abcdef"
        if not isinstance(hex, str):
            err, s = (TypeError, "Parameter 'hex' is not a string")
            raise err(s)
        tmps = hex.lower()
        if tmps.startswith("0x"): tmps = re.sub(r"^0x", "", tmps)
        elif tmps.startswith("#"): tmps = re.sub(r"^#", "", tmps)
        for c in tmps:
            if c not in HEX:
                err, s = (ValueError, f"Passed string to parameter 'hex' isn't purely a hex string. Expected digits from range 0-9 and letters from range a-f, optionally preceded by 0x. Character, which led to this error: '{c}'")
                raise err(s)
        if reckon(tmps) != 6:
            err, s = (ValueError, "Expected hexadecimal string have 6 hexadecimal characters (from 0-9 and a-f). Case isn't sensitive")
            raise err(s)
        return tuple(int(tmps[i : i + 2], 16) for i in abroad(6, modifier = 2))
    @_sm
    def toHex(*integers: int, include_0x: _opt[bool] = True):
        """
        \\@since 0.3.24 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class ANSIColor
        ```
        Integers to hexadecimal format
        """
        HEX = "0123456789abcdef"
        for i in abroad(integers):
            if not isinstance(integers[i], int):
                err = TypeError
                s = f"One of passed integers in parameter 'integers' isn't an integer. Item at index '{i}' is not an integer"
                raise err(s)
            elif integers[i] < 0 or integers[i] > 255:
                err = ValueError
                s = f"One of passed integers in parameter 'integers' isn't an integer from range 0-255. Integer at index '{i}' led to this error; value: '{integers[i]}'"
                raise err(s)
        a: list[str] = []
        for i in abroad(integers):
            a.append(hex(integers[i]) if include_0x else hex(integers[i])[2:])
        return a
    @_sm
    def __local_inside_op(fbu: _ColorType[int], init: int = 0):
        paramName = ("foreground", "background", "underline")
        ret = ""
        if ANSIColor.__local_changer == 24:
            if init == 0: ret = "38;2;"
            elif init == 1: ret = "48;2;"
            elif init == 2: ret = "58;2;"
            if isinstance(fbu, int):
                # 0xffffff is 16777215; hex in CSS supports 6-char hex code if not counting opacity toggle
                if fbu < 0 or fbu > 16777215:
                    err, s = (ValueError, "For 24-bit colors expected integer value for 0 to 16777216.")
                    raise err(s)
                for e in ANSIColor.toRgb(fbu):
                    ret += f"{e};"
            elif isinstance(fbu, tuple):
                if reckon(fbu) != 3:
                    err, s = (ValueError, "Passed tuple does not have 3 items, ensure tuple has exactly 3 integer items.")
                    raise err(s)
                for e in fbu:
                    if not isinstance(e, int):
                        err = TypeError
                        s = f"One of tuple items in '{paramName[init]}' parameter isn't actually an integer. This item is of type '{type(e).__name__}'."
                        raise err(s)
                    elif e < 0 or e > 255:
                        err = ValueError
                        s = f"For 24-bit colors expected integer value for 0 to 16777216. Integer value of one of items of a tuple in '{paramName[init]}' parameter does not satisfy this requirement."
                        raise err(s)
                    ret += f"{e};"
            elif isinstance(fbu, str):
                for e in ANSIColor.toRgb(fbu):
                    ret += f"{e};"
            elif fbu is None: pass
            else:
                err = TypeError
                s = f"Invalid type of '{paramName[init]}' parameter: '{type(fbu).__name__}'. Expected either a hexadecimal string, an integer or an integer tuple with 3 items."
                raise err(s)
        elif ANSIColor.__local_changer == 8:
            if init == 0: ret = "38;5;"
            elif init == 1: ret = "48;5;"
            elif init == 2: ret = "58;5;"
            if isinstance(fbu, int):
                if fbu < 0 or fbu > 255:
                    err, s = (ValueError, "For 8-bit colors expected integer value for 0 to 255.")
                    raise err(s)
                ret += str(fbu)
            elif isinstance(fbu, str):
                try:
                    tmp = int(fbu)
                    if tmp < 0 or tmp > 255:
                        err, s = (ValueError, "For 8-bit colors expected integer value for 0 to 255.")
                        raise err(s)
                    ret += fbu
                except ValueError:
                    err, s = (ValueError, "Unsupported characters inside string.")
                    raise err(s)
            elif fbu is None: pass
            else:
                err, s = (TypeError, "For 8-bit colors expected an integer or string.")
                raise err(s)
        elif ANSIColor.__local_changer in (3, 4):
            if isinstance(fbu, int):
                if fbu >= 1 and fbu <= 8:
                    if init == 0: ret += str(fbu + 29)
                    elif init == 1: ret += str(fbu + 39)
                    else:
                        err, s = (ValueError, "Unsupported value or attempt to access colors via underline color identifier 58.")
                        raise err(s)
                elif fbu >= 9 and fbu <= 16:
                    if init == 0: ret += str(fbu + 89)
                    elif init == 1: ret += str(fbu + 109)
                    else:
                        err, s = (ValueError, "Unsupported value or attempt to access colors via underline color identifier 58.")
                        raise err(s)
                else:
                    err, s = (ValueError, "For 4-bit colors expected integer value for 1 to 16.")
                    raise err(s)
            elif isinstance(fbu, str):
                try:
                    tmp = int(fbu)
                    if tmp >= 1 and tmp <= 8:
                        if init == 0: ret += str(tmp + 29)
                        elif init == 1: ret += str(tmp + 39)
                        else:
                            err, s = (ValueError, "Unsupported value or attempt to access colors via underline color identifier 58.")
                            raise err(s)
                    elif tmp >= 9 and tmp <= 16:
                        if ANSIColor.__local_changer == 3:
                            err, s = (ValueError, "For 3-bit colors expected integer value for 1 to 8.")
                            raise err(s)
                        if init == 0: ret += str(tmp + 89)
                        elif init == 1: ret += str(tmp + 99)
                        else:
                            err, s = (ValueError, "Unsupported value or attempt to access colors via underline color identifier 58.")
                            raise err(s)
                    else:
                        err, s = (ValueError, "For 4-bit colors expected integer value for 1 to 16.")
                        raise err(s)
                except ValueError:
                    err, s = (ValueError, "Unsupported characters inside string.")
                    raise err(s)
            else:
                err, s = (TypeError, "For 3-, 4-bit colors expected an integer or string.")
                raise err(s)
        else:
            err, s = (ValueError, "Incorrect bits amount provided, expected: 3, 4, 8 or 24.")
            raise err(s)
        return ret
    @_sm
    def __local_invocation(id: int, string: str, /, foreground: _ColorType[int] = None, background: _ColorType[int] = None, underline: _ColorType[int] = None):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class ANSIColor
        ```
        """
        ret = f"\033[{id};"
        if not isinstance(string, str):
            err = TypeError
            s = f"Parameter 'string' is not a string. Ensure argument got value of type 'str'."
            raise err(s)
        if (
            (foreground is not None and underline is not None) or
            (foreground is not None and background is not None) or
            (background is not None and underline is not None)
        ):
            err = ValueError
            s = f"Only one parameters from these: 'background', 'foreground' and 'underline', may have non-empty value. Issue to be fixed in the future."
            raise err(s)
        else:
            if foreground is not None:
                ret += ANSIColor.__local_inside_op(foreground, 0)
            elif background is not None:
                ret += ANSIColor.__local_inside_op(background, 1)
            elif underline is not None:
                ret += ANSIColor.__local_inside_op(underline, 2)
            else:
                ret += "0;"
        ret = re.sub(r";$", "m", ret)
        return ret + string
    @_sm
    def normal(string: str, /, foreground: _ColorType[int] = None, background: _ColorType[int] = None, underline: _ColorType[int] = None):
        """
        \\@since 0.3.24 \\
        \\@modified 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class ANSIColor
        ```
        """
        return ANSIColor.__local_invocation(0, string, foreground = foreground, background = background, underline = underline)
    @_sm
    def bold(string: str, /, foreground: _ColorType[int] = None, background: _ColorType[int] = None, underline: _ColorType[int] = None):
        """
        \\@since 0.3.24 \\
        \\@modified 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class ANSIColor
        ```
        """
        return ANSIColor.__local_invocation(1, string, foreground = foreground, background = background, underline = underline)
    @_sm
    def faint(string: str, /, foreground: _ColorType[int] = None, background: _ColorType[int] = None, underline: _ColorType[int] = None):
        """
        \\@since 0.3.24 \\
        \\@modified 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class ANSIColor
        ```
        """
        return ANSIColor.__local_invocation(2, string, foreground = foreground, background = background, underline = underline)
    @_sm
    def italic(string: str, /, foreground: _ColorType[int] = None, background: _ColorType[int] = None, underline: _ColorType[int] = None):
        """
        \\@since 0.3.24 \\
        \\@modified 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class ANSIColor
        ```
        """
        return ANSIColor.__local_invocation(3, string, foreground = foreground, background = background, underline = underline)
    @_sm
    def underline(string: str, /, foreground: _ColorType[int] = None, background: _ColorType[int] = None, underline: _ColorType[int] = None):
        """
        \\@since 0.3.24 \\
        \\@modified 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class ANSIColor
        ```
        """
        return ANSIColor.__local_invocation(4, string, foreground = foreground, background = background, underline = underline)
    @_sm
    def blink(string: str, /, blink: _lit["slow", "rapid"] = "slow", foreground: _ColorType[int] = None, background: _ColorType[int] = None, underline: _ColorType[int] = None):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class ANSIColor
        ```
        """
        if blink not in ("slow", "rapid"):
            err = TypeError
            s = "Parameter 'blink' is either invalid type or has incorrect string value. Possible values: \"slow\" and \"rapid\"."
            raise err(s)
        elif blink == "slow":
            return ANSIColor.__local_invocation(5, string, foreground = foreground, background = background, underline = underline)
        else:
            return ANSIColor.__local_invocation(6, string, foreground = foreground, background = background, underline = underline)
    @_sm
    def strike(string: str, /, foreground: _ColorType[int] = None, background: _ColorType[int] = None, underline: _ColorType[int] = None):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class ANSIColor
        ```
        """
        return ANSIColor.__local_invocation(9, string, foreground = foreground, background = background, underline = underline)
    @_sm
    def frame(string: str, /, foreground: _ColorType[int] = None, background: _ColorType[int] = None, underline: _ColorType[int] = None):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class ANSIColor
        ```
        """
        return ANSIColor.__local_invocation(51, string, foreground = foreground, background = background, underline = underline)
    @_sm
    def encircle(string: str, /, foreground: _ColorType[int] = None, background: _ColorType[int] = None, underline: _ColorType[int] = None):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class ANSIColor
        ```
        """
        return ANSIColor.__local_invocation(52, string, foreground = foreground, background = background, underline = underline)
    @_sm
    def overline(string: str, /, foreground: _ColorType[int] = None, background: _ColorType[int] = None, underline: _ColorType[int] = None):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class ANSIColor
        ```
        """
        return ANSIColor.__local_invocation(53, string, foreground = foreground, background = background, underline = underline)

class NennɅIAbroads:
    """
    \\@since 0.3.24 \\
    \\@author Aveyzan
    ```ts \\
    in module tense.extensions
    ```
    You are discouraged to use this class, use class `Tense` from \\
    `tense` module instead. `Tense` class inherits this class.

    Reference from TenseTS (Tense TypeScript; former Tense03). \\
    Basing on former class `Tense03NennɅIAbroads`; has special \\
    variations of `abroad()` function. Extended by class `Tense` \\
    to avoid possible yells because of special character used in \\
    the class (`Ʌ`).
    """
    @_cm
    def abroadPositive(self, value1: _AbroadValue1[_T1], /, value2: _AbroadValue2[_T2] = None, modifier: _AbroadModifier[_T3] = None) -> _AbroadInitializer:
        """
        \\@since 0.3.24 \\
        \\@modified 0.3.25 (moved slash to between `value1` and `value2`) \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class NennɅIAbroads
        ```
        Every negative integer is coerced to positive.
        """
        a: list[int] = []
        for i in abroad(value1, value2, modifier):
            a.append(abs(i))
        return a
    @_cm
    def abroadNegative(self, value1: _AbroadValue1[_T1], /, value2: _AbroadValue2[_T2] = None, modifier: _AbroadModifier[_T3] = None) -> _AbroadInitializer:
        """
        \\@since 0.3.24 \\
        \\@modified 0.3.25 (moved slash to between `value1` and `value2`) \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class NennɅIAbroads
        ```
        Every positive integer is coerced to negative.
        """
        a: list[int] = []
        for i in abroad(value1, value2, modifier):
            a.append(-abs(i))
        return a
    @_cm
    def abroadPositiveFlip(self, value1: _AbroadValue1[_T1], /, value2: _AbroadValue2[_T2] = None, modifier: _AbroadModifier[_T3] = None) -> _AbroadInitializer:
        """
        \\@since 0.3.24 \\
        \\@modified 0.3.25 (moved slash to between `value1` and `value2`) \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class NennɅIAbroads
        ```
        Every negative integer is coerced to positive, then sequence is reversed.
        """
        a: list[int] = []
        for i in abroad(value1, value2, modifier):
            a.append(abs(i))
        a.reverse()
        return a
    @_cm
    def abroadNegativeFlip(self, value1: _AbroadValue1[_T1], /, value2: _AbroadValue2[_T2] = None, modifier: _AbroadModifier[_T3] = None) -> _AbroadInitializer:
        """
        \\@since 0.3.24 \\
        \\@modified 0.3.25 (moved slash to between `value1` and `value2`) \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class NennɅIAbroads
        ```
        Every positive integer is coerced to negative, then sequence is reversed.
        """
        a: list[int] = []
        for i in abroad(value1, value2, modifier):
            a.append(-abs(i))
        a.reverse()
        return a
    @_cm
    def abroadPack(self, *values: _AbroadPackType[_T]) -> _AbroadInitializer:
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class NennɅIAbroads
        ```
        This variation of `abroad()` function bases on `zip()` Python function.
        """
        limit = reckonLeast(values)
        a: list[int] = []
        for i in abroad(limit):
            a.append(i)
        return a
    @_cm
    def abroadExclude(self, value1: _AbroadValue1[_T1], /, value2: _AbroadValue2[_T2] = None, modifier: _AbroadModifier[_T3] = None, *excludedIntegers: int) -> _AbroadInitializer:
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class NennɅIAbroads
        ```
        This variation of `abroad()` function is the same as `abroad()` function, \\
        but it also allows to exclude specific integers from the returned list. \\
        If all are excluded, returned is empty integer list. If integers excluded \\
        do not exist in returned sequence normally, this issue is omitted.
        """
        a: list[int] = []
        for i in abroad(value1, value2, modifier):
            for e in excludedIntegers:
                if not isinstance(e, int):
                    err, s = (TypeError, "Parameter 'exclude' has an item, which isn't an integer. Ensure every item is an integer.")
                    raise err(s)
                if i != e:
                    a.append(i)
        return a
    @_cm
    def abroadPrecede(self, value1: _AbroadValue1[_T1], /, value2: _AbroadValue2[_T2] = None, modifier: _AbroadModifier[_T3] = None, prefix: _opt[str] = None) -> _AbroadInitializer:
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 09.07.2024
        "class method" in class NennɅIAbroads
        ```
        This variation of `abroad()` function returns strings in a list. If `prefix` is `None`, \\
        returned are integers in strings, otherwise added is special string prefix before integers.
        """
        a: list[str] = []
        for i in abroad(value1, value2, modifier):
            if prefix is None:
                a.append(str(i))
            elif isinstance(prefix, str):
                a.append(prefix + str(i))
            else:
                err, s = (TypeError, f"Parameter '{prefix.__name__}' is not a string. Ensure argument got value of type 'str'. Received type: {type(prefix).__name__}")
                raise err(s)
        return a
    @_cm
    def abroadSufcede(self, value1: _AbroadValue1[_T1], /, value2: _AbroadValue2[_T2] = None, modifier: _AbroadModifier[_T3] = None, suffix: _opt[str] = None) -> _AbroadStringInitializer:
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 09.07.2024
        "class method" in class NennɅIAbroads
        ```
        This variation of `abroad()` function returns strings in a list. If `prefix` is `None`, \\
        returned are integers in strings, otherwise added is special string suffix after integers.
        """
        a: list[str] = []
        for i in abroad(value1, value2, modifier):
            if suffix is None:
                a.append(str(i))
            elif isinstance(suffix, str):
                a.append(str(i) + suffix)
            else:
                err, s = (TypeError, f"Parameter '{suffix.__name__}' is not a string. Ensure argument got value of type 'str'. Received type: {type(suffix).__name__}")
                raise err(s)
        return a
    @_cm
    def abroadInside(self, value1: _AbroadValue1[_T1], /, value2: _AbroadValue2[_T2] = None, modifier: _AbroadModifier[_T3] = None, string: _opt[str] = None) -> _AbroadStringInitializer:
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 09.07.2024
        "class method" in class NennɅIAbroads
        ```
        This variation of `abroad()` function returns strings in a list. If `string` is `None`, \\
        returned are integers in strings, otherwise integers are placed inside `{}` of the string.
        """
        a: list[str] = []
        for i in abroad(value1, value2, modifier):
            if string is None:
                a.append(str(i))
            elif isinstance(string, str):
                a.append(string.format(str(i)))
            else:
                err, s = (TypeError, f"Parameter '{string.__name__}' is not a string. Ensure argument got value of type 'str'. Received type: {type(string).__name__}")
                raise err(s)
        return a
    @_cm
    def abroadImmutable(self, value1: _AbroadValue1[_T1], /, value2: _AbroadValue2[_T2] = None, modifier: _AbroadModifier[_T3] = None) -> _AbroadImmutableInitializer:
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 09.07.2024
        "class method" in class NennɅIAbroads
        ```
        Immutable variation of `abroad()` function - instead of list returned is tuple. \\
        Equals `tuple(abroad(...))`.
        """
        return tuple(abroad(value1, value2, modifier))
    @_cm
    def abroadConvect(self, *values: _AbroadConvectType[_T]) -> _AbroadInitializer:
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 09.07.2024
        "class method" in class NennɅIAbroads
        ```
        Typical math sum operation before returned is list from `abroad()` function. \\
        If from values a value is:
        - an integer - added is this integer
        - a float - added is this number, without fraction
        - a complex - added are both real and imaginary parts
        - sizeable object - added is its length

        Notice: you can also provide negative entities! If resulted number is negative, \\
        up to `abroad()` function, sequence will go in range [values_sum, -1]. Otherwise,
        it will take this form: [0, values_sum - 1].
        """
        i = 0
        if reckon(values) == 0:
            err, s = (tcs.MissingValueError, "Expected at least one item in parameter 'values'.")
            raise err(s)
        for e in values:
            if not isinstance(e, (_ReckonNGT, int, float, complex, ModernString)):
                err, s = (TypeError, f"From gamut of supported types, parameter 'values' has at least one unsupported type: '{type(e).__name__}'")
                raise err(s)
            elif isinstance(e, int):
                i += e
            elif isinstance(e, float):
                i += trunc(e)
            elif isinstance(e, complex):
                i += trunc(e.real) + trunc(e.imag)
            else:
                i += reckon(e)
        return abroad(i)
    @_cm
    def abroadLive(self, *values: _AbroadLiveType[_T]) -> _AbroadInitializer:
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 09.07.2024
        "class method" in class NennɅIAbroads
        ```
        Concept from non-monotonous sequences from math. Like graph, \\
        which changes per time. If from values a value is:
        - an integer - this is next point
        - a float - next point doesn't have fraction
        - a complex - next point is sum of real and imaginary parts
        - sizeable object - its length is next point
        """
        a: list[int] = []
        ret: list[int] = []
        if reckon(values) == 0:
            err, s = (tcs.MissingValueError, "Expected at least one item in parameter 'values'.")
            raise err(s)
        for e in values:
            if not isinstance(e, (_ReckonNGT, int, float, complex, ModernString)):
                err, s = TypeError, f"From gamut of supported types, parameter 'values' has at least one unsupported type: '{type(e).__name__}'"
                raise err(s)
            elif isinstance(e, int):
                a.append(e)
            elif isinstance(e, float):
                a.append(trunc(e))
            elif isinstance(e, complex):
                a.append(trunc(e.real) + trunc(e.imag))
            else:
                a.append(reckon(e))
        for i1 in abroad(1, a):
            tmp = a[i1]
            if tmp < 0: tmp -= 1
            else: tmp += 1
            for i2 in abroad(a[i1 - 1], tmp): 
                ret.append(i2)
        return ret
    @_cm
    def abroadFloaty(self, value1: _AbroadValue1[_T1], /, value2: _AbroadValue2[_T2] = None, modifier: _AbroadModifier[_T3] = None, div: tcs.FloatOrInteger = 10) -> _AbroadFloatyInitializer:
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 09.07.2024
        "class method" in class NennɅIAbroads
        ```
        Every item from `abroad()` function will be divided by parameter `div`. \\
        It's default value is `10`.
        """
        ret: list[float] = []
        if not isinstance(div, (int, float, tcs.SupportsFloat, tcs.SupportsInt, tcs.SupportsIndex)):
            err, s = (TypeError, f"Parameter 'div' is not an integer nor floating-point number. Ensure argument got value of type 'int' or 'float'. Received type: {type(div).__name__}")
            raise err(s)
        elif isinstance(div, float) and div in (math.nan, math.inf):
            err, s = (ValueError, "Parameter 'div' may not be infinity or not a number.")
            raise err(s)
        elif (isinstance(div, int) and div == 0) or (isinstance(div, float) and div == .0):
            err, s = (ZeroDivisionError, "Parameter 'div' may not be equal zero. This is attempt to divide by zero")
            raise err(s)
        for i in abroad(value1, value2, modifier):
            ret.append(i / div)
        return ret
    @_cm
    def abroadSplit(self, value1: _AbroadValue1[_T1], /, value2: _AbroadValue2[_T2] = None, modifier: _AbroadModifier[_T3] = None, limit = 2) -> _AbroadMultiInitializer:
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 09.07.2024
        "class method" in class NennɅIAbroads
        ```
        Reference to string slicing. Limit is amount of items, \\
        which can be in one sub-list. May not be equal or below 1.
        """
        lim = 0
        tmp: list[int] = []
        a: list[list[int]] = [[]]
        if not isinstance(limit, int):
            err, s = (TypeError, f"Parameter 'limit' is not an integer. Ensure argument got value of type 'int'. Received type: {type(limit).__name__}")
            raise err(s)
        elif limit < 1:
            err, s = (ValueError, "Parameter 'limit' may not be negative, or have value 0 or 1. Start from 2.")
            raise err(s)
        for i in abroad(value1, value2, modifier):
            if lim % limit == 0:
                a.append(tmp)
                tmp.clear()
            else:
                tmp.append(i)
            lim += 1
        return a
    @_cm
    def abroadVivid(self, *values: _AbroadVividType[_V1, _V2, _M]) -> _AbroadMultiInitializer:
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 09.07.2024
        "class method" in class NennɅIAbroads
        ```
        For every value in `values` returned is list `[abroad(V1_1, V2_1?, M_1?), abroad(V1_2, V2_2?, M_2?), ...]`. \\
        Question marks are here to indicate optional values.
        """
        a: list[list[int]] = [[]]
        if reckon(values) < 2:
            err, s = (ValueError, "Expected at least 2 items in parameter 'values'.")
            raise err(s)
        for e in values:
            if not isinstance(e, tuple):
                err, s = (TypeError, f"Parameter 'values' has an item, which isn't a tuple. Ensure every item is of type 'tuple'. Received type: {type(e).__name__}")
                raise err(s)
            if reckon(e) == 1:
                a.append(abroad(e[0]))
            elif reckon(e) == 2:
                a.append(abroad(e[0], e[1]))
            elif reckon(e) == 3:
                a.append(abroad(e[0], e[1], e[2]))
            else:
                err, s = (ValueError, "Parameter 'values' may not have empty tuples, nor tuples of size above 3.")
                raise err(s)
        return a
    @_cm
    def abroadEach(self, value1: _AbroadValue1[_T1], /, value2: _AbroadValue2[_T2] = None, modifier: _AbroadModifier[_T3] = None, each: _opt[_cal[[int], _T]] = None) -> _AbroadIntFloatInitializer[_T]:
        """
        \\@since 0.3.25 (experimental for 0.3.25 - 0.3.26b1) \\
        \\@author Aveyzan
        ```ts \\
        // created 10.07.2024
        "class method" in class NennɅIAbroads
        ```
        Invoked is `each` callback for every item in `abroad()` function.
        """
        a: list[int] = []
        if each is None:
            a: list[int] = []
        else:
            a: list[_uni[int, float]] = []
        for i in abroad(value1, value2, modifier):
            if each is None:
                a.append(i)
            else:
                tmp = each(i)
                if not isinstance(tmp, (int, float)):
                    err, s = (ValueError, "Parameter 'each' returns invalid type or has invalid parameter type (expected 'int'), has too much parameters, or is not a callable object. Use 'lambda' expression, like 'lambda x: Tense.cbrt(x)'.")
                    raise err(s)
                a.append(tmp)
        return a
    @_cm
    def abroadHex(self, value1: _AbroadValue1[_T1], /, value2: _AbroadValue2[_T2] = None, modifier: _AbroadModifier[_T3] = None, mode: _lit[0, 1, 2] = 0) -> _AbroadStringInitializer:
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 10.07.2024
        "class method" in class NennɅIAbroads
        ```
        This variation of `abroad()` function returns hexadecimal representation of each integer.

        Modes:
        - `0` - appends `0x` to each string. It faciliates casting to integer.
        - `1` - appends `#` to each string. Reference from CSS.
        - `2` - nothing is appended.
        """
        a: list[str] = []
        for i in abroad(value1, value2, modifier):
            if mode not in (0, 1, 2) and not isinstance(mode, int):
                err, s = (ValueError, "Expected an integer from 0 to 2 in parameter 'mode'.")
                raise err(s)
            elif mode == 0:
                a.append(hex(i))
            elif mode == 1:
                a.append(re.sub(r"^0x", "#", hex(i)))
            else:
                a.append(re.sub(r"^0x", "", hex(i)))
        return a
    @_cm
    def abroadBinary(self, value1: _AbroadValue1[_T1], /, value2: _AbroadValue2[_T2] = None, modifier: _AbroadModifier[_T3] = None, include_0b = True) -> _AbroadStringInitializer:
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 10.07.2024
        "class method" in class NennɅIAbroads
        ```
        This variation of `abroad()` function returns binary representation of each integer. \\
        Parameter `include_0b` allows to append `0b` before binary notation, what allows \\
        to faciliate casting to integer. Defaults to `True`
        """
        a: list[str] = []
        for i in abroad(value1, value2, modifier):
            if not isinstance(include_0b, bool):
                err, s = (TypeError, "Expected parameter 'include_0b' to be of type 'bool'.")
                raise err(s)
            elif include_0b:
                a.append(bin(i))
            else:
                a.append(re.sub(r"^0b", "", bin(i)))
        return a
    @_cm
    def abroadOctal(self, value1: _AbroadValue1[_T1], /, value2: _AbroadValue2[_T2] = None, modifier: _AbroadModifier[_T3] = None) -> _AbroadStringInitializer:
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 18.07.2024
        "class method" in class NennɅIAbroads
        ```
        This variation of `abroad()` function returns octal representation of each integer. \\
        Every string will be preceded with `0o`
        """
        a: list[str] = []
        for i in abroad(value1, value2, modifier):
            # if not isinstance(include_0b, bool):
            #    err, s = (TypeError, "Expected parameter 'include_0b' to be of type 'bool'.")
            #    raise err(s)
            # elif include_0b:
                a.append(oct(i))
            # else:
            #   a.append(re.sub(r"^0b", "", oct(i)))
        return a

class NennɅIStringz:
    """
    \\@since 0.3.25 (experimental) \\
    \\@author Aveyzan
    ```ts \\
    in module tense.extensions
    ```
    You are discouraged to use this class, use class `Tense` from \\
    `tense` module instead. `Tense` class inherits this class.
    """
    # SANITIZE_AROUND = TenseType(8376.1)
    # SANITIZE_ALL = TenseType(8376.2)
    # SANITIZE_ACF = TenseType(8376.3)
    # SANITIZE_LEFT = TenseType(8376.4)
    # SANITIZE_RIGHT = TenseType(8376.5)
    # SANITIZE_CENTER = TenseType(8376.6)
    
    @_cm
    def sanitize(self, string: str, /, mode = 0):
        """
        \\@since 0.3.25 (experimental) \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class NennɅIStringz
        ```
        1 of 6 options (`SANITIZE_ACF`) is experimental, expect behavior to change! \\
        All other are supported normally.
        """
        if not isinstance(string, str):
            err = TypeError
            s = f"Parameter 'string' is not a string. Ensure argument got value of type 'str'. Received type: {type(string).__name__}"
            raise err(s)
        if not isinstance(mode, TenseType):
            err = TypeError
            s = f"Parameter 'mode' is not an instance of 'TenseType'. Ensure argument got value of type 'TenseType'. Received type: {type(mode).__name__}"
            raise err(s)
        checkout = [i / 10 for i in abroad(83761, 83767)]
        for e in checkout:
            if mode.receive == e: break
        if mode.receive() not in checkout:
            err = ValueError
            s = f"Parameter 'mode' has incorrect 'TenseType' value. Ensure you are using one of constants starting with 'SANITIZE_' as value of this parameter."
            raise err(s)
        def ws(char: str): return reckon(char) == 1 and char in "\n\f\r\v\t"
        ret = ""
        arr = [""]
        arr.clear()
        for c in string: arr.append(c)
        if mode == 0:
            ret = string.strip()
        elif mode == 1:
            for i in abroad(ret):
                if not ws(arr[i]): ret += arr[i]
        elif mode == 3:
            ret = string.lstrip()
        elif mode == 4:
            ret = string.rstrip()
        elif mode == 5:
            g1, g2 = (0, reckon(arr) - 1)
            while ws(arr[g1]): g1 += 1
            while ws(arr[g2]): g2 -= 1
            for _ in abroad(g1): ret += " "
            for i in abroad(g1, g2 + 1):
                if not ws(arr[i]): ret += arr[i]
            for _ in abroad(g2 + 1, arr): ret += " "
            ret = str(ret)
        return ret
    @_cm
    def sanitizeAround(self, string: str, /, left: int = -1, right: int = -1):
        """
        \\@since 0.3.25 (experimental) \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class NennɅIStringz
        ```
        Alias to `self.sanitize(string, mode = self.SANITIZE_AROUND)`. \\
        Parameters `left` and `right` allow to describe, how many whitespaces \\
        shall be excluded from returned string.
        """
        ret = ""
        if not isinstance(string, str):
            err, s = (TypeError, f"Parameter 'string' is not a string. Ensure argument got value of type 'str'. Received type: {type(string).__name__}")
            raise err(s)
        if not isinstance(left, int):
            err, s = (TypeError, f"Parameter 'left' is not an integer. Ensure argument got value of type 'int'. Received type: {type(left).__name__}")
            raise err(s)
        if not isinstance(right, int):
            err, s = (TypeError, f"Parameter 'left' is not an integer. Ensure argument got value of type 'int'. Received type: {type(right).__name__}")
            raise err(s)
        if left < -1 or right < -1:
            err, s = (ValueError, f"Either 'left' or 'right' is below -1. Make sure both parameter have positive values or -1. Received values: 'left' -> {left}, 'right' -> {right}")
            raise err(s)
        if left == 0 and right == 0:
            return string
        if left == -1:
            ret = string.lstrip()
        elif left > 0:
            ret = re.sub("^[\f\r\n\t\v]{" + str(left) + "}", "", string)
        if right == -1:
            ret = string.rstrip()
        elif right > 0:
            ret = re.sub("[\f\r\n\t\v]{" + str(right) + "}$", "", string)
        return ret

class NennɅIRandomize:
    """
    \\@since 0.3.25 \\
    \\@author Aveyzan
    ```ts \\
    // created 14.07.2024
    in module tense.extensions
    ```
    Class for randomizing things. \\
    Extended by class `Tense` to avoid possible yells because of \\
    special character used in the class (`Ʌ`).
    """
    @_cm
    def randomize(self, sequence: _RandomizeType[_T], /) -> _T:
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 14.07.2024
        "class method" in class NennɅIRandomize
        ```
        Same as `Tense.pick()`, returns any item from a sequence.

        As much wanting to provide version with `*items` parameter, \\
        returned type may be unfortunately an united one.
        """
        return sequence[randint(0, reckon(sequence) - 1)]
    @_cm
    def randomizeInt(self, x: int, y: int, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 15.07.2024
        "class method" in class NennɅIRandomize
        ```
        Same as `Tense.random()`.
        """
        _rand = randint
        if x > y:
            return _rand(y, x)
        elif x == y:
            return x
        else:
            return _rand(x, y)
    @_cm
    def randomizeStr(self, lower = True, upper = True, digits = True, special = True, length = 10):
        """
        \\@since 0.3.9 \\
        \\@lifetime ≥ 0.3.9; < 0.3.24; ≥ 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 15.07.2024
        "class method" in class NennɅIRandomize
        ```
        - `lower` - determine, if you want to include all lowercased letters from english alphabet. Defaults to `True`
        - `upper` - determine, if you want to include all uppercased letters from english alphabet. Defaults to `True`
        - `digits` - determine, if you want to include all numbers. Defaults to `True`
        - `special` - determine, if you want to include all remaining chars accessible normally via English keyboard. \\
        Defaults to `True`
        - `length` - allows to specify the length of returned string. Defaults to `10`.
        """
        conv: list[str] = []
        ret = ""
        if lower:
            for e in ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"):
                conv.append(e)
        if upper:
            for e in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"):
                conv.append(e)
        if digits:
            for e in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                conv.append(e)
        if special:
            for e in ("!", "@", "~", "`", "^", "%", "#", "&", "*", "/", "+", "-", "_", "|", "\\", "\"", "'", ":", ";", ">", "<", "?", ",", "."):
                conv.append(e)
        for _ in abroad(length): ret += self.randomize(conv)
        return ret
    @_cm
    def randomizeStr2(self, string: str, /):
        """
        \\@since 0.3.26b3 \\
        \\@author Aveyzan
        ```ts \\
        // created 25.07.2024
        "class method" in class NennɅIRandomize
        ```
        Return shuffled string
        """
        tmp = list(string)
        random.shuffle(tmp)
        return "".join(tmp)
    @_cm
    def randomizeUuid(self):
        """
        \\@since 0.3.26a1 \\
        \\@author Aveyzan
        ```ts \\
        // created 20.07.2024
        "class method" in class NennɅIRandomize
        ```
        Return a random UUID. Alias to `Tense.uuidRandom()`
        """
        return uuid.uuid4()

# between @since and @author there is unnecessarily long line spacing
# hence this warning is being thrown; it is being disabled.
warnings.filterwarnings("ignore", r"^invalid escape sequence '\\@'", SyntaxWarning)

if __name__ == "__main__":
    err = RuntimeError
    s = "This file is not for compiling, moreover, this file does not have a complete TensePy declarations collection. Consider importing module 'tense' instead."
    raise err(s)

del uuid, sys
            