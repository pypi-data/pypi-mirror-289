"""
**TensePy Types & Constants**

\\@since 0.3.26b3 \\
\\@author Aveyzan \\
https://aveyzan.glitch.me/tense/py/module.tcs.html
```ts \\
module tense.tcs
```
Types and constants package for TensePy.
"""

import sys

if sys.version_info < (3, 9):
    err, s = (RuntimeError, "Use 'tense_eight' module for Python versions below 3.9.")
    raise err(s)

import os, tkinter as tk, typing as tp, types as ty, io, math as ma, collections as ct, warnings as wa, functools as fn, abc
from mmap import mmap
from array import array

#################################### VERSION COMPONENTS (0.3.26b3) ####################################
# Consider NOT changing the version values, as it may be
# mistaken, and possibly you may not be up-to-date.

_a = "alpha"
"""An alpha release; this kind of version is not stable and may not offer some functions"""
_b = "beta"
"""A beta release; this kind of version may have some errors, although may offer all functions"""
_c = "candidate"
"""A candidate release; this kind of version can be released as ultimate, unless there won't be errors on the way"""
_rc = "final"
"""Same as `c`, but it is considered newer release"""
_p = "post-release"
"""A post release; this kind of version is uploaded after factual upload of ultimate version"""
_d = "developer"
"""A dev release; shouldn't be used"""

VERSION = "0.3.26b3"
"""Returns currently used version of Tense"""
VERSION_TUPLE = (0, 3, 26, _b, 3)
"""Returns currently used version of Tense as a tuple"""

#################################### MATH CONSTANTS (0.3.26b3) ####################################

NAN = ma.nan
INF = ma.inf
E = 2.718281828459045235360287471352
PI = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461
TAU = 6.283185307179586476925287
SQRT2 = 1.4142135623730950488016887242097
THOUSAND           = 1000 # 1e+3
MILLION            = 1000000 # 1e+6
BILLION            = 1000000000 # 1e+9
TRILLION           = 1000000000000 # 1e+12
QUADRILLION        = 1000000000000000 # 1e+15
QUINTILLION        = 1000000000000000000 # 1e+18
SEXTILLION         = 1000000000000000000000 # 1e+21
SEPTILLION         = 1000000000000000000000000 # 1e+24
OCTILLION          = 1000000000000000000000000000 # 1e+27
NONILLION          = 1000000000000000000000000000000 # 1e+30
DECILLION          = 1000000000000000000000000000000000 # 1e+33
UNDECILLION        = 1000000000000000000000000000000000000 # 1e+36
DUODECILLION       = 1000000000000000000000000000000000000000 # 1e+39
TREDECILLION       = 1000000000000000000000000000000000000000000 # 1e+42
QUATTUOR_DECILLION = 1000000000000000000000000000000000000000000000 # 1e+45
QUINDECILLION      = 1000000000000000000000000000000000000000000000000 # 1e+48
SEXDECILLION       = 1000000000000000000000000000000000000000000000000000 # 1e+51
SEPTEN_DECILLION   = 1000000000000000000000000000000000000000000000000000000 # 1e+54
OCTODECILLION      = 1000000000000000000000000000000000000000000000000000000000 # 1e+57
NOVEMDECILLION     = 1000000000000000000000000000000000000000000000000000000000000 # 1e+60
VIGINTILLION       = 1000000000000000000000000000000000000000000000000000000000000000 # 1e+63
GOOGOL             = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 # 1e+100
CENTILLION         = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 # 1e+303


#################################### OTHER CONSTANTS ####################################

JS_MIN_SAFE_INTEGER = -9007199254740991
"""
\\@since 0.3.26b3

`-(2^53 - 1)` - the smallest safe integer in JavaScript
"""
JS_MAX_SAFE_INTEGER = 9007199254740991
"""
\\@since 0.3.26b3

`2^53 - 1` - the biggest safe integer in JavaScript
"""
JS_MIN_VALUE = 4.940656458412465441765687928682213723650598026143247644255856825006755072702087518652998363616359923797965646954457177309266567103559397963987747960107818781263007131903114045278458171678489821036887186360569987307230500063874091535649843873124733972731696151400317153853980741262385655911710266585566867681870395603106249319452715914924553293054565444011274801297099995419319894090804165633245247571478690147267801593552386115501348035264934720193790268107107491703332226844753335720832431936092382893458368060106011506169809753078342277318329247904982524730776375927247874656084778203734469699533647017972677717585125660551199131504891101451037862738167250955837389733598993664809941164205702637090279242767544565229087538682506419718265533447265625e-324
"""
\\@since 0.3.26b3

`2^-1074` - the smallest possible number in JavaScript \\
Precision per digit
"""
JS_MAX_VALUE = 17976931348623139118889956560692130772452639421037405052830403761197852555077671941151929042600095771540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368
"""
\\@since 0.3.26b3

`2^1024 - 2^971` - the biggest possible number in JavaScript \\
Precision per digit
"""

