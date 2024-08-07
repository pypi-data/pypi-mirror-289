"""\t
TensePy Primary
+++++
\\@since 0.3.24 \\
\\@author Aveyzan
```ts \\
module tense.primary
```
You are discouraged to import this module, import `tense` module instead.

All first TensePy declarations are inside the `tense.primary` module, which isn't necessary to import, when e.g. `tense`
or `tense.core` module is imported. `tense.primary` module holds these 2 special functions: `abroad()` and `reckon()`, \\
crucial TensePy declarations, which are equivalents to Python functions `range()` and `len()`.

"""

import sys

if sys.version_info < (3, 9):
    err, s = (RuntimeError, "Use 'tense_eight' module for Python versions below 3.9.")
    raise err(s)

import os
import tense.tcs as tcs, re, json, tkinter as tk
from typing import TypeVar, Union, Counter, MutableSequence, IO, Literal, final, Optional, TextIO, BinaryIO, Sequence, MutableSequence, Mapping, MutableMapping, MutableSet, AbstractSet, Iterable, Protocol, Generic, Any, AsyncIterable
from collections import deque, defaultdict, ChainMap, OrderedDict
from mmap import mmap
from array import array
from tkinter import StringVar
from io import TextIOWrapper, FileIO, BufferedRandom, BufferedReader, BufferedWriter, BufferedRWPair, BytesIO, BufferedIOBase, StringIO
from math import trunc, inf, nan
from random import randint
from hashlib import sha1, sha224, sha256, sha384, sha512, md5
import tkinter as tk, math
from datetime import datetime
from warnings import filterwarnings

# between @since and @author there is unnecessarily long line spacing
# hence this warning is being thrown; it is being disabled.
filterwarnings("ignore", category = SyntaxWarning)

# types
_var = TypeVar
_package = open(os.path.dirname(os.path.abspath(__file__)) + "/package.json")
_package_load = json.load(_package)
_package.close()

_T = _var("_T")
_T_cov = _var("_T_cov", covariant = True)
_T1 = _var("_T1")
_T2 = _var("_T2")
_T3 = _var("_T3")

RAM = int
_AbroadInitializer = tcs.AbroadInitializer[int]
_Ellipsis = tcs.Ellipsis
_ReckonTypePre = tcs.ReckonType[_T]
_ReckonNGTPre = tcs.ReckonNGT
_AbroadValue1Pre = tcs.AbroadValue1[_T]
_AbroadValue2Pre = tcs.AbroadValue2[_T]
_AbroadModifierPre = tcs.AbroadModifier[_T]
_SupportsModernReplace = tcs.ModernReplace[str] # since 0.3.24
_SupportsPick = tcs.PickSequence[_T]
_SupportsIndex = tcs.SupportsIndex
_SanitizeMode = tcs.SanitizeMode
# _SupportsTenseVersion = tcs.TenseVersionType[int] # Union[list[_T], tuple[_T, _T, _T]]
_FloatOrInteger = tcs.FloatOrInteger
_SupportsAbs = Union[tcs.FloatOrInteger, tcs.SupportsAbs[_T_cov]]
_ReleaseLevel = Literal["alpha", "beta", "candidate", "final"]
_TenseVersionType = tcs.TenseVersionType[int]

