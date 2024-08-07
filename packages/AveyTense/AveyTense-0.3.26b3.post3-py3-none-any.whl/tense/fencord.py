"""
**TensePy Fencord** \n
\\@since 0.3.24 \\
\\@modified 0.3.25 \\
\\@author Aveyzan
```ts \\
module tense.fencord
```
Since 0.3.25 this module is called `tense.fencord` instead of `tense.core`. \\
Import this module only, if:
- you have Python 3.8 or above
- you have discord.py via `pip install discord`

This TensePy module features `Fencord` class.
"""
import sys

if sys.version_info < (3, 9):
    err, s = (RuntimeError, "Not allowed to import this module when having Python version least than 3.9.")
    raise err(s)

import tense.tcs as tcs
from typing import Any, Coroutine #, ParamSpec, Concatenate, TypeAlias
from tense import *
from warnings import filterwarnings
from discord import Intents, Interaction, Message, Client, Member
from discord.abc import Snowflake
from discord.app_commands import CommandTree, AppCommand, Command
from discord.app_commands.commands import CommandCallback, Binding, Group
from discord.app_commands.translator import locale_str
import re

    
# between @since and @author there is unnecessarily long line spacing
# hence this warning is being thrown; it is being disabled.
filterwarnings("ignore", category = SyntaxWarning)

_var = TypeVar
# _spec = ParamSpec

# _T = _var("_T")
# _P = _spec("_P")

_T_coroutine = _var("_T_coroutine", bound = Callable[..., Coroutine[Any, Any, list[AppCommand]]])

_DiscordHandler = Union[Interaction[Client], Message] # since 0.3.24
# _SupportsSlashCommandServers = Union[_T, list[_T], tuple[_T, ...], set[_T], frozenset[_T], deque[_T], None] # since 0.3.25

@final
class Fencord:
    """
    Fencord
    +++++++
    \\@since 0.3.24 (before 0.3.25 as `DC`) \\
    \\@author Aveyzan
    ```ts \\
    in module tense.fencord
    ```
    Providing methods to help integrating with Discord.

    This class is not yet prepared to become subclassed
    """
    __commandtree = None
    __client = None
    __intents = None
    __synccorountine = None
    @property
    def user(self):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "property" in class Fencord
        ```
        Returns user of this client
        """
        return self.__client.user
    @property
    def servers(self):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "property" in class Fencord
        ```
        Returns servers/guilds tuple in which client is
        """
        return self.__client.guilds
    @property
    def getClient(self):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "property" in class Fencord
        ```
        Returns reference to `Client` instance inside the class.
        """
        return self.__client
    @property
    def getTree(self):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "property" in class Fencord
        ```
        Returns reference to `CommandTree` instance inside the class.

        This might be needed to invoke decorator `CommandTree.command()` \\
        for slash/application commands, since projected method for this class \\
        (`Fencord.slashCommand()`) leads to errors.
        """
        return self.__commandtree
    def __init__(self, intents: Intents = ..., messageContent: bool = True):
        """
        Fencord
        +++++++
        \\@since 0.3.24 (before 0.3.25 as `DC`) \\
        \\@author Aveyzan
        ```ts \\
        in module tense.fencord
        ```
        Providing methods to help integrating with Discord.
        Parameters:
        - `intents` - Instance of `discord.Intents`.
        - `messageContent` - When `True`, `client.message_content` setting is set to `True`, \\
        `False` otherwise. Defaults to `True`.
        """
        if not isinstance(intents, (Intents, tcs.Ellipsis)):
            err = TypeError
            s = f"Parameter 'intends' must have instance of class 'discord.Intents' or an ellipsis, instead received: '{type(intents).__name__}'"
            raise err(s)
        if not isinstance(messageContent, bool):
            err = TypeError
            s = f"Parameter 'messageContent' must have boolean value, instead received: '{type(intents).__name__}'"
            raise err(s)
        if isinstance(intents, tcs.Ellipsis): self.__intents = Intents.default()
        else: self.__intents = intents
        if messageContent: self.__intents.message_content = True
        self.__client = Client(intents = self.__intents)
        self.__commandtree = CommandTree(self.__client)
        e = Time.fencordFormat()
        print(f"\33[1;90m{e}\33[1;36m INITIALIZATION\33[0m Class '{__class__.__name__}' was successfully initalized. Line {inspect.currentframe().f_back.f_lineno}")
    @staticmethod
    def returnName(handler: _DiscordHandler, /, target: Optional[Member] = None, mention: Optional[bool] = None, name: Optional[bool] = None):
        """
        \\@since 0.3.24 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class Fencord
        ```
        Shorthand method for faciliating returning name: display name, mention or just username
        """
        m = ""
        if isinstance(target, Member):
            if mention is True:
                m = target.mention
            else:
                if name is True: m = target.name
                else: m = target.display_name
        else:
            if isinstance(handler, Interaction):
                if mention is True:
                    m = handler.user.mention
                else:
                    if name is True: m = handler.user.name
                    else: m = handler.user.display_name
            else:
                if mention is True:
                    m = handler.author.mention
                else:
                    if name is True: m = handler.author.name
                    else: m = handler.author.display_name
        return m
    @staticmethod
    def initClient():
        """
        \\@since 0.3.24 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class Fencord
        ```
        Shortcut to the following lines of code: 
        ```py \\
        intends = discord.Intends.default()
        intends.message_content = True
        client = discord.Client(intends = intends)
        ```
        Returned is new instance of `Client` class. \\
        It does not apply to variables inside this class.
        """
        intends = Intents.default()
        intends.message_content = True
        return Client(intents = intends)
    @staticmethod
    def commandInvoked(name: str, author: Union[Interaction, Message], /, parameters: Optional[dict[str, str]] = None, error: Optional[str] = None):
        """
        \\@since 0.3.24 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class Fencord
        ```
        Prints `INVOCATION` to the console. If `error` is a string, it is returned as `INVOCATION ERROR`
        """
        e = Time.fencordFormat()
        if error is None:
            if isinstance(author, Message): t = f"\33[1;90m{e}\33[1;38;5;99m INVOCATION\33[0m Invoked message command '{name.lower()}' by '{Fencord.returnName(author, name = True)}'"
            else: t = f"\33[1;90m{e}\33[1;38;5;99m INVOCATION\33[0m Invoked slash command '{name.lower()}' by '{Fencord.returnName(author, name = True)}'"
        else:
            if isinstance(author, Message): t = f"\33[1;90m{e}\33[1;38;5;9m INVOCATION ERROR\33[0m Attempt to invoke message command '{name.lower()}' by '{Fencord.returnName(author, name = True)}'"
            else: t = f"\33[1;90m{e}\33[1;38;5;9m INVOCATION ERROR\33[0m Attempt to invoke slash command '{name.lower()}' by '{Fencord.returnName(author, name = True)}'"
        if parameters is not None:
            t += " with parameter values: "
            for e in parameters:
                t += f"'{e}' -> {parameters[e]}, "
            t = re.sub(r", $", "", t)
        if error is not None: t += f"; \33[4m{error}\33[0m"
        return t
    @staticmethod
    def commandEquals(message: Message, *words: str):
        """
        \\@since 0.3.24 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class Fencord
        ```
        In reality just string comparison operation; an auxiliary \\
        method for message commands. Case is insensitive
        """
        for string in words:
            if message.content.lower() == string: return True
        return False
    
#    def slashCommand(
#        self,
#        name: Optional[Union[str, locale_str]] = None,
#        desc: Optional[Union[str, locale_str]] = None,
#        nsfw: bool = False,
#        servers: _SupportsSlashCommandServers[Snowflake] = None,
#        autoLocaleStrings: bool = True,
#        extras: Optional[dict[Any, Any]] = None,
#        override: bool = False
#        ) -> Callable[[CommandCallback[Group, _P, _T]], Command[Group, _P, _T]]:
        """
        \\@since 0.3.25 (experimental) \\
        \\@author Aveyzan
        ```ts
        "method" in class Fencord
        ```
        A decorator for slash/application commands. Typically a slight remake of `discord.app_commands.command()`.

        Parameters (all are optional):
        - `name` - The name of the command. If none provided, command name will be name of the callback, fully lowercased. \\
        If `name` was provided, method will convert the string to lowercase, if there is necessity. Defaults to `None`.
        - `desc` - Description of the command. This shows up in the UI to describe the command. If not given, it defaults to the \\
        first line of the docstring of the callback shortened to 100 characters. Defaults to `None`.
        - `nsfw` - Indicate, whether this command is NSFW (Not Safe For Work) or not. Defaults to `False`.
        - `servers` - List/tuple/set/frozenset/deque of servers/guilds (there instances of `discord.Object`). If `None` given, command \\
        becomes global. This parameter can be also single instance of `discord.Object`. Defaults to `None`.
        - `autoLocaleString` - When it is `True`, then all translatable strings will implicitly be wrapped into `locale_str` \\
        rather than `str`. This could avoid some repetition and be more ergonomic for certain defaults such as default \\
        command names, command descriptions, and parameter names. Defaults to `True`.
        - `extras` - A dictionary that can be used to store extraneous data. The library will not touch any values or keys within this \\
        dictionary. Defaults to `None`.
        - `override` - If set to `True`, no exception is raised and command may be simply overwritten. Defaults to `False`.
        """
#        if self.__commandtree is None:
#            err, s = (IncorrectValueError, f"Since 0.3.25 the '{__class__.__name__}' class must be concretized and needs to take '{Client.__name__}' class argument.")
#            raise err(s)
#        else:
#            def _decorator(_function: CommandCallback[Group, _P, _T]) -> Command[Group, _P, _T]:
#                if not inspect.iscoroutinefunction(_function):
#                    err, s = (TypeError, "Expected command function to be a coroutine function")
#                    raise err(s)
#                cmd = Command(
#                    name = name.lower() if isinstance(name, str) else name if name is not None else _function.__name__,
#                    description = desc if desc is not None else "..." if _function.__doc__ is None else _function.__doc__[:100],
#                    callback = _function,
#                    nsfw = nsfw,
#                    parent = None,
#                    auto_locale_strings = autoLocaleStrings,
#                    extras = extras
#                )
#                self.__commandtree.add_command(
#                    cmd,
#                    guild = servers if isinstance(servers, Snowflake) else servers[0] if not isinstance(servers, Snowflake) and reckon(servers) == 1 else None,
#                    guilds = tuple(servers) if not isinstance(servers, Snowflake) and reckon(servers) > 1 else None,
#                    override = override
#                )
#                return cmd
#            return _decorator

    def sync(self, server: Optional[Snowflake] = None):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "method" in class Fencord
        ```
        Sync all slash/application commands, display them on Discord, and translate all strings to `locale_str`. \\
        Used for `on_ready()` event as `await fencord.sync(server?)`. If class wasn't initialized, thrown is error \\
        `tense.primary.NotInitializedError`.

        Parameters:
        - `server` (Optional) - The server/guild to sync the commands to. If `None` then it syncs all global commands \\
        instead.
        """
        if self.__commandtree is None:
            err, s  = (tcs.NotInitializedError, f"Since 0.3.25 the '{__class__.__name__}' class must be concretized.")
            raise err(s)
        else:
            self.__synccorountine = self.__commandtree.sync(guild = server)
            return self.__synccorountine
    
    def event(self, coroutine: _T_coroutine, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "method" in class Fencord
        ```
        A decorator which defines an event for client to listen to.

        Function injected with this decorator must have valid name,
        those can be for example: `on_message()`, `on_ready()`
        """
        if self.__client is None:
            err, s = (tcs.NotInitializedError, f"Since 0.3.25 the '{__class__.__name__}' class must be concretized.")
            raise err(s)
        elif not inspect.iscoroutinefunction(coroutine):
            err, s = (TypeError, "Expected 'coroutine' parameter to be a coroutine.")
            raise err(s)
        else:
            return self.__client.event(coroutine)
        
    @staticmethod
    def bold(text: str, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class Fencord
        ```
        On Discord: make text bold
        """
        return f"**{text}**"
    @staticmethod
    def italic(text: str, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class Fencord
        ```
        On Discord: make text italic
        """
        return f"*{text}*"
    @staticmethod
    def underline(text: str, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class Fencord
        ```
        On Discord: make text underlined
        """
        return f"__{text}__"
    @staticmethod
    def code(text: str, language: Optional[str] = None, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class Fencord
        ```
        On Discord: coded text
        """
        if language is None:
            return f"`{text}`"
        else:
            return f"```{language}\n{text}\n```"
    @staticmethod
    def big(text: str, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class Fencord
        ```
        On Discord: make text big
        """
        return f"# {text}"
    @staticmethod
    def medium(text: str, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class Fencord
        ```
        On Discord: make text medium
        """
        return f"## {text}"
    @staticmethod
    def small(text: str, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class Fencord
        ```
        On Discord: make text small
        """
        return f"### {text}"
    @staticmethod
    def smaller(text: str, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class Fencord
        ```
        On Discord: make text smaller
        """
        return f"-# {text}"
    @staticmethod
    def quote(text: str, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class Fencord
        ```
        On Discord: transform text to quote
        """
        return f"> {text}"
    @staticmethod
    def spoiler(text: str, /):
        """
        \\@since 0.3.25 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class Fencord
        ```
        On Discord: make text spoiled
        """
        return f"||{text}||"
    @staticmethod
    def textUrl(text: str, url: str, hideEmbed = True):
        """
        \\@since 0.3.26a2 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class Fencord
        ```
        On Discord: make text become hyperlink, leading to specified URL
        """
        return f"[{text}](<{url}>)" if hideEmbed else f"[{text}]({url})"
    @staticmethod
    def silent(text: str):
        """
        \\@since 0.3.26a3 \\
        \\@author Aveyzan
        ```ts \\
        "static method" in class Fencord
        ```
        Make a message silent. Usable for Direct Messages. \\
        As a tip, refer `@silent` as `> ` (quote), and message \\
        MUST be prefixed with `@silent`.
        """
        return f"@silent {text}"

del filterwarnings
                    
if __name__ == "__main__":
    err = RuntimeError
    s = "This file is not for compiling, consider importing it instead."
    raise err(s)