SMASH_HIT_CHECKPOINTS = 12
"""
\\@since 0.3.26b3

Amount of checkpoints in Smash Hit (11 normal + 1 endless)
"""
MC_ENCHANTS = 42
"""
\\@since 0.3.26b3

Amount of enchantments in Minecraft
"""
MC_DURABILITY = {
    "helmet_turtleShell": 275,
    "helmet_leather": 55,
    "helmet_golden": 77,
    "helmet_chainmail": 165,
    "helmet_iron": 165,
    "helmet_diamond": 363,
    "helmet_netherite": 407,
    "chestplate_leather": 80,
    "chestplate_golden": 112,
    "chestplate_chainmail": 240,
    "chestplate_iron": 240,
    "chestplate_diamond": 528,
    "chestplate_netherite": 592,
    "leggings_leather": 75,
    "leggings_golden": 105,
    "leggings_chainmail": 225,
    "leggings_iron": 225,
    "leggings_diamond": 495,
    "leggings_netherite": 555,
    "boots_leather": 65,
    "boots_golden": 91,
    "boots_chainmail": 195,
    "boots_iron": 195,
    "boots_diamond": 429,
    "boots_netherite": 481,
    "bow": 384,
    "shield": 336,
    "trident": 250,
    "elytra": 432,
    "crossbow_java": 465,
    "crossbow_bedrock": 464,
    "brush": 64,
    "fishingRod_java": 64,
    "fishingRod_bedrock": 384,
    "flintAndSteel": 64,
    "carrotOnStick": 25,
    "warpedFungusOnStick": 100,
    "sparkler_bedrock": 100,
    "glowStick_bedrock": 100,
    "tool_gold": 32,
    "tool_wood": 65,
    "tool_stone": 131,
    "tool_iron": 250,
    "tool_diamond": 1561,
    "tool_netherite": 2031
}

NULL = None # 0.3.26b3


###### TYPES ######
# I am wondering what that magic variable __slots__ is for

_var = tp.TypeVar
_lit = tp.Literal
_opt = tp.Optional
_uni = tp.Union
_cal = tp.Callable

_T = _var("_T")
_T1 = _var("_T1")
_T2 = _var("_T2")
_T_cov = _var("_T_cov", covariant = True)
_T_con = _var("_T_con", contravariant = True)
_KT = _var("_KT")
_KT_cov = _var("_KT_cov", covariant = True)
_KT_con = _var("_KT_con", contravariant = True)
_VT = _var("_VT")
_VT_cov = _var("_VT_cov", covariant = True)
# abroad types basing on parameter names
_V1 = _var("_V1")
_V2 = _var("_V2")
_M = _var("_M")


class MissingValueError(Exception):
    """
    \\@since 0.3.19 \\
    \\@author Aveyzan
    ```ts \\
    in module tense.tcs // to 0.3.26b3 in module tense.primary
    ```
    Missing value (empty parameter)
    """
    ...
class IncorrectValueError(Exception):
    """
    \\@since 0.3.19 \\
    \\@author Aveyzan
    ```ts \\
    in module tense.tcs // to 0.3.26b3 in module tense.primary
    ```
    Incorrect value of a parameter, having correct type
    """
    ...
class NotInitializedError(Exception):
    """
    \\@since 0.3.25 \\
    \\@author Aveyzan
    ```ts \\
    in module tense.tcs // to 0.3.26b3 in module tense.primary
    ```
    Class was not instantiated
    """
    ...
class InitializedError(Exception):
    """
    \\@since 0.3.26b3 \\
    \\@author Aveyzan
    ```ts \\
    in module tense.tcs
    ```
    Class was instantiated
    """
    ...
class NotReassignableError(Exception):
    """
    \\@since 0.3.26b3 \\
    \\@author Aveyzan
    ```ts \\
    in module tense.tcs
    ```
    Attempt to re-assign a value
    """
    ...

class NotReassignable(tp.Protocol[_T_con]):
    """
    \\@since 0.3.26b3

    This class does not support any form of re-assignment, those are augmented \\
    assignment operators: `+=`, `-=`, `*=`, `**=`, `/=`, `//=`, `%=`, `>>=`, `<<=`, \\
    `&=`, `|=`, `^=`. Setting new value also is prohibited.
    """
    def __error(self):
        err, s = (NotReassignableError, "Cannot modify a final variable")
        raise err(s)
    def __set__(self, i: tp.Self, v: _T_con):
        self.__error()
    def __iadd__(self, o: _T_con):
        self.__error()
    def __isub__(self, o: _T_con):
        self.__error()
    def __imul__(self, o: _T_con):
        self.__error()
    def __ifloordiv__(self, o: _T_con):
        self.__error()
    def __idiv__(self, o: _T_con):
        self.__error()
    def __itruediv__(self, o: _T_con):
        self.__error()
    def __imod__(self, o: _T_con):
        self.__error()
    def __ipow__(self, o: _T_con):
        self.__error()
    def __ilshift__(self, o: _T_con):
        self.__error()
    def __irshift__(self, o: _T_con):
        self.__error()
    def __iand__(self, o: _T_con):
        self.__error()
    def __ior__(self, o: _T_con):
        self.__error()
    def __ixor__(self, o: _T_con):
        self.__error()

class NotComparable(tp.Protocol[_T_con]):
    """
    \\@since 0.3.26b3

    Cannot be compared with operators `==`, `!=`, `>`, `<`, `>=`, `<=`, `in`
    """
    def __error(self):
        err, s = (TypeError, "Cannot compare")
        raise err(s)
    def __lt__(self, other: _T_con):
        self.__error()
    def __gt__(self, other: _T_con):
        self.__error()
    def __le__(self, other: _T_con):
        self.__error()
    def __ge__(self, other: _T_con):
        self.__error()
    def __eq__(self, other: _T_con):
        self.__error()
    def __ne__(self, other: _T_con):
        self.__error()
    def __contains__(self, other: _T_con):
        self.__error()

class NotIterable:
    """
    \\@since 0.3.26b3

    This class disallows iteration
    """
    # __slots__ = ()
    __iter__ = None

Iterable = tp.Iterable[_T]
Iterator = tp.Iterator[_T]

class LeastComparable(tp.Protocol[_T_con]):
    """
    \\@since 0.3.26b3

    Can be compared with `<`
    """
    def __lt__(self, other: _T_con) -> bool: ...

class GreaterComparable(tp.Protocol[_T_con]):
    """
    \\@since 0.3.26b3

    Can be compared with `>`
    """
    def __gt__(self, other: _T_con) -> bool: ...

class LeastEqualComparable(tp.Protocol[_T_con]):
    """
    \\@since 0.3.26b3

    Can be compared with `<=`
    """
    def __le__(self, other: _T_con) -> bool: ...

class GreaterEqualComparable(tp.Protocol[_T_con]):
    """
    \\@since 0.3.26b3

    Can be compared with `>=`
    """
    def __ge__(self, other: _T_con) -> bool: ...

class Comparable(LeastComparable[tp.Any], GreaterComparable[tp.Any], LeastEqualComparable[tp.Any], GreaterEqualComparable[tp.Any]):
    """
    \\@since 0.3.26b3

    An ABC supporting any form of comparison with operators \\
    `>`, `<`, `>=`, `<=`
    """
    ...

class FinalVar(NotReassignable[_T], Comparable): # 0.3.26b3
    """
    \\@since 0.3.26b3

    Indicates a name should be final, and may not be re-assigned. In this case, names \\
    marked with `tense.tcs.FinalVar` are treated as *immutable*, as constants.
    ```py \\
    reassign_me = 96000 # ok
    reassign_me += 3 # ok; gets value 96003
    reassign_me = FinalVar(96000) # ok
    reassign_me += 3 # error
    ```
    To receive value, use one of following:
    ```py \\
    f = FinalVar(69)
    Tense.print(+f) # 69
    Tense.print(-f) # 69
    Tense.print(~f) # 69
    Tense.print(f()) # 69
    Tense.print(f[0]) # 69
    Tense.print(f | 0) # 69
    Tense.print(f & 0) # 69
    Tense.print(f ^ 0) # 69
    Tense.print(f + 0) # 69
    Tense.print(f - 0) # 69
    Tense.print(f ** 0) # 69
    Tense.print(f << 0) # 69
    Tense.print(f >> 0) # 69
    Tense.print(abs(f)) # 69
    Tense.print(math.trunc(f)) # 69
    ```
    """
    __var = None
    def __error(self, code = 1):
        if code == 1:
            err, s = (NotInitializedError, f"Class '{__class__.__qualname__}' was not initalized")
            raise err(s)
        elif code == 2:
            err, s = (TypeError, "Failed to do operation: inappropriate type provided or type does not support specific operators")
            raise err(s)
        elif code == 3:
            err, s = (ValueError, "Could not compare types - at least one of them does not support comparison operators")
            raise err(s)
        else:
            err, s = (TypeError, "Cannot modify a final variable")
            raise err(s)

    def __init__(self, v: _T):
        self.__var = v
    def __get__(self, instance: tp.Self, owner: _T = None) -> _T:
        """Receive value of the final variable"""
        if self.__var is None:
            self.__error(1)
        return self.__var
    def __pos__(self) -> _T:
        """Receive value of the final variable"""
        if self.__var is None:
            self.__error(1)
        return self.__var
    def __neg__(self) -> _T:
        """Receive value of the final variable"""
        if self.__var is None:
            self.__error(1)
        return self.__var
    def __invert__(self) -> _T:
        """Receive value of the final variable"""
        if self.__var is None:
            self.__error(1)
        else:
            return self.__var
    def __call__(self) -> _T:
        """Receive value of the final variable"""
        if self.__var is None:
            self.__error(1)
    def __getitem__(self, index: _lit[0]) -> _T:
        """Receive value of the final variable"""
        if self.__var is None:
            self.__error(1)
        else:
            if index != 0:
                self.__error(2)
            return self.__var
    def __or__(self, other: _lit[0]) -> _T:
        """Receive value of the final variable"""
        if self.__var is None:
            self.__error(1)
        else:
            if other != 0:
                self.__error(2)
            return self.__var
    def __xor__(self, other: _lit[0]) -> _T:
        """Receive value of the final variable"""
        if self.__var is None:
            self.__error(1)
        else:
            if other != 0:
                self.__error(2)
            return self.__var
    def __and__(self, other: _lit[0]) -> _T:
        """Receive value of the final variable"""
        if self.__var is None:
            self.__error(1)
        else:
            if other != 0:
                self.__error(2)
            return self.__var
    def __pow__(self, other: _lit[0]) -> _T:
        """Receive value of the final variable"""
        if self.__var is None:
            self.__error(1)
        else:
            if other != 0:
                self.__error(2)
            return self.__var
    def __add__(self, other: _lit[0]) -> _T:
        """Receive value of the final variable"""
        if self.__var is None:
            self.__error(1)
        else:
            if other != 0:
                self.__error(2)
            return self.__var
    def __sub__(self, other: _lit[0]) -> _T:
        """Receive value of the final variable"""
        if self.__var is None:
            self.__error(1)
        else:
            if other != 0:
                self.__error(2)
            return self.__var
    def __abs__(self) -> _T:
        """Receive value of the final variable"""
        if self.__var is None:
            self.__error(1)
        else:
            return self.__var
    def __trunc__(self) -> _T:
        """Receive value of the final variable"""
        if self.__var is None:
            self.__error(1)
        else:
            return self.__var
    def __lshift__(self, other: _lit[0]) -> _T:
        """Receive value of the final variable"""
        if self.__var is None:
            self.__error(1)
        else:
            if other != 0:
                self.__error(2)
            return self.__var
    def __rshift__(self, other: _lit[0]) -> _T:
        """Receive value of the final variable"""
        if self.__var is None:
            self.__error(1)
        else:
            if other != 0:
                self.__error(2)
            return self.__var
    def __lt__(self, other: _T):
        tmp = True
        if self.__var is None:
            self.__error(1)
        try:
            tmp = bool(self.__var < other)
        except (SyntaxError, TypeError, ValueError):
            self.__error(3)
        return tmp
    def __gt__(self, other: _T):
        tmp = True
        if self.__var is None:
            self.__error(1)
        try:
            tmp = bool(self.__var > other)
        except (SyntaxError, TypeError, ValueError):
            self.__error(3)
        return tmp
    def __le__(self, other: _T):
        tmp = True
        if self.__var is None:
            self.__error(1)
        try:
            tmp = bool(self.__var <= other)
        except (SyntaxError, TypeError, ValueError):
            self.__error(3)
        return tmp
    def __ge__(self, other: _T):
        tmp = True
        if self.__var is None:
            self.__error(1)
        try:
            tmp = bool(self.__var >= other)
        except (SyntaxError, TypeError, ValueError):
            self.__error(3)
        return tmp
    def __eq__(self, other: _T):
        return self.__var == other
    def __ne__(self, other: _T):
        return self.__var != other

if sys.version_info >= (3, 10):
    # this part of the code is basing on source found from builtins.pyi file
    Ellipsis = ty.EllipsisType

else:
    @tp.final
    class ellipsis: ...
    Ellipsis = ellipsis

def final(f: _T):
    """
    \\@since 0.3.26b3

    Decorator for final methods and classes. Classes preceded by this \\
    decorator cannot be subclassed. Final methods cannot be overriden \\
    by the subclass. Better use this decorator instead of class `tense.tcs.Final`.

    Examples:
    ```py
        @final
        class FinalClass: ... # ok
        class SubclassOfFinalClass(FinalClass): ... # error
        class ClassWithFinalMethod:
            @final
            def example(self): ... # ok
        class SubclassOfClassWithFinalMethod(ClassWithFinalMethod):
            def example(self): ... # error
    ```
    """
    try:
        f.__final__ = True
    except (AttributeError, TypeError):
        pass
    return f

def abstract(f: _T):
    """
    \\@since 0.3.26b3

    Decorator for abstract methods and properties

    Example:
    ```py \\
    class Example:
    @abstract
    def test1(): ... # method

    @abstract
    @property
    def test2(): ... # property
    ```
    """
    f.__isabstractmethod__ = True
    return f

class Abstract:
    """
    \\@since 0.3.26b3

    Class for abstract classes. Classes extending this class cannot \\
    be instantiated.

    Usage:
    ```py \\
    class AbstractClass(Abstract): ... # ok
    abstract_instance = AbstractClass() # error
    ```
    """
    def __init__(self, /, *args, **kwds):
        err, s = (TypeError, "Cannot initialize an abstract class")
        raise err(s)

def classvar(v: _T, /):
    """
    \\@since 0.3.26b3 (experimental)

    Transform variable in a class to a class variable.

    This will be valid only whether this function is \\
    invoked inside a class.
    Use it as:
    ```py \\
    class Example:
        test = classvar(96000) # has value 96000
    ```
    """
    class _t:
        _v: ClassVar[_T] = v
    return _t._v

def finalvar(v: _T, /):
    """
    \\@since 0.3.26b3 (experimental)

    Use it as:
    ```py \\
    reassign_me = finalvar(96000) # has value 96000
    reassign_me += 3 # error
    ```
    """
    return FinalVar(v)

class Final:
    """
    \\@since 0.3.26b3 (experimental)

    This class disallows class inheritance. For class members use `final` decorator, \\
    which can also operate on classes

    Usage:
    ```py \\
    class FinalClass(Final): ...
    class SubclassOfFinalClass(FinalClass): ... # error
    ```
    """
    # __slots__ = ('__weakref__',)
    __final__ = True
    def __init_subclass__(cls, /, *args, **kwds):
        try:
            if super().__final__ is True:
                err, s = (TypeError, "Cannot subclass a final class")
                raise err(s)
        except (AttributeError, TypeError):
            pass
        if 'predicate_sentinel' not in kwds or ('predicate_sentinel' in kwds and kwds is not True):
             err, s = (TypeError, "Cannot subclass a final class")
             raise err(s)

class Deprecated:
    """
    \\@since 0.3.26b3 (experimental)

    This class marks a class as deprecated. Every keyword parameter accord to \\
    the ones `warnings.warn()` method has. Instead of `skip_file_prefixes` you \\
    can also use `skipFilePrefixes` and instead of `stacklevel` - `stackLevel`. \\
    Excluded is only `category` parameter, which has value `DeprecationWarning`.

    Parameters: `message`, `stacklevel`, `source`, `skip_file_prefixes`, as in:
    ```py \\
    class IAmDeprecatedClass(Deprecated, message = ..., stacklevel = ..., ...)
    ```
    """
    def __init_subclass__(cls, /, *args, **kwds):
        wa.simplefilter("always", DeprecationWarning)
        wa.warn(
            str(kwds["message"]) if "message" in kwds else "Deprecated class.",
            DeprecationWarning,
            int(kwds["stacklevel"]) if "stacklevel" in kwds else 2,
            kwds["source"] if "source" in kwds else None,
            skip_file_prefixes = kwds["skipFilePrefixes"] if "skipFilePrefixes" in kwds else kwds["skip_file_prefixes"] if "skip_file_prefixes" in kwds else ()
        )
        wa.simplefilter("default", DeprecationWarning)

class SupportsAbs(tp.Protocol[_T_cov]): # 0.3.26b3
    def __abs__(self) -> _T_cov: ...

class SupportsInt(tp.Protocol): # 0.3.26b3
    def __int__(self) -> int: ...

class SupportsIndex(tp.Protocol): # 0.3.26b3
    def __index__(self) -> int: ...

class SupportsFloat(tp.Protocol): # 0.3.26b3
    def __float__(self) -> float: ...

class SupportsBytes(tp.Protocol): # 0.3.26b3
    def __bytes__(self) -> bytes: ...

class SupportsItems(tp.Protocol[_KT_cov, _VT_cov]): # 0.3.26b3
    def items(self) -> tp.AbstractSet[tuple[_KT_cov, _VT_cov]]: ...

class SupportsKeysAndGetItem(tp.Protocol[_KT_cov, _VT_cov]): # 0.3.26b3
    def keys(self) -> tp.Iterable[_KT_cov]: ...
    def __getitem__(self, key: _KT, /) -> _VT_cov: ...

class SupportsLenAndGetItem(tp.Protocol[_T_con]): # 0.3.26b3
    def __len__(self) -> int: ...
    def __getitem__(self, k: int, /) -> _T_con: ...

class SupportsContainsAndGetItem(tp.Protocol[_KT_con, _VT_cov]): # 0.3.26b3
    def __contains__(self, x: tp.Any, /) -> bool: ...
    def __getitem__(self, key: _KT_con, /) -> _VT_cov: ...

class SupportsItemAccess(tp.Protocol[_KT_con, _VT_cov]):
    def __contains__(self, x: tp.Any, /) -> bool: ...
    def __getitem__(self, key: _KT_con, /) -> _KT: ...
    def __setitem__(self, key: _KT_con, value: _VT, /) -> None: ...
    def __delitem__(self, key: _KT_con, /) -> None: ...

class SupportsAdd(tp.Protocol[_T_con, _T_cov]): # 0.3.26b3
    def __add__(self, x: _T_con, /) -> _T_cov: ...

class SupportsAddReflected(tp.Protocol[_T_con, _T_cov]): # 0.3.26b3
    def __radd__(self, x: _T_con, /) -> _T_cov: ...

class SupportsSub(tp.Protocol[_T_con, _T_cov]): # 0.3.26b3
    def __sub__(self, x: _T_con, /) -> _T_cov: ...

class SupportsSubReflected(tp.Protocol[_T_con, _T_cov]): # 0.3.26b3
    def __rsub__(self, x: _T_con, /) -> _T_cov: ...

class SupportsDivMod(tp.Protocol[_T_con, _T_cov]): # 0.3.26b3
    def __divmod__(self, other: _T_con, /) -> _T_cov: ...

class SupportsDivModReflected(tp.Protocol[_T_con, _T_cov]): # 0.3.26b3
    def __rdivmod__(self, other: _T_con, /) -> _T_cov: ...

class SupportsAiter(tp.Protocol[_T_cov]):
    """
    \\@since 0.3.26b3

    An ABC with magic method `__aiter__`, covariant to its type
    """
    def __aiter__(self) -> _T_cov: ...

class SupportsAnext(tp.Protocol[_T_cov]):
    """
    \\@since 0.3.26b3

    An ABC with magic method `__anext__`, covariant to its type
    """
    def __anext__(self) -> tp.Awaitable[_T_cov]: ...

class SupportsCeil(tp.Protocol[_T_cov]):
    """
    \\@since 0.3.26b3

    An ABC with magic method `__ceil__`, covariant to its type
    """
    def __ceil__(self) -> _T_cov: ...

class SupportsFloor(tp.Protocol[_T_cov]):
    """
    \\@since 0.3.26b3

    An ABC with magic method `__floor__`, covariant to its type
    """
    def __floor__(self) -> _T_cov: ...

class SupportsIter(tp.Protocol[_T_cov]):
    """
    \\@since 0.3.26b3

    An ABC with magic method `__iter__`, covariant to its type
    """
    def __iter__(self) -> tp.Iterator[_T_cov]: ...

class SupportsNext(tp.Protocol[_T_cov]):
    """
    \\@since 0.3.26b3

    An ABC with magic method `__next__`, covariant to its type
    """
    def __next__(self) -> _T_cov: ...

class SupportsTrunc(tp.Protocol[_T_cov]):
    """
    \\@since 0.3.26b3

    An ABC with magic method `__trunc__`, covariant to its type
    """
    def __trunc__(self) -> _T_cov: ...

class SupportsHash(tp.Protocol):
    """
    \\@since 0.3.26b3

    An ABC with magic method `__hash__`
    """
    def __hash__(self) -> int: ...

class SupportsRepr(tp.Protocol):
    """
    \\@since 0.3.26b3

    An ABC with magic method `__repr__`
    """
    def __repr__(self) -> str: ...


RichComparable = _uni[LeastComparable[tp.Any], GreaterComparable[tp.Any]]
_T_richComparable = _var("_T_richComparable", bound = RichComparable)