Null = tcs.NULL
"""
\\@since 0.3.25 \\
\\@author Aveyzan
```ts \\
in module tense.primary
```
Alias to `None`. Referring to many known programming languages
"""
@final
class _TenseVersion:
    """
    \\@since 0.3.25 \\
    \\@author Aveyzan
    ```ts \\
    in module tense.primary
    ```
    Special class for Tense version checking
    """
    __local_version = tcs.VERSION_TUPLE
    @property
    def major(self): return tcs.VERSION_TUPLE[0]
    @property
    def minor(self): return tcs.VERSION_TUPLE[1]
    @property
    def micro(self): return tcs.VERSION_TUPLE[2]
    @property
    def releaselevel(self): return tcs.VERSION_TUPLE[3]
    @property
    def serial(self): return tcs.VERSION_TUPLE[4]
    STRING_VER: tcs.ClassVar[str] = tcs.VERSION # since 0.3.26b2
    """
    \\@since 0.3.26b3 \\
    \\@author Aveyzan
    ```ts \\
    const in class _TenseVersion
    ```
    Returns current Tense version as a string. \\
    *Warning*: it is managed automatically, and \\
    hence it shouldn't be changed.
    """
    @classmethod
    def receive(self):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class _TenseVersion
        ```
        Returns current Tense version
        """
        return self.__local_version
    def __ge__(self, other: _TenseVersionType):
        """
        \\@since 0.3.26b3 \\
        \\@author Aveyzan
        ```ts \\
        'operator >=' in class _TenseVersion
        ```
        Comparison: Check whether version is greater than or equal current one.
        """
        return (
            other[0] >= self.major or
            other[1] >= self.minor or
            other[2] >= self.micro
        )
    def __le__(self, other: _TenseVersionType):
        """
        \\@since 0.3.26b3 \\
        \\@author Aveyzan
        ```ts \\
        'operator <=' in class _TenseVersion
        ```
        Comparison: Check whether version is least than or equal current one.
        """
        return (
            other[0] <= self.major or
            other[1] <= self.minor or
            other[2] <= self.micro
        )
    def __gt__(self, other: _TenseVersionType):
        """
        \\@since 0.3.26b3 \\
        \\@author Aveyzan
        ```ts \\
        'operator >' in class _TenseVersion
        ```
        Comparison: Check whether version is greater than current one.
        """
        return (
            other[0] > self.major or
            other[1] > self.minor or
            other[2] > self.micro
        )
    def __lt__(self, other: _TenseVersionType):
        """
        \\@since 0.3.26b3 \\
        \\@author Aveyzan
        ```ts \\
        'operator <' in class _TenseVersion
        ```
        Comparison: Check whether version is least then current one.
        """
        return (
            other[0] < self.major or
            other[1] < self.minor or
            other[2] < self.micro
        )
    def __eq__(self, other: _TenseVersionType):
        """
        \\@since 0.3.26b3 \\
        \\@author Aveyzan
        ```ts \\
        'operator ==' in class _TenseVersion
        ```
        Comparison: Check whether version is equal the current one.
        """
        return (
            other[0] == self.major and
            other[1] == self.minor and
            other[2] == self.micro
        )
    def __ne__(self, other: _TenseVersionType):
        """
        \\@since 0.3.26b3 \\
        \\@author Aveyzan
        ```ts \\
        'operator !=' in class _TenseVersion
        ```
        Comparison: Check whether version is inequal to the current one.
        """
        return (
            other[0] != self.major or
            other[1] != self.minor or
            other[2] != self.micro
        )

@tcs.final
class TenseType(Generic[_T]):
    """
    \\@since 0.3.25 (experimental) \\
    \\@author Aveyzan
    ```ts \\
    in module tense.primary
    ```
    Special class to satisfy several type requirements. Under testing, \\
    this type still causes mistakes
    """
    __locale = None
    def __init__(self, value: _T):
        self.__locale = value
    def receive(self):
        if self.__locale is None:
            err = ValueError
            s = f"Required is to build instance of class '{__class__.__name__}', with specific value except 'None'."
            raise err(s)
        else: return self.__locale

TENSE_VERSION = _TenseVersion()
"""
\\@since 0.3.24 \\
\\@author Aveyzan
```ts \\
in module tense.primary
```
Return currently used Tense version as a tuple. \\
Since 0.3.25 returns instance of local class `_TenseVersion`, \\
hence to gain version as a tuple, use class method `receive()`.
"""
def tenseVersion(asTuple = False):
    """
    \\@since 0.3.8 \\
    \\@author Aveyzan
    ```ts \\
    in module tense.primary
    ``` \n
    ``` \n
    # since 0.3.24
    def tenseVersion(asTuple: bool = False): ...
    # before 0.3.24
    def tenseVersion(): ...
    ```
    Returns Tense version installed. Ensure you have version up-to-date to make everything actually working. If optional parameter \\
    is set to `True`, returned is tuple with 3 items, which together compose version of Tense. This argument is also responsible for \\
    deletion of global function `tenseVersionAsTuple()` on 0.3.24.
    """
    if asTuple: return TENSE_VERSION.receive()
    else: return TENSE_VERSION.STRING_VER

def _tenseVersionAsTuple():
    """function cancelled on 0.3.24"""
    return TENSE_VERSION.receive()


# declarations

""""""

# class Tense08AbroadRadex(object):
"""
    `Tense08AbroadRadex`
    ++++
    https://aveyzan.glitch.me/tense/08/class.Tense08AbroadRadex.html \\
    \\@since 0.3.12, to 0.3.24 \\
    \\@standard-since 0.3.12 \\
    \\@last-change 0.3.24 \\
    \\@author Aveyzan

    Appendix to the last parameter in `abroad()` method.
    """
    # __arr: list[int] = []
    # @classmethod
    # def __new__(self, *values: int):
    #    i = 0
    #    while i < len(values):
    #        self.__arr.append(values[i])
    #        i += 1
    # @classmethod
    # def retrieve(self): return self.__arr

def _reckon_prepend_init(*countables: _ReckonTypePre[_T]):
    i = 0
    for e in countables:
        if isinstance(e, array): i += e.__len__()
        elif isinstance(e, (TextIOWrapper, FileIO, BufferedWriter, BufferedRandom, BufferedReader, IO, TextIO, BinaryIO, BufferedIOBase, BufferedRWPair, BytesIO, StringIO)):
            for r in e.read():
                if isinstance(r, (bytes, str)):
                    for _ in r:
                        i += 1
                else: i += 1
        # elif isinstance(e, StringVar):
        #    for _ in e.get():
        #        i += 1
        elif isinstance(e, (str, enumerate, Sequence, MutableSequence, deque, list, tuple, Counter, defaultdict, dict, set, frozenset, range, bytes, bytearray, mmap, memoryview,
                            Mapping, MutableMapping, OrderedDict, ChainMap, MutableSet, AbstractSet, Iterable, AsyncIterable)):
            for _ in e:
                i += 1
        else:
            err = TypeError
            s = "Supported types: `set`, `deque`, `list`, `str`, `tuple`, `dict`, `bytes`, `bytearray`, `memoryview`, `range`, `mmap`, `array`, `StringVar`, `enumerate`, `frozenset`, `typing.Counter`, `defaultdict`, `TextIOWrapper`,"
            s += "since 0.3.24: `FileIO`, `BufferedWriter`, `BufferedRandom`, `BufferedReader`, `IO`,"
            s += "since 0.3.25: `StringIO`, `BufferedRWPair`, `BufferedIOBase`, `BytesIO`."
            s += f"Passed type `{type(e).__name__}` does not match any of this list."
            raise err(s)
    return i

def _reckon_init(*countables: _ReckonTypePre[_T]):
    return _reckon_prepend_init(*countables)

def _abroad_prepend_init(value1: _AbroadValue1Pre[_T1], /, value2: _AbroadValue2Pre[_T2] = None, modifier: _AbroadModifierPre[_T3] = None):
    conv: list[int] = []
    [v1, v2, m] = [0, 0, 0]
    # v1 (value1)
    if isinstance(value1, _ReckonNGTPre):
        v1 = _reckon_init(value1)
    elif isinstance(value1, int):
        v1 = value1
    elif isinstance(value1, float):
        if value2 == inf or value2 == nan:
            err = tcs.IncorrectValueError
            s = "'inf' or 'nan' as value for 'value1' (1st parameter) is not allowed."
            raise err(s)
        else:
            v1 = trunc(value1)
    elif isinstance(value1, complex):
        v1 = trunc(value1.real)
    else:
        err = TypeError
        s = f"Missing value or invalid type of 'value1' (1st parameter). Used type '{str(type(value1).__name__)}' does not match any of types, which are allowed in this parameter."
        raise err(s)
    # v2 (value2)
    if isinstance(value2, _ReckonNGTPre):
        v2 = _reckon_init(value2)
    elif isinstance(value2, (bool, _Ellipsis)) or value2 is None:
        if isinstance(value1, complex): v2 = trunc(value1.imag)
        else: v2 = v1
    elif isinstance(value2, int):
        v2 = value2
    elif isinstance(value2, float):
        if value2 == inf or value2 == nan:
            err = tcs.IncorrectValueError
            s = "'inf' or 'nan' as value for 'value2' (2nd parameter) is not allowed."
            raise err(s)
        else:
            v2 = trunc(value2)
    else:
        err = TypeError
        s = f"Invalid type of 'value2' (2nd parameter). Used type '{str(type(value2).__name__)}' does not match any of types, which are allowed in this parameter."
        raise err(s)
    # m (modifier)
    if isinstance(modifier, _ReckonNGTPre):
        m = _reckon_init(modifier)
        if m == 0: m = 1
    elif isinstance(modifier, int):
        if modifier == 0: m = 1
        else: m = abs(modifier)
        if m == 0: m = 1
    elif isinstance(modifier, float):
        if modifier == inf:
            err = tcs.IncorrectValueError
            s = "'inf' as value for 'modifier' (3rd parameter) is not allowed."
            raise err(s)
        elif modifier == nan:
            m = 1
        else:
            m = abs(trunc(modifier))
            if m == 0: m = 1
    elif isinstance(modifier, complex):
        m = trunc(modifier.real) + trunc(modifier.imag)
        if m < 0: m = abs(m)
        elif m == 0: m = 1
    elif isinstance(modifier, _Ellipsis) or modifier is None:
        m = 1
    else:
        err = TypeError
        s = f"Invalid type of 'modifier' (3rd parameter). Used type '{str(type(modifier).__name__)}' does not match any of types, which are allowed in this parameter."
        raise err(s)
    # iteration begins
    if (v1 == v2 or isinstance(value1, complex)) and (isinstance(value2, bool) or value2 is None):
        if isinstance(value1, complex):
            v1 = trunc(value1.real)
            v2 = trunc(value1.imag)
            if v1 < v2:
                i = v1
                while i < v2:
                    if value2 is False:
                        conv.append(-i - 1)
                    else:
                        conv.append(i)
                    i += m
            else:
                i = v1
                while i > v2:
                    if value2 is False:
                        conv.append(-i - 1)
                    else:
                        conv.append(i)
                    i -= m
            if value2 is False:
                conv.reverse()
        else:
            if v1 > 0:
                i = 0
                while i < v1:
                    if value2 is False:
                        conv.append(-i - 1)
                    else:
                        conv.append(i)
                    i += m
            else:
                i = v1
                while i < 0:
                    if value2 is False:
                        conv.append(-i - 1)
                    else:
                        conv.append(i)
                    i += m
            if value2 is False:
                conv.reverse()
        return conv
    if isinstance(value2, float):
        if v2 >= 0 or (v1 < 0 and v2 < 0):
            v2 += 1
        else:
            v2 -= 1
    if v1 < v2:
        i = v1
        while i < v2:
            conv.append(i)
            i += m
    else:
        i = v1
        while i > v2:
            conv.append(i)
            i -= m
    return conv
def _abroad_init(value1: _AbroadValue1Pre[_T1], /, value2: _AbroadValue2Pre[_T2] = None, modifier: _AbroadModifierPre[_T3] = None) -> _AbroadInitializer:
    return _abroad_prepend_init(value1, value2, modifier)
def _random_pick(countable: _SupportsPick[_T]) -> _T:
    return countable[randint(0, _reckon_init(countable) - 1)]

class Time:
    """
    \\@since 0.3.25 \\
    \\@author Aveyzan
    ```ts \\
    // created 04.07.2024
    in module tense.primary
    ```
    Access to time
    """
    __forced_unix_year_range = False
    @classmethod
    def forceUnixYearRange(self, option = False, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Time
        ```
        Forces year range to 1st Jan 1970 - 19th Jan 2038. \\
        If set to `False`, it is reset.
        """
        self.__forced_unix_year_range = option
        return self
    @classmethod
    def fencordFormat(self):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Time
        ```
        Returned is present time in `tense.fencord.Fencord` class format.
        Formatted as `%Y-%m-%d %H:%M:%S`. Timezone is user's local timezone. \\
        This format also uses `discord` module.
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    @classmethod
    def isLeapYear(self, year: int):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Time
        ```
        Returned is `True` only when:
        - year is an integer and is positive (above 0)
        - year is divisible by 4 and not divisible by 100 or year is divisible by 400
        - if Unix year range is enforced, only years in range 1970 - 2038

        If none of these requirements are granted, returned is `False`.
        """
        b = ((isinstance(year, int) and year >= 1) and (year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
        if self.__forced_unix_year_range: b = b and (year >= 1970 and year <= 2038)
        return b
    @classmethod
    def verifyDate(self, year: int, month: int, day: int):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Time
        ```
        Returned is `True` only when every parameter is an integer and year is from 1 up, \\
        month is from 1 up and day is from 1 up, and one of these statements are granted:
        - day has value 31 for months: 1, 3, 5, 7, 8, 10, 12
        - day has value 30 for every month in range 1-12 excluding 2
        - day has value 29 for every month in range 1-12, for 2 only if year is leap
        - day is in range 1-28 for every month in range 1-12
        - additionally, if Unix year range is enforced, year is in range 1970-2038

        If none of these requirements are granted, returned is `False`.
        """
        return (
                isinstance(year, int) and isinstance(month, int) and isinstance(day, int)) and (year >= 1 and month >= 1 and day >= 1) and (
                (day == 31 and month in (1, 3, 5, 7, 8, 10, 12)) or (day == 30 and month in (1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) or
                (day == 29 and month in _abroad_init(1, 12.1) and self.isLeapYear(year)) or (day < 29 and month in _abroad_init(1, 12.1))
            )
    @classmethod
    def getMillennium(self):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Time
        ```
        Returns current millennium. Expected would be only `return 3`, \\
        but code itself in reality verifies current date and what not.
        """
        return trunc(int(datetime.now().strftime("%Y")) / 1000) + 1
    @classmethod
    def getCentury(self):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Time
        ```
        Returns current century. Expected would be only `return 21`, \\
        but code itself in reality verifies current date and what not.
        """
        return trunc(int(datetime.now().strftime("%Y")) / 100) + 1
    @classmethod
    def getDecade(self):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Time
        ```
        Returns current decade. Warning: it does not return something like \\
        3rd decade of 21st century, but decade in overall, which have elapsed 
        since Anno Domini time period. So what that means: for 2024 (4th July \\
        2024, when created this method) returned is 203.

        It does not match 0-to-9 decades, but 1-to-0, so 203 will be returned \\
        by years in range 2021-2030 (not in 2020-2029), including both points.
        """
        return trunc(int(datetime.now().strftime("%Y")) / 10) + 1
    @classmethod
    def getYear(self):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Time
        ```
        Returns current year
        """
        return int(datetime.now().strftime("%Y"))
    @classmethod
    def getMonth(self):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Time
        ```
        Returns current month
        """
        return int(datetime.now().strftime("%m"))
    @classmethod
    def getDay(self):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Time
        ```
        Returns current day. Basing on local timezone.
        Warning: This doesn't return day of the year \\
        or day of the week, but only day of the month
        """
        return int(datetime.now().strftime("%d"))
    @classmethod
    def getHour(self):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Time
        ```
        Returns current hour. Basing on local timezone.
        """
        return int(datetime.now().strftime("%H"))
    @classmethod
    def getMinute(self):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Time
        ```
        Returns current minute. Basing on local timezone.
        """
        return int(datetime.now().strftime("%M"))
    @classmethod
    def getSecond(self):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Time
        ```
        Returns current second. Basing on local timezone.
        """
        return int(datetime.now().strftime("%S"))
    
class Math:
    """
    \\@since 0.3.25 \\
    \\@author Aveyzan
    ```ts \\
    // created 04.07.2024
    in module tense.primary
    ```
    Math methods and constants
    """
    PI: tcs.ClassVar[float] = tcs.PI
    """
    \\@since 0.3.25 \\
    \\@author Aveyzan
    ```ts \\
    // created 04.07.2024
    const in class Math
    ```
    Value of irrational constant π (pi). This well-known constant \\
    is used in circles, that is ratio of its circumference to its diameter. \\
    First use of this letter was found in the essay written by William \\
    Jones back on 1706.
    """
    E: tcs.ClassVar[float] = tcs.E
    """
    \\@since 0.3.25 \\
    \\@author Aveyzan
    ```ts \\
    // created 04.07.2024
    const in class Math
    ```
    Value of irrational constant `e`. Known as Euler's constant \\
    or Napier's constant. Who knows, maybe its definition should \\
    have forenames of both mathematicians, like Euler-Napier's \\
    constant? However, back then on 1683, Swiss mathematician \\
    Jacob Bernoulli was the first person to discover `e`. It could \\
    be an interesting subject to conduct.
    """
    INF: tcs.ClassVar[float] = tcs.INF
    """
    \\@since 0.3.25 \\
    \\@author Aveyzan
    ```ts \\
    // created 05.07.2024
    const in class Math
    ```
    Infinity
    """
    NAN: tcs.ClassVar[float] = tcs.NAN
    """
    \\@since 0.3.25 \\
    \\@author Aveyzan
    ```ts \\
    // created 05.07.2024
    const in class Math
    ```
    Not a number
    """
    TAU: tcs.ClassVar[float] = tcs.TAU
    """
    \\@since 0.3.25 \\
    \\@author Aveyzan
    ```ts \\
    // created 05.07.2024
    const in class Math
    ```
    Value of irrational constant τ (tau)
    """
    SQRT2: tcs.ClassVar[float] = tcs.SQRT2
    """
    \\@since 0.3.25 \\
    \\@author Aveyzan
    ```ts \\
    // created 05.07.2024
    const in class Math
    ```
    Square root of 2. Reference from JavaScript: `Math.SQRT2`
    """
    CENTILLION: tcs.ClassVar[int] = tcs.CENTILLION
    """
    \\@since 0.3.25 \\
    \\@author Aveyzan
    ```ts \\
    // created 19.07.2024
    const in class Math
    ```
    `1e+303`
    """
    @classmethod
    def __verify(x: _FloatOrInteger, y: Optional[_FloatOrInteger] = None):
        if not isinstance(x, (int, float)):
            err = TypeError
            s = f"Argument 'x' is neither 'int' nor 'float'. Received type '{type(x).__name__}'"
            raise err(s)
        if y is not None and not isinstance(y, (int, float)):
            err = TypeError
            s = f"Argument 'y' is neither 'int' nor 'float'. Received type '{type(y).__name__}'"
            raise err(s)
    @classmethod
    def outOfRoot(self, number: int, rootScale: int, /):
        """Since 0.3.?"""
        i = number
        while not isinstance(pow(number, 1/rootScale), int): i -= 1
        return [int(pow(i, 1/rootScale)), number - i]
    @classmethod
    def asin(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns arc sine of `x` \\
        Result is in range [-π/2, π/2]
        """
        return math.asin(x)
    @classmethod
    def acos(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns arc cosine of `x` \\
        Result is in range [0, π]
        """
        return math.acos(x)
    @classmethod
    def atan(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns arc tangent of `x` \\
        Result is in range [-π/2, π/2]
        """
        return math.atan(x)
    @classmethod
    def asinh(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns inverse hyperbolic sine of `x`
        """
        return math.asinh(x)
    @classmethod
    def acosh(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns inverse hyperbolic cosine of `x`
        """
        return math.acosh(x)
    @classmethod
    def atanh(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns inverse hyperbolic tangent of `x`
        """
        return math.atanh(x)
    @classmethod
    def sin(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns sine of `x`
        """
        return math.sin(x)
    @classmethod
    def cos(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns cosine of `x`
        """
        return math.cos(x)
    @classmethod
    def tan(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns tangent of `x`
        """
        return math.tan(x)
    @classmethod
    def sinh(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns hyperbolic sine of `x`
        """
        return math.sinh(x)
    @classmethod
    def cosh(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns hyperbolic cosine of `x`
        """
        return math.cosh(x)
    @classmethod
    def tanh(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns hyperbolic tangent of `x`
        """
        return math.tanh(x)
    @classmethod
    def cosec(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns cosecant of `x`
        """
        return 1 / self.sin(x)
    @classmethod
    def sec(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns secant of `x`
        """
        return 1 / self.cos(x)
    @classmethod
    def acosec(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "class method" in class Math
        ```
        Returns inverse cosecant of `x`. Equals `asin(1 / x)`
        """
        return self.asin(1 / x)
    @classmethod
    def asec(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "class method" in class Math
        ```
        Returns inverse secant of `x`. Equals `acos(1 / x)`
        """
        return self.acos(1 / x)
    @classmethod
    def cot(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns cotangent of `x`. That is inversed tangent
        """
        return 1 / self.tan(x)
    @classmethod
    def versin(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns versed sine of `x`. That is 1 minus its cosine
        """
        return 1 - self.cos(x)
    @classmethod
    def coversin(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns coversed sine of `x`. That is 1 minus its sine
        """
        return 1 - self.sin(x)
    @classmethod
    def vercosin(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns versed cosine of `x`. That is 1 plus its cosine
        """
        return 1 + self.cos(x)
    @classmethod
    def covercosin(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns coversed cosine of `x`. That is 1 plus its sine
        """
        return 1 + self.sin(x)
    @classmethod
    def haversin(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns haversed sine of `x`. That is half of its versed sine
        """
        return self.versin(x) / 2
    @classmethod
    def havercosin(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns haversed cosine of `x`. That is half of its coversed sine
        """
        return self.coversin(x) / 2
    @classmethod
    def hacoversin(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns hacoversed sine of `x`. That is half of its versed cosine
        """
        return self.vercosin(x) / 2
    @classmethod
    def hacovercosin(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns hacoversed cosine of `x`. That is half of its coversed cosine
        """
        return self.covercosin(x) / 2
    @classmethod
    def aversin(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns inverse versed sine of `x`. Equals `acos(1 - x)`
        """
        return self.acos(1 - x)
    @classmethod
    def acoversin(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns inverse coversed sine of `x`. Equals `acos(x - 1)`
        """
        return self.acos(x - 1)
    @classmethod
    def avercosin(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns inverse versed cosine of `x`. Equals `asin(1 - x)`
        """
        return self.asin(1 - x)
    @classmethod
    def acovercosin(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 04.07.2024
        "class method" in class Math
        ```
        Returns inverse coversed cosine of `x`. Equals `asin(x - 1)`
        """
        return self.asin(x - 1)
    @classmethod
    def ahaversin(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "class method" in class Math
        ```
        Returns inverse haversed sine of `x`. Equals `acos(1 - 2x)`
        """
        return self.acos(1 - (2 * x))
    @classmethod
    def ahavercosin(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "class method" in class Math
        ```
        Returns inverse haversed cosine of `x`. Equals `acos(2x - 1)`
        """
        return self.acos(2 * x - 1)
    @classmethod
    def ahacoversin(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "class method" in class Math
        ```
        Returns inverse hacoversed sine of `x`. Equals `asin(1 - 2x)`
        """
        return self.asin(1 - (2 * x))
    @classmethod
    def ahacovercosin(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "class method" in class Math
        ```
        Returns inverse hacoversed cosine of `x`. Equals `asin(2x - 1)`
        """
        return self.asin(2 * x - 1)
    @classmethod
    def exsec(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "class method" in class Math
        ```
        Returns exsecant of `x`. That is its secant minus 1
        """
        return self.sec(x) - 1
    @classmethod
    def excsc(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "class method" in class Math
        ```
        Returns excosecant/coexsecant of `x`. That is its cosecant minus 1
        """
        return self.cosec(x) - 1
    @classmethod
    def aexsec(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "class method" in class Math
        ```
        Returns inverse exsecant of `x`. Equals `asec(x + 1)`
        """
        return self.asec(x + 1)
    @classmethod
    def aexcsc(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "class method" in class Math
        ```
        Returns inverse excosecant of `x`. Equals `acosec(x + 1)`
        """
        return self.acosec(x + 1)
    @classmethod
    def log(self, x: _FloatOrInteger, base: Optional[_FloatOrInteger] = None):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "class method" in class Math
        ```
        Logarithm of `x` with specified base. If `base` is omitted, \\
        returned is logarithm of base e.
        """
        if base is not None:
            self.__verify(base)
            return math.log(x, base)
        else:
            return math.log(x)
    @classmethod
    def log2(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "class method" in class Math
        ```
        Logarithm of `x` with base 2.
        """
        return math.log2(x)
    @classmethod
    def log3(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "class method" in class Math
        ```
        Logarithm of `x` with base 3.
        """
        return self.log(x, 3)
    @classmethod
    def log5(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "class method" in class Math
        ```
        Logarithm of `x` with base 5.
        """
        return self.log(x, 5)
    @classmethod
    def log7(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "class method" in class Math
        ```
        Logarithm of `x` with base 7.
        """
        return self.log(x, 7)
    @classmethod
    def ln(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "class method" in class Math
        ```
        Natural logarithm of `x`. That is logarithm with base `e`.
        """
        return self.log(x, self.E)
    @classmethod
    def log10(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "class method" in class Math
        ```
        Logarithm of `x` with base 10.
        """
        return math.log10(x)
    @classmethod
    def sqrt(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "class method" in class Math
        ```
        Square root of `x`.
        """
        return math.sqrt(x)
    @classmethod
    def cbrt(self, x: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "class method" in class Math
        ```
        Cube root of `x`.
        """
        return math.cbrt(x)
    @classmethod
    def pow(self, x: _FloatOrInteger, y: _FloatOrInteger, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "class method" in class Math
        ```
        Power with base `x` and exponent `y`. \\
        Equals `x**y`(`x` to the power of `y`).
        """
        return math.pow(x, y)
    @classmethod
    def abs(self, x: _SupportsAbs):
        """
        \\@since 0.3.? \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        If passed is integer, returned is integer, \\
        if passed is floating-point number, then \\
        it is returned. In both cases returned is \\
        absolute value of the parameter.
        """
        if x < 0: return -x
        else: return x


class ModernString:
    """
    \\@since 0.3.24 \\
    \\@author Aveyzan
    ```ts \\
    in module tense.primary
    ```
    """
    REPLACE_ALL = -1 # since 0.3.24
    SANITIZE_AROUND = 0 # since 0.3.24
    SANITIZE_ALL = 1 # since 0.3.24
    SANITIZE_ACF = 2 # since 0.3.24
    SANITIZE_LEFT = 3 # since 0.3.24
    SANITIZE_RIGHT = 4 # since 0.3.24
    SANITIZE_CENTER = 5 # since 0.3.24
    if sys.version_info > (3, 8):
        __loc_arr: list[str] = [] # since 0.3.24
    else:
        __loc_arr: Union["list[str]"] = [] # since 0.3.24
    __loc_int = 0 # since 0.3.24
    @classmethod
    def __obtain(self):
        """obtain a string from replacement methods, available during 0.3.9 - 0.3.23, removed on 0.3.24, replacing this method with `get()`"""
        pass
    def __init__(self, *strings: str):
        for i in _abroad_init(strings): # since 0.3.9
            self.__loc_arr.append(strings[i])
        self.__loc_int = _reckon_init(self.__loc_arr) - 1
    @classmethod
    def sha1(self, string: Union[str, bytes, None] = None, hexdigest: bool = True):
        """
        \\@since 0.3.24 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class ModernString
        ```
        Returned is SHA-1 message digest of a string. If `string` is \\
        a string, this string will be used, otherwise it comes to string \\
        currently pointed by the class. That string is **not** changed. \\
        If `hexdigest` is `True`, returned is hexadecimal digest. \\
        Otherwise returned is result in byte format.
        """
        if string is not None and not isinstance(string, (str, bytes, bytearray, memoryview)):
            err = TypeError
            s = f"Inappropriate type of parameter 'string'. Expected a string or None. Received type: {type(string).__name__}"
            raise err(s)
        if not isinstance(hexdigest, bool):
            err = TypeError
            s = f"Inappropriate type of parameter 'hexdigest'. Expected a string or None. Received type: {type(hexdigest).__name__}"
            raise err(s)
        if string is None:
            if hexdigest: return sha1(bytes(self.get())).hexdigest()
            else: return sha1(bytes(self.get())).digest()
        elif isinstance(string, bytes):
            if hexdigest: return sha1(string).hexdigest()
            else: return sha1(string).digest()
        else:
            if hexdigest: return sha1(bytes(string, "utf-8")).hexdigest()
            else: return sha1(bytes(string, "utf-8")).digest()
    @classmethod
    def sha224(self, string: Union[str, bytes, None] = None, hexdigest: bool = True):
        """
        \\@since 0.3.24 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class ModernString
        ```
        Returned is SHA-224 message digest of a string. If `string` is \\
        a string, this string will be used, otherwise it comes to string \\
        currently pointed by the class. That string is **not** changed. \\
        If `hexdigest` is `True`, returned is hexadecimal digest. \\
        Otherwise returned is result in byte format.
        """
        if string is not None and not isinstance(string, (str, bytes, bytearray, memoryview)):
            err = TypeError
            s = f"Inappropriate type of parameter 'string'. Expected a string or None. Received type: {type(string).__name__}"
            raise err(s)
        if not isinstance(hexdigest, bool):
            err = TypeError
            s = f"Inappropriate type of parameter 'hexdigest'. Expected a string or None. Received type: {type(hexdigest).__name__}"
            raise err(s)
        if string is None:
            if hexdigest: return sha224(bytes(self.get())).hexdigest()
            else: return sha224(bytes(self.get())).digest()
        elif isinstance(string, bytes):
            if hexdigest: return sha224(string).hexdigest()
            else: return sha224(string).digest()
        else:
            if hexdigest: return sha224(bytes(string, "utf-8")).hexdigest()
            else: return sha224(bytes(string, "utf-8")).digest()
    @classmethod
    def sha256(self, string: Union[str, bytes, None] = None, hexdigest: bool = True):
        """
        \\@since 0.3.24 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class ModernString
        ```
        Returned is SHA-256 message digest of a string. If `string` is \\
        a string, this string will be used, otherwise it comes to string \\
        currently pointed by the class. That string is **not** changed. \\
        If `hexdigest` is `True`, returned is hexadecimal digest. \\
        Otherwise returned is result in byte format.
        """
        if string is not None and not isinstance(string, (str, bytes, bytearray, memoryview)):
            err = TypeError
            s = f"Inappropriate type of parameter 'string'. Expected a string or None. Received type: {type(string).__name__}"
            raise err(s)
        if not isinstance(hexdigest, bool):
            err = TypeError
            s = f"Inappropriate type of parameter 'hexdigest'. Expected a string or None. Received type: {type(hexdigest).__name__}"
            raise err(s)
        if string is None:
            if hexdigest: return sha256(bytes(self.get())).hexdigest()
            else: return sha256(bytes(self.get())).digest()
        elif isinstance(string, bytes):
            if hexdigest: return sha256(string).hexdigest()
            else: return sha256(string).digest()
        else:
            if hexdigest: return sha256(bytes(string, "utf-8")).hexdigest()
            else: return sha256(bytes(string, "utf-8")).digest()
    @classmethod
    def sha384(self, string: Union[str, bytes, None] = None, hexdigest: bool = True):
        """
        \\@since 0.3.24 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class ModernString
        ```
        Returned is SHA-384 message digest of a string. If `string` is \\
        a string, this string will be used, otherwise it comes to string \\
        currently pointed by the class. That string is **not** changed. \\
        If `hexdigest` is `True`, returned is hexadecimal digest. \\
        Otherwise returned is result in byte format.
        """
        if string is not None and not isinstance(string, (str, bytes, bytearray, memoryview)):
            err = TypeError
            s = f"Inappropriate type of parameter 'string'. Expected a string or None. Received type: {type(string).__name__}"
            raise err(s)
        if not isinstance(hexdigest, bool):
            err = TypeError
            s = f"Inappropriate type of parameter 'hexdigest'. Expected a string or None. Received type: {type(hexdigest).__name__}"
            raise err(s)
        if string is None:
            if hexdigest: return sha384(bytes(self.get())).hexdigest()
            else: return sha384(bytes(self.get())).digest()
        elif isinstance(string, bytes):
            if hexdigest: return sha384(string).hexdigest()
            else: return sha384(string).digest()
        else:
            if hexdigest: return sha384(bytes(string, "utf-8")).hexdigest()
            else: return sha384(bytes(string, "utf-8")).digest()
    @classmethod
    def sha512(self, string: Union[str, bytes, None] = None, hexdigest: bool = True):
        """
        \\@since 0.3.24 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class ModernString
        ```
        Returned is SHA-512 message digest of a string. If `string` is \\
        a string, this string will be used, otherwise it comes to string \\
        currently pointed by the class. That string is **not** changed. \\
        If `hexdigest` is `True`, returned is hexadecimal digest. \\
        Otherwise returned is result in byte format.
        """
        if string is not None and not isinstance(string, (str, bytes, bytearray, memoryview)):
            err = TypeError
            s = f"Inappropriate type of parameter 'string'. Expected a string or None. Received type: {type(string).__name__}"
            raise err(s)
        if not isinstance(hexdigest, bool):
            err = TypeError
            s = f"Inappropriate type of parameter 'hexdigest'. Expected a string or None. Received type: {type(hexdigest).__name__}"
            raise err(s)
        if string is None:
            if hexdigest: return sha512(bytes(self.get())).hexdigest()
            else: return sha512(bytes(self.get())).digest()
        elif isinstance(string, bytes):
            if hexdigest: return sha512(string).hexdigest()
            else: return sha512(string).digest()
        else:
            if hexdigest: return sha512(bytes(string, "utf-8")).hexdigest()
            else: return sha512(bytes(string, "utf-8")).digest()
    @classmethod
    def md5(self, string: Union[str, bytes, None] = None, hexdigest: bool = True):
        """
        \\@since 0.3.24 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class ModernString
        ```
        Returned is MD5 message digest of a string. If `string` is \\
        a string, this string will be used, otherwise it comes to string \\
        currently pointed by the class. That string is **not** changed. \\
        If `hexdigest` is `True`, returned is hexadecimal digest. \\
        Otherwise returned is result in byte format.
        """
        if string is not None and not isinstance(string, (str, bytes, bytearray, memoryview)):
            err = TypeError
            s = f"Inappropriate type of parameter 'string'. Expected a string or None. Received type: {type(string).__name__}"
            raise err(s)
        if not isinstance(hexdigest, bool):
            err = TypeError
            s = f"Inappropriate type of parameter 'hexdigest'. Expected a string or None. Received type: {type(hexdigest).__name__}"
            raise err(s)
        if string is None:
            if hexdigest: return md5(bytes(self.get())).hexdigest()
            else: return md5(bytes(self.get())).digest()
        elif isinstance(string, bytes):
            if hexdigest: return md5(string).hexdigest()
            else: return md5(string).digest()
        else:
            if hexdigest: return md5(bytes(string, "utf-8")).hexdigest()
            else: return md5(bytes(string, "utf-8")).digest()
    @classmethod
    def new(self, *values: str):
        """
        \\@since 0.3.24 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class ModernString
        ```
        Append new string or strings to the class. \\
        Returned is reference to this class.
        """
        if _reckon_init(values) > 0:
            for i in _abroad_init(values):
                self.__loc_arr.append(values[i])
        return self
    @classmethod
    def delete(self, index: int = ..., /):
        """
        \\@since 0.3.24 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class ModernString
        ```
        Remove a string at specified index. If `index` \\
        is an ellipsis, deleted is currently pointed string. \\
        Returned is reference to this class.
        """
        if isinstance(index, Ellipsis):
            del self.__loc_arr[self.__loc_int]
        if isinstance(index, int):
            del self.__loc_arr[index]
        else:
            err = TypeError
            s = f"Parameter 'index' has incorrect type, expected an integer, or leaving this field empty."
            raise err(s)
        return self
    @classmethod
    def drop(self, index: int, /):
        """
        \\@since 0.3.24 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class ModernString
        ```
        Alias to class method `ModernString.delete()`.
        """
        self.delete(index)
        return self
    @classmethod
    def get(self, index: _SupportsIndex = ..., /):
        """
        \\@since 0.3.24 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class ModernString
        ```
        Receive currently pointed string. If `index` is \\
        an integer, returned is string in this index. Throws \\
        `TypeError`, if `index` is neither integer nor ellipsis.
        """
        if isinstance(index, _Ellipsis):
            return self.__loc_arr[self.__loc_int]
        elif isinstance(index, int):
            if (
                (index >= 0 and index > _reckon_init(self.__loc_arr) - 1) or
                (index < 0 and _reckon_init(self.__loc_arr) - abs(index) >= 0)
            ):
                return self.__loc_arr[index]
            else:
                err = ValueError
                s = f"Parameter 'index' leads to out of range."
                raise err(s)
        else:
            err = TypeError
            s = f"Parameter 'index' has incorrect type, expected an integer, or leaving this field empty."
            raise err(s)
    @classmethod
    def set(self, value: str, index: _SupportsIndex = ..., /):
        """
        \\@since 0.3.24 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class ModernString
        ```
        Replace a string at specified index. If `index` is \\
        ellipsis, replaced is string in current item. If item \\
        doesn't exist, throws `ValueError`.
        """
        if not isinstance(value, str):
            err = TypeError
            s = f"First parameter is either empty or has inacceptable type. Expected a string of type '{type(str).__name__}'"
            raise err(s)
        if isinstance(index, Ellipsis):
                self.__loc_arr[self.__loc_int] = value
        elif isinstance(index, int):
            if index < -_reckon_init(value) and index > _reckon_init(value) - 1:
                err = ValueError
                s = "String with that index doesn't exist. Consider making changes in strings already existent."
                raise err(s)
            else:
                self.__loc_arr[index] = value
        else:
            err = TypeError
            s = f"Parameter 'index' has incorrect type: '{type(index).__name__}', expected an integer, or leaving this field empty."
            raise err(s)
        return self
    @classmethod
    def replace(self, oldStrings: _SupportsModernReplace, newStrings: _SupportsModernReplace, applyOn: int = REPLACE_ALL, /): # since 0.3.9
        """
        \\@since 0.3.9 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class ModernString
        ```
        1st and 2nd parameter may be either strings, lists or tuples, 3rd parameter equals `str.replace()` and is optional. \\
        It determines, how many instances of old substrings to replace. `REPLACE_ALL` (before 0.3.24 `ALL`) constant as default value applies \\
        to all occurences (equals `-1`). Possibilities because of complex required parameter types:
        - if 1st parameter is a string and 2nd is a list or tuple, replacement bases on randomizer - from 2nd parameter picks an item, \\
        which will be replaced with old substring. Usable for users that want to suprise others
        - if 1st parameter is a list or tuple and 2nd is a string, all old substrings will be replaced with substring passed to the \\
        2nd parameter
        - if both 1st and 2nd parameters are strings, operation will be simple - nothing changes there, normally invoking `str.replace()` method
        - if both 1st and 2nd parameters are lists or tuples, just make sure that their lengths are equal, otherwise `ValueError` will be raised. \\
        Each item from 1st parameter corresponds with item from 2nd parameter with the same index and these with equal index will be replaced. \\
        It will occur to whole items list or tuple \n
        Returned is string after replacement operation. String provided as 1st parameter isn't mutated. This method is more complex rework of \\
        `str.replace()` method. Also called as deputy of `Tense08.replaceTitled()` method, which was more strict
        """
        conv = self.__loc_arr[self.__loc_int] # since 0.3.9
        # START since since 0.3.24
        if not isinstance(oldStrings, (str, list, tuple)):
            err = TypeError
            s = f"Parameter 'oldStrings' has incorrect type: '{str(type(oldStrings).__name__)}', expected from one of these types: '{type(str).__name__}', '{type(list).__name__}', '{type(tuple).__name__}'."
            raise err(s)
        if not isinstance(newStrings, (str, list, tuple)):
            err = TypeError
            s = f"Parameter 'newStrings' has incorrect type: '{str(type(newStrings).__name__)}', expected from one of these types: '{type(str).__name__}', '{type(list).__name__}', '{type(tuple).__name__}'."
            raise err(s)
        if isinstance(applyOn, int) and (applyOn < -1 or applyOn == 0):
            err = ValueError
            s = "Parameter 'applyOn' cannot contain zero or numbers below -1."
            raise err(s)
        # END since 0.3.24
        # START since 0.3.9
        if (not isinstance(oldStrings, str) and not isinstance(newStrings, str)) and (_reckon_init(oldStrings) != _reckon_init(newStrings)):
            raise ValueError(f"Sizes of 'oldStrings' and 'newStrings' parameters sequence arguments (respectively, '{type(oldStrings).__name__}' and '{type(newStrings).__name__}') are incompatible.")
        # 3rd param is string
        elif isinstance(newStrings, str) and not isinstance(newStrings, (tuple, list)) and isinstance(oldStrings, (tuple, list)):
            for i in _abroad_init(oldStrings): conv = conv.replace(oldStrings[i], newStrings, applyOn)
        # 2nd param is string - cause magic randomizer!
        elif isinstance(oldStrings, str) and not isinstance(oldStrings, (tuple, list)) and isinstance(newStrings, (tuple, list)):
            conv = conv.replace(oldStrings, _random_pick(newStrings), applyOn)
        # 2nd & 3rd params are strings - it just acts normally, just like normal replace method
        elif isinstance(oldStrings, str) and isinstance(newStrings, str) and not isinstance(oldStrings, (list, tuple)) and not isinstance(newStrings, (list, tuple)):
            conv = conv.replace(oldStrings, newStrings, applyOn)
        # 2nd & 3rd params are lists or tuples
        else:
            for i in _abroad_init(list(oldStrings)): conv = conv.replace(oldStrings[i], newStrings[i], applyOn)
        return ModernString(conv) # END since 0.3.9
    @classmethod
    def replaceAll(self, oldStrings: _SupportsModernReplace, newStrings: _SupportsModernReplace, applyOn = REPLACE_ALL, /):
        """
        \\@since 0.3.9 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class ModernString
        ```
        A variation of `replace()` method, which appends all of these versions: lowercased, uppercased, capitalized (titled) and untitled string values \\
        to the inner string list. 1st and 2nd parameter may be either strings, lists or tuples, 3rd parameter equals `str.replace()` and is optional. \\
        It determines, how many instances of old substrings to replace. `ALL` constant as default value applies \\
        to all occurences (equals `-1`). Possibilities because of complex required parameter types:
        - if 1st parameter is a string and 2nd is a list or tuple, replacement bases on randomizer - from 2nd parameter picks an item, \\
        which will be replaced with old substring. Usable for users that want to suprise others
        - if 1st parameter is a list or tuple and 2nd is a string, all old substrings will be replaced with substring passed to the \\
        2nd parameter
        - if both 1st and 2nd parameters are strings, operation will be simple - nothing changes there, normally invoking `str.replace()` method
        - if both 1st and 2nd parameters are lists or tuples, just make sure that their lengths are equal, otherwise `ValueError` will be raised. \\
        Each item from 1st parameter corresponds with item from 2nd parameter with the same index and these with equal index will be replaced. \\
        It will occur to whole items list or tuple \n
        Returned is string after replacement operation. String provided as 1st parameter isn't mutated.
        """
        conv = self.__loc_arr[self.__loc_int]
        if (not isinstance(oldStrings, str) and not isinstance(newStrings, str)) and (reckon(oldStrings) != reckon(newStrings)): raise ValueError("Lists or tuples length aren't equal")
        # 3rd param is string
        elif isinstance(newStrings, str) and not isinstance(newStrings, (tuple, list)) and isinstance(oldStrings, (tuple, list)):
            tmp1: list[str] = oldStrings
            for i in _abroad_init(oldStrings): tmp1.append(oldStrings[i].upper(), oldStrings[i].lower(), oldStrings[i].title(), oldStrings[i].title().swapcase())
            tmp2: list[str] = [newStrings, newStrings.upper(), newStrings.lower(), newStrings.title(), newStrings.title().swapcase()]
            for i in _abroad_init(tmp1):
                if tmp1[i].swapcase().istitle(): conv = conv.replace(tmp1[i], tmp2[4], applyOn)
                elif tmp1[i].istitle(): conv = conv.replace(tmp1[i], tmp2[3], applyOn)
                elif tmp1[i].islower(): conv = conv.replace(tmp1[i], tmp2[2], applyOn)
                elif tmp1[i].isupper(): conv = conv.replace(tmp1[i], tmp2[1], applyOn)
                else: conv = conv.replace(tmp1[i], tmp2[0], applyOn)
        # 2nd param is string - cause magic randomizer!
        elif isinstance(oldStrings, str) and not isinstance(oldStrings, (tuple, list)) and isinstance(newStrings, (tuple, list)):
            tmp1: list[str] = newStrings
            for i in _abroad_init(newStrings): tmp1.append(newStrings[i].upper(), newStrings[i].lower(), newStrings[i].title(), newStrings[i].title().swapcase())
            tmp2: list[str] = [oldStrings, oldStrings.upper(), oldStrings.lower(), oldStrings.title(), oldStrings.title().swapcase()]
            tmp3 = tmp1[randint(0, _reckon_init(tmp1) - 1)]
            if tmp3.swapcase().istitle(): conv = conv.replace(tmp2[4], tmp3, applyOn)
            elif tmp3.istitle(): conv = conv.replace(tmp2[3], tmp3, applyOn)
            elif tmp3.islower(): conv = conv.replace(tmp2[2], tmp3, applyOn)
            elif tmp3.isupper(): conv = conv.replace(tmp2[1], tmp3, applyOn)
            else:
                conv = conv.replace(tmp2[0], tmp3, applyOn)
        # 2nd & 3rd params are strings - it just acts normally, just like normal replace method
        elif isinstance(oldStrings, str) and isinstance(newStrings, str) and not isinstance(oldStrings, (list, tuple)) and not isinstance(newStrings, (list, tuple)):
            tmp1: list[str] = [oldStrings, oldStrings.upper(), oldStrings.lower(), oldStrings.title(), oldStrings.title().swapcase()]
            tmp2: list[str] = [newStrings, newStrings.upper(), newStrings.lower(), newStrings.title(), newStrings.title().swapcase()]
            for i in _abroad_init(tmp1):
                conv = conv.replace(tmp1[i], tmp2[i], applyOn)
        # 2nd & 3rd params are lists or tuples
        elif isinstance(oldStrings, (list, tuple)) and isinstance(newStrings, (list, tuple)):
            tmp1: list[str] = oldStrings
            tmp2: list[str] = newStrings
            for i in _abroad_init(oldStrings):
                tmp1.append(_s for _s in (oldStrings[i].upper(), oldStrings[i].lower(), oldStrings[i].title(), oldStrings[i].title().swapcase()))
                tmp2.append(_s for _s in (newStrings[i].upper(), newStrings[i].lower(), newStrings[i].title(), newStrings[i].title().swapcase()))
            for i in _abroad_init(tmp1):
                conv = conv.replace(str(tmp1[i]), str(tmp2[i]), applyOn)
        return ModernString(conv)
    @classmethod
    def sanitize(self, string: Optional[str] = None, mode: _SanitizeMode = SANITIZE_AROUND) -> str:
        """
        \\@since 0.3.24 (experimental) \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class ModernString
        ```
        Rewritten method from C++. Works like `trim()` function, and this method is inspired \\
        by it. There are 6 modes this method supports (parameter `mode`; `self` = this class):
        - `0 / self.SANITIZE_AROUND` (default) removes whitespaces around the string.
        - `1 / self.SANITIZE_ALL` removes all whitespaces no matter their placement. 
        - `2 / self.SANITIZE_ACF` removes all whitespaces, keeping only one between words. EXPERIMENTAL!
        - `3 / self.SANITIZE_LEFT` removes all whitespaces placed on the left of the string.
        - `4 / self.SANITIZE_RIGHT` removes all whitespaces placed on the right of the string.
        - `5 / self.SANITIZE_CENTER` removes all whitespaces placed inside the string.
        """
        def ws(char: str): return _reckon_init(char) == 1 and char in "\f\n\r\t\v"
        # according to JavaScript regular expressions
        # this string with all these special characters is all the matters
        if string is None:
            tmps = self.__loc_arr[self.__loc_int]
        elif isinstance(string, str):
            tmps = string
        else:
            err = TypeError
            s = f"Parameter 'string' isn't of type 'str'. Please ensure that this parameter is either empty or has argument of type 'str'."
            raise err(s)
        if not isinstance(mode, int):
            err = TypeError
            s = f"Parameter 'mode' isn't of type 'int'. Please ensure that this parameter is either empty or has argument of type 'int'."
            raise err(s)
        s = ""
        a = [""]
        EMPTY = " "
        a.clear()
        for c in tmps: a.append(c)
        if mode == self.SANITIZE_AROUND: # 0
            g1, g2 = (0, _reckon_init(a) - 1)
            while ws(a[g1]): g1 += 1
            while ws(a[g2]): g2 -= 1
            for i in _abroad_init(g1, g2 + 1):
                s += a[i]
        elif mode == self.SANITIZE_ALL: # 1
            for i in _abroad_init(a):
                if not ws(a[i]):
                    s += a[i]
        elif mode == self.SANITIZE_ACF: # 2
            g1, g2 = (0, _reckon_init(a) - 1)
            while ws(a[g1]): g1 += 1
            while ws(a[g2]): g2 -= 1
            for i in _abroad_init(g1, g2 + 1):
                if ws(a[i]) and ws(a[i + 1]):
                    s += EMPTY
                else:
                    s += a[i]
        elif mode == self.SANITIZE_LEFT: # 3
            g = 0
            while ws(a[g]): g += 1
            while g < _reckon_init(a):
                s += a[g]
                g += 1
        elif mode == self.SANITIZE_RIGHT: # 4
            g = _reckon_init(a) - 1
            while ws(a[g]): g -= 1
            for i in _abroad_init(g + 1):
                s += a[i]
        elif mode == self.SANITIZE_CENTER: # 5
            g1, g2 = (0, _reckon_init(a) - 1)
            while ws(a[g1]): g1 += 1
            while ws(a[g2]): g2 -= 1
            for i in _abroad_init(g1): s += EMPTY
            for i in _abroad_init(g1, g2 + 1):
                if not ws(a[i]): s += a[i]
            for i in _abroad_init(g2 + 1, a): s += EMPTY
        else:
            err = ValueError
            s = f"Parameter 'mode' as an integer does not accept values out from range 0-5. For uncertainty, consider using one of constants inside this class."
            raise err(s)
        return s

_ReckonType = Union[_ReckonTypePre[_T], ModernString]
_AbroadValue1 = Union[_AbroadValue1Pre[_T], ModernString]
_AbroadValue2 = Union[_AbroadValue2Pre[_T], ModernString]
_AbroadModifier = Union[_AbroadModifierPre[_T], ModernString]

def abroad(value1: _AbroadValue1[_T1], /, value2: _AbroadValue2[_T2] = None, modifier: _AbroadModifier[_T3] = None):
    """
    \\@since 0.3.9  (standard since 0.3.10) \\
    \\@modified 0.3.25 (moved slash to between `value1` and `value2`) \\
    \\@author Aveyzan
    https://aveyzan.glitch.me/tense/py/function.abroad.html
    ```ts \\
    in module tense.primary
    ```
    ```py

    # Syntax
    for i in abroad(...): ...
    ```
    Same function as `range()`, but more improved. `abroad()` has the following advantages:
    - supports countable objects, without using `len()` function, for all parameters
    - no overloads, only one version of function; that means there are 3 parameters, last 2 are optional
    - returns mutable sequence of integers, while `range()` returns integer-typed immutable sequence
    - `abroad()` is a function to faciliate recognizion; `range` is simultaneously a function and class
    - modifier will be always positive, negative values doesn't matter (!)
    - sequence begins from least of `value1` and `value2`, if `value2` is `bool` or `None`, begins \\
    from 0 to `value1` (or from `value1` to 0, if `value1` is negative)
    - `value2` as floating-point number allows the truncated integer to become endpoint, which will \\
    be included

    If `value2` is set to `None`, it will behave identically as `True` boolean value. It allows the \\
    iteration to go normally. Setting to `False` will flip the order and making all integers negative, \\
    put in ascending order.

    Function supports `range` class itself. \\
    Below `range()` values and `abroad()` function equivalents:
    ```py \\
    range(23) = abroad(23)
    range(2, 23) = abroad(2, 23)
    range(2, 24) = abroad(2, 23.6) # or just abroad(2, 24)
    range(23, 5, -1) = abroad(23, 5) # modifier skipped, default is 1
    range(23, 5, -3) = abroad(23, 5, 3) # there 3 also can be -3
    range(len("Perfect!")) = abroad("Perfect!")
    ``` \n
    By providing `range()` as an argument of this function, it simultaneously allows to alter the \\
    sequence from immutable to mutable. It is actually recommended to keep the same endpoint as \\
    `range` has, otherwise it may bind with returning not these results. Keep on mind this syntax:
    ```py \\
    abroad(range(0, x, m), x, m) # x - endpoint; m (optional) - step/modifier
    ```
    where `x` is stop/endpoint and `m` is step/modifier. That `m` can be omitted. \\
    That number 0 is set specially, because it may lead with returning unexpected \\
    sequence of numbers. But if it is intentional - sure, why not! But from Aveyzan's \\
    perspective it isn't recommended. \\
    For example:
    ```py \\
    abroad(range(0, 13), 13) # empty sequence
    abroad(range(0, 13), 13.24) # 13
    abroad(range(0, 13), 13, 2) # empty sequence
    abroad(range(0, 13, 2), 13, 2) # 7, 9, 11 (13 / 2 (round up) = 7)
    abroad(range(5, 13), 13) # 7, 8, 9, 10, 11, 12 (13 - 5 - 1 = 7)
    ```

    If `range` function is used commonly, with one parameter, syntax will be shortened:
    ```py \\
    abroad(range(x)) # x - endpoint
    ```
    where `x` is stop/endpoint. This is the common way to convert the immutable sequence to mutable.

    Usages:
    ```py \\
    # value1 = integer | Countable
    # value2 = None
    # modifier = 1
    abroad(92) # 0, 1, 2, 3, ..., 90, 91
    abroad(-92) # -92, -91, -90, ..., -2, -1
    abroad(["jump", "on", "the", "roof"]) # 0, 1, 2, 3
    abroad("Hello!") # 0, 1, 2, 3, 4, 5

    # value1 = integer
    # value2 = integer, float
    # modifier = 1
    abroad(92, 3) # 92, 91, 90, ..., 5, 4
    abroad(3, 92) # 3, 4, 5, ..., 90, 91
    abroad(92, 3.05) # 92, 91, 90, ..., 5, 4, 3 (!)
    abroad(3, 92.05) # 3, 4, 5, ..., 90, 91, 92 (!)

    # value1 = integer
    # value2 = bool | None | ... (None and ellipsis equal True)
    # modifier = 1
    abroad(92, True) # 0, 1, 2, 3, ..., 90, 91
    abroad(-92, True) # -92, -91, -90, ..., -2, -1
    abroad(92, False) # -92, -91, -90, ..., -2, -1
    abroad(-92, False) # 0, 1, 2, 3, ..., 90, 91

    # value1 = complex (under experiments)
    # value2 = bool | None | ... (None and ellipsis equal True)
    # modifier = 1
    abroad(3+9j, True) # 3, 4, ..., 7, 8
    abroad(3+9j, False) # -9, -8, ..., -5, -4
    abroad(3-9j, True) # 3, 2, 1, ..., -7, -8
    abroad(3-9j, False) # 7, 6, 5, ..., -3, -4
    abroad(-3+9j, True) # -3, -2, ..., 7, 8
    abroad(-3+9j, False) # -9, -8, ..., 1, 2
    abroad(-3-9j, True) # -3, -4, -5, ..., -7, -8
    abroad(-3-9j, False) # 7, 6, 5, ..., 3, 2

    # value1 = integer
    # value2 = bool | None (None equals True)
    # modifier = 4 (-4 will also result 4)
    abroad(92, True, 4) # 0, 4, 8, 12, ..., 84, 88
    abroad(-92, True, 4) # -92, -88, -84, ..., -8, -4
    abroad(92, False, 4) # -92, -88, -84, ..., -8, -4
    abroad(-92, False, 4) # 0, 4, 8, 12, ..., 84, 88
    ```
    """
    if isinstance(value1, ModernString): v1 = value1.get()
    else: v1 = value1
    if isinstance(value2, ModernString): v2 = value2.get()
    else: v2 = value2
    if isinstance(modifier, ModernString): m = modifier.get()
    else: m = modifier
    return _abroad_init(v1, v2, m)

def reckon(*countables: _ReckonType[_T]):
    """
    \\@since 0.3.7 (standard since 0.3.7) \\
    \\@modified 0.3.25 \\
    \\@author Aveyzan
    https://aveyzan.glitch.me/tense/tsl/reckon.html
    ```ts \\
    in module tense.primary
    ```
    Efficient build 0.3.20: Since that version function also supports \\
    deques and sets, moreover, user can now assign more than one countables \\
    (what in Python is `Sized` class counterpart). Thereupon, function will \\
    sum lengths of all countable objects - no matter if they are mutable or not.

    Supported types: `set`, `deque`, `list`, `str`, `tuple`, `dict` (counts pairs), \\
    `bytes`, `bytearray`, `memoryview`, `range`, `mmap`, `array`, `enumerate`, \\
    `frozenset`, `typing.Counter`, `defaultdict` (also counts pairs), \\
    `TextIOWrapper` (all chars in a file). Since 0.3.24, function accepts remaining \\
    types from `open()` function: `FileIO`, `BufferedWriter`, `BufferedRandom`, \\
    `BufferedReader` and `IO`, since 0.3.25: `BufferedRWPair`, `BytesIO`, \\
    `StringIO`, `Mapping`, `MutableMapping`, `OrderedDict`, `ChainMap`, \\
    `MutableSet`, `AbstractSet`, `Iterable`, `Sequence` and `MutableSequence`.
    """
    i = 0
    for e in countables:
        if isinstance(e, ModernString):
            for _ in e.get():
                i += 1
        else: i += _reckon_init(e)
    return i

def reckonLeast(*countables: _ReckonType[_T]):
    """
    \\@since 0.3.25 (standard since 0.3.25) \\
    \\@author Aveyzan
    ```ts \\
    in module tense.primary
    ```
    Get least length from iterable objects passed.
    """
    n = 0
    for e in countables:
        if n > reckon(e):
            n = reckon(e)
    return n

def reckonGreatest(*countables: _ReckonType[_T]):
    """
    \\@since 0.3.25 (standard since 0.3.25) \\
    \\@author Aveyzan
    ```ts \\
    in module tense.primary
    ```
    Get greatest length from iterable objects passed.
    """
    n = 0
    for e in countables:
        if n < reckon(e):
            n = reckon(e)
    return n

def reckonIsLeast(countable1: _ReckonType[_T], countable2: _ReckonType[_T], /):
    """
    \\@since 0.3.25 (standard since 0.3.25) \\
    \\@author Aveyzan
    ```ts \\
    in module tense.primary
    ```
    Comparison: Check whether first argument is length-less than the second.
    """
    return reckon(countable1) < reckon(countable2)


def reckonIsGreater(countable1: _ReckonType[_T], countable2: _ReckonType[_T], /):
    """
    \\@since 0.3.25 (standard since 0.3.25) \\
    \\@author Aveyzan
    ```ts \\
    in module tense.primary
    ```
    Comparison: Check whether first argument is length-greater than the second.
    """
    return reckon(countable1) > reckon(countable2)

class Reckon:
    """
    \\@since 0.3.25 (standard since 0.3.25) \\
    \\@author Aveyzan
    ```ts \\
    // created 05.07.2024
    in module tense.primary
    ```
    Class version of function `reckon()`
    """
    __countables = None
    def __init__(self, *countables: _ReckonType[_T]):
        self.__countables: list[_ReckonType[_T]] = []
        for e in countables:
            self.__countables.append(e)
    def get(self, specific: Optional[int] = None, /):
        """
        \\@since 0.3.25 (standard since 0.3.25) \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "method" in class Reckon
        ```
        Return size of all sizeable objects together. \\
        If `specific` is not `None`, returned is only \\
        at specified index. Out of range is typical \\
        Python error.
        """
        if specific is not None: return reckon(self.__countables[specific])
        else: return reckon(self.__countables)
    def least(self):
        """
        \\@since 0.3.25 (standard since 0.3.25) \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "method" in class Reckon
        ```
        Get least length from iterable objects passed to the constructor.
        """
        n = 0
        for e in self.__countables:
            if n > reckon(e):
                n = reckon(e)
        return n
    def greatest(self):
        """
        \\@since 0.3.25 (standard since 0.3.25) \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "method" in class Reckon
        ```
        Get greatest length from iterable objects passed to the constructor.
        """
        n = 0
        for e in self.__countables:
            if n < reckon(e):
                n = reckon(e)
        return n
    def isLeast(self, index1: int, index2: int, /):
        """
        \\@since 0.3.25 (standard since 0.3.25) \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "method" in class Reckon
        ```
        Both arguments lead to sizeable objects passed to the constructor. \\
        Returned is `True`, if size of object at index `index1` is least than \\
        object at index `index2`
        """
        return reckon(self.__countables[index1]) < reckon(self.__countables[index2])
    def isGreater(self, index1: int, index2: int, /):
        """
        \\@since 0.3.25 (standard since 0.3.25) \\
        \\@author Aveyzan
        ```ts \\
        // created 05.07.2024
        "method" in class Reckon
        ```
        Both arguments lead to sizeable objects passed to the constructor. \\
        Returned is `True`, if size of object at index `index1` is greater than \\
        object at index `index2`
        """
        return reckon(self.__countables[index1]) > reckon(self.__countables[index2])

class protogen(MutableSequence[int]):
    """
    \\@since 0.3.20 (standard since 0.3.20) \\
    \\@modified 0.3.24, 0.3.25 \\
    \\@author Aveyzan \\
    https://aveyzan.glitch.me/tense/py/function.abroad.html
    ```ts \\
    in module tense.primary
    ```
    ```py

    # Usage
    from tense import protogen
    sequence = protogen(...)
    for ram in sequence: ...
    ```

    This class is a joke, but alternative of `abroad()` function.
    """
    _ProtogenActivate = list[RAM]
    def __new__(self, value1: _AbroadValue1[_T1], /, value2: _AbroadValue2[_T2] = None, modifier: _AbroadModifier[_T3] = None) -> _ProtogenActivate:
        """
        \\@since 0.3.20 (standard since 0.3.20) \\
        \\@modified 0.3.24, 0.3.25 \\
        \\@author Aveyzan \\
        https://aveyzan.glitch.me/tense/08/function.abroad.html
        ```ts \\
        in module tense.primary
        ```
        ```py

        # i or ram variable equals RAM type, which is int equivalent
        # protogen equals abroad() function
        for i in protogen(...): ...
        for ram in protogen(...): ...
        ```
        Construct a new `protogen` object, which will produce next integers, until an endpoint is caught. \\
        For more information, see `abroad()` function.
        """
        return abroad(value1, value2, modifier)
    @staticmethod
    def info():
        """Receive information about this class."""
        print(
            f"Class name: protogen",
            f"Class name for furry community: a furry species",
            f"Class author: Aveyzan",
            f"Extends: MutableSequence[int] (can be recognized as list)",
            f"Created: 31.10.2023 (31st October 2023)",
            f"Available since: Tense 0.3.20",
            f"Standard since: Tense 0.3.20",
            f"Main target: replacing range() function due to functionality",
            f"Usage: similar to range(), identical to abroad()",
            sep = "\n"
        )

class YamiTk:
    """
    \\@since 0.3.24 \\
    \\@author Aveyzan
    ```ts \\
    in module tense.primary
    ```
    TensePy Tk class from `tkinter` module equivalent.
    """
    __loc_tk = None
    __loc_frame = None
    __loc_label = None
    __loc_button = None
    __loc_buttons = None
    __loc_checkbutton = None
    __loc_checkbuttons = None
    __loc_radiobutton = None
    __loc_radiobuttons = None
    def __init__(self, screenName: Optional[str] = None, baseName: Optional[str] = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: Union[str, None] = None) -> None:
        self.__loc_tk = tk.Tk(
            screenName = screenName,
            baseName = baseName,
            className = className,
            useTk = useTk,
            sync = sync,
            use = use
        )
        self.__loc_frame = tk.Frame(self.__loc_tk)
    def mainloop(self, n = 0):
        """
        \\@since 0.3.24 \\
        \\@author Aveyzan
        ```ts \\
        "method" in class YamiTk
        ```
        Call main loop of Tk
        """
        if self.__loc_tk is not None:
            self.__loc_tk.mainloop(n)
        else:
            err, s = (tcs.NotInitializedError, f"Class '{__class__.__name__}' was not initialized.")
            raise err(s)
        return self
    def setWindowSize(self, x: int, y: int, /):
        """
        \\@since 0.3.26a3 \\
        \\@author Aveyzan
        ```ts \\
        "method" in class YamiTk
        ```
        Set the window size measured in pixels. \\
        `x` means width, and `y` means height of the window
        """
        if self.__loc_tk is not None:
            self.__loc_tk.geometry(f"{x}x{y}")
        else:
            err, s = (tcs.NotInitializedError, f"Class '{__class__.__name__}' was not initialized.")
            raise err(s)
        return self
    def setMaxWindowSize(self, x: int, y: int, /):
        """
        \\@since 0.3.26a3 \\
        \\@author Aveyzan
        ```ts \\
        "method" in class YamiTk
        ```
        Set the max window size measured in pixels. \\
        `x` means width, and `y` means height of the window
        """
        if self.__loc_tk is not None:
            self.__loc_tk.maxsize(x, y)
        else:
            err, s = (tcs.NotInitializedError, f"Class '{__class__.__name__}' was not initialized.")
            raise err(s)
        return self
    def setTitle(self, title: str, /):
        """
        \\@since 0.3.26a3 \\
        \\@author Aveyzan
        ```ts \\
        "method" in class YamiTk
        ```
        Set title of the window
        """
        if self.__loc_tk is not None:
            self.__loc_tk.title(title)
        else:
            err, s = (tcs.NotInitializedError, f"Class '{__class__.__name__}' was not initialized.")
            raise err(s)
        return self
    @property
    def getTk(self):
        """
        \\@since 0.3.26a3 \\
        \\@author Aveyzan
        ```ts \\
        "property" in class YamiTk
        ```
        Return `tkinter.Tk` instance within the class
        """
        if self.__loc_tk is None:
            err, s = (tcs.NotInitializedError, f"Class '{__class__.__name__}' was not initialized.")
            raise err(s)
        return self.__loc_tk
    @property
    def getFrame(self):
        """
        \\@since 0.3.26a3 \\
        \\@author Aveyzan
        ```ts \\
        "property" in class YamiTk
        ```
        Return `tkinter.Frame` instance within the class
        """
        if self.__loc_frame is None:
            err, s = (tcs.NotInitializedError, f"Class '{__class__.__name__}' was not initialized.")
            raise err(s)
        return self.__loc_frame
    def setFrame(self, frame: tk.Frame, /):
        """
        \\@since 0.3.26a3 \\
        \\@author Aveyzan
        ```ts \\
        "method" in class YamiTk
        ```
        Overwrite current `tkinter.Frame` instance
        """
        if self.__loc_frame is None:
            err, s = (tcs.NotInitializedError, f"Class '{__class__.__name__}' was not initialized.")
            raise err(s)
        elif not isinstance(frame, tk.Frame):
            err, s = (TypeError, "Parameter 'frame' is not of instance 'tkinter.Frame'.")
            raise err(s)
        else:
            self.__loc_frame = frame
        return self
    def setLabel(self, label: tk.Label, /):
        """
        \\@since 0.3.26a3 \\
        \\@author Aveyzan
        ```ts \\
        "method" in class YamiTk
        ```
        Overwrite current `tkinter.Label` instance or set a new value
        """
        if self.__loc_frame is None:
            err, s = (tcs.NotInitializedError, f"Class '{__class__.__name__}' was not initialized.")
            raise err(s)
        elif not isinstance(label, tk.Label):
            err, s = (TypeError, "Parameter 'label' is not of instance 'tkinter.Label'.")
            raise err(s)
        else:
            self.__loc_label = label
        return self
    
    

if __name__ == "__main__":
    err = RuntimeError
    s = "This file is not for compiling, moreover, this file does not have a complete TensePy declarations collection. Consider importing module 'tense' instead."
    raise err(s)

del re, sys, RAM