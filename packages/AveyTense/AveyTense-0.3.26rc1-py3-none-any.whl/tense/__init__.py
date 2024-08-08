"""
# TensePy

\\@since 0.3.24 \\
\\@author Aveyzan
```ts \\
module tense
```
Users, which use Python 3.9 or higher, **can use this module**. For least versions use module `tense_eight`. \\
Documentation: https://aveyzan.glitch.me/tense/py.html

This module holds complete collection of TensePy declarations via importing submodule `tense.extensions`. \\
Submodules:
- `tense.eight` - (for 0.3.26b2) providing accordance with Python versions below 3.9. Moved to module \\
    `tense_eight`.
- `tense.tcs` - types and constants for TensePy
- `tense.fencord` - connection with Discord. Nevertheless you are obligated to have `discord` \\
    module installed
- `tense.primary` - holds first declarations, like functions `abroad()` and `reckon()`
- `tense.extensions` - wrapper of NennɅI classes extended by class `tense.Tense`
"""

import sys

if sys.version_info < (3, 9):
    err, s = (RuntimeError, "Use 'tense.eight' module for Python versions below 3.9.")
    raise err(s)

import tense.tcs as tcs, tense.primary as t, inspect, time, warnings, uuid
from collections import deque
from tense.extensions import *
from tense.primary import *
from tkinter import BooleanVar, StringVar


# between @since and @author there is unnecessarily long line spacing
# hence this warning is being thrown; it is being disabled.
warnings.filterwarnings("ignore")

_var = tcs.TypeVar
_uni = tcs.Union
_lit = tcs.Literal
_opt = tcs.Optional
_cal = tcs.Callable
_cm = classmethod
_sm = staticmethod
_p = property

_T = _var("_T")
_T_strseq = _var("_T_strseq", bound = tcs.ShuffleType[tcs.Any])

_Color = tcs.Union[int, str, None]
_Bits = tcs.Literal[3, 4, 8, 24]
_ProbabilityType = tcs.ProbabilityType[_T] # expected int
_ProbabilitySeqNoDict = _uni[list, deque, set, frozenset, tuple]
_SequenceLike = tcs.TypeOrFinalVarType[tcs.PickSequence[_T]]
_StringOrStringSequence = _uni[_T, tcs.PickSequence[_T]] # expected str
_FileType = tcs.FileType
_FileMode = tcs.FileMode
_FileOpener = tcs.FileOpener
_EnchantedBookQuantity = tcs.EnchantedBookQuantity
_TicTacToeBoard = tcs.TicTacTorBoarrd

_ErrorType = _uni[
    UnicodeDecodeError, UnboundLocalError, UnicodeEncodeError, UnicodeError, UnicodeTranslateError, RuntimeError, KeyError, TabError, NameError, TypeError, IndexError, ValueError, BufferError, EOFError,
    ImportError, LookupError, MemoryError, SyntaxError, TimeoutError, OSError, AssertionError, AttributeError, ZeroDivisionError, RecursionError, ReferenceError, ConnectionAbortedError, ConnectionError,
    ConnectionRefusedError, ConnectionResetError, OverflowError, ArithmeticError, BrokenPipeError, FileExistsError, PermissionError, IndentationError, InterruptedError, ChildProcessError, FileNotFoundError,
    IsADirectoryError, NotImplementedError,
    tcs.MissingValueError, tcs.IncorrectValueError, tcs.NotInitializedError, tcs.NotInvocableError, tcs.NotComparableError, tcs.NotIterableError, tcs.NotReassignableError, tcs.InitializedError
]
_Ellipsis = tcs.Ellipsis

class Tense(NennɅIAbroads, NennɅIStringz, NennɅIRandomize, Time, Math, tcs.Positive, tcs.Negative, tcs.Invertible):
    """
    \\@since 0.3.24 (standard since 0.3.24) \\
    \\@author Aveyzan
    ```ts \\
    in module tense
    ```
    Root of TensePy for Python 3.9 or above, which cannot be subclassed \\
    before version 0.3.26b3.

    This class extends every NennɅI class defined in `tense.extensions` \\
    module. https://aveyzan.glitch.me/tense/py.html
    """
    import random as __ra, uuid as __uu, warnings as __wa, re as __re, tense.tcs as tcs, time as __ti, tkinter as __tk # math as __ma
    PROBABILITY_COMPUTE = -1
    @_p
    def version(self):
        return t.TENSE_VERSION.receive()
    """since 0.3.24"""
    __formername__ = "Tense08"
    def __init__(self) -> None:
        e = super().fencordFormat()
        print(f"\33[1;90m{e}\33[1;36m INITIALIZATION\33[0m Class '{__class__.__name__}' was successfully initalized. Line {inspect.currentframe().f_back.f_lineno}")
    @_cm
    def __str__(self):
        e = super().fencordFormat()
        if self.__formername__ != "Tense08":
            err, s = (ValueError, f"When invoking string constructor of '{self.__name__}', do not rename variable '__formername__'")
            raise err(s)
        try:
            subcl = f"'{self.__subclasses__()[0]}', "
            for i in abroad(1, self.__subclasses__()):
                subcl += f"'{self.__subclasses__()[i]}', "
            subcl = re.sub(r", $", "", subcl)
        except IndexError:
            subcl = f"'{NennɅIAbroads.__name__}', '{NennɅIRandomize.__name__}, '{NennɅIStringz.__name__}', '{t.Math.__name__}', '{t.Time.__name__}'"
        return f"""
            \33[1;90m{e}\33[1;38;5;51m INFORMATION\33[0m Basic '{self.__name__}' class information (in module 'tense')

            Created by Aveyzan for version 0.3.24 as a deputy of cancelled class '{self.__formername__}'. The '{self.__name__}' class is a subclass of various classes located inside other
            TensePy files: {subcl}. Class itself cannot be subclassed. Generally speaking, the '{self.__name__}' class
            is a collection of many various methods inherited from all of these classes, but also has some defined within its body itself, like methods: probability(),
            random(), pick() etc.
        """
    @_cm
    def __pos__(self):
        "Return information about this class. Since 0.3.26c1"
        return self.__str__()
    @_cm
    def __neg__(self):
        "Return information about this class. Since 0.3.26c1"
        return self.__str__()
    @_cm
    def __invert__(self):
        "Return information about this class. Since 0.3.26c1"
        return self.__str__()
    @_cm
    def isNone(self, value) -> tcs.TypeIs[None]:
        """
        \\@since 0.3.26b3 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        Determine whether a value is of type `None`
        """
        return value is None
    @_cm
    def isBool(self, v: object) -> tcs.TypeIs[bool]:
        """
        \\@since 0.3.26b3 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        Determine whether a value is of type `bool`
        """
        return v is True or v is False
    @_cm
    def isBoolean(self, v: object) -> tcs.TypeIs[bool]:
        """
        \\@since 0.3.26c1 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        Alias to `Tense.isBool()`

        Determine whether a value is of type `bool`
        """
        return v is True or v is False
    @_cm
    def isInt(self, v: object) -> tcs.TypeIs[int]:
        """
        \\@since 0.3.26b3 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        Determine whether a value is of type `int`
        """
        return isinstance(v, int)
    @_cm
    def isInteger(self, v: object) -> tcs.TypeIs[int]:
        """
        \\@since 0.3.26c1 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        Alias to `Tense.isInt()`

        Determine whether a value is of type `int`
        """
        return isinstance(v, int)
    @_cm
    def isFloat(self, v: object) -> tcs.TypeIs[float]:
        """
        \\@since 0.3.26b3 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        Determine whether a value is of type `float`
        """
        return isinstance(v, float)
    @_cm
    def isComplex(self, v: object) -> tcs.TypeIs[complex]:
        """
        \\@since 0.3.26b3 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        Determine whether a value is of type `complex`
        """
        return isinstance(v, complex)
    @_cm
    def isStr(self, v: object) -> tcs.TypeIs[str]:
        """
        \\@since 0.3.26b3 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        Determine whether a value is of type `str`
        """
        return isinstance(v, str)
    @_cm
    def isString(self, v: object) -> tcs.TypeIs[str]:
        """
        \\@since 0.3.26c1 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        Alias to `Tense.isStr()`

        Determine whether a value is of type `str`
        """
        return isinstance(v, str)
    @_cm
    def isTuple(self, v: object) -> tcs.TypeIs[tuple[tcs.Any, ...]]:
        """
        \\@since 0.3.26c1 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        Determine whether a value is of type `tuple`
        """
        return isinstance(v, tuple)
    @_cm
    def isList(self, v: object) -> tcs.TypeIs[list[tcs.Any]]:
        """
        \\@since 0.3.26c1 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        Determine whether a value is of type `list`
        """
        return isinstance(v, list)
    @_cm
    def shuffle(self, v: _T_strseq) -> _T_strseq:
        """
        \\@since 0.3.26c1
        ```ts \\
        "class method" in class Tense
        ```
        Shuffle a string or a list. Comparing to `random.shuffle()` in case of lists, \\
        shuffled list is returned and the one passed to the parameter isn't modified.
        """
        if self.isStr(v):
            return super().randomizeStr2(v)
        else:
            tmp = v
            self.__ra.shuffle(tmp)
            return tmp
    @_cm
    def print(self, *values: object, separator: _opt[str] = " ", ending: _opt[str] = "\n", file: _opt[str] = None, flush: bool = False, invokeAs = "INSERTION"):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        Same as `print()`, just with `INSERTION` beginning. It can be \\
        changed with `invokeAs` parameter. Since 0.3.26a1 this method \\
        returns reference to this class.
        """
        e = super().fencordFormat()
        print(f"\33[1;90m{e}\33[1;38;5;45m {invokeAs}\33[0m", *values, sep = separator, end = ending, file = file, flush = flush)
        return self
    @_cm
    def random(self, x: int, y: int, /):
        """
        \\@since 0.3.24 (standard since 0.3.25) \\
        \\@lifetime ≥ 0.3.24 \\
        \\@modified 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        Return a pseudo-random integer from range [x, y], including both points. If `x` is \\
        greater than `y`, returned is random integer from range [y, x]. If `x` and `y` are equal, \\
        returned is `x`. This interesting move perhaps doesn't return a random number, both \\
        points may not together generate floating-point numbers, since this method returns \\
        integer!
        """
        # _x = x if self.isInt(x) else +x
        # _y = y if self.isInt(y) else +y
        # return super().randomizeInt(_x, _y)
        return super().randomizeInt(x, y)
    @_cm
    def uuidPrimary(self, node: _opt[tcs.TypeOrFinalVarType[int]] = None, clockSeq: _opt[tcs.TypeOrFinalVarType[int]] = None):
        """
        \\@since 0.3.26a1 \\
        \\@author Aveyzan
        ```ts \\
        // created 20.07.2024
        "class method" in class Tense
        ```
        Return an UUID from host ID, sequence number and the current time.
        """
        _n = node if self.isInt(node) or self.isNone(node) else +node
        _c = clockSeq if self.isInt(clockSeq) or self.isNone(clockSeq) else +clockSeq
        return self.__uu.uuid1(node = _n, clock_seq = _c)
    @_cm
    def uuidMd5(self, namespace: tcs.TypeOrFinalVarType[uuid.UUID], name: tcs.TypeOrFinalVarType[_uni[str, StringVar]]):
        """
        \\@since 0.3.26a1 \\
        \\@author Aveyzan
        ```ts \\
        // created 20.07.2024
        "class method" in class Tense
        ```
        Return an UUID from the MD5 (Message Digest) hash of a namespace UUID and a name
        """
        _ret1 = namespace if isinstance(namespace, self.__uu.UUID) else +namespace
        _ret2 = name if self.isStr(name) or isinstance(name, self.__tk.StringVar) else +name
        _ret2 = _ret2 if self.isStr(_ret2) else _ret2.get()
        return self.__uu.uuid3(namespace = _ret1, name = _ret2)
    @_cm
    def uuidRandom(self):
        """
        \\@since 0.3.26a1 \\
        \\@author Aveyzan
        ```ts \\
        // created 20.07.2024
        "class method" in class Tense
        ```
        Return a random UUID
        """
        return self.__uu.uuid4()
    @_cm
    def uuidSha1(self, namespace: tcs.TypeOrFinalVarType[__uu.UUID], name: tcs.TypeOrFinalVarType[_uni[str, StringVar]]):
        """
        \\@since 0.3.26a1 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        Return an UUID from the SHA-1 (Secure Hash Algorithm) hash of a namespace UUID and a name
        """
        _ret1 = namespace if isinstance(namespace, self.__uu.UUID) else +namespace
        _ret2 = name if self.isStr(name) or isinstance(name, StringVar) else +name
        _ret2 = _ret2 if self.isStr(_ret2) else _ret2.get()
        return self.__uu.uuid5(namespace = _ret1, name = _ret2)
    @_cm
    def pick(self, seq: _SequenceLike[_T]) -> _T:
        """
        \\@since 0.3.8 (standard since 0.3.24) \\
        \\@lifetime ≥ 0.3.8 \\
        \\@modified 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        Returns random item from a sequence
        """
        _ret = +seq if isinstance(seq, self.tcs.FinalVar) else seq
        return _ret[self.random(0, reckon(_ret) - 1)]
    def error(self, handler: type[_ErrorType], message: _uni[str, None] = None):
        """
        \\@since 0.3.24 \\
        \\@deprecated since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        """
        self.__wa.warn("This method is deprecated since 0.3.25. Consider manually setting errors instead.", DeprecationWarning)
        err = handler
        s = message
        if s is None:
            raise err()
        else:
            raise err(s)
    @_cm
    def probability2(self, x: _T = 1, y: _T = 0, frequency: _uni[int, __tk.IntVar] = 1, length: _uni[int, __tk.IntVar] = int(1e+4)):
        """
        \\@since 0.3.8 (standard since 0.3.9) \\
        \\@lifetime ≥ 0.3.8; < 0.3.24; ≥ 0.3.25 \\
        \\@modified 0.3.26a3, 0.3.26c1 \\
        \\@author Aveyzan \\
        https://aveyzan.glitch.me/tense/py/method.probability.html#2
        ```ts \\
        "class method" in class Tense
        ``` \n
        ``` \n
        # syntax since 0.3.25
        def probability2(x = 1, y = 0, frequency = 1, length = 10000): ...
        # syntax for 0.3.19 - 0.3.23; on 0.3.19 renamed from probability()
        def probability2(rareValue = 1, usualValue = 0, frequency = 1, length = 10000): ...
        # syntax before 0.3.19
        def probability(value = 1, frequency = 1, length = 10000): ...
        ```
        Randomize a value using probability `frequency/length` applied on parameter `x`. \\
        Probability for parameter `y` will be equal `(length - frequency)/length`. \\
        Default values:
        - for `x`: 1
        - for `y`: 0
        - for `frequency`: 1
        - for `length`: 10000 (since 0.3.26a3 `length` can also have value `-1`)

        To be more explanatory, `x` has `1/10000` chance to be returned by default (in percents: 0.01%), \\
        meanwhile the rest chance goes to `y` (`9999/10000`, 99.99%), hence `y` will be returned more \\
        frequently than `x`. Exceptions:
        - for `frequency` equal 0 or `x` equal `y`, returned is `y`
        - for `frequency` greater than (or since 0.3.25 equal) `length` returned is `x`
        """
        a: list[_T] = []
        _length = length if self.isInt(length) else length.get()
        if self.isInt(frequency) or isinstance(frequency, self.__tk.IntVar):
            _frequency = frequency if self.isInt(frequency) else frequency.get()
        # elif self.isFloat(frequency) or isinstance(frequency, self.__tk.DoubleVar):
        #    _frequency = self.__ma.trunc(frequency) if self.isFloat(frequency) else self.__ma.trunc(frequency.get())
        else:
            err, s = (TypeError, "Parameter 'frequency' isn't an integer. Ensure passed value to this parameter is an integer.")
            raise err(s)
        if type(x).__qualname__ != type(y).__qualname__:
            err, s = (TypeError, f"Types of parameters 'x' and 'y' do not match. Received types: for 'x' -> '{type(y).__name__}', for 'y' -> '{type(x).__name__}'")
            raise err(s)
        elif _frequency < 0:
            err, s = (ValueError, "Parameter 'frequency' may not have a negative integer value.")
            raise err(s)
        if not self.isInt(_length):
            err, s = (TypeError, "Parameter 'length' isn't an integer. Ensure passed value to this parameter is an integer.")
            raise err(s)
        elif _length == 0:
            err, s = (ZeroDivisionError, "Parameter 'length' may not be equal zero. Formed probability fraction leads to division by zero")
            raise err(s)
        elif _length > sys.maxsize:
            err, s = (ValueError, f"Parameter 'length' has too high value, expected value below or equal {sys.maxsize}")
            raise err(s)
        elif _length == -1:
            _length = 10000
        elif _length < -1:
            err, s = (ValueError, "Parameter 'length' may not have a negative integer value.")
            raise err(s)
        tmp1, tmp2 = (x, y)
        if tmp1 == tmp2 or _frequency == 0:
            return tmp2
        if _frequency >= _length:
            return tmp1
        for _ in abroad(_length - _frequency): a.append(tmp2)
        for _ in abroad(_length - _frequency, _length): a.append(tmp1)
        return self.pick(a)
    @_cm
    def probability(self, *vf: _ProbabilityType[int], length: tcs.TypeOrFinalVarType[int] = PROBABILITY_COMPUTE) -> int: # no matter what, it HAS to return integer
        """
        \\@since 0.3.8 (standard since 0.3.9) \\
        \\@lifetime ≥ 0.3.8 \\
        \\@modified 0.3.19, 0.3.24, 0.3.25, 0.3.26a3, 0.3.26b3, 0.3.26c1 \\
        \\@author Aveyzan
        https://aveyzan.glitch.me/tense/py/method.probability.html
        ```ts \\
        "class method" in class Tense
        ``` \n
        ``` \n
        # since 0.3.25
        def probability(*vf: int | list[int] | tuple[int, int | None] | dict[int, int | None] | deque[int], length: int = PROBABILITY_COMPUTE): ...

        # for 0.3.24
        def probability(*valuesAndFrequencies: int | list[int] | tuple[int] | dict[int, int | None], length: int = PROBABILITY_ALL): ...

        # during 0.3.19 - 0.3.23; on 0.3.19 renamed
        def probability(*valuesAndFrequencies: int | list[int] | tuple[int], length: int = -1): ...

        # during 0.3.8 - 0.3.18
        def complexity(values: list[_T] | tuple[_T], frequencies: int | list[int] | tuple[int], length: int = 10000): ...
        ```
        Extended version of `Tense.probability2()` method. Instead of only 2 values user can put more than 2. \\
        Nevertheless, comparing to the same method, it accepts integers only.

        Parameters:

        \\- `vf` - this parameter waits at least for 3 values (before 0.3.26a3), for 2 values you need to use `Tense.probability2()` method \\
        instead, because inner code catches unexpected exception `ZeroDivisionError`. For version 0.3.25 this parameter accepts: 
        - integers
        - integer lists of size 1-2
        - integer tuples of size 1-2
        - integer deques of size 1-2
        - integer key-integer/`None`/`...` value dicts
        - integer sets and frozensets of size 1-2 both

        \\- `length` (Optional) - integer which has to be a denominator in probability fraction. Defaults to `-1`, what means this \\
        number is determined by `vf` passed values (simple integer is plus 1, dicts - plus value or 1 if it is `None` or ellipsis, \\
        sequence - 2nd item; if `None`, then plus 1). Since 0.3.26b3 put another restriction: length must be least than or equal \\
        `sys.maxsize`, which can be either equal 2\\*\\*31 - 1 (2,147,483,647) or 2\\*\\*63 - 1 (9,223,372,036,854,775,807; like in \\
        Aveyzan's case). Since 0.3.26c1 you can also append `tense.tcs.FinalVar` instance, which holds an integer.
        """
        # explanation:
        # a1 is final list, which will be used to return the integer
        # a2 is temporary list, which will store all single integers, without provided "frequency" value (item 2)
        a1, a2 = [[0] for _ in abroad(2)]
        a1.clear()
        a2.clear()
        # c1 sums all instances of single numbers, and with provided "frequency" - plus it
        # c2 is substraction of length and c1
        # c3 has same purpose as c1, but counts only items without "frequency" (second) item
        # c4 is last variable, which is used as last from all of these - counts the modulo of c2 and c3 (but last one minus 1 as well)
        # c5 gets value from rearmost iteration 
        c1, c2, c3, c4, c5 = [0 for _ in abroad(5)]
        if not isinstance(length, (int, self.tcs.FinalVar)) or (isinstance(length, self.tcs.FinalVar) and not isinstance(+length, int)):
            # "length" parameter is not an integer
            err, s = (TypeError, "Expected integer or final integer variable ('tcs.FinalVar[int]') value of 'length' parameter")
            raise err(s)
        elif length < -1:
            # "length" is negative (that parameter is denominator of probability fraction, so it cannot be negative)
            err, s = (ValueError, "Expected integer value from -1 or above in 'length' parameter")
            raise err(s)
        elif length == 0:
            err, s = (ZeroDivisionError, "Expected integer value from -1 or above in 'length' parameter, but not equal zero")
            raise err(s)
        elif length > sys.maxsize:
            # since 0.3.26b3; cannot be greater than sys.maxsize
            err, s = (ValueError, f"Parameter 'length' has too high value, expected value below or equal {sys.maxsize}")
            raise err(s)
        # START 0.3.26a3
        if reckon(vf) == 2:
            _length = +length if not self.isInt(length) else 10000 if length == -1 else length
            e1, e2 = (vf[0], vf[1])
            if isinstance(e1, int) and isinstance(e2, int):
                return self.probability2(e1, e2, length = 2)
            elif isinstance(e1, int) and isinstance(e2, (_ProbabilitySeqNoDict, dict)):
                if isinstance(e2, _ProbabilitySeqNoDict):
                    if reckon(e2) == 1:
                        tmp = e2[0]
                        if not isinstance(tmp, int):
                            err, s = (TypeError, f"First item in a list/tuple/set/frozenset/deque is not an integer")
                            raise err(s)
                        return self.probability2(e1, tmp, length = 2)
                    # those are, respectively, "value" and "frequency"
                    elif reckon(e2) == 2:
                        tmp1, tmp2 = (e2[0], e2[1])
                        if not isinstance(tmp1, int):
                            err, s = (TypeError, f"First item in a list/tuple/set/frozenset/deque is not an integer")
                            raise err(s)
                        if not isinstance(tmp2, (int, _Ellipsis)) and tmp2 is not None:
                            err, s = (TypeError, "Second item in a list/tuple/set/frozenset/deque is neither an integer, 'None', nor an ellipsis")
                            raise err(s)
                        if tmp2 is None or isinstance(tmp2, _Ellipsis):
                            return self.probability2(e1, tmp1, length = _length)
                        elif tmp2 < 1: # probability fraction cannot be negative
                            err, s = (ValueError, f"Second item in a list/tuple/set/frozenset/deque is negative or equal zero")
                            raise err(s)
                        return self.probability2(e1, tmp1, frequency = tmp2, length = _length)
                    else:
                        err, s = (IndexError, f"Length of list/tuple/set/frozenset/deque may have length 1-2 only")
                        raise err(s)
                elif isinstance(e2, dict):
                    if reckon(e2) != 1:
                        err, s = (ValueError, f"Expected only one pair in dictonary, received {reckon(e2)}")
                        raise err(s)
                    tmp1, tmp2 = (0, 0)
                    for f in e2:
                        if f in e2:
                            tmp1, tmp2 = (f, e2[f])
                            break
                    if tmp2 is None or isinstance(tmp2, _Ellipsis):
                        return self.probability2(e1, tmp1, length = _length)
                    elif tmp2 < 1: # probability fraction cannot be negative
                            err, s = (ValueError, f"Second item in a list/tuple/set/frozenset/deque is negative or equal zero")
                            raise err(s)
                    return self.probability2(e1, tmp1, frequency = tmp2, length = _length)
            elif isinstance(e1, (_ProbabilitySeqNoDict, dict)) and isinstance(e2, int):
                if isinstance(e1, _ProbabilitySeqNoDict):
                    if reckon(e1) == 1:
                        tmp = e1[0]
                        if not isinstance(tmp, int):
                            err, s = (TypeError, f"First item in a list/tuple/set/frozenset/deque is not an integer")
                            raise err(s)
                        return self.probability2(tmp, e2, length = 2)
                    # those are, respectively, "value" and "frequency"
                    elif reckon(e1) == 2:
                        tmp1, tmp2 = (e1[0], e1[1])
                        if not isinstance(tmp1, int):
                            err, s = (TypeError, f"First item in a list/tuple/set/frozenset/deque is not an integer")
                            raise err(s)
                        if not isinstance(tmp2, (int, _Ellipsis)) and tmp2 is not None:
                            err, s = (TypeError, "Second item in a list/tuple/set/frozenset/deque is neither an integer, 'None', nor an ellipsis")
                            raise err(s)
                        if tmp2 is None or isinstance(tmp2, _Ellipsis):
                            return self.probability2(tmp1, e2, length = _length)
                        elif tmp2 < 1: # probability fraction cannot be negative
                            err, s = (ValueError, f"Second item in a list/tuple/set/frozenset/deque is negative or equal zero")
                            raise err(s)
                        return self.probability2(tmp1, e2, frequency = _length - tmp2, length = _length)
                    else:
                        err, s = (IndexError, f"Length of list/tuple/set/frozenset/deque may have length 1-2 only")
                        raise err(s)
                elif isinstance(e1, dict):
                    if reckon(e1) != 1:
                        err, s = (ValueError, f"Expected only one pair in dictonary, received {reckon(e1)}")
                        raise err(s)
                    tmp1, tmp2 = (0, 0)
                    for f in e1:
                        if f in e1:
                            tmp1, tmp2 = (f, e1[f])
                            break
                    if tmp2 is None or isinstance(tmp2, _Ellipsis):
                        return self.probability2(tmp1, e2, length = _length)
                    elif tmp2 < 1: # probability fraction cannot be negative
                            err, s = (ValueError, f"Second item in a list/tuple/set/frozenset/deque is negative or equal zero")
                            raise err(s)
                    return self.probability2(tmp1, e2, frequency = _length - tmp2, length = _length)
            elif isinstance(e1, (_ProbabilitySeqNoDict, dict)) and isinstance(e2, (_ProbabilitySeqNoDict, dict)):
                if isinstance(e1, _ProbabilitySeqNoDict):
                    if isinstance(e2, _ProbabilitySeqNoDict):
                        if reckon(e1) == 1:
                            if reckon(e2) == 1:
                                tmp1, tmp2 = (e1[0], e2[0])
                                if not isinstance(tmp1, int) or not isinstance(tmp2, int):
                                    err, s = (TypeError, f"First item in a list/tuple/set/frozenset/deque is not an integer")
                                    raise err(s)
                                return self.probability2(tmp1, tmp2, length = _length)
                            elif reckon(e2) == 2:
                                tmp1, tmp2_1, tmp2_2 = (e1[0], e2[0], e2[1])
                                if not isinstance(tmp1, int) or not isinstance(tmp2_1, int):
                                    err, s = (TypeError, f"First item in a list/tuple/set/frozenset/deque is not an integer")
                                    raise err(s)
                                if not isinstance(tmp2_2, (int, _Ellipsis)) and tmp2_2 is not None:
                                    err, s = (TypeError, "Second item in a list/tuple/set/frozenset/deque is neither an integer, 'None', nor an ellipsis")
                                    raise err(s)
                                if tmp2_2 is None or isinstance(tmp2_2, _Ellipsis):
                                    return self.probability2(tmp1, tmp2_1, length = _length)
                                return self.probability2(tmp1, tmp2_1, frequency = tmp2_2, length = _length)
                            else:
                                err, s = (IndexError, f"Length of list/tuple/set/frozenset/deque may have length 1-2 only")
                                raise err(s)
                        elif reckon(e1) == 2:
                            if reckon(e2) == 1:
                                tmp1_1, tmp1_2, tmp2 = (e1[0], e1[1], e2[0])
                                if not isinstance(tmp1_1, int) or not isinstance(tmp2, int):
                                    err, s = (TypeError, f"First item in a list/tuple/set/frozenset/deque is not an integer")
                                    raise err(s)
                                if not isinstance(tmp1_2, (int, _Ellipsis)) and tmp1_2 is not None:
                                    err, s = (TypeError, "Second item in a list/tuple/set/frozenset/deque is neither an integer, 'None', nor an ellipsis")
                                    raise err(s)
                                if tmp1_2 is None or isinstance(tmp1_2, _Ellipsis):
                                    return self.probability2(tmp1_1, tmp2, length = _length)
                                return self.probability2(tmp1_1, tmp2, frequency = _length - tmp1_2, length = _length)
                            elif reckon(e2) == 2:
                                tmp1_1, tmp1_2, tmp2_1, tmp2_2 = (e1[0], e1[1], e2[0], e2[1])
                                if not isinstance(tmp1_1, int) or not isinstance(tmp2_1, int):
                                    err, s = (TypeError, f"First item in a list/tuple/set/frozenset/deque is not an integer")
                                    raise err(s)
                                if (not isinstance(tmp1_2, (int, _Ellipsis)) and tmp1_2 is not None) or (not isinstance(tmp2_2, (int, _Ellipsis)) and tmp2_2 is not None):
                                    err, s = (TypeError, "Second item in a list/tuple/set/frozenset/deque is neither an integer, 'None', nor an ellipsis")
                                    raise err(s)
                                if tmp1_2 is None or isinstance(tmp1_2, _Ellipsis):
                                    if tmp2_2 is None or isinstance(tmp2_2, _Ellipsis):
                                        return self.probability2(tmp1_1, tmp2_1, length = _length)
                                    else:
                                        return self.probability2(tmp1_1, tmp2_1, frequency = _length - tmp2_2, length = _length)
                                else:
                                    if tmp2_2 is None or isinstance(tmp2_2, _Ellipsis):
                                        return self.probability2(tmp1_1, tmp2_1, frequency = tmp1_2, length = _length)
                                    else:
                                        return self.probability2(tmp1_1, tmp2_1, frequency = tmp1_2, length = _length if _length > tmp1_2 + tmp2_2 else tmp1_2 + tmp2_2)
                            else:
                                err, s = (IndexError, f"Length of list/tuple/set/frozenset/deque may have length 1-2 only")
                                raise err(s)
                        else:
                            err, s = (IndexError, f"Length of list/tuple/set/frozenset/deque may have length 1-2 only")
                            raise err(s)
                    elif isinstance(e2, dict):
                        if reckon(e2) != 1:
                            err, s = (ValueError, f"Expected only one pair in dictonary, received {reckon(e2)}")
                            raise err(s)
                        if reckon(e1) == 1:
                            tmp1, tmp2_1, tmp2_2 = (e1[0], 0, 0)
                            for v in e2:
                                if not isinstance(v, int):
                                    err, s = (KeyError, f"Key in dictionary is not an integer")
                                    raise err(s)
                                if not isinstance(e2[v], (int, _Ellipsis)) and e2[v] is not None:
                                    err, s = (ValueError, f"Value in dictionary is neither an integer, 'None', nor an ellipsis")
                                    raise err(s)
                                if e2[v] < 1:
                                    err, s = (ValueError, f"Value in dictionary is negative integer or equal zero")
                                    raise err(s)
                                tmp2_1, tmp2_2 = (v, e2[v])
                                break
                            if not isinstance(tmp1, int):
                                err, s = (TypeError, f"First item in a list/tuple/set/frozenset/deque is not an integer")
                                raise err(s)
                            if not isinstance(tmp2_2, (int, _Ellipsis)) and tmp2_2 is not None:
                                err, s = (TypeError, "Second item in a list/tuple/set/frozenset/deque is neither an integer, 'None', nor an ellipsis")
                                raise err(s)
                            if tmp2_2 is None or isinstance(tmp2_2, _Ellipsis):
                                return self.probability2(tmp1, tmp2_1, length = _length)
                            return self.probability2(tmp1, tmp2_1, frequency = tmp2_2, length = _length)
                        elif reckon(e1) == 2:
                            tmp1_1, tmp1_2, tmp2_1, tmp2_2 = (e1[0], e1[1], 0, 0)
                            for v in e2:
                                if not isinstance(v, int):
                                    err, s = (KeyError, f"Key in dictionary is not an integer")
                                    raise err(s)
                                if not isinstance(e2[v], (int, _Ellipsis)) and e2[v] is not None:
                                    err, s = (ValueError, f"Value in dictionary is neither an integer, 'None', nor an ellipsis")
                                    raise err(s)
                                if e2[v] < 1:
                                    err, s = (ValueError, f"Value in dictionary is negative integer or equal zero")
                                    raise err(s)
                                tmp2_1, tmp2_2 = (v, e2[v])
                                break
                            if not isinstance(tmp1_1, int) or not isinstance(tmp2_1, int):
                                err, s = (TypeError, f"First item in a list/tuple/set/frozenset/deque is not an integer")
                                raise err(s)
                            if (not isinstance(tmp1_2, (int, _Ellipsis)) and tmp1_2 is not None) or (not isinstance(tmp2_2, (int, _Ellipsis)) and tmp2_2 is not None):
                                err, s = (TypeError, "Second item in a list/tuple/set/frozenset/deque is neither an integer, 'None', nor an ellipsis")
                                raise err(s)
                            if tmp1_2 is None or isinstance(tmp1_2, _Ellipsis):
                                if tmp2_2 is None or isinstance(tmp2_2, _Ellipsis):
                                    return self.probability2(tmp1_1, tmp2_1, length = _length)
                                else:
                                    return self.probability2(tmp1_1, tmp2_1, frequency = _length - tmp2_2, length = _length)
                            else:
                                if tmp2_2 is None or isinstance(tmp2_2, _Ellipsis):
                                    return self.probability2(tmp1_1, tmp2_1, frequency = tmp1_2, length = _length)
                                else:
                                    return self.probability2(tmp1_1, tmp2_1, frequency = tmp1_2, length = _length if _length > tmp1_2 + tmp2_2 else tmp1_2 + tmp2_2)
                        else:
                            err, s = (IndexError, f"Length of list/tuple/set/frozenset/deque may have length 1-2 only")
                            raise err(s)
                    else:
                        err, s = (TypeError, f"Inappropriate type found. Allowed types: 'int', 'dict', 'set', 'frozenset', 'tuple', 'list', 'deque'")
                        raise err(s)
                elif isinstance(e1, dict):
                    if isinstance(e2, _ProbabilitySeqNoDict):
                        if reckon(e1) != 1:
                            err, s = (ValueError, f"Expected only one pair in dictonary, received {reckon(e1)}")
                            raise err(s)
                        if reckon(e2) == 1:
                            tmp1_1, tmp1_2, tmp2 = (0, 0, e2[0])
                            for v in e1:
                                if not isinstance(v, int):
                                    err, s = (KeyError, f"Key in dictionary is not an integer")
                                    raise err(s)
                                if not isinstance(e1[v], (int, _Ellipsis)) and e1[v] is not None:
                                    err, s = (ValueError, f"Value in dictionary is neither an integer, 'None', nor an ellipsis")
                                    raise err(s)
                                if e1[v] < 1:
                                    err, s = (ValueError, f"Value in dictionary is negative integer or equal zero")
                                    raise err(s)
                                tmp1_1, tmp1_2 = (v, e1[v])
                                break
                            if not isinstance(tmp1_1, int) or not isinstance(tmp2, int):
                                err, s = (TypeError, f"First item in a list/tuple/set/frozenset/deque is not an integer")
                                raise err(s)
                            if not isinstance(tmp1_2, (int, _Ellipsis)) and tmp1_2 is not None:
                                err, s = (TypeError, "Second item in a list/tuple/set/frozenset/deque is neither an integer, 'None', nor an ellipsis")
                                raise err(s)
                            if tmp1_2 is None or isinstance(tmp1_2, _Ellipsis):
                                return self.probability2(tmp1_1, tmp2, length = _length)
                            return self.probability2(tmp1_1, tmp2, frequency = _length - tmp1_2, length = _length)
                        elif reckon(e2) == 2:
                            tmp1_1, tmp1_2, tmp2_1, tmp2_2 = (0, 0, e2[0], e2[1])
                            for v in e1:
                                if not isinstance(v, int):
                                    err, s = (KeyError, f"Key in dictionary is not an integer")
                                    raise err(s)
                                if not isinstance(e1[v], (int, _Ellipsis)) and e1[v] is not None:
                                    err, s = (ValueError, f"Value in dictionary is neither an integer, 'None', nor an ellipsis")
                                    raise err(s)
                                if e1[v] < 1:
                                    err, s = (ValueError, f"Value in dictionary is negative integer or equal zero")
                                    raise err(s)
                                tmp1_1, tmp1_2 = (v, e1[v])
                                break
                            if not isinstance(tmp1_1, int) or not isinstance(tmp2_1, int):
                                err, s = (TypeError, f"First item in a list/tuple/set/frozenset/deque is not an integer")
                                raise err(s)
                            if (not isinstance(tmp1_2, (int, _Ellipsis)) and tmp1_2 is not None) or (not isinstance(tmp2_2, (int, _Ellipsis)) and tmp2_2 is not None):
                                err, s = (TypeError, "Second item in a list/tuple/set/frozenset/deque is neither an integer, 'None', nor an ellipsis")
                                raise err(s)
                            if tmp1_2 is None or isinstance(tmp1_2, _Ellipsis):
                                if tmp2_2 is None or isinstance(tmp2_2, _Ellipsis):
                                    return self.probability2(tmp1_1, tmp2_1, length = _length)
                                else:
                                    return self.probability2(tmp1_1, tmp2_1, frequency = _length - tmp2_2, length = _length)
                            else:
                                if tmp2_2 is None or isinstance(tmp2_2, _Ellipsis):
                                    return self.probability2(tmp1_1, tmp2_1, frequency = tmp1_2, length = _length)
                                else:
                                    return self.probability2(tmp1_1, tmp2_1, frequency = tmp1_2, length = _length if _length > tmp1_2 + tmp2_2 else tmp1_2 + tmp2_2)
                        else:
                            err, s = (IndexError, f"Length of list/tuple/set/frozenset/deque may have length 1-2 only")
                            raise err(s)
                    elif isinstance(e2, dict):
                        if reckon(e2) != 1:
                            err, s = (ValueError, f"Expected only one pair in dictonary, received {reckon(e2)}")
                            raise err(s)
                        tmp1_1, tmp1_2, tmp2_1, tmp2_2 = (0, 0, 0, 0)
                        for v in e1:
                            if not isinstance(v, int):
                                err, s = (KeyError, f"Key in dictionary is not an integer")
                                raise err(s)
                            if not isinstance(e1[v], (int, _Ellipsis)) and e1[v] is not None:
                                err, s = (ValueError, f"Value in dictionary is neither an integer, 'None', nor an ellipsis")
                                raise err(s)
                            if e1[v] < 1:
                                err, s = (ValueError, f"Value in dictionary is negative integer or equal zero")
                                raise err(s)
                            tmp1_1, tmp1_2 = (v, e1[v])
                            break
                        for v in e2:
                            if not isinstance(v, int):
                                err, s = (KeyError, f"Key in dictionary is not an integer")
                                raise err(s)
                            if not isinstance(e2[v], (int, _Ellipsis)) and e2[v] is not None:
                                err, s = (ValueError, f"Value in dictionary is neither an integer, 'None', nor an ellipsis")
                                raise err(s)
                            if e2[v] < 1:
                                err, s = (ValueError, f"Value in dictionary is negative integer or equal zero")
                                raise err(s)
                            tmp2_1, tmp2_2 = (v, e2[v])
                            break
                        if not isinstance(tmp1_1, int) or not isinstance(tmp2_1, int):
                            err, s = (TypeError, f"First item in a list/tuple/set/frozenset/deque is not an integer")
                            raise err(s)
                        if (not isinstance(tmp1_2, (int, _Ellipsis)) and tmp1_2 is not None) or (not isinstance(tmp2_2, (int, _Ellipsis)) and tmp2_2 is not None):
                            err, s = (TypeError, "Second item in a list/tuple/set/frozenset/deque is neither an integer, 'None', nor an ellipsis")
                            raise err(s)
                        if tmp1_2 is None or isinstance(tmp1_2, _Ellipsis):
                            if tmp2_2 is None or isinstance(tmp2_2, _Ellipsis):
                                return self.probability2(tmp1_1, tmp2_1, length = _length)
                            else:
                                return self.probability2(tmp1_1, tmp2_1, frequency = _length - tmp2_2, length = _length)
                        else:
                            if tmp2_2 is None or isinstance(tmp2_2, _Ellipsis):
                                return self.probability2(tmp1_1, tmp2_1, frequency = tmp1_2, length = _length)
                            else:
                                return self.probability2(tmp1_1, tmp2_1, frequency = tmp1_2, length = _length if _length > tmp1_2 + tmp2_2 else tmp1_2 + tmp2_2)
                    else:
                        err, s = (TypeError, f"Inappropriate type found. Allowed types: 'int', 'dict', 'set', 'frozenset', 'tuple', 'list', 'deque'")
                        raise err(s)
                else:
                    err, s = (TypeError, f"Inappropriate type found. Allowed types: 'int', 'dict', 'set', 'frozenset', 'tuple', 'list', 'deque'")
                    raise err(s)
            else:
                err, s = (TypeError, f"Inappropriate type found. Allowed types: 'int', 'dict', 'set', 'frozenset', 'tuple', 'list', 'deque'")
                raise err(s)
        # END 0.3.26a3
        elif reckon(vf) < 2:
            # lack of integers
            err, s = (self.tcs.MissingValueError, f"Expected at least 2 items in 'vf' parameter, received {reckon(vf)}")
            raise err(s)
        # reading all items provided
        for e in vf:
            # value is an integer (that means it cannot have "frequency"),
            # which is "value" parameter equivalent
            if isinstance(e, int):
                a1.append(e)
                a2.append(e)
                c1 += 1
                c3 += 1
            elif isinstance(e, _ProbabilitySeqNoDict):
                # we have only one item, and that item is "value"
                # 0.3.25 (additional statement for tuple and overall)
                if reckon(e) == 1:
                    if not isinstance(e[0], int):
                        err, s = (TypeError, f"First item in a list/tuple/set/frozenset/deque is not an integer. Ensure every first item of lists/tuples/sets/frozensets/deques is an integer. Error thrown by item: '{e[0]}'")
                        raise err(s)
                    a1.append(e[0])
                    a2.append(e[0])
                    c1 += 1
                    c3 += 1
                # those are, respectively, "value" and "frequency"
                elif reckon(e) == 2:
                    if not isinstance(e[0], int):
                        err, s = (TypeError, f"First item in a list/tuple/set/frozenset/deque is not an integer. Ensure every first item of lists/tuples/sets/frozensets/deques is an integer. Error thrown by item: '{e[0]}'")
                        raise err(s)
                    if not isinstance(e[1], (int, _Ellipsis)) and e[1] is not None:
                        err, s = (TypeError, "Second item in a list/tuple/set/frozenset/deque is neither an integer, 'None', nor an ellipsis. Ensure every second item of lists/tuples/sets/frozensets/deques " + \
                        f"satisfies this requirement. Error thrown by item: '{e[1]}'")
                        raise err(s)
                    if e[1] is None or isinstance(e[1], _Ellipsis):
                        a1.append(e[0])
                        a2.append(e[0])
                        c1 += 1
                        c3 += 1
                    elif e[1] < 1: # probability fraction cannot be negative
                        err, s = (ValueError, f"Second item in a list/tuple/set/frozenset/deque is negative or equal zero. Ensure every second item of lists/tuples/sets/frozensets/deques are positive. Error thrown by item: '{e[1]}'")
                        raise err(s)
                    for _ in abroad(e[1]): a1.append(e[0])
                    c1 += int(e[1])
                # if thought that the length is third item, that is wrong presupposition
                else:
                    err, s = (IndexError, f"Length of lists/tuples/sets/frozensets/deques may have length 1-2 only, one of them has length 0 or greater than 2. Error thrown by item: '{e}'")
                    raise err(s)
            # 0.3.24 (dict support)
            elif isinstance(e, dict):
                if reckon(e) == 0:
                   err, s = (ValueError, f"Expected at least one pair in every dictonary, received {reckon(e)}")
                   raise err(s)
                for f in e:
                    if not isinstance(f, int):
                        err, s = (KeyError, f"One of keys in dictionaries is not an integer. Ensure every key is of type 'int'. Error thrown by item: '{f}'")
                        raise err(s)
                    if not isinstance(e[f], (int, _Ellipsis)) and e[f] is not None:
                        err, s = (ValueError, f"One of values in dictionaries is neither an integer, 'None', nor an ellipsis. Ensure every values satisfies this requirement. Error thrown by item: '{f}'")
                        raise err(s)
                    if e[f] < 1:
                        err, s = (ValueError, f"One of values in dictionaries is negative integer or equal zero. Ensure every value is positive integer. Error thrown by item: '{e[f]}'")
                        raise err(s)
                    elif e[f] is None or isinstance(e[f], _Ellipsis):
                        a1.append(f)
                        a2.append(f)
                        c1 += 1
                        c3 += 1
                    else:
                        for _ in abroad(e[f]): a1.append(f)
                        c1 += 1
            # incorrect type defined
            else:
                err, s = (TypeError, f"One of values has inappropriate type. Ensure every value are of types: 'int', 'dict', 'set', 'frozenset', 'tuple', 'list', 'deque'. Error thrown by item: '{e}', of type '{type(e).__name__}'")
                raise err(s)
        # length minus times when single integers are provided is needed
        # to continue extended probability
        if length == self.PROBABILITY_COMPUTE: c2 = c1
        else: c2 = length - c1
        # hint: if not that minus one, last item will be also included
        # and we want the modulo just for the last item
        c3 -= 1
        # that instruction shouldn't be complicated
        # also, it is impossible to get into here, since
        # most values do not have "frequency" (aka 2nd item)
        if c2 != c1 and c2 > length:
            tmp = [0]
            tmp.clear()
            for i in abroad(length): tmp.append(a1[i])
            a1 = tmp
        # look in here: used is abroad() method, but before the valid
        # loop, all items of temporary variable will become positive
        elif c2 == c1 or (c2 != c1 and c2 < length):
            for i in abroad(c2):
                # there we are looking for the highest number, which will
                # be divisible by number of integers passed to "vf" parameter
                if i % c3 == 0:
                    c5 = i
                    break
            # this loop is nested as we use to repeat all items from a2 list
            for i2 in abroad(a2):
                for _ in abroad(c5 / c3): a1.append(a2[i2])
            # modulo will be used merely there
            c4 = c2 % c3
            # that one will be always done (more likely)
            if c4 > 0:
                for _ in abroad(c4): a1.append(a2[reckon(a2) - 1])
        return self.pick(a1)
    @_cm
    def until(self, desiredString: _StringOrStringSequence[str], /, message: _opt[str] = None, caseInsensitive: bool = True):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        Console method, which will repeat the program until user won't \\
        write correct string. Case is insensitive, may be configured via \\
        optional parameter `caseInsensitive`, which by default has \\
        value `True`. Returned is reference to this class.
        """
        s = ""
        c = False
        while c:
            s = input(message if message is not None and message != "" else "")
            c = s.lower() != desiredString.lower() if isinstance(desiredString, str) else s.lower() not in (_s.lower() for _s in desiredString)
            if not caseInsensitive: c = s != desiredString if isinstance(desiredString, str) else s not in desiredString
        return self
    @_cm
    def sleep(self, seconds: float, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        Define an execution delay, which can be a floating-point number \\
        with 2 fractional digits. Returned is reference to this class.
        """
        self.__ti.sleep(seconds)
        return self
    @_cm
    def repeat(self, value: _T, times: int = 2, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        Returns list with `value` repeated `times` times. \\
        `times` has default value `2`.
        """
        if not isinstance(times, int):
            err, s = (TypeError, "Expected 'times' parameter to be of type 'int'")
            raise err(s)
        elif times < 1:
            err, s = (ValueError, "Expected integer value above 1.")
            raise err(s)
        return [value] * times
    @_cm
    def __local_owoify_template(self, string: str, /) -> str: # since 0.3.26b1
        s: str = string
        s = self.__re.sub(r"\s{2}", " UrU ", s, flags = re.M)
        s = self.__re.sub(r"XD", "UrU", s, flags = re.M | re.I)
        s = self.__re.sub(r":D", "UrU", s, flags = re.M)
        s = self.__re.sub(r"lenny face", "OwO", s, flags = re.M | re.I)
        s = self.__re.sub(r":O", "OwO", s, flags = re.M | re.I)
        s = self.__re.sub(r":\)", ":3", s, flags = re.M)
        s = self.__re.sub(r"\?", " uwu?", s, flags = re.M) # ? is a metachar
        s = self.__re.sub(r"!", " owo!", s, flags = re.M)
        s = self.__re.sub(r"; ", "~ ", s, flags = re.M)
        s = self.__re.sub(r", ", "~ ", s, flags = re.M)
        s = self.__re.sub(r"you are", "chu is", s, flags = re.M)
        s = self.__re.sub(r"You are", "chu is".capitalize(), s, flags = re.M)
        s = self.__re.sub(r"You Are", "chu is".title(), s, flags = re.M)
        s = self.__re.sub(r"YOU ARE", "chu is".upper(), s, flags = re.M)
        s = self.__re.sub(r"wat's this", "OwO what's this", s, flags = re.M)
        s = self.__re.sub(r"Wat's [Tt]his", "OwO What's this", s, flags = re.M)
        s = self.__re.sub(r"WAT'S THIS", "OwO what's this".upper(), s, flags = re.M)
        s = self.__re.sub(r"old person", "greymuzzle", s, flags = re.M)
        s = self.__re.sub(r"Old [Pp]erson", "greymuzzle".capitalize(), s, flags = re.M)
        s = self.__re.sub(r"OLD PERSON", "greymuzzle".upper(), s, flags = re.M)
        s = self.__re.sub(r"forgive me father, I have sinned", "sowwy daddy~ I have been naughty", s, flags = re.M)
        s = self.__re.sub(r"Forgive me father, I have sinned", "sowwy daddy~ I have been naughty".capitalize(), s, flags = re.M)
        s = self.__re.sub(r"FORGIVE ME FATHER, I HAVE SINNED", "sowwy daddy~ I have been naughty".upper(), s, flags = re.M)
        s = self.__re.sub(r"your ", "ur ", s, flags = re.M)
        s = self.__re.sub(r"Your ", "Ur ", s, flags = re.M)
        s = self.__re.sub(r"YOUR ", "UR ", s, flags = re.M)
        s = self.__re.sub(r" your", " ur", s, flags = re.M)
        s = self.__re.sub(r" Your", " Ur", s, flags = re.M)
        s = self.__re.sub(r" YOUR", " UR", s, flags = re.M)
        s = self.__re.sub(r"(^your)| your", "ur", s, flags = re.M)
        s = self.__re.sub(r"(^Your)| Your", "Ur", s, flags = re.M)
        s = self.__re.sub(r"(^YOUR)| YOUR", "UR", s, flags = re.M)
        s = self.__re.sub(r"you", "chu", s, flags = re.M)
        s = self.__re.sub(r"You", "Chu", s, flags = re.M)
        s = self.__re.sub(r"YOU", "CHU", s, flags = re.M)
        s = self.__re.sub(r"with ", "wif ", s, flags = re.M)
        s = self.__re.sub(r"With ", "Wif ", s, flags = re.M)
        s = self.__re.sub(r"wITH ", "wIF ", s, flags = re.M)
        s = self.__re.sub(r"what", "wat", s, flags = re.M)
        s = self.__re.sub(r"What", "Wat", s, flags = re.M)
        s = self.__re.sub(r"WHAT", "WAT", s, flags = re.M)
        s = self.__re.sub(r"toe", "toe bean", s, flags = re.M)
        s = self.__re.sub(r"Toe", "Toe Bean", s, flags = re.M)
        s = self.__re.sub(r"TOE", "TOE BEAN", s, flags = re.M)
        s = self.__re.sub(r"this", "dis", s, flags = re.M)
        s = self.__re.sub(r"This", "Dis", s, flags = re.M)
        s = self.__re.sub(r"THIS", "DIS", s, flags = re.M)
        s = self.__re.sub(r"(?!hell\w+)hell", "hecc", s, flags = re.M)
        s = self.__re.sub(r"(?!Hell\w+)Hell", "Hecc", s, flags = re.M)
        s = self.__re.sub(r"(?!HELL\w+)HELL", "HECC", s, flags = re.M)
        s = self.__re.sub(r"the ", "teh ", s, flags = re.M)
        s = self.__re.sub(r"^the$", "teh", s, flags = re.M)
        s = self.__re.sub(r"The ", "Teh ", s, flags = re.M)
        s = self.__re.sub(r"^The$", "Teh", s, flags = re.M)
        s = self.__re.sub(r"THE ", "TEH ", s, flags = re.M)
        s = self.__re.sub(r"^THE$", "TEH", s, flags = re.M)
        s = self.__re.sub(r"tare", "tail", s, flags = re.M)
        s = self.__re.sub(r"Tare", "Tail", s, flags = re.M)
        s = self.__re.sub(r"TARE", "TAIL", s, flags = re.M)
        s = self.__re.sub(r"straight", "gay", s, flags = re.M)
        s = self.__re.sub(r"Straight", "Gay", s, flags = re.M)
        s = self.__re.sub(r"STRAIGHT", "GAY", s, flags = re.M)
        s = self.__re.sub(r"source", "sauce", s, flags = re.M)
        s = self.__re.sub(r"Source", "Sauce", s, flags = re.M)
        s = self.__re.sub(r"SOURCE", "SAUCE", s, flags = re.M)
        s = self.__re.sub(r"(?!slut\w+)slut", "fox", s, flags = re.M)
        s = self.__re.sub(r"(?!Slut\w+)Slut", "Fox", s, flags = re.M)
        s = self.__re.sub(r"(?!SLUT\w+)SLUT", "FOX", s, flags = re.M)
        s = self.__re.sub(r"shout", "awoo", s, flags = re.M)
        s = self.__re.sub(r"Shout", "Awoo", s, flags = re.M)
        s = self.__re.sub(r"SHOUT", "AWOO", s, flags = re.M)
        s = self.__re.sub(r"roar", "rawr", s, flags = re.M)
        s = self.__re.sub(r"Roar", "Rawr", s, flags = re.M)
        s = self.__re.sub(r"ROAR", "RAWR", s, flags = re.M)
        s = self.__re.sub(r"pawlice department", "paw patrol", s, flags = re.M)
        s = self.__re.sub(r"Paw[Ll]ice [Dd]epartment", "Paw Patrol", s, flags = re.M)
        s = self.__re.sub(r"PAWLICE DEPARTMENT", "PAW PATROL", s, flags = re.M)
        s = self.__re.sub(r"police", "pawlice", s, flags = re.M)
        s = self.__re.sub(r"Police", "Pawlice", s, flags = re.M)
        s = self.__re.sub(r"POLICE", "PAWLICE", s, flags = re.M)
        s = self.__re.sub(r"pervert", "furvert", s, flags = re.M)
        s = self.__re.sub(r"Pervert", "Furvert", s, flags = re.M)
        s = self.__re.sub(r"PERVERT", "FURVERT", s, flags = re.M)
        s = self.__re.sub(r"persona", "fursona", s, flags = re.M)
        s = self.__re.sub(r"Persona", "Fursona", s, flags = re.M)
        s = self.__re.sub(r"PERSONA", "FURSONA", s, flags = re.M)
        s = self.__re.sub(r"perfect", "purrfect", s, flags = re.M)
        s = self.__re.sub(r"Perfect", "Purrfect", s, flags = re.M)
        s = self.__re.sub(r"PERFECT", "PURRFECT", s, flags = re.M)
        s = self.__re.sub(r"(?!not\w+)not", "nawt", s, flags = re.M)
        s = self.__re.sub(r"(?!Not\w+)Not", "Nawt", s, flags = re.M)
        s = self.__re.sub(r"(?!NOT\w+)NOT", "NAWT", s, flags = re.M)
        s = self.__re.sub(r"naughty", "nawt", s, flags = re.M)
        s = self.__re.sub(r"Naughty", "Nawt", s, flags = re.M)
        s = self.__re.sub(r"NAUGHTY", "NAWT", s, flags = re.M)
        s = self.__re.sub(r"name", "nyame", s, flags = re.M)
        s = self.__re.sub(r"Name", "Nyame", s, flags = re.M)
        s = self.__re.sub(r"NAME", "NYAME", s, flags = re.M)
        s = self.__re.sub(r"mouth", "maw", s, flags = re.M)
        s = self.__re.sub(r"Mouth", "Maw", s, flags = re.M)
        s = self.__re.sub(r"MOUTH", "MAW", s, flags = re.M)
        s = self.__re.sub(r"love", "luv", s, flags = re.M)
        s = self.__re.sub(r"Love", "Luv", s, flags = re.M)
        s = self.__re.sub(r"LOVE", "LUV", s, flags = re.M)
        s = self.__re.sub(r"lol", "waw", s, flags = re.M)
        s = self.__re.sub(r"Lol", "Waw", s, flags = re.M)
        s = self.__re.sub(r"LOL", "WAW", s, flags = re.M)
        s = self.__re.sub(r"lmao", "hehe~", s, flags = re.M)
        s = self.__re.sub(r"Lmao", "Hehe~", s, flags = re.M)
        s = self.__re.sub(r"LMAO", "HEHE~", s, flags = re.M)
        s = self.__re.sub(r"kiss", "lick", s, flags = re.M)
        s = self.__re.sub(r"Kiss", "Lick", s, flags = re.M)
        s = self.__re.sub(r"KISS", "LICK", s, flags = re.M)
        s = self.__re.sub(r"lmao", "hehe~", s, flags = re.M)
        s = self.__re.sub(r"Lmao", "Hehe~", s, flags = re.M)
        s = self.__re.sub(r"LMAO", "HEHE~", s, flags = re.M)
        s = self.__re.sub(r"hyena", "yeen", s, flags = re.M)
        s = self.__re.sub(r"Hyena", "Yeen", s, flags = re.M)
        s = self.__re.sub(r"HYENA", "YEEN", s, flags = re.M)
        s = self.__re.sub(r"^hi$", "hai", s, flags = re.M)
        s = self.__re.sub(r" hi ", " hai~ ", s, flags = re.M)
        s = self.__re.sub(r"hi(,| )", "hai~ ", s, flags = re.M)
        s = self.__re.sub(r"hi!", "hai!", s, flags = re.M)
        s = self.__re.sub(r"hi\?", "hai?", s, flags = re.M)
        s = self.__re.sub(r"^Hi$", "Hai", s, flags = re.M)
        s = self.__re.sub(r" Hi ", " Hai~ ", s, flags = re.M)
        s = self.__re.sub(r"Hi(,| )", "Hai~ ", s, flags = re.M)
        s = self.__re.sub(r"Hi!", "Hai!", s, flags = re.M)
        s = self.__re.sub(r"Hi\?", "Hai?", s, flags = re.M)
        s = self.__re.sub(r"^HI$", "HAI", s, flags = re.M)
        s = self.__re.sub(r" HI ", " HAI~ ", s, flags = re.M)
        s = self.__re.sub(r"HI(,| )", "HAI~ ", s, flags = re.M)
        s = self.__re.sub(r"HI!", "HAI!", s, flags = re.M)
        s = self.__re.sub(r"HI\?", "HAI?", s, flags = re.M)
        s = self.__re.sub(r"(?!handy)hand", "paw", s, flags = re.M)
        s = self.__re.sub(r"(?!Handy)Hand", "Paw", s, flags = re.M)
        s = self.__re.sub(r"(?!HANDY)HAND", "PAW", s, flags = re.M)
        s = self.__re.sub(r"handy", "pawi", s, flags = re.M)
        s = self.__re.sub(r"Handy", "Pawi", s, flags = re.M)
        s = self.__re.sub(r"HANDY", "PAWI", s, flags = re.M)
        s = self.__re.sub(r"for", "fur", s, flags = re.M)
        s = self.__re.sub(r"For", "Fur", s, flags = re.M)
        s = self.__re.sub(r"FOR", "FUR", s, flags = re.M)
        s = self.__re.sub(r"foot", "footpaw", s, flags = re.M)
        s = self.__re.sub(r"Foot", "Footpaw", s, flags = re.M)
        s = self.__re.sub(r"FOOT", "FOOTPAW", s, flags = re.M)
        s = self.__re.sub(r"father", "daddy", s, flags = re.M)
        s = self.__re.sub(r"Father", "Daddy", s, flags = re.M)
        s = self.__re.sub(r"FATHER", "DADDY", s, flags = re.M)
        s = self.__re.sub(r"fuck", "fluff", s, flags = re.M)
        s = self.__re.sub(r"Fuck", "Fluff", s, flags = re.M)
        s = self.__re.sub(r"FUCK", "FLUFF", s, flags = re.M)
        s = self.__re.sub(r"dragon", "derg", s, flags = re.M)
        s = self.__re.sub(r"Dragon", "Derg", s, flags = re.M)
        s = self.__re.sub(r"DRAGON", "DERG", s, flags = re.M)
        s = self.__re.sub(r"(?!doggy)dog", "good boi", s, flags = re.M)
        s = self.__re.sub(r"(?!Doggy)Dog", "Good boi", s, flags = re.M)
        s = self.__re.sub(r"(?!DOGGY)DOG", "GOOD BOI", s, flags = re.M)
        s = self.__re.sub(r"disease", "pathOwOgen", s, flags = re.M)
        s = self.__re.sub(r"Disease", "PathOwOgen", s, flags = re.M)
        s = self.__re.sub(r"DISEASE", "PATHOWOGEN", s, flags = re.M)
        s = self.__re.sub(r"cyborg|robot|computer", "protogen", s, flags = re.M)
        s = self.__re.sub(r"Cyborg|Robot|Computer", "Protogen", s, flags = re.M)
        s = self.__re.sub(r"CYBORG|ROBOT|COMPUTER", "PROTOGEN", s, flags = re.M)
        s = self.__re.sub(r"(?!children)child", "cub", s, flags = re.M)
        s = self.__re.sub(r"(?!Children)Child", "Cub", s, flags = re.M)
        s = self.__re.sub(r"(?!CHILDREN)CHILD", "CUB", s, flags = re.M)
        s = self.__re.sub(r"(?!cheese[ds])cheese", "sergal", s, flags = re.M)
        s = self.__re.sub(r"(?!Cheese[ds])Cheese", "Sergal", s, flags = re.M)
        s = self.__re.sub(r"(?!CHEESE[DS])CHEESE", "SERGAL", s, flags = re.M)
        s = self.__re.sub(r"celebrity", "popufur", s, flags = re.M)
        s = self.__re.sub(r"Celebrity", "Popufur", s, flags = re.M)
        s = self.__re.sub(r"CELEBRITY", "POPUFUR", s, flags = re.M)
        s = self.__re.sub(r"bye", "bai", s, flags = re.M)
        s = self.__re.sub(r"Bye", "Bai", s, flags = re.M)
        s = self.__re.sub(r"BYE", "BAI", s, flags = re.M)
        s = self.__re.sub(r"butthole", "tailhole", s, flags = re.M)
        s = self.__re.sub(r"Butthole", "Tailhole", s, flags = re.M)
        s = self.__re.sub(r"BUTTHOLE", "TAILHOLE", s, flags = re.M)
        s = self.__re.sub(r"bulge", "bulgy-wulgy", s, flags = re.M)
        s = self.__re.sub(r"Bulge", "Bulgy-wulgy", s, flags = re.M)
        s = self.__re.sub(r"BULGE", "BULGY-WULGY", s, flags = re.M)
        s = self.__re.sub(r"bite", "nom", s, flags = re.M)
        s = self.__re.sub(r"Bite", "Nom", s, flags = re.M)
        s = self.__re.sub(r"BITE", "NOM", s, flags = re.M)
        s = self.__re.sub(r"awful", "pawful", s, flags = re.M)
        s = self.__re.sub(r"Awful", "Pawful", s, flags = re.M)
        s = self.__re.sub(r"AWFUL", "PAWFUL", s, flags = re.M)
        s = self.__re.sub(r"awesome", "pawsome", s, flags = re.M)
        s = self.__re.sub(r"Awesome", "Pawsome", s, flags = re.M)
        s = self.__re.sub(r"AWESOME", "PAWSOME", s, flags = re.M)
        s = self.__re.sub(r"(?!ahh(h)+)ahh", "murr", s, flags = re.M)
        s = self.__re.sub(r"(?!Ahh[Hh]+)Ahh", "Murr", s, flags = re.M)
        s = self.__re.sub(r"(?!AHH(H)+)AHH", "MURR", s, flags = re.M)
        s = self.__re.sub(r"(?![Gg]reymuzzle|[Tt]ail(hole)?|[Pp]aw [Pp]atrol|[Pp]awlice|luv|lick|[Ff]luff|[Ss]ergal|[Pp]awful)l", "w", s, flags = re.M)
        s = self.__re.sub(r"(?!GREYMUZZLE|TAIL(HOLE)?|PAW PATROL|PAWLICE|L(uv|UV)|L(ick|ICK)|FLUFF|SERGAL|PAWFUL)L", "W", s, flags = re.M)
        s = self.__re.sub(r"(?![Gg]reymuzzle|ur|[Rr]awr|[Ff]ur(sona|vert)?|[Pp]urrfect|[Vv]ore|[Dd]erg|[Pp]rotogen|[Ss]ergal|[Pp]opufur|[Mm]urr)r", "w", s, flags = re.M)
        s = self.__re.sub(r"(?!GREYMUZZLE|UR|RAWR|FUR(SONA|VERT)?|PURRFECT|VORE|DERG|PROTOGEN|SERGAL|POPUFUR|MURR)R", "W", s, flags = re.M)
        # above: 0.3.26a3, below: 0.3.26b1
        s = self.__re.sub(r"gweymuzzwe", "greymuzzle", s, flags = re.M)
        s = self.__re.sub(r"Gweymuzzwe", "Greymuzzle", s, flags = re.M)
        s = self.__re.sub(r"GWEYMUZZWE", "GREYMUZZLE", s, flags = re.M)
        s = self.__re.sub(r"taiwhowe", "tailhole", s, flags = re.M)
        s = self.__re.sub(r"Taiwhowe", "Tailhole", s, flags = re.M)
        s = self.__re.sub(r"TAIWHOWE", "TAILHOLE", s, flags = re.M)
        s = self.__re.sub(r"paw patwow", "paw patrol", s, flags = re.M)
        s = self.__re.sub(r"Paw Patwow", "Paw Patrol", s, flags = re.M)
        s = self.__re.sub(r"PAW PATWOW", "PAW PATROL", s, flags = re.M)
        s = self.__re.sub(r"pawwice", "pawlice", s, flags = re.M)
        s = self.__re.sub(r"Pawwice", "Pawlice", s, flags = re.M)
        s = self.__re.sub(r"PAWWICE", "PAWLICE", s, flags = re.M)
        s = self.__re.sub(r"wuv", "luv", s, flags = re.M)
        s = self.__re.sub(r"Wuv", "Luv", s, flags = re.M)
        s = self.__re.sub(r"WUV", "LUV", s, flags = re.M)
        s = self.__re.sub(r"wick", "lick", s, flags = re.M)
        s = self.__re.sub(r"Wick", "Lick", s, flags = re.M)
        s = self.__re.sub(r"WICK", "LICK", s, flags = re.M)
        s = self.__re.sub(r"fwuff", "fluff", s, flags = re.M)
        s = self.__re.sub(r"Fwuff", "Fluff", s, flags = re.M)
        s = self.__re.sub(r"FWUFF", "FLUFF", s, flags = re.M)
        s = self.__re.sub(r"sewgaw", "sergal", s, flags = re.M)
        s = self.__re.sub(r"Sewgaw", "Sergal", s, flags = re.M)
        s = self.__re.sub(r"SEWGAW", "SERGAL", s, flags = re.M)
        s = self.__re.sub(r"pawfuw", "pawful", s, flags = re.M)
        s = self.__re.sub(r"Pawfuw", "Pawful", s, flags = re.M)
        s = self.__re.sub(r"PAWFUW", "PAWFUL", s, flags = re.M)
        s = self.__re.sub(r"(?!uwu)uw", "ur", s, flags = re.M)
        s = self.__re.sub(r"(?!Uwu)Uw", "Ur", s, flags = re.M)
        s = self.__re.sub(r"(?!UWU)UW", "UR", s, flags = re.M)
        s = self.__re.sub(r"waww", "rawr", s, flags = re.M)
        s = self.__re.sub(r"Waww", "Rawr", s, flags = re.M)
        s = self.__re.sub(r"WAWW", "RAWR", s, flags = re.M)
        s = self.__re.sub(r"fuw", "fur", s, flags = re.M)
        s = self.__re.sub(r"Fuw", "Fur", s, flags = re.M)
        s = self.__re.sub(r"FUW", "FUR", s, flags = re.M)
        s = self.__re.sub(r"furvewt", "furvert", s, flags = re.M)
        s = self.__re.sub(r"Furvewt", "Furvert", s, flags = re.M)
        s = self.__re.sub(r"FURVEWT", "FURVERT", s, flags = re.M)
        s = self.__re.sub(r"puwwfect", "purrfect", s, flags = re.M)
        s = self.__re.sub(r"Puwwfect", "Purrfect", s, flags = re.M)
        s = self.__re.sub(r"PUWWFECT", "PURRFECT", s, flags = re.M)
        s = self.__re.sub(r"vowe", "vore", s, flags = re.M)
        s = self.__re.sub(r"Vowe", "Vore", s, flags = re.M)
        s = self.__re.sub(r"VOWE", "VORE", s, flags = re.M)
        s = self.__re.sub(r"dewg", "derg", s, flags = re.M)
        s = self.__re.sub(r"Dewg", "Derg", s, flags = re.M)
        s = self.__re.sub(r"DEWG", "DERG", s, flags = re.M)
        s = self.__re.sub(r"pwotogen", "protogen", s, flags = re.M)
        s = self.__re.sub(r"Pwotogen", "Protogen", s, flags = re.M)
        s = self.__re.sub(r"PWOTOGEN", "PROTOGEN", s, flags = re.M)
        s = self.__re.sub(r"popufuw", "popufur", s, flags = re.M)
        s = self.__re.sub(r"Popufuw", "Popufur", s, flags = re.M)
        s = self.__re.sub(r"POPUFUW", "POPUFUR", s, flags = re.M)
        s = self.__re.sub(r"muww", "murr", s, flags = re.M)
        s = self.__re.sub(r"Muww", "Murr", s, flags = re.M)
        s = self.__re.sub(r"MUWW", "MURR", s, flags = re.M)
        # end 0.3.26b1
        return s
    @_cm
    def owoify(self, string: str, /):
        """
        \\@since 0.3.9 \\
        \\@lifetime ≥ 0.3.9; < 0.3.24; ≥ 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        Joke method translating a string to furry equivalent. \\
        Basing on https://lingojam.com/FurryTalk. Several words \\
        aren't included normally (0.3.26a3, 0.3.26b1), still, most are, \\
        several have different translations
        """
        return self.__local_owoify_template(string)
    @_cm
    def aeify(self, string: str, /):
        """
        \\@since 0.3.9 \\
        \\@lifetime ≥ 0.3.9; < 0.3.24; ≥ 0.3.26a4 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        Joke method which converts every a and e into \u00E6. Ensure your \\
        compiler reads characters from ISO/IEC 8859-1 encoding, because \\
        without it you might meet question marks instead
        """
        s: str = string
        s = self.__re.sub(r"[ae]", "\u00E6", s, flags = re.M)
        s = self.__re.sub(r"[AE]", "\u00C6", s, flags = re.M)
        return s
    @_cm
    def oeify(self, string: str, /):
        """
        \\@since 0.3.9 \\
        \\@lifetime ≥ 0.3.9; < 0.3.24; ≥ 0.3.26a4 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Tense
        ```
        Joke method which converts every o and e into \u0153. Ensure your \\
        compiler reads characters from ISO/IEC 8859-1 encoding, because \\
        without it you might meet question marks instead
        """
        s: str = string
        s = self.__re.sub(r"[oe]", "\u0153", s, flags = re.M)
        s = self.__re.sub(r"[OE]", "\u0152", s, flags = re.M)
        return s
    
class File:
    """
    \\@since 0.3.25 \\
    \\@author Aveyzan
    ```ts \\
    // created 18.07.2024
    in module tense
    ```
    Providing file IO operations
    """
    __filename = None
    __fileinstance = None
    def __init__(self, file: _FileType, mode: _FileMode, buffering = -1, encoding: _opt[str] = None, errors: _opt[str] = None, newline: _opt[str] = None, closefd = True, opener: _opt[_FileOpener] = None) -> None:
        if mode in ('rb+', 'r+b', '+rb', 'br+', 'b+r', '+br', 'wb+', 'w+b', '+wb', 'bw+', 'b+w', '+bw', 'ab+', 'a+b', '+ab', 'ba+', 'b+a', '+ba', 'xb+', 'x+b', '+xb', 'bx+', 'b+x', '+bx', 'rb', 'br', 'rbU', 'rUb', 'Urb', 'brU', 'bUr', 'Ubr', 'wb', 'bw', 'ab', 'ba', 'xb', 'bx'):
            if buffering == 0:
                # expected FileIO
                self.__fileinstance = open(file = file, mode = mode, buffering = buffering, encoding = encoding, errors = errors, newline = newline, closefd = closefd, opener = opener)
            elif buffering in (-1, 1):
                if mode in ('wb', 'bw', 'ab', 'ba', 'xb', 'bx'):
                    # expected BufferedWriter
                    self.__fileinstance = open(file = file, mode = mode, buffering = buffering, encoding = encoding, errors = errors, newline = newline, closefd = closefd, opener = opener)
                elif mode in ('rb', 'br', 'rbU', 'rUb', 'Urb', 'brU', 'bUr', 'Ubr'):
                    # expected BufferedReader
                    self.__fileinstance = open(file = file, mode = mode, buffering = buffering, encoding = encoding, errors = errors, newline = newline, closefd = closefd, opener = opener)
                else:
                    # expected BufferedRandom
                    self.__fileinstance = open(file = file, mode = mode, buffering = buffering, encoding = encoding, errors = errors, newline = newline, closefd = closefd, opener = opener)
            else:
                # expected BinaryIO
                self.__fileinstance = open(file = file, mode = mode, buffering = buffering, encoding = encoding, errors = errors, newline = newline, closefd = closefd, opener = opener)
        elif mode in ('r+', '+r', 'rt+', 'r+t', '+rt', 'tr+', 't+r', '+tr', 'w+', '+w', 'wt+', 'w+t', '+wt', 'tw+', 't+w', '+tw', 'a+', '+a', 'at+', 'a+t', '+at', 'ta+', 't+a', '+ta', 'x+', '+x', 'xt+', 'x+t', '+xt', 'tx+', 't+x', '+tx', 'w', 'wt', 'tw', 'a', 'at', 'ta', 'x', 'xt', 'tx', 'r', 'rt', 'tr', 'U', 'rU', 'Ur', 'rtU', 'rUt', 'Urt', 'trU', 'tUr', 'Utr'):
            # expected TextIOWrapper
            self.__fileinstance = open(file = file, mode = mode, buffering = buffering, encoding = encoding, errors = errors, newline = newline, closefd = closefd, opener = opener)
        else:
            # expected IO[Any]
            self.__fileinstance = open(file = file, mode = mode, buffering = buffering, encoding = encoding, errors = errors, newline = newline, closefd = closefd, opener = opener)
        self.__filename = file

class Games:
    """
    \\@since 0.3.25 \\
    \\@author Aveyzan
    ```ts \\
    // created 15.07.2024
    in module tense
    ```
    Class being a deputy of class `Tense08Games`.
    """
    import tkinter as __tk, re as __re
    def __init__(self) -> None:
        pass
    MC_ENCHANTS = 42
    """
    \\@since 0.3.25 \\
    \\@author Aveyzan
    ```ts \\
    // created 18.07.2024
    const in class Games
    ```
    Returns amount of enchantments as for Minecraft 1.21. \\
    It does not include max enchantment level sum.
    """
    SMASH_HIT_CHECKPOINTS = 12
    """
    \\@since 0.3.26a2 \\
    \\@author Aveyzan
    ```ts \\
    // created 20.07.2024
    const in class Games
    ```
    Returns amount of checkpoints in Smash Hit. \\
    11 + endless (1) = 12
    """
    @_cm
    def mcEnchBook(
        self,
        target: _uni[str, __tk.StringVar] = "@p",
        quantity: _EnchantedBookQuantity = 1,
        name: _opt[_uni[str, __tk.StringVar]] = None,
        lore: _opt[_uni[str, __tk.StringVar]] = None,
        file: _uni[_FileType, None] = None,
        *,
        aquaAffinity: _uni[bool, __tk.BooleanVar, _lit[1, None]] = None,
        baneOfArthropods: _lit[1, 2, 3, 4, 5, None] = None,
        blastProtection: _lit[1, 2, 3, 4, None] = None,
        breach: _lit[1, 2, 3, 4, None] = None,
        channeling: _uni[bool, __tk.BooleanVar, _lit[1, None]] = None,
        curseOfBinding: _uni[bool, __tk.BooleanVar, _lit[1, None]] = None,
        curseOfVanishing: _uni[bool, __tk.BooleanVar, _lit[1, None]] = None,
        density: _lit[1, 2, 3, 4, 5, None] = None,
        depthStrider: _lit[1, 2, 3, None] = None,
        efficiency: _lit[1, 2, 3, 4, 5, None] = None,
        featherFalling: _lit[1, 2, 3, 4, None] = None,
        fireAspect: _lit[1, 2, None] = None,
        fireProtection: _lit[1, 2, 3, 4, None] = None,
        flame: _uni[bool, __tk.BooleanVar, _lit[1, None]] = None,
        fortune: _lit[1, 2, 3, None] = None,
        frostWalker: _lit[1, 2, None] = None,
        impaling: _lit[1, 2, 3, 4, 5, None] = None,
        infinity: _uni[bool, __tk.BooleanVar, _lit[1, None]] = None,
        knockback: _lit[1, 2, None] = None,
        looting: _lit[1, 2, 3, None] = None,
        loyalty: _lit[1, 2, 3, None] = None,
        luckOfTheSea: _lit[1, 2, 3, None] = None,
        lure: _lit[1, 2, 3, None] = None,
        mending: _uni[bool, __tk.BooleanVar, _lit[1, None]] = None,
        multishot: _uni[bool, __tk.BooleanVar, _lit[1, None]] = None,
        piercing: _lit[1, 2, 3, 4, None] = None,
        power: _lit[1, 2, 3, 4, 5, None] = None,
        projectileProtection: _lit[1, 2, 3, 4, None] = None,
        protection: _lit[1, 2, 3, 4, None] = None,
        punch: _lit[1, 2, None] = None,
        quickCharge: _lit[1, 2, 3, None] = None,
        respiration: _lit[1, 2, 3, None] = None,
        riptide: _lit[1, 2, 3, None] = None,
        sharpness: _lit[1, 2, 3, 4, 5, None] = None,
        silkTouch: _uni[bool, __tk.BooleanVar, _lit[1, None]] = None,
        smite: _lit[1, 2, 3, 4, 5, None] = None,
        soulSpeed: _lit[1, 2, 3, None] = None,
        sweepingEdge: _lit[1, 2, 3, None] = None,
        swiftSneak: _lit[1, 2, 3, None] = None,
        thorns: _lit[1, 2, 3, None] = None,
        unbreaking: _lit[1, 2, 3, None] = None,
        windBurst: _lit[1, 2, 3, None] = None
        ):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        https://aveyzan.glitch.me/tense/py/method.mcEnchBook.html
        ```ts \\
        // created 18.07.2024
        "class method" in class Games
        ```
        Minecraft `/give <target> ...` command generator for specific enchanted books.
        Basing on https://www.digminecraft.com/generators/give_enchanted_book.php.
        
        Parameters (all are optional):
        - `target` - registered player name or one of special identifiers: `@p` (closest player), \\
        `@a` (all players), `@r` (random player), `@s` (entity running command; will not work in \\
        command blocks). Defaults to `@p`
        - `quantity` - amount of enchanted books to give to the target. Due to fact that enchanted \\
        books aren't stackable, there is restriction put to 36 (total inventory slots, excluding left hand) \\
        instead of 64 maximum. Defaults to 1
        - `name` - name of the enchanted book. Does not affect enchants; it is like putting that book \\
        to anvil and simply renaming. Defaults to `None`
        - `lore` - lore of the enchanted book. Totally I don't know what it does. Defaults to `None`
        - `file` - file to write the command into. This operation will be only done, when command has \\
        been prepared and will be about to be returned. This file will be open in `wt` mode. If file \\
        does not exist, code will attempt to create it. Highly recommended to use file with `.txt` \\
        extension. Defaults to `None`

        Next parameters are enchants. For these having level 1 only, a boolean value can be passed: \\
        in this case `False` will be counterpart of default value `None` of each, `True` means 1.
        """
        if not isinstance(target, (str, self.__tk.StringVar)):
            err, s = (TypeError, "Parameter 'target' has incorrect type, expected 'str' or 'tkinter.StringVar'")
            raise err(s)
        _result = "/give "
        _target = target if isinstance(target, str) else target.get()
        if _target.lower() in ("@a", "@s", "@p", "@r") or self.__re.search(r"[^a-zA-Z0-9_]", _target) is None:
            _result += _target
        else:
            err, s = (ValueError, "Parameter 'target' has invalid value, either selector or player name. Possible selectors: @a, @s, @p, @r. Player name may only have chars from ranges: a-z, A-Z, 0-9 and underscores (_)")
            raise err(s)
        _result += " enchanted_book["
        if not isinstance(quantity, int):
            err, s = (TypeError, "Parameter 'quantity' has incorrect type, expected 'int'.")
            raise err(s)
        elif quantity not in abroad(1, 37):
            err, s = (ValueError, "Paramater 'quantity' has incorrect value, expected from range 1-36.")
            raise err(s)
        if name is not None:
            if not isinstance(name, (str, self.__tk.StringVar)):
                err, s = (TypeError, "Parameter 'name' has incorrect type, expected 'str' 'tkinter.StringVar' or 'None'")
                raise err(s)
            else:
                _name = name if isinstance(name, str) else name.get()
                _result += "custom_name={}, ".format("{\"text\": \"" + _name + "\"}")
        if lore is not None:
            if not isinstance(lore, (str, self.__tk.StringVar)):
                err, s = (TypeError, "Parameter 'lore' has incorrect type, expected 'str', 'tkinter.StringVar' or 'None'")
                raise err(s)
            else:
                _lore = lore if isinstance(lore, str) else lore.get()
                _result += "lore=[{}], ".format("{\"text\": \"" + _lore + "\"}")
        ###################################################################################### enchants
        # assumed total: 42
        _aqua, _bane, _blast, _breach, _channeling, _curseB, _curseV, _density, _depth, _efficiency, _feather, _flame, _fireA, _fireP, _fortune = ["" for _ in abroad(15)]
        _frost, _impaling, _infinity, _knockback, _looting, _loyalty, _luck, _lure, _mending, _multishot, _piercing, _power, _projectile = ["" for _ in abroad(13)]
        _protection, _punch, _quick, _respiration, _riptide, _sharpness, _silk, _smite, _soul, _sweeping, _swift, _thorns, _unbreaking, _wind = ["" for _ in abroad(14)]
        _enchantslack, _param = (0, "")
        if aquaAffinity is not None:
            _param, _cmd, _check = ("aquaAffinity", "aqua_affinity", aquaAffinity)
            if not isinstance(_check, (int, bool, self.__tk.BooleanVar)):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int', 'bool', 'tkinter.BooleanVar' or 'None'.")
                raise err(s)
            elif isinstance(_check, int) and not isinstance(_check, bool) and _check != 1:
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected 1.")
                raise err(s)
            _check = True if (isinstance(_check, self.__tk.BooleanVar) and _check.get() is True) or _check is True or _check == 1 else False
            if _check:
                _aqua = "\"{}\": 1, ".format(_cmd)
        else: _enchantslack += 1
        if baneOfArthropods is not None:
            _param, _cmd, _check, _h = ("baneOfArthropods", "bane_of_arthropods", baneOfArthropods, 5)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _bane = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if blastProtection is not None:
            _param, _cmd, _check, _h = ("blastProtection", "blast_protection", blastProtection, 4)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _blast = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if breach is not None:
            _param, _cmd, _check, _h = ("breach", "breach", breach, 4)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _breach = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if channeling is not None:
            _param, _cmd, _check = ("channeling", "channeling", channeling)
            if not isinstance(_check, (int, bool, self.__tk.BooleanVar)):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int', 'bool', 'tkinter.BooleanVar' or 'None'.")
                raise err(s)
            elif isinstance(_check, int) and not isinstance(_check, bool) and _check != 1:
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected 1.")
                raise err(s)
            _check = True if (isinstance(_check, self.__tk.BooleanVar) and _check.get() is True) or _check is True or _check == 1 else False
            if _check:
                _channeling = "\"{}\": 1, ".format(_cmd)
        else: _enchantslack += 1
        if curseOfBinding is not None:
            _param, _cmd, _check = ("curseOfBinding", "curse_of_binding", curseOfBinding)
            if not isinstance(_check, (int, bool, self.__tk.BooleanVar)):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int', 'bool', 'tkinter.BooleanVar' or 'None'.")
                raise err(s)
            elif isinstance(_check, int) and not isinstance(_check, bool) and _check != 1:
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected 1.")
                raise err(s)
            _check = True if (isinstance(_check, self.__tk.BooleanVar) and _check.get() is True) or _check is True or _check == 1 else False
            if _check:
                _curseB = "\"{}\": 1, ".format(_cmd)
        else: _enchantslack += 1
        if curseOfVanishing is not None:
            _param, _cmd, _check = ("curseOfVanishing", "curse_of_vanishing", curseOfVanishing)
            if not isinstance(_check, (int, bool, self.__tk.BooleanVar)):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int', 'bool', 'tkinter.BooleanVar' or 'None'.")
                raise err(s)
            elif isinstance(_check, int) and not isinstance(_check, bool) and _check != 1:
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected 1.")
                raise err(s)
            _check = True if (isinstance(_check, self.__tk.BooleanVar) and _check.get() is True) or _check is True or _check == 1 else False
            if _check:
                _curseV = "\"{}\": 1, ".format(_cmd)
        else: _enchantslack += 1
        if density is not None:
            _param, _cmd, _check, _h = ("density", "density", density, 5)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _density = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if depthStrider is not None:
            _param, _cmd, _check, _h = ("depthStrider", "depth_strider", depthStrider, 3)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _depth = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if efficiency is not None:
            _param, _cmd, _check, _h = ("efficiency", "efficiency", efficiency, 5)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _efficiency = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if featherFalling is not None:
            _param, _cmd, _check, _h = ("featherFalling", "feather_falling", featherFalling, 4)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _feather = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if fireAspect is not None:
            _param, _cmd, _check, _h = ("fireAspect", "fire_aspect", fireAspect, 2)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _fireA = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if fireProtection is not None: 
            _param, _cmd, _check, _h = ("fireProtection", "fire_protection", fireProtection, 4)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _fireP = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if flame is not None:
            _param, _cmd, _check = ("flame", "flame", flame)
            if not isinstance(_check, (int, bool, self.__tk.BooleanVar)):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int', 'bool', 'tkinter.BooleanVar' or 'None'.")
                raise err(s)
            elif isinstance(_check, int) and not isinstance(_check, bool) and _check != 1:
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected 1.")
                raise err(s)
            _check = True if (isinstance(_check, self.__tk.BooleanVar) and _check.get() is True) or _check is True or _check == 1 else False
            if _check:
                _flame = "\"{}\": 1, ".format(_cmd)
        else: _enchantslack += 1
        if fortune is not None:
            _param, _cmd, _check, _h = ("fortune", "fortune", fortune, 3)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _fortune = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if frostWalker is not None:
            _param, _cmd, _check, _h = ("frostWalker", "frost_walker", frostWalker, 2)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _frost = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if impaling is not None:
            _param, _cmd, _check, _h = ("impaling", "impaling", impaling, 5)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _impaling = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if infinity is not None:
            _param, _cmd, _check = ("infinity", "infinity", infinity)
            if not isinstance(_check, (int, bool, self.__tk.BooleanVar)):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int', 'bool', 'tkinter.BooleanVar' or 'None'.")
                raise err(s)
            elif isinstance(_check, int) and not isinstance(_check, bool) and _check != 1:
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected 1.")
                raise err(s)
            _check = True if (isinstance(_check, self.__tk.BooleanVar) and _check.get() is True) or _check is True or _check == 1 else False
            if _check:
                _infinity = "\"{}\": 1, ".format(_cmd)
        else: _enchantslack += 1
        if knockback is not None:
            _param, _cmd, _check, _h = ("knockback", "knockback", knockback, 2)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _knockback = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if looting is not None:
            _param, _cmd, _check, _h = ("looting", "looting", looting, 3)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _looting = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if loyalty is not None:
            _param, _cmd, _check, _h = ("loyalty", "loyalty", loyalty, 3)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _loyalty = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if luckOfTheSea is not None:
            _param, _cmd, _check, _h = ("luckOfTheSea", "luck_of_the_sea", luckOfTheSea, 3)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _luck = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if lure is not None:
            _param, _cmd, _check, _h = ("lure", "lure", lure, 3)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _lure = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if mending is not None:
            _param, _cmd, _check = ("mending", "mending", mending)
            if not isinstance(_check, (int, bool, self.__tk.BooleanVar)):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int', 'bool', 'tkinter.BooleanVar' or 'None'.")
                raise err(s)
            elif isinstance(_check, int) and not isinstance(_check, bool) and _check != 1:
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected 1.")
                raise err(s)
            _check = True if (isinstance(_check, self.__tk.BooleanVar) and _check.get() is True) or _check is True or _check == 1 else False
            if _check:
                _mending = "\"{}\": 1, ".format(_cmd)
        else: _enchantslack += 1
        if multishot is not None:
            _param, _cmd, _check = ("multishot", "multishot", multishot)
            if not isinstance(_check, (int, bool, self.__tk.BooleanVar)):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int', 'bool', 'tkinter.BooleanVar' or 'None'.")
                raise err(s)
            elif isinstance(_check, int) and not isinstance(_check, bool) and _check != 1:
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected 1.")
                raise err(s)
            _check = True if (isinstance(_check, self.__tk.BooleanVar) and _check.get() is True) or _check is True or _check == 1 else False
            if _check:
                _multishot = "\"{}\": 1, ".format(_cmd)
        else: _enchantslack += 1
        if piercing is not None:
            _param, _cmd, _check, _h = ("piercing", "piercing", piercing, 5)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _piercing = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if power is not None: 
            _param, _cmd, _check, _h = ("power", "power", power, 5)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _power = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if projectileProtection is not None:
            _param, _cmd, _check, _h = ("projectileProtection", "projectile_protection", projectileProtection, 4)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _projectile = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if protection is not None:
            _param, _cmd, _check, _h = ("protection", "protection", protection, 4)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _protection = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if punch is not None:
            _param, _cmd, _check, _h = ("punch", "punch", punch, 2)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _punch = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if quickCharge is not None:
            _param, _cmd, _check, _h = ("quickCharge", "quick_charge", quickCharge, 3)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _quick = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if respiration is not None:
            _param, _cmd, _check, _h = ("respiration", "respiration", respiration, 3)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _respiration = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if riptide is not None:
            _param, _cmd, _check, _h = ("riptide", "riptide", riptide, 3)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _riptide = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if sharpness is not None:
            _param, _cmd, _check, _h = ("sharpness", "sharpness", sharpness, 5)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _sharpness = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if silkTouch is not None:
            _param, _cmd, _check = ("silkTouch", "silk_touch", silkTouch)
            if not isinstance(_check, (int, bool, self.__tk.BooleanVar)):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int', 'bool', 'tkinter.BooleanVar' or 'None'.")
                raise err(s)
            elif isinstance(_check, int) and not isinstance(_check, bool) and _check != 1:
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected 1.")
                raise err(s)
            _check = True if (isinstance(_check, self.__tk.BooleanVar) and _check.get() is True) or _check is True or _check == 1 else False
            if _check:
                _silk = "\"{}\": 1, ".format(_cmd)
        else: _enchantslack += 1
        if smite is not None:
            _param, _cmd, _check, _h = ("smite", "smite", smite, 5)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _smite = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if soulSpeed is not None:
            _param, _cmd, _check, _h = ("soulSpeed", "soul_speed", soulSpeed, 3)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _soul = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if sweepingEdge is not None:
            _param, _cmd, _check, _h = ("sweepingEdge", "sweeping_edge", sweepingEdge, 5)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _sweeping = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if swiftSneak is not None:
            _param, _cmd, _check, _h = ("swiftSneak", "swift_sneak", swiftSneak, 3)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _swift = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if thorns is not None:
            _param, _cmd, _check, _h = ("thorns", "thorns", thorns, 3)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _thorns = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if unbreaking is not None:
            _param, _cmd, _check, _h = ("unbreaking", "unbreaking", unbreaking, 3)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _unbreaking = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        if windBurst is not None:
            _param, _cmd, _check, _h = ("windBurst", "wind_burst", windBurst, 3)
            if not isinstance(_check, int):
                err, s = (TypeError, f"Parameter '{_param}' has incorrect type, expected 'int'.")
                raise err(s)
            elif _check not in abroad(1, _h + 1):
                err, s = (ValueError, f"Paramater '{_param}' has incorrect integer value, expected in range 1-{_h}.")
                raise err(s)
            else:
                _wind = "\"{}\": {:d}, ".format(_cmd, _check)
        else: _enchantslack += 1
        ###################################################################################### final
        if _enchantslack == self.MC_ENCHANTS:
            if name is None and lore is None:
                _result = self.__re.sub(r"enchanted_book\[", "enchanted_book ", _result)
            _result = self.__re.sub(r", $", "] ", _result) + str(quantity)
            return _result
        else:
            _result += "stored_enchantments={"
        for e in (
            _aqua, _bane, _blast, _breach, _channeling, _curseB, _curseV, _density, _depth, _efficiency, _feather, _fireA, _fireP, _flame, _fortune,
            _frost, _impaling, _infinity, _knockback, _looting, _loyalty, _luck, _lure, _mending, _multishot, _piercing, _power, _projectile,
            _protection, _punch, _quick, _respiration, _riptide, _sharpness, _silk, _smite, _soul, _sweeping, _swift, _thorns, _unbreaking, _wind
            ):
            _result += e
        _result = self.__re.sub(r", $", "}] ", _result) + str(quantity)
        if file is not None:
            if not isinstance(file, _FileType):
                err, s = (TypeError, "Parameter 'file' has incorrect file name or type")
                raise err(s)
            try:
                f = open(file, "x")
            except FileExistsError:
                f = open(file, "wt")
            f.write(_result)
            f.close()
        return _result
    O = "o"
    X = "x"
    __ttBoard = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    __ttPlayerChar = X
    __ttPlayerId = 1
    __ttPlayerChar1 = "x"
    __ttPlayerChar2 = "o"
    @_cm
    def isBoardFilled(self):
        """
        \\@since 0.3.7 \\
        \\@lifetime ≥ 0.3.7; < 0.3.24; ≥ 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Games
        ```
        Determine whether the whole board is filled, but there is no winner
        """
        return (self.__ttBoard[0][0] != self.ttEmptyField() and self.__ttBoard[0][1] != self.ttEmptyField() and self.__ttBoard[0][2] != self.ttEmptyField() and
                self.__ttBoard[1][0] != self.ttEmptyField() and self.__ttBoard[1][1] != self.ttEmptyField() and self.__ttBoard[1][2] != self.ttEmptyField() and
                self.__ttBoard[2][0] != self.ttEmptyField() and self.__ttBoard[2][1] != self.ttEmptyField() and self.__ttBoard[2][2] != self.ttEmptyField())
    @_cm
    def isLineMatched(self):
        """
        \\@since 0.3.7 \\
        \\@lifetime ≥ 0.3.7; < 0.3.24; ≥ 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Games
        ```
        Determine whether a line is matched on the board
        """
        return ((
            # horizontal match
            self.__ttBoard[0][0] == self.__ttPlayerChar and self.__ttBoard[0][1] == self.__ttPlayerChar and self.__ttBoard[0][2] == self.__ttPlayerChar) or (
            self.__ttBoard[1][0] == self.__ttPlayerChar and self.__ttBoard[1][1] == self.__ttPlayerChar and self.__ttBoard[1][2] == self.__ttPlayerChar) or (
            self.__ttBoard[2][0] == self.__ttPlayerChar and self.__ttBoard[2][1] == self.__ttPlayerChar and self.__ttBoard[2][2] == self.__ttPlayerChar) or (
            
            # vertical match
            self.__ttBoard[0][0] == self.__ttPlayerChar and self.__ttBoard[1][0] == self.__ttPlayerChar and self.__ttBoard[2][0] == self.__ttPlayerChar) or (
            self.__ttBoard[0][1] == self.__ttPlayerChar and self.__ttBoard[1][1] == self.__ttPlayerChar and self.__ttBoard[2][1] == self.__ttPlayerChar) or (
            self.__ttBoard[0][2] == self.__ttPlayerChar and self.__ttBoard[1][2] == self.__ttPlayerChar and self.__ttBoard[2][2] == self.__ttPlayerChar) or (
            
            # cursive match
            self.__ttBoard[0][0] == self.__ttPlayerChar and self.__ttBoard[1][1] == self.__ttPlayerChar and self.__ttBoard[2][2] == self.__ttPlayerChar) or (
            self.__ttBoard[2][0] == self.__ttPlayerChar and self.__ttBoard[1][1] == self.__ttPlayerChar and self.__ttBoard[0][2] == self.__ttPlayerChar
        ))
    @_cm
    def ttEmptyField(self):
        """
        \\@since 0.3.7 \\
        \\@lifetime ≥ 0.3.7; < 0.3.24; ≥ 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Games
        ```
        Returns empty field for tic-tac-toe game.
        """
        return " "
    @_cm
    def ttBoardGenerate(self) -> _TicTacToeBoard:
        """
        \\@since 0.3.7 \\
        \\@lifetime ≥ 0.3.7; < 0.3.24; ≥ 0.3.25 \\
        \\@modified 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Games
        ```
        Generates a new tic-tac-toe board.
        Content: `list->list(3)->str(3)` (brackets: amount of strings `" "`)
        """
        return Tense.repeat(Tense.repeat(" ", 3))
    @_cm
    def ttIndexCheck(self, input: int, /):
        """
        \\@since 0.3.6 \\
        \\@lifetime ≥ 0.3.6; < 0.3.24; ≥ 0.3.25 \\
        \\@modified 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Games
        ```
        . : Tic-Tac-Toe (Tense 0.3.6) : . \n
        To return `True`, number must be in in range 1-9. There \\
        is template below. Number 0 exits program.

        `1 | 2 | 3` \\
        `4 | 5 | 6` \\
        `7 | 8 | 9` \n
        """
        if input == 0:
            Tense.print("Exitting...")
            exit()
        elif input >= 1 and input <= 9:
            check = " "
            if input == 1: check = self.__ttBoard[0][0]
            elif input == 2: check = self.__ttBoard[0][1]
            elif input == 3: check = self.__ttBoard[0][2]
            elif input == 4: check = self.__ttBoard[1][0]
            elif input == 5: check = self.__ttBoard[1][1]
            elif input == 6: check = self.__ttBoard[1][2]
            elif input == 7: check = self.__ttBoard[2][0]
            elif input == 8: check = self.__ttBoard[2][1]
            else: check = self.__ttBoard[2][2]

            if check != self.__ttPlayerChar1 and check != self.__ttPlayerChar2: return True
        return False
    
    @_cm
    def ttFirstPlayer(self):
        """
        \\@since 0.3.6 \\
        \\@lifetime ≥ 0.3.6; < 0.3.24; ≥ 0.3.25 \\
        \\@modified 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Games
        ```
        . : Tic-Tac-Toe (Tense 0.3.6) : . \n
        Selects first player to start the tic-tac-toe game. \n
        First parameter will take either number 1 or 2, meanwhile second -
        \"x\" or \"o\" (by default). This setting can be changed via `ttChangeChars()` method \n
        **Warning:** do not use `ttChangeChars()` method during the game, do it before, as since you can mistaken other player \n
        Same case goes to this method. Preferably, encase whole game in `while self.ttLineMatch() == 2:` loop
        """
        self.__ttPlayerId = Tense.pick((1, 2))
        self.__ttPlayerChar = ""
        if self.__ttPlayerId == 1: self.__ttPlayerChar = self.__ttPlayerChar1
        else: self.__ttPlayerChar = self.__ttPlayerChar2
        return self
    @_cm
    def ttNextPlayer(self):
        """
        \\@since 0.3.6 \\
        \\@lifetime ≥ 0.3.6; < 0.3.24; ≥ 0.3.25 \\
        \\@modified 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Games
        ```
        . : Tic-Tac-Toe (Tense 0.3.6) : . \n
        Swaps the player turn to its concurrent (aka other player) \n
        """
        if self.__ttPlayerId == 1:
            self.__ttPlayerId = 2
            self.__ttPlayerChar = self.__ttPlayerChar2
        else:
            self.__ttPlayerId = 1
            self.__ttPlayerChar = self.__ttPlayerChar1
        return self
    @_cm
    def ttBoardDisplay(self):
        """
        \\@since 0.3.6 \\
        \\@lifetime ≥ 0.3.6; < 0.3.24; ≥ 0.3.25 \\
        \\@modified 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Games
        ```
        . : Tic-Tac-Toe (Tense 0.3.6) : . \\
        Allows to display the board after modifications, either clearing or placing another char \n
        """
        print(self.__ttBoard[0][0] + " | " + self.__ttBoard[0][1] + " | " + self.__ttBoard[0][2])
        print(self.__ttBoard[1][0] + " | " + self.__ttBoard[1][1] + " | " + self.__ttBoard[1][2])
        print(self.__ttBoard[2][0] + " | " + self.__ttBoard[2][1] + " | " + self.__ttBoard[2][2])
        return self
    @_cm
    def ttBoardLocationSet(self, _input: int):
        """
        \\@since 0.3.7 \\
        \\@lifetime ≥ 0.3.7; < 0.3.24; ≥ 0.3.25 \\
        \\@modified 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Games
        ```
        This method places a char on the specified index on the board
        """
        while not self.ttIndexCheck(_input):
            _input = int(input())
        print("Location set! Modifying the board: \n\n")
        if _input == 1: self.__ttBoard[0][0] = self.__ttPlayerChar
        elif _input == 2: self.__ttBoard[0][1] = self.__ttPlayerChar
        elif _input == 3: self.__ttBoard[0][2] = self.__ttPlayerChar
        elif _input == 4: self.__ttBoard[1][0] = self.__ttPlayerChar
        elif _input == 5: self.__ttBoard[1][1] = self.__ttPlayerChar
        elif _input == 6: self.__ttBoard[1][2] = self.__ttPlayerChar
        elif _input == 7: self.__ttBoard[2][0] = self.__ttPlayerChar
        elif _input == 8: self.__ttBoard[2][1] = self.__ttPlayerChar
        else: self.__ttBoard[2][2] = self.__ttPlayerChar
        self.ttBoardDisplay()
        return self
    @_cm
    def ttBoardClear(self):
        """
        \\@since 0.3.6 \\
        \\@lifetime ≥ 0.3.6; < 0.3.24; ≥ 0.3.25 \\
        \\@modified 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Games
        ```
        Clears the tic-tac-toe board. It is ready for another game
        """
        self.__ttBoard = self.ttBoardGenerate()
        return self
    @_cm
    def ttBoardSyntax(self):
        """
        \\@since 0.3.7 \\
        \\@lifetime ≥ 0.3.7; < 0.3.24; ≥ 0.3.25 \\
        \\@modified 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Games
        ```
        Displays tic-tac-toe board syntax
        """
        print("""
        1 | 2 | 3
        4 | 5 | 6
        7 | 8 | 9
        """)
        return self
    @_cm
    def ttLineMatch(self, messageIfLineDetected: str = "Line detected! Player " + str(__ttPlayerId) + " wins!", messageIfBoardFilled: str = "Looks like we have a draw! Nice gameplay!"):
        """
        \\@since 0.3.6 \\
        \\@lifetime ≥ 0.3.6; < 0.3.24; ≥ 0.3.25 \\
        \\@modified 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Games
        ```
        Matches a line found in the board. Please ensure that the game has started. \\
        Returned values:
        - `0`, when a player matched a line in the board with his character. Game ends after.
        - `1`, when there is a draw - board got utterly filled. Game ends with no winner.
        - `2`, game didn't end, it's still going (message for this case isnt sent, because it can disturb during the game).

        """
        if self.isLineMatched():
            Tense.print(messageIfLineDetected)
            return 0
        elif self.isBoardFilled():
            Tense.print(messageIfBoardFilled)
            return 1
        else: return 2

    @_cm
    def ttChangeChars(self, char1: str = "x", char2: str = "o", /):
        """
        \\@since 0.3.7 \\
        \\@lifetime ≥ 0.3.7; < 0.3.24; ≥ 0.3.25 \\
        \\@modified 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "class method" in class Games
        ```
        Allows to replace x and o chars with different char. \\
        If string is longer than one char, first char of that string is selected \\
        Do it BEFORE starting a tic-tac-toe game
        """
        if reckon(char1) == 1: self.__ttPlayerChar1 = char1
        else: self.__ttPlayerChar1 = char1[0]
        if reckon(char2) == 1: self.__ttPlayerChar2 = char2
        else: self.__ttPlayerChar2 = char2[0]
        return self

def FinalVar(v: _T):
    """
    \\@since 0.3.26c1 \\
    \\@lifetime ≥ 0.3.26c1 \\
    \\@author Aveyzan
    ```ts \\
    in module tense
    ```
    A class-like function referring to class `tense.tcs.FinalVar`. \\
    This creates a final variable

    Use `~instance`, `+instance` or `-instance` to return \\
    value passed to the constructor.
    """
    from tense.tcs import FinalVar as _FinalVar
    return _FinalVar(v)

class _ChangeVarState(tcs.IntegerFlag):
    "\\@since 0.3.26c1. Interal class for `ChangeVar.setState()` method"
    I = 1
    D = 2

_ChangeVarStateSelection = tcs.Literal[_ChangeVarState.D, _ChangeVarState.I]

class ChangeVar(tcs.UnaryOperable, tcs.Comparable, tcs.AdditionReassignable, tcs.SubtractionReassignable):
    """
    \\@since 0.3.26c1 \\
    \\@lifetime ≥ 0.3.26c1 \\
    \\@author Aveyzan
    ```ts \\
    in module tense
    ```
    Auxiliary class for creating sentinel inside `while` loop.

    Use `~instance` to receive integer value. \\
    Use `+instance` to increment by 1. \\
    Use `-instance` to decrement by 1. \\
    Use `instance += any_int` to increment by `any_int`. \\
    Use `instance -= any_int` to decrement by `any_int`.
    """
    D = _ChangeVarState.D
    I = _ChangeVarState.I
    __v = 0
    __m = 1
    __default = 0
    def __init__(self, initialValue = 0):
        if not Tense.isInteger(initialValue):
            err, s = (TypeError, "Expected an integer value")
            raise err(s)
        self.__v = initialValue
        self.__default = initialValue
    def __pos__(self):
        self.__v += self.__m
    def __neg__(self):
        self.__v -= self.__m
    def __invert__(self):
        return self.__v
    def __eq__(self, other: int):
        return self.__v == other
    def __contains__(self, value: int):
        return self.__v == value
    def __ne__(self, other: int):
        return self.__v != other
    def __ge__(self, other: int):
        return self.__v >= other
    def __gt__(self, other: int):
        return self.__v > other
    def __le__(self, other: int):
        return self.__v <= other
    def __lt__(self, other: int):
        return self.__v < other
    def __iadd__(self, other: int):
        if not Tense.isInteger(self.__v):
            err, s = (tcs.NotInitializedError, "Class was not initialized")
            raise err(s)
        _tmp = self.__v
        _tmp += other
        self.__v = _tmp
        return _tmp
    def __isub__(self, other: int):
        if not Tense.isInteger(self.__v):
            err, s = (tcs.NotInitializedError, "Class was not initialized")
            raise err(s)
        _tmp = self.__v
        _tmp -= other
        self.__v = _tmp
        return _tmp
    def reset(self):
        """
        \\@since 0.3.26c1

        Reset the counter to value passed to the constructor, or - \\
        if `setDefault()` was invoked before - to value passed \\
        to that method.
        """
        self.__v = self.__default
    def setDefault(self, value: int):
        """
        \\@since 0.3.26c1

        Set a new default value. This overwrites current default value. \\
        Whether `reset()` method is used after, internal variable \\
        will have the default value, which was passed to this method. \\
        Otherwise it will refer to value passed to constructor
        """
        if not Tense.isInteger(value):
            err, s = (TypeError, "Expected an integer value")
            raise err(s)
        self.__default = value
    def setState(self, s: _ChangeVarStateSelection = I, m: int = 1):
        """
        \\@since 0.3.26c1

        Alternative for `+` and `-` unary operators.

        If `D` for `s` parameter is passed, sentinel will be decremented \\
        by 1, otherwise incremented by 1 (option `I`). Additionally, you \\
        can set a different step via `m` parameter.
        """
        _m = m
        if not Tense.isInteger(_m):
            err, _s = (TypeError, "Expected integer value for 'm' parameter")
            raise err(_s)
        elif abs(_m) == 0:
            _m = 1
        if s == self.D:
            self.__v -= abs(_m)
        elif s == self.I:
            self.__v += abs(_m)
        else:
            err, _s = (TypeError, "Expected 'ChangeVar.I' or 'ChangeVar.D' for 's' parameter")
            raise err(_s)
    def setModifier(self, m: int):
        """
        \\@since 0.3.26c1

        Changes behavior for `+` and `-` unary operators. \\
        If passed integer value was negative, code will \\
        retrieve absolute value of it.
        """
        if not Tense.isInteger(m):
            err, s = (TypeError, "Expected integer value for 'm' parameter")
            raise err(s)
        elif abs(m) == 0:
            self.__m == 1
        self.__m = abs(m)

class _ColorStyling(tcs.IntegerFlag):
    "\\@since 0.3.26c1. Internal class for `%` operator in class `Color`."
    NORMAL = 0
    BOLD = 1
    FAINT = 2
    ITALIC = 3
    UNDERLINE = 4
    SLOW_BLINK = 5
    RAPID_BLINK = 6
    REVERSE = 7
    HIDE = 8
    STRIKE = 9
    PRIMARY_FONT = 10
    # 11-19 alternative font
    GOTHIC = 20
    DOUBLE_UNDERLINE = 21
    NORMAL_INTENSITY = 22
    NO_ITALIC = 23
    NO_UNDERLINE = 24
    NO_BLINK = 25
    PROPOTIONAL = 26
    NO_REVERSE = 27
    UNHIDE = 28
    NO_STRIKE = 29
    # 30-37 foreground color, 3-bit
    # 38 foreground color, 3 4 8 24-bit
    FOREGROUND_DEFAULT = 39
    # 40-47 background color, 3-bit
    # 48 background color, 3 4 8 24-bit
    BACKGROUND_DEFAULT = 49
    NO_PROPOTIONAL = 50
    FRAME = 51
    ENCIRCLE = 52
    OVERLINE = 53
    NO_FRAME = 54 # including "no encircle"
    NO_OVERLINE = 55
    # 56 and 57 undefined
    # 58 underline color, 3 4 8 24-bit
    UNDERLINE_DEFAULT = 59
    IDEOGRAM_UNDERLINE = 60
    IDEOGRAM_DOUBLE_UNDERLINE = 61
    IDEOGRAM_OVERLINE = 62
    IDEOGRAM_DOUBLE_OVERLINE = 63
    IDEOGRAM_STRESS = 64
    NO_IDEOGRAM = 65
    # 66-72 undefined
    SUPERSCRIPT = 73
    SUBSCRIPT = 74
    NO_SUPERSCRIPT = 75
    # 76 undefined but recommended value: no subscript
    # 77-89 undefined
    # 90-97 bright foreground color, 4-bit
    # 100-107 bright background color, 4-bit

_ColorStylingType = tcs.Literal[
    _ColorStyling.NORMAL,
    _ColorStyling.BOLD,
    _ColorStyling.FAINT,
    _ColorStyling.ITALIC,
    _ColorStyling.UNDERLINE,
    _ColorStyling.SLOW_BLINK,
    _ColorStyling.RAPID_BLINK,
    _ColorStyling.HIDE,
    _ColorStyling.STRIKE,
    _ColorStyling.PROPOTIONAL,
    _ColorStyling.FRAME,
    _ColorStyling.ENCIRCLE,
    _ColorStyling.OVERLINE,
]

class Color(tcs.ModuloOperable, tcs.UnaryOperable):
    """
    \\@since 0.3.26c1 \\
    \\@lifetime ≥ 0.3.26c1 \\
    \\@author Aveyzan
    ```ts \\
    in module tense
    ```
    Deputy of experimental class `tense.extensions.ANSIColor`.

    `+instance`, `-instance` and `~instance` allow to get colored string. \\
    `instance % _ColorStylingType` to decorate the string more. Examples::

        Color("Tense") % Color.BOLD
        Color("Countryside!", 8, 0o105) % Color.ITALIC # italic, blue text
        Color("Creativity!", 24, 0xc0ffee) % Color.BOLD # bold, c0ffee hex code text
        Color("Illusive!", 24, 0, 0xc0ffee) % Color.BOLD # bold, c0ffee hex code background, black text
    """
    import re as __re, os as __os
    __fg = None
    __bg = None
    __un = None
    __text = ""
    __bits = 24

    NORMAL = _ColorStyling.NORMAL
    "\\@since 0.3.26c1. Normal text style. Nothing changes there"
    BOLD = _ColorStyling.BOLD
    "\\@since 0.3.26c1. Makes text bold"
    FAINT = _ColorStyling.FAINT
    "\\@since 0.3.26c1"
    ITALIC = _ColorStyling.ITALIC
    "\\@since 0.3.26c1. Makes text italic"
    UNDERLINE = _ColorStyling.UNDERLINE
    "\\@since 0.3.26c1. Adds line below the text. *Experimental*"
    SLOW_BLINK = _ColorStyling.SLOW_BLINK
    "\\@since 0.3.26c1"
    RAPID_BLINK = _ColorStyling.RAPID_BLINK
    "\\@since 0.3.26c1"
    HIDE = _ColorStyling.HIDE
    "\\@since 0.3.26c1. Hide text"
    STRIKE = _ColorStyling.STRIKE
    "\\@since 0.3.26c1. Text becomes crossed out"
    PROPOTIONAL = _ColorStyling.PROPOTIONAL
    "\\@since 0.3.26c1. Propotional spacing. *Experimental*"
    FRAME = _ColorStyling.FRAME
    "\\@since 0.3.26c1"
    ENCIRCLE = _ColorStyling.ENCIRCLE
    "\\@since 0.3.26c1"
    OVERLINE = _ColorStyling.OVERLINE
    "\\@since 0.3.26c1. Adds line above the text. *Experimental*"

    def __isHex(self, target: str):
        _t = target
        HEX = "0123456789abcdef"
        if target.startswith("0x"):
            _t = self.__re.sub(r"^0x", "", _t)
        for c in target:
            if c not in HEX:
                return False
        return True
    def __isDec(self, target: str):
        DEC = "0123456789"
        for c in target:
            if c not in DEC:
                return False
        return True
    def __isOct(self, target: str):
        OCT = "01234567"
        if target.startswith("0o"):
            _t = self.__re.sub(r"^0o", "", _t)
        for c in target:
            if c not in OCT:
                return False
        return True
    def __isBin(self, target: str):
        BIN = "01"
        if target.startswith("0b"):
            _t = self.__re.sub(r"^0b", "", _t)
        for c in target:
            if c not in BIN:
                return False
        return True
    def __pre_convert(self, target: str):
        if self.__isHex(target):
            return int(target, 16)
        elif self.__isDec(target):
            return int(target, 10)
        elif self.__isOct(target):
            return int(target, 8)
        elif self.__isBin(target):
            return int(target, 2)
        else:
            return int(target)
    def __prepare_return(self):
        _s = "\033["
        for e in (self.__fg, self.__bg, self.__un):
            if e is not None:
                if self.__bits == 3 and e not in abroad(0x8):
                    err, s = (ValueError, f"Interal error. For 3-bit colors, expected integer or string value in range 0-7. One of foreground, background or underline values doesn't match this requirement")
                    raise err(s)
                elif self.__bits == 4 and e not in abroad(0x10):
                    err, s = (ValueError, f"Interal error. For 4-bit colors, expected integer or string value in range 0-15. One of foreground, background or underline values doesn't match this requirement")
                    raise err(s)
                elif self.__bits == 8 and e not in abroad(0x100):
                    err, s = (ValueError, f"Interal error. For 8-bit colors, expected integer or string value in range 0-255. One of foreground, background or underline values doesn't match this requirement")
                    raise err(s)
                elif self.__bits == 24 and e not in abroad(0x1000000):
                    err, s = (ValueError, f"Interal error. For 24-bit colors, expected integer or string value in range 0-16777215. One of foreground, background or underline values doesn't match this requirement")
                    raise err(s)
        if self.__bits == 3:
            _s += str(30 + self.__fg) + ";" if self.__fg is not None else ""
            _s += str(40 + self.__bg) + ";" if self.__bg is not None else ""
            _s += "58;5;" + str(self.__un) + ";" if self.__un is not None else ""
        elif self.__bits == 4:
            _s += str(30 + self.__fg) + ";" if self.__fg is not None and self.__fg in abroad(0x8) else ""
            _s += str(40 + self.__bg) + ";" if self.__bg is not None and self.__bg in abroad(0x8) else ""
            _s += str(90 + self.__fg) + ";" if self.__fg is not None and self.__fg in abroad(0x8, 0x10) else ""
            _s += str(100 + self.__bg) + ";" if self.__bg is not None and self.__bg in abroad(0x8, 0x10) else ""
            _s += "58;5;" + str(self.__un) + ";" if self.__un is not None else ""
        elif self.__bits == 8:
            _s += "38;5;" + str(self.__fg) + ";" if self.__fg is not None else ""
            _s += "48;5;" + str(self.__bg) + ";" if self.__bg is not None else ""
            _s += "58;5;" + str(self.__un) + ";" if self.__un is not None else ""
        elif self.__bits == 24:
            _f = hex(self.__fg) if self.__fg is not None else ""
            _b = hex(self.__bg) if self.__bg is not None else ""
            _u = hex(self.__un) if self.__un is not None else ""
            _f = self.__re.sub(r"^0x", "", _f) if reckon(_f) > 0 else ""
            _b = self.__re.sub(r"^0x", "", _b) if reckon(_b) > 0 else ""
            _u = self.__re.sub(r"^0x", "", _u) if reckon(_u) > 0 else ""
            _hf = (int("0x" + _f[0:2], 16), int("0x" + _f[2:4], 16), int("0x" + _f[4:6], 16)) if reckon(_f) > 0 else None
            _hb = (int("0x" + _b[0:2], 16), int("0x" + _b[2:4], 16), int("0x" + _b[4:6], 16)) if reckon(_b) > 0 else None
            _hu = (int("0x" + _u[0:2], 16), int("0x" + _u[2:4], 16), int("0x" + _u[4:6], 16)) if reckon(_u) > 0 else None
            _s += "38;2;" + str(_hf[0]) + ";" + str(_hf[1]) + ";" + str(_hf[2]) + ";" if _hf is not None else ""
            _s += "48;2;" + str(_hb[0]) + ";" + str(_hb[1]) + ";" + str(_hb[2]) + ";" if _hb is not None else ""
            _s += "58;2;" + str(_hu[0]) + ";" + str(_hu[1]) + ";" + str(_hu[2]) + ";" if _hu is not None else ""
        else:
            err, s = (ValueError, f"Internal 'bits' variable value is not one from following: 3, 4, 8, 24")
            raise err(s)
        if _s != "\033[":
            _s = self.__re.sub(r";$", "m", _s)
            _s += self.__text + "\033[0m"
        else:
            _s = self.__text
        return _s
    def __init__(self, text: str, bits: _Bits = 24, foregroundColor: _Color = None, backgroundColor: _Color = None, underlineColor: _Color = None) -> None:
        """
        \\@since 0.3.26c1. Parameters:
        - `text` - string to be colored. Required parameter
        - `bits` - number of bits, possible values: 3, 4, 8, 24, Defaults to 24
        - `foregroundColor` - color of the foreground (text). String/integer/`None`. Defaults to `None`
        - `backgroundColor` - color of the background. String/integer/`None`. Defaults to `None`
        - `underlineColor` (experimental) - color of the underline. String/integer/`None`. Defaults to `None`
        """
        self.__os.system("color")
        if not Tense.isString(text):
            err, s = (TypeError, "Expected string value for 'text' parameter")
            raise err(s)
        if not Tense.isInteger(bits) or (Tense.isInteger(bits) and bits not in (3, 4, 8, 24)):
            err, s = (TypeError, "Expected integer value: 3, 4, 8 or 24, for 'bits' parameter")
            raise err(s)
        for e in (foregroundColor, backgroundColor, underlineColor):
            if not Tense.isInteger(e) and not Tense.isString(e) and e is not None:
                err, s = (TypeError, f"Expected integer, string or 'None' value for '{e.__name__}' parameter")
                raise err(s)
            elif Tense.isString(e) and (
                not self.__isBin(e) and
                not self.__isDec(e) and
                not self.__isHex(e) and
                not self.__isOct(e)
            ):
                err, s = (TypeError, f"Malformed string in parameter '{e.__name__}', expected clean binary, decimal, hexademical or octal string")
                raise err(s)
            elif bits == 24 and e is not None and (
                Tense.isInteger(e) and e not in abroad(0x1000000) or
                Tense.isString(e) and self.__pre_convert(e) not in abroad(0x1000000)
            ):
                err, s = (ValueError, f"For 24-bit colors, expected integer or string value in range 0-16777215")
                raise err(s)
            elif bits == 8 and e is not None and (
                Tense.isInteger(e) and e not in abroad(0x100) or
                Tense.isString(e) and self.__pre_convert(e) not in abroad(0x100)
            ):
                err, s = (ValueError, f"For 8-bit colors, expected integer or string value in range 0-255")
                raise err(s)
            elif bits == 4 and e is not None and (
                Tense.isInteger(e) and e not in abroad(0x10) or
                Tense.isString(e) and self.__pre_convert(e) not in abroad(0x10)
            ):
                err, s = (ValueError, f"For 4-bit colors, expected integer or string value in range 0-15")
                raise err(s)
            elif bits == 3 and e is not None and (
                Tense.isInteger(e) and e not in abroad(0x8) or
                Tense.isString(e) and self.__pre_convert(e) not in abroad(0x8)
            ):
                err, s = (ValueError, f"For 3-bit colors, expected integer or string value in range 0-7")
                raise err(s)
        self.__text = text
        self.__bits = bits
        self.__fg = foregroundColor if Tense.isInteger(foregroundColor) else self.__pre_convert(foregroundColor) if Tense.isString(foregroundColor) else None
        self.__bg = backgroundColor if Tense.isInteger(backgroundColor) else self.__pre_convert(backgroundColor) if Tense.isString(backgroundColor) else None
        self.__un = underlineColor if Tense.isInteger(underlineColor) else self.__pre_convert(underlineColor) if Tense.isString(underlineColor) else None
    def clear(self):
        """
        \\@since 0.3.26c1
        
        Clear every color for foreground, background and underline. Should \\
        be used before `setBits()` method invocation to avoid conflicts. \\
        By default bits value is reset to 24.
        """
        self.__fg = None
        self.__bg = None
        self.__un = None
        self.__bits = 24
        return self
    def setBits(self, bits: _Bits = 24, /):
        """
        \\@since 0.3.26c1

        Possible values: 3, 4, 8, 24. Default is 24
        """
        if not Tense.isInteger(bits) or (Tense.isInteger(bits) and bits not in (3, 4, 8, 24)):
            err, s = (TypeError, "Expected integer value: 3, 4, 8 or 24, for 'bits' parameter")
            raise err(s)
        for e in (self.__fg, self.__bg, self.__un):
            if e is not None:
                if bits == 24 and e not in abroad(0x1000000):
                    err, s = (ValueError, "Interal conflict caught while setting 'bits' value to 24. One of foreground, background or underline values is beyond range 0-16777215. To prevent this conflict, use method 'Color.clear()'.")
                    raise err(s)
                elif bits == 8 and e not in abroad(0x100):
                    err, s = (ValueError, "Interal conflict caught while setting 'bits' value to 8. One of foreground, background or underline values is beyond range 0-255. To prevent this conflict, use method 'Color.clear()'.")
                    raise err(s)
                elif bits == 4 and e not in abroad(0x10):
                    err, s = (ValueError, "Interal conflict caught while setting 'bits' value to 4. One of foreground, background or underline values is beyond range 0-15. To prevent this conflict, use method 'Color.clear()'.")
                    raise err(s)
                elif bits == 3 and e not in abroad(0x8):
                    err, s = (ValueError, "Interal conflict caught while setting 'bits' value to 3. One of foreground, background or underline values is beyond range 0-7. To prevent this conflict, use method 'Color.clear()'.")
                    raise err(s)
        self.__bits = bits
    def setForegroundColor(self, color: _Color = None, /):
        """
        \\@since 0.3.26c1
        
        Set foreground color manually.
        """
        _c = color if Tense.isInteger(color) or color is None else self.__pre_convert(color)
        if _c is not None:
            if self.__bits == 3 and _c not in abroad(0x8):
                err, s = (ValueError, f"For 3-bit colors, expected integer or string value in range 0-7")
                raise err(s)
            elif self.__bits == 4 and _c not in abroad(0x10):
                err, s = (ValueError, f"For 4-bit colors, expected integer or string value in range 0-15")
                raise err(s)
            elif self.__bits == 8 and _c not in abroad(0x100):
                err, s = (ValueError, f"For 8-bit colors, expected integer or string value in range 0-255")
                raise err(s)
            elif self.__bits == 24 and _c not in abroad(0x1000000):
                err, s = (ValueError, f"For 24-bit colors, expected integer or string value in range 0-16777215")
                raise err(s)
            else:
                err, s = (ValueError, f"Internal 'bits' variable value is not one from following: 3, 4, 8, 24")
                raise err(s)
        self.__fg = _c
        return self
    def setBackgroundColor(self, color: _Color = None, /):
        """
        \\@since 0.3.26c1
        
        Set background color manually.
        """
        _c = color if Tense.isInteger(color) or color is None else self.__pre_convert(color)
        if _c is not None:
            if self.__bits == 3 and _c not in abroad(0x8):
                err, s = (ValueError, f"For 3-bit colors, expected integer or string value in range 0-7")
                raise err(s)
            elif self.__bits == 4 and _c not in abroad(0x10):
                err, s = (ValueError, f"For 4-bit colors, expected integer or string value in range 0-15")
                raise err(s)
            elif self.__bits == 8 and _c not in abroad(0x100):
                err, s = (ValueError, f"For 8-bit colors, expected integer or string value in range 0-255")
                raise err(s)
            elif self.__bits == 24 and _c not in abroad(0x1000000):
                err, s = (ValueError, f"For 24-bit colors, expected integer or string value in range 0-16777215")
                raise err(s)
            else:
                err, s = (ValueError, f"Internal 'bits' variable value is not one from following: 3, 4, 8, 24")
                raise err(s)
        self.__bg = _c
        return self
    def setUnderlineColor(self, color: _Color = None, /):
        """
        \\@since 0.3.26c1
        
        Set underline color manually.
        """
        _c = color if Tense.isInteger(color) or color is None else self.__pre_convert(color)
        if _c is not None:
            if self.__bits == 3 and _c not in abroad(0x8):
                err, s = (ValueError, f"For 3-bit colors, expected integer or string value in range 0-7")
                raise err(s)
            elif self.__bits == 4 and _c not in abroad(0x10):
                err, s = (ValueError, f"For 4-bit colors, expected integer or string value in range 0-15")
                raise err(s)
            elif self.__bits == 8 and _c not in abroad(0x100):
                err, s = (ValueError, f"For 8-bit colors, expected integer or string value in range 0-255")
                raise err(s)
            elif self.__bits == 24 and _c not in abroad(0x1000000):
                err, s = (ValueError, f"For 24-bit colors, expected integer or string value in range 0-16777215")
                raise err(s)
            else:
                err, s = (ValueError, f"Internal 'bits' variable value is not one from following: 3, 4, 8, 24")
                raise err(s)
        self.__un = _c
        return self
    def __pos__(self):
        """\\@since 0.3.26c1. Receive colored string"""
        return self.__prepare_return()
    def __neg__(self):
        """\\@since 0.3.26c1. Receive colored string"""
        return self.__prepare_return()
    def __invert__(self):
        """\\@since 0.3.26c1. Receive colored string"""
        return self.__prepare_return()
    def __mod__(self, other: _ColorStylingType):
        """
        \\@since 0.3.26c1
        
        Further styling
        """
        if other == self.NORMAL:
            return self.__prepare_return()
        elif other == self.BOLD:
            return self.__re.sub(r"^(\033\[|\u001b\[)", "\033[1;", self.__prepare_return())
        elif other == self.FAINT:
            return self.__re.sub(r"^(\033\[|\u001b\[)", "\033[2;", self.__prepare_return())
        elif other == self.ITALIC:
            return self.__re.sub(r"^(\033\[|\u001b\[)", "\033[3;", self.__prepare_return())
        elif other == self.UNDERLINE:
            return self.__re.sub(r"^(\033\[|\u001b\[)", "\033[4;", self.__prepare_return())
        elif other == self.SLOW_BLINK:
            return self.__re.sub(r"^(\033\[|\u001b\[)", "\033[5;", self.__prepare_return())
        elif other == self.RAPID_BLINK:
            return self.__re.sub(r"^(\033\[|\u001b\[)", "\033[6;", self.__prepare_return())
        elif other == self.HIDE:
            return self.__re.sub(r"^(\033\[|\u001b\[)", "\033[8;", self.__prepare_return())
        elif other == self.STRIKE:
            return self.__re.sub(r"^(\033\[|\u001b\[)", "\033[9;", self.__prepare_return())
        elif other == self.PROPOTIONAL:
            return self.__re.sub(r"^(\033\[|\u001b\[)", "\033[26;", self.__prepare_return())
        elif other == self.FRAME:
            return self.__re.sub(r"^(\033\[|\u001b\[)", "\033[51;", self.__prepare_return())
        elif other == self.ENCIRCLE:
            return self.__re.sub(r"^(\033\[|\u001b\[)", "\033[52;", self.__prepare_return())
        elif other == self.OVERLINE:
            return self.__re.sub(r"^(\033\[|\u001b\[)", "\033[53;", self.__prepare_return())
        else:
            err, s = (TypeError, "Expected any from constant values: NORMAL, BOLD, FAINT, ITALIC, UNDERLINE, SLOW_BLINK, RAPID_BLINK, HIDE, STRIKE, PROPOTIONAL, FRAME, ENCIRCLE, OVERLINE")
            raise err(s)

    

if __name__ == "__main__":
    err, s = (RuntimeError, "This file is not for compiling, consider importing it instead. Notice it is 'tense' module, but it should be treated as a module to import-only")
    raise err(s)

del deque, t, tcs, time, warnings, uuid, BooleanVar, StringVar # Not for export

__all__ = sorted([n for n in globals() if n[:1] != "_"])