EnchantedBookQuantity = _lit[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36] # since 0.3.26b3
FileType = _uni[str, int, bytes, os.PathLike[str], os.PathLike[bytes]] # since 0.3.26b3
FileMode = _lit[
    'r+', '+r', 'rt+', 'r+t', '+rt', 'tr+', 't+r', '+tr', 'w+', '+w', 'wt+', 'w+t', '+wt', 'tw+', 't+w', '+tw', 'a+', '+a', 'at+', 'a+t', '+at', 'ta+', 't+a', '+ta', 'x+', '+x', 'xt+',
    'x+t', '+xt', 'tx+', 't+x', '+tx', 'w', 'wt', 'tw', 'a', 'at', 'ta', 'x', 'xt', 'tx', 'r', 'rt', 'tr', 'U', 'rU', 'Ur', 'rtU', 'rUt', 'Urt', 'trU', 'tUr', 'Utr', 'rb+', 'r+b', '+rb',
    'br+', 'b+r', '+br', 'wb+', 'w+b', '+wb', 'bw+', 'b+w', '+bw', 'ab+', 'a+b', '+ab', 'ba+', 'b+a', '+ba', 'xb+', 'x+b', '+xb', 'bx+', 'b+x', '+bx', 'rb', 'br', 'rbU', 'rUb', 'Urb',
    'brU', 'bUr', 'Ubr', 'wb', 'bw', 'ab', 'ba', 'xb', 'bx'
] # since 0.3.26b3
FileOpener = _cal[[str, int], int] # since 0.3.26b3
TickTockBoard = list[list[str]] # since 0.3.26b3

ReckonType = _uni[
        dict[_T],
        list[_T],
        tuple[_T, ...],
        str,
        ct.deque[_T],
        set[_T],
        bytes,
        bytearray,
        memoryview,
        range,
        mmap,
        array[_T],
        enumerate[_T],
        frozenset[_T],
        tp.Counter[_T],
        ct.defaultdict[_T],
        io.TextIOWrapper,
        # since 0.3.24
        io.FileIO,
        io.BufferedWriter,
        io.BufferedRandom,
        io.BufferedReader,
        tp.IO[tp.Any],
        # since 0.3.25
        tp.TextIO,
        tp.BinaryIO,
        io.StringIO,
        io.BufferedRWPair,
        tp.Sequence[_T],
        tp.MutableSequence[_T],
        io.BytesIO,
        io.BufferedIOBase,
        tp.Mapping[_T, tp.Any],
        tp.MutableMapping[_T, tp.Any],
        tp.MutableSet[_T],
        tp.AbstractSet[_T],
        tp.Iterable[_T],
        ct.ChainMap[_T],
        ct.OrderedDict[_T],
        # since 0.3.26b3
        tp.AsyncIterable[_T]
] # since 0.3.25
"""
\\@since 0.3.25 \\
\\@author Aveyzan
```ts \\
in module tense.tcs // to 0.3.26b3 in module tense.types
```
Package of types, which are considered countable and satisfy type requirement \\
for function `reckon()`. To 0.3.26b3 also known as `SupportsCountables`.
"""
ReckonNGT = _uni[
        dict,
        list,
        tuple,
        str,
        ct.deque,
        set,
        bytes,
        bytearray,
        memoryview,
        range,
        mmap,
        array,
        enumerate,
        frozenset,
        tp.Counter,
        ct.defaultdict,
        io.TextIOWrapper,
        # since 0.3.24
        io.FileIO,
        io.BufferedWriter,
        io.BufferedRandom,
        io.BufferedReader,
        tp.IO,
        # since 0.3.25
        tp.TextIO,
        tp.BinaryIO,
        io.StringIO,
        io.BufferedRWPair,
        tp.Sequence,
        tp.MutableSequence,
        io.BytesIO,
        io.BufferedIOBase,
        tp.Mapping,
        tp.MutableMapping,
        tp.MutableSet,
        tp.AbstractSet,
        tp.Iterable,
        ct.ChainMap,
        ct.OrderedDict
] # since 0.3.25, renamed from SupportsCountablesLackOfGeneric (0.3.26b3)


ColorType = _opt[_uni[_T, str, tuple[_T, _T, _T]]] # since 0.3.25, renamed from SupportsColor (0.3.26b3)
ColourType = ColorType[_T] # since 0.3.26b3
AbroadValue1 = _uni[int, float, complex, ReckonType[_T]] # since 0.3.25, renamed from SupportsAbroadValue1 (0.3.26b3)
AbroadValue2 = _opt[_uni[int, float, bool, ReckonType[_T], Ellipsis]] # since 0.3.25, renamed from SupportsAbroadValue2 (0.3.26b3)
AbroadModifier = _opt[_uni[AbroadValue1[_T], Ellipsis]] # since 0.3.25, renamed from SupportsAbroadModifier (0.3.26b3)
ModernReplace = _uni[list[_T], tuple[_T, ...], _T] # since 0.3.25, expected string; renamed from SupportsModernReplace (0.3.26b3)
PickSequence = _uni[list[_T], tuple[_T, ...], set[_T], frozenset[_T], ct.deque[_T], tp.Sequence[_T], tp.MutableSequence[_T]] # since 0.3.25, added support for Sequence and MutableSequence, renamed from SupportsPick (0.3.26b3)
SanitizeMode = _lit[0, 1, 2, 3, 4, 5] # since 0.3.25, renamed from SupportsSanitizeMode (0.3.26b3)
TenseVersionType = tuple[_T, _T, _T] # since 0.3.25, renamed from SupportsTenseVersion (0.3.26b3)
AbroadPackType = _uni[list[_T], tuple[_T, ...], ct.deque[_T], set[_T], enumerate[_T], frozenset[_T]] # since 0.3.25, lose of dict and defaultdict support, added frozenset, renamed from SupportsAbroadPackValues (0.3.26b3)
AbroadConvectType = AbroadValue1[_T] # since 0.3.25, renamed from SupportsAbroadConvectValues (0.3.26b3)
AbroadLiveType = AbroadConvectType[_T] # since 0.3.25, renamed from SupportsAbroadLiveValues (0.3.26b3)
AbroadVividType = _uni[tuple[AbroadValue1[_V1]], tuple[AbroadValue1[_V1], AbroadValue2[_V2]], tuple[AbroadValue1[_V1], AbroadValue2[_V2], AbroadModifier[_M]]] # since 0.3.25, renamed from SupportsAbroadVividValues (0.3.26)
# SupportsAbroadDivisor = _uni[int, float] # for 0.3.25 - 0.3.26b3, use FloatOrInteger instead
AbroadInitializer = list[_T] # since 0.3.25
AbroadMultiInitializer = list[list[_T]] # since 0.3.25
FloatOrInteger = _uni[int, float, SupportsFloat, SupportsInt, SupportsIndex] # since 0.3.25
ProbabilityType = _uni[_T, list[_opt[_T]], tuple[_T, _opt[_T]], dict[_T, _opt[_T]], ct.deque[_opt[_T]], set[_opt[_T]], frozenset[_opt[_T]]] # since 0.3.25, expected integer; renamed from SupportsProbabilityValuesAndFrequencies (0.3.26b3)

Integer = int # since 0.3.26b3
Float = float # since 0.3.26b3
Complex = complex # since 0.3.26b3
Boolean = bool # since 0.3.26b3
List = list[_T] # since 0.3.26b3
Tuple = tuple[_T, ...] # since 0.3.26b3
Deque = ct.deque[_T] # since 0.3.26b3
Array = array[_T] # since 0.3.26b3
Dict = dict[_KT, _VT] # since 0.3.26b3
Bytes = bytes # since 0.3.26b3
ByteArray = bytearray # since 0.3.26b3
Filter = filter # since 0.3.26b3
Type = type # since 0.3.26b3
TypeVar = tp.TypeVar # since 0.3.26b3
TypeAlias = tp.TypeAlias # since 0.3.26b3
TypeGuard = tp.TypeGuard[_T] # since 0.3.26b3
Zip = zip # since 0.3.26b3
if sys.version_info >= (3, 10):
    SpecVar = tp.ParamSpec # since 0.3.26b3
    SpecVarArgs = tp.ParamSpecArgs # since 0.3.26b3
    SpecVarKwargs = tp.ParamSpecKwargs # since 0.3.26b3
if sys.version_info >= (3, 11):
    TypeTupleVar = tp.TypeVarTuple # since 0.3.26b3
Unpack = tp.Unpack # since 0.3.26b3
Pack = tp.Concatenate # since 0.3.26b3
Concatenate = Pack # since 0.3.26b3
Container = tp.Container[_T] # since 0.3.26b3
Unzip = Unpack # since 0.3.26b3
Union = tp.Union # since 0.3.26b3
Optional = tp.Optional # since 0.3.26b3
NotRequired = tp.NotRequired # 0.3.26b3
Required = tp.Required # 0.3.26b3
NoReturn = tp.NoReturn # 0.3.26b3
Void = NoReturn # 0.3.26b3
Enumerate = enumerate[_T] # 0.3.26b3
ClassVar = tp.ClassVar[_T] # 0.3.26b3
"""
\\@since 0.3.26b3

Transform variable in a class to a class variable.

Use as:
```py
class Example:
    test1: ClassVar[int] = 96
    test2: ClassVar[str] = "rel"
    test3: ClassVar[list[int]] = []
```
"""
classmember = classmethod
staticmember = staticmethod
abstractmember = abstract

__all__ = [n for n in globals() if n[:1] != "_"]