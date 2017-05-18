![](http://i.imgur.com/V7Fr14e.jpg)

1. Ordering of python lists is persistent. [src][stackoverflow]
1. Pycharm hinting:

```
        """
        Exploit the workers by hanging on to outdated imperialist dogma which
        perpetuates the economic and social differences in our society.

        @type peasant: Person
        @param peasant: Person to oppress.
                        http://grammarist.com/usage/oppress-repress-suppress/
        """
```

1. [PEP 3107](http://legacy.python.org/dev/peps/pep-3107/) hinting:

```
def foo(a: 'what is a', b: 5 + 6, c: list) -> max(2, 9):
    # foo accepts a (commented), b (11), c (any kind of list), and returns 9
```

1. Under normal circumstances, `register.simple_tag` is all you need for your django templating needs.
1. To pretty-format a JSON file, do `cat ugly.json | python -mjson.tool > pretty.json`.
1. `re.VERBOSE`, aka `re.X`, will ignore all whitespaces in a regex. Will Also ignore everything after a `#`.
1. Python does not raise a rounding exception when a large number is used. The typical check is `n + 1 == n`.
1. To speed up a read-only query, try adding `.values_list(fields...)` to a QuerySet, which returns simple tuples.
1. It is absolutely possible that django `loaddata` is a douchebag.
  Therefore, to import all objects without referential errors, use `python manage.py loaddata init_dev.json`,
  which provides all references before inserting.
1. Multiple args: calling a `function(a, b, **kwargs)` where kwargs contains `a=4` or `b=[]` will raise an Exception.
1. `dict(a=4,b=5)` === `{'a': 4, 'b': 5}`
1. There is such thing as a [for else][stackoverflow 2] condition, where the `else` part doesn't execute only if the for loop is `break`ed from within.
1. `for` also runs `else` if the loop is never run (e.g. has 0 items).
1. There is also a [while-else loop](http://www.tutorialspoint.com/python/python_while_loop.htm) that runs when the variable changes to `False`.
1. [Django creates the project for you.][djangoproject]
1. Variables can be *accessed* from an inner scope, but the outer value of the same variable will not be changed. Use [`nonlocal`][stackoverflow 3] to change the outer value.
1. `*args` is of type tuple, not list.
1. Use the `for-else` loop to avoid setting "flag variables", e.g. `found = False ...`. Faster than flags in Python.
1. `dict(a dict)` clones the dict (for one level).
1. `list(a list)` clones the list (for one level).
1. These three are successively better than the former.

```
for k in d:
    print k, d[k]

for k, v in d.items():
    print k, v

for k, v in d.iteritems():
    print k, v
```

1. `dict`s have a `setdefault` method: avoids `KeyError`s.
1. Instead of updating dictionaries with another dictionary, there is a `ChainMap` in Python 3 that handles the common "defaults" use case.
1. [Use full kwargs everywhere, except in loops][youtu]
1. `NamedTuple` is a subclass of `Tuple` that lets you express what the tuple values actually are.
1. Built-in tuple unpacking (`a, b = (1, 2)`) is faster than loading them with indices.
1. Always concatenate strings with `.join`.
1. Python 3.4 can ignore all but some exceptions using `with ignored(TypeError, ValueError, ...):`.
1. Generator expressions, e.g. `sum(i for i in list)` is faster than `sum([i for i in list])`.
1. Django or nosetests runs any `TestCase` subclass in files with their names beginning with `test` when you run `manage.py test`.
1. `django.http` contains http error classes that handle the nitty gritty (e.g. allowed methods in 405)
1. [You cannot make a `dict`, `json.loads`, `json.dumps`, or otherwise, with integer keys in python][stackoverflow 4].
1. If you are a jackass, you [can][stackoverflow 5] write recursive lambdas.
1. Decorators can return functions that are already wrapped with decorators, by virtue that decorators can be wrapped in anything.
1. Every module is imported only once, but every `import` call will invoke a check to make sure the module is imported.
1. `@functools.wraps(fn)` is used to wrap a the wrapper function inside a decorator that helps preserve the original function's docstrings.
1. [`apply`][python] is a keyword. It is a bit like `map`.
1. "Almost every time you use `reduce` means you are doing something wrong", so `reduce()` was moved into `functools.reduce()` in Python3.
1. [`__contains__`][stackoverflow 6] controls the behaviour of `a in obj`.
1. [Django `smart_str`][djangoproject 2] along with `smart_unicode` probably solves all of Python 2's problems.
1. [Python `Enum`][stackoverflow 7] Spoiler: 3.4+
1. The `buffer` type is used to create [multiple "varied" reference to some parts of a large object in memory][stackoverflow 8].
1. `for` creates a new scope. `for foo in foo` if `foo` is `"bar"` then it prints b, a, then r.
1. Keys can be pretty much anything, and they are not stringified: `{None: 'b', 1: 5, <function __main__.<lambda>>: 4, '1': 6}`
1. Taking that right back, [lists cannot be dictionary keys][python 2].
1. "You don't mock out any part of our system, you mock out other people's code"
1. [`assertEquals` is deprecated][python 3]
1. If `assertEqual` receives two `dict`s, it automatically calls `assertDictEqual`.
1. [`itertools.cycle`][python 4]: for when you want to loop over something, over and over
1. Django's `QueryDict` can be converted to a dict by calling `.dict()`.
1. [`StringIO.StringIO`][python 5] is **not** used for performance reasons. It is used to [convert a string into a memory-bound file][stackoverflow 9] so functions that expect a file can work without writing the string to a file first.
1. There is a `3to2`!
1. You can [decorate functions with classes][bitbucket] that have `__call__`!
1. Instance variables (`class.foo == 'far'`) are class variables (`class.foo == Class.foo`) as long as [the instance doesn't change its instance variable's value][stackoverflow 10].
1. `[:]` (aka `[None:None]`) [copies a list][stackoverflow 11] (Fast copy; Thanks Ford)
1. `enumerate()`: returns tuples with index as the first value
1. `re.sub(pattern, repl, string)` is technically `re.sub(pattern, lambda repl: repl, string)`, which allows [text munging][python 6].
1. `yield`s are formally referred to as [coroutines][wikipedia] -- function with multiple entry/resume points.
1. The `signal` package has an `alarm` method that can [timeout a long-running function][python 7].
1. [Python3 exceptions are only accessible within the `except` block, for GC reasons][toptal]. Interestingly, even if the same name existed outside the `except` block, [Python3 will remove the variable of the same name from the outer scope](http://www.wefearchange.org/2013/04/python-3-language-gotcha-and-short.html).
1. Set generators are [already available in python2.7][wikipedia 2].
1. The `set`'s `discard` method makes stupid things like `new_set = {x for x in old_set if x != 'foo'}` a little bit redundant.
1. Lambda expressions can have parameter defaults, positional and keyword arguments!
1. Django Foreign keys default to `None`.
1. `__future__` imports can only be done at the top of a file.
1. Override `parse_start_url` to diagnose Scrapy errors that occur on start urls.
1. [You can and should use monads in your code in almost any programming language][valuedlessons]
1. `a >> b` can be overridden using the magic method `__rshift__`.
1. I don't know what the author was talking about, but python has something called the [bidirectional generator][google] which no one explained.
1. Override `parse_start_url` to diagnose Scrapy errors that occur on start urls.
1. In Django, `admin.site.register(Model)` doesn't need an admin (e.g. `admin.site.register(Model, ModelAdmin)`) if all you want is an automatic form.
1. `\d` [isn't][stackoverflow 12] `0-9` -- it also contains digits from other locales.
1. Contrary to popular opinion, `requirements.txt` simply came from `pip freeze > requirements.txt`.
1. `pip freeze` also removes duplicate package requirements, so it helps you clean up the file in a way.
1. Generate random test urls using `itertools.product`: http://stackoverflow.com/questions/2535924/simple-way-to-create-possible-case/2535934#2535934
1. ~~It is not necessary to `urlunparse` a url before generating a new url with parts changed. `urlparse(url, scheme='http')` changes the schema of that url to http.~~ I lied. It only works for `scheme`.
1. `unicode`'s `translate` is different from `str`'s `translate`; their translation tables are [not interchangeable][stackoverflow 13] (`unicode` strings require `unicode` tables)
1. Every single [virtual environment][python-guide] directory (`venv`) has a `bin/activate` which you can `.`.
1. And, get this, your repository does not need to be cloned into the virtual environment directory.
1. Trick from the Internet: "To automatically unpack a list containing a single item, append a trailing comma to the variable name on the left of the assignment operation."
1. Tastypie allows only GET by default. `authorization = Authorization()` is required in the `Meta` class to allow insecure PATCHes.
1. An instance's class [can be changed][stackoverflow 14] dynamically, restricted to user-defined classes only; it's unadvisable to do so regardless.
1. `if` statements do NOT have an `else` equivalent of `for...else`, i.e. if [none of the branches are completely run](http://stackoverflow.com/q/21612910/1558430), because `if` statements don't have `break`s.
1. `if` statements do NOT have any kind of `for...else`-type block that is run whenever any one or more conditions above are run.
1. Python does not optimise tail calls.
1. `def foo(a, (b, c), d)` destructures the second tuple. (Thanks @sboparen)
1. Django `TestCase` has a `@skip` decorator that, if added to any `def test_` methods, will disable the test. (`from django.utils.unittest.case import skip`)
1. [Certain evidence](http://programmers.stackexchange.com/a/187471) points to recommend importing just a module (`import module` instead of `from module import func1, func2`) if a lot of things are used from that module. (Then again, how you can live with writing `module.func1` and `module.func2` all the time is beyond me.)
1. `()` is a thing, and `(this,)` is a thing. A trailing comma is required only if the tuple contains exactly one item.
1. `setattr(a_django_object, ...)` will silently update the object's `__dict__`. Doing the same `setattr` to an object will cause an `AttributeError` if the attribute was not defined in the class.
1. `python -m webbrowser <url>` opens... that url in your browser.
1. Python 3.0 ~ 3.2 don't have the `u'unicode string literal'` syntax, which would crash any python2 script that are otherwise the same as its python3 counterpart.
1. Apparently [you can get `easy_install` from `python-setuptools`](http://www.mediawiki.org/wiki/Gerrit/git-review).
1. Apparently [you can get `pip` from `easy_install`](http://www.mediawiki.org/wiki/Gerrit/git-review), too.
1. Python 2.7+ is the only python2 version that comes with the set notation (`{1, 2, 3}`).
1. [PyLint expects all global variables to be constants, and be named in ALL_UPPERCASE](http://docs.pylint.org/tutorial.html)
1. Want a monad for absolutely no work? Get [PyMonad](https://pypi.python.org/pypi/PyMonad/)!
1. [Marisa-trie](https://github.com/kmike/marisa-trie) consumes less memory than if you decide to build your own trie in python.
1. `bytes(...)`: turn strings into sequences of anything from 0 to 255.
1. [`simplejson` is subjectively better than `json`](http://stackoverflow.com/questions/712791/what-are-the-differences-between-json-and-simplejson-python-modules) -- to use either, `import simplejson as json`.
1. It is [an insanely stupid idea](http://stackoverflow.com/questions/6031584/python-importing-from-builtin-library-when-module-with-same-name-exists) to have a folder that has the same name as one of the built-in libraries.
1. It wasn't possible to `import (many things with brackets)` [until python 2.7](http://legacy.python.org/dev/peps/pep-0328/).
1. `range()` can actually be faster in some cases - eg. if iterating over the same sequence multiple times.  `xrange()` has to reconstruct the integer object every time, but `range()` will have real integer objects. (It will always perform worse in terms of memory however, and there is no such thing as Python2's `range()` in Python3.)
1. If you aren't being code reviewed or anything, you can subclass `namedtuple` like this:

```
class Foo(namedtuple('lol', 'a b c')): pass
```

1. `namedtuple` accepts pretty much anything for its second argument. These all work.

```
namedtuple('a', ['b', 'c'])
namedtuple('a', 'b, c')
namedtuple('a', 'b c')
namedtuple('a', """
b
c
""")
```

1. If a function is decorated with `contextlib.contextmanager`, then [it can be used as a `with` statement](https://docs.python.org/2/library/contextlib.html). The function must contain exactly one `yield`, where things that happen before the `yield` works like `__enter__`, and what happens after the `yield` is treated like `__exit__`.
1. Eloborating on `contextmanager`, the `yield` must be *run* only once; the statement cannot be in a loop.
1. [`contextlib.suppress(BaseException)`](https://docs.python.org/3/library/contextlib.html#contextlib.suppress) is basically the `never_fail` decorator. And oops, it is only for Python 3.
1. `random.seed()` is better than `random.seed(0)`, because [the parameter default is the system time](https://docs.python.org/2/library/random.html#random.seed).
1. `hash(-2)` is the same as `hash(-1)`.
1. Objects that have an overridden __eq__ cannot be hashed, unless their __hash__ are also defined.
1. Python2 does [float multiplications](https://github.com/python/cpython/blob/10d5f4d9b6279945ba8062fd04c0314e5ead0a53/Objects/intobject.c#L533) internally to compute results of integer multiplications, presumably to find out of two numbers multiplying each other will cause an overflow.
1. It is possible to [`__import__('python-module-with-dashes-in-the-filename'`](http://stackoverflow.com/questions/761519/is-it-ok-to-use-dashes-in-python-files-when-trying-to-import-them), but if you create a file such as this, you deserve to be shot.
1. `os.getenv('HOME')` works, only because `$HOME` is populated by the shell.
1. [You can compare tuples](http://stackoverflow.com/a/5292332/1558430)! `(1,2)` is less than `(3, 4)`.
1. You can assign to spliced arrays: `arr[:4] = [9,9]` replaces the first 4 items of the array with `[9,9]`.
1. `round()` doesn't work on `Decimal`s. To round a `Decimal` to certain digits, do: `Decimal(123.456789).quantize(Decimal("0.001"))  # 3 decimal points`
1. `Decimal.quantize` is called that because it also makes up more decimal points if you ask it to: `Decimal(1234.56789).quantize(Decimal("0.000000000000000001"))  # Decimal('1234.567890000000033979')`
1. You *can* `def foo(bar=NamedTupleAsDefaultValue())`, but would you...?
1. `arrow.replace()` accepts singluar nouns like `hour` that replaces the component, or plural forms like `hours` that shifts the value relatively, instead.
1. [Guido](https://mail.python.org/pipermail/python-dev/2010-April/099459.html) doesn't like `merged_dict = dict(some_dict, **another_dict)`, and nor do you. (it only handles string keys)
1. In Python3, arguments can be [forced named](http://stackoverflow.com/a/14298976/1558430): with `def foo(a, * must_use_kwargs_for_this_arg)`.
1. One-liner `if` clauses are executed before the assignment, so `b = a.foo if a else 2` will not raise `AttributeError` even if `a = None`.
1. ["Never (create, change, or delete models) directly"](http://www.dabapps.com/blog/django-models-and-encapsulation/) - Tom Christie
1. `bool` is a subclass of `int`, and cannot be subclassed further.
1. "Either or" is `bool(a) != bool(b)`, or just `operator.xor`. This is different from `nand`, which is false when both are false, and not `nor`, which is true when both are true.
1. As much as tuples are immutable, its contents are:

```
>>> a = ([], [])
>>> a[0].append(1)
>>> a
([1], [])
```

1. `logging.debug("{}".format(123))` builds strings unnecessarily when logging level is set to above debug. To combat this, use `logging.debug(u"%s", 123)` instead, where the arguments must be positional. For internal reference, the Gerrit ID is 626.
1. Strings can also be formatted traditionally with a keywords: `'Today is %(month)s %(day)s.') % {'month': m, 'day': d}`
1. [`python -W all`](http://stackoverflow.com/a/18996013/1558430) prints all `PendingDeprecationWarning`s, and is the preferred way to run python locally.
1. [`j` is the only notation for complex numbers.](http://stackoverflow.com/a/8370696/1558430)

```python
>>> abs(1+12i)
  File "<stdin>", line 1
    abs(1+12i)
            ^
SyntaxError: invalid syntax
>>> abs(1+12j)
12.041594578792296
```

1. The `abs()` of a complex number is the dot product of its real-imaginary plane. If this is not intended, use `math.fabs()` instead, which raises on imaginary numbers.
1. Unit test `self.assert*`s take a last parameter that is the failure message: `self.assertIn(0, [1,2,3], "0 not found in list")`
1. `(str).casefold()` is meant to normalise all variants of the same string, such as `['False', 'false', 'FALSE']` into something you can put into a switch-case block. Then again, there isn't switch-case in Python, only dict keys.
1. The [try-finally block](https://wiki.python.org/moin/HandlingExceptions) has no `except`, so it runs the finally block (which typically rolls back something), then raises the exception.
1. Although there are no docstring type-hinting standards, [this one by PyCharm](https://www.jetbrains.com/pycharm/help/type-hinting-in-pycharm.html) will do: `:param parameter_name: x.y.ParameterClass | None`
1. [`sum()` takes a second parameter](https://docs.python.org/2/library/functions.html#sum), `start`. It really means `sum() + start`.
1. `history` is always a variable in ipython.
1. Booleans are inherited from `int`, so you can add them together.
1. "Tim Peters also snuck some subtle jokes into the Zen itself (notice the dashes on the TOOWTDI line do it two different ways?"
1. Multiple assignments (e.g. `a = b = []`) assigns the same reference to each variable, even if the value is primitive (e.g. `5`).
1. [When called with three arguments, type acts like a constructor, so you can create new types in an inline fashion.](http://ivansmirnov.io/python-metaclasses/)
1. There's [a whole package](https://pypi.python.org/pypi/lockfile) for the `process.pid` thing.
1. Sending gzip requests through the `requests` library is [completely manual](http://stackoverflow.com/questions/28656068/compressing-request-body-with-python-requests). You really have to construct a gzip stream and modify the headers.
1. As an asider, [`Transfer-Encoding: gzip` is a better header than `Content-Encoding: gzip`](http://stackapps.com/questions/916/why-content-encoding-gzip-rather-than-transfer-encoding-gzip) because the latter does not imply the final content type of `.gz`.
1. In Python 3, unbound methods don't exist. There is `unbound_method()` in six that achieves a similar goal.
1. [django-rest-swagger](https://github.com/marcgibbons/django-rest-swagger/) documents the API.
1. `max(None, 0)` is 0. `max(0, None)` is also 0. `min(None, 0)` is `None`. Therefore, `None < 0`. In fact, `None < float('-inf')`.
1. `UnicodeEncodeError` and `UnicodeDecodeError` in a nutshell:

```
>>> "{}".format('Café')                  # str to str
'Caf\xc3\xa9'                            # ok
>>> u"{}".format(u'Café')                # utf8 to utf8
u'Caf\xe9'                               # ok
>>> u"{}".format('Café'.decode('utf8'))  # utf8 to utf8
u'Caf\xe9'                               # ok
>>> "{}".format(u'Café')                 # utf8 to str
UnicodeEncodeError: 'ascii' codec can't encode character u'\xe9' in position 3: ordinal not in range(128)
>>> u"{}".format('Café')                 # str to utf8
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 3: ordinal not in range(128)
```

1. [**There's no formal guarantee about the stability of sets (or dicts, for that matter.)**](http://stackoverflow.com/a/3812600) However, in the CPython implementation, as long as nothing changes the set, the items will be produced in the same order.
1. [Assigning attributes to a function doesn't raise `AttributeError`s](https://mail.python.org/pipermail/python-dev/2000-April/003364.html). PEP 232 [tries to justify it](https://www.python.org/dev/peps/pep-0232/)--the gist being, "it doesn't hurt."
1. `isinstance()` accepts a tuple worth of types.
1. Installing `python-examples` apparently [gives access to `reindent.py`](http://stackoverflow.com/a/1024489/1558430), which obviously reindents python scripts.
1. Splicing a `range` (which is `xrange`) in python3 gives you another `range`. The equivalent `xrange` cannot be spliced in python2.
1. By overriding the behaviour of `__lt__`, `__gt__`, `__eq__`, etc., things that often do comparisons (and therefore return bools) now return SQL "Expression" objects, like so:

```
>>> str(db.Column('a') > db.Column('b'))
'a > b'  # look ma, not a bool
```

1. [An `Enum`'s class attributes have itself as its own class](https://docs.python.org/3/library/enum.html). `isinstance(Color.green, Color) is True`.
1. But with every `Enum` having every attribute in its own class, they don't have access to other attributes: `Color.red.blue  # AttributeError`
1. Depending on version, [Python2 and 3 raise different errors](http://stackoverflow.com/a/23703899/1558430) when an `object()` is asked if it is equal to another `object()`.
1. Exploiting the tuple syntax can make multidimentional "arrays" very easy to work with:

```
>>> a = {(1,2): 4}  # This can be a subclass of `dict` with list indexing
>>> a[1,2]
4
```

1. If you use `python2` to run a script with a `#!/... python3` shebang in it, it runs with python2, man. Duh.
1. `UnicodeError` is the superclass of `UnicodeDecodeError`, `UnicodeEncodeError`, and the lesser-known `UnicodeTranslateError`.
1. The `exceptions` library contains all built-in exceptions. All files have an implicit `from exceptions import *`.
1. `mock.patch` [needs](http://alexmarandon.com/articles/python_mock_gotchas/) a direct reference to the function where it is called. To patch `from a import b` running in module `c`, patch `c.b`, not `a.b`.
1. Whatever you think `-0.0` is, it exists... and it is equal to `0.0`.
1. [`pwd.getpwall()`](https://docs.python.org/2.7/library/pwd.html), misleadingly, does not return a list of all passwords. They are usually `*` or `x`, due to the use of a shadow password system, explained in the link.
1. The implementation of [`keyword.iskeyword()`](https://hg.python.org/cpython/file/2.7/Lib/keyword.py#l17) is a real misfortune.
1. Python2 has [`WeakReference`](https://docs.python.org/2/library/weakref.html)s too!
1. `basestring` is just `str` in python3.
1. Python3's type hinting [enforces nothing](https://www.python.org/dev/peps/pep-0484/#the-meaning-of-annotations). For the same reason, they called it annotations. For really enforcing these rules, consider [mypy](http://mypy.readthedocs.org/en/latest/duck_type_compatibility.html).
1. `set().update(...)` can handle lists as well, not just sets.
1. Splicing indices don't have to be integers... at least not now. `[1,2,3][:None]` returns a copy of `[1,2,3]`, just as `[1,2,3][:]` would.
1. Python's `foo = set()` has an `update(bar)`, too. It just adds what's in `bar` into `foo`.
1. Comparing any integer outside [-5, 256] with `is` is [incorrect](http://stackoverflow.com/a/306353/1558430): "The current implementation keeps an array of integer objects for all integers between -5 and 256, when you create an int in that range you actually just get back a reference to the existing object."
1. Returning inside a `try` *or* an `except` block will still run the `finally` block, if one exists.

```
>>> def foo():
    try:
        print 'foo'
        raise Exception(4)
        return 5
    except:
        print 'baz'
        return 6
    finally:
        print 'bar'

>>> print foo()
foo
baz
bar
6
```

1. As far as SQLAlchemy is concerned, [there is no difference between `== true()` and `.is_(True)`](https://groups.google.com/forum/#!msg/sqlalchemy/T2bKLjzO6KA/1EwA6spA9QsJ). Howveer, pep8 and co. will complain about the former, so you should use the latter.
1. `__all__` only concerns `import *` statements. It carries no weight anywhere else.
1. `{}` is [definitely](https://www.reddit.com/r/learnpython/comments/42ymhl/returning_is_faster_than_returning_dict_even/) faster than `dict()`. This is also why you should always use literals where possible.
1. Django's [`TransactionTestCase`](https://docs.djangoproject.com/en/1.9/topics/testing/tools/#django.test.TransactionTestCase) is different from its `TestCase` in that while `TestCase` uses a transaction to roll back the database after each test, and--get this--`TransactionTestCase` does *not* use transactions. It just truncates all the tables.
1. `list` is a type.
1. You can test if a function was called with anything using [`mock.assert_called_once_with('foo', bar=ANY)`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.ANY)
1. [Welcome to unicode](https://eev.ee/blog/2015/09/12/dark-corners-of-unicode/), where `e < f < é`:

```
>>> words = ['cafeteria', 'caffeine', 'café']
>>> words.sort()
>>> words
['cafeteria', 'caffeine', 'café']
```

1. There is no `.none()` in SQLAlchemy; only [`.filter(sqlalchemy.sql.false())`](http://stackoverflow.com/questions/10345327/sqlalchemy-create-an-intentionally-empty-query). The latter still incurs one query.
1. `ModelA.query.join(ModelB)` does a JOIN on whichever `db.relationship(ModelB)` ModelA defines. Don't ask what happens if there are multiple relationships right now.
1. The `entry_points` thing in setup.py installs scripts inside your `(venv path)/bin/` directory.
1. SQLAlchemy's equivalent of `.values_list('id', flat=True)` is `.options(load_only('id'))`. I have not tested this.
1. [Putting code in the `try-else` block](http://stackoverflow.com/a/855764/1558430) is meant to *avoid* catching the same exception in the `else` block, while still running a `finally` if the `else` block fails; basically, syntactic sugar for two try blocks.
1. `sys.modules` contains an import, e.g. `datetime`, only after you import it.
1. You can `''.join([u'a', u'\u3000', 'bunch', 'of', u'unicode', 'strings'])`, but not `'{}'.format(u'a unicode \u3000 string')`, because reasons. (python2)
1. `dict()` unzips iterables of iterables. `dict( (('a', 'b'), ('c', 'd')) ) == {'a': 'b', 'c': 'd'}` (and if there are key conflicts, keys with a higher list index prevails)
1. Providing the same kwargs to a `partial()`ed function overrides the default:

```
>>> import functools
>>> def foo(**kwargs):
...     print kwargs
...
>>> foo2 = functools.partial(foo, a=2)
>>> foo2()
{'a': 2}
>>> foo2(a=4)
{'a': 4}
```

1. Regex flags can be [directly put inside the match string](http://stackoverflow.com/a/38250089/1558430): like `re.findall("/foo/s", "foo")`.
1. [PEP 318](https://www.python.org/dev/peps/pep-0318/) rejected the `def foo @decorator (bar, baz):` syntax on the basis that it no longer allows `def foo(` to be grepped. THANK YOU.
1. [`PuDB`](https://pypi.python.org/pypi/pudb) exists as a concept; it is a graphical pdb.
1. `os.tmpnam()` makes a temp path up for you, but the thing is vulnerable for some reason related to symlinks, so now you need to use `os.tmpfile()`, which opens the file for you as well.
1. `textwrap.dedent` is a standard library function.
1. When generating reports/exports of any sort, remember to [also generate a metadata file](https://www.airpair.com/python/posts) that records how the data was generated at the time, so you can check the validity of the data later on.
1. pip has the `ncu` equivalent built in: `pip list -o`
1. Values in `Enum` cannot be compared with those in `IntEnum`, even when both values are exactly integer `1`s.
1. [PEP 440](https://www.python.org/dev/peps/pep-0440/), which rings a bell because of CHEM 440, describes python's SemVer. The `rc` in `X.Y.ZrcN` is Release Candidate, not "RideCo", the vapourware company.
1. Of all the spacing requirements in python, the space between the `n` and `[` in `for i in[1,2,3,4] :` is not necessary. Nor does the redundant space between `]` and `:` matter. Your life is a lie.
1. numpy's `array` is not an instance of `list`.
1. numpy's odd way of [telling if an array contains only 1 or 0](http://stackoverflow.com/a/40596003/1558430) is `((arr == 0) | (arr == 1)).all()`, or `~((arr != 0) & (arr != 1)).any()`.
1. ["Celery"](http://stackoverflow.com/questions/13440875/pros-and-cons-to-use-celery-vs-rq) is python's way of saying "I will make a small mistake of choosing Celery now, to avoid a bigger mistake later on".
1. You can specify [requirements for each platform and python version](http://stackoverflow.com/questions/29222269/is-there-a-way-to-have-a-conditional-requirements-txt-file-for-my-python-applica/35614580#35614580) in requirements, like this: `atomac==1.1.0; sys_platform == 'darwin'`
1. Backticking a variable `x` is equivalent to `repr(x)`, but since it is only for python2, it is better if you never learned it.
1. Doing [`from builtins import dict`](http://python-future.org/compatible_idioms.html#dictionaries) (provided by the [future](http://askubuntu.com/a/728339) package) in a file automatically makes any `dict()`'s `.values()` an iterable, saving memory in python2 and 3 without `.itervalues()`. This does not apply to dict literals.
1. `**kwargs` do not need to contain variable name-only keys. You can call `foo(**{' ': None})` if you want.
1. `nosetests` (Python?) accepts a `-a foo` parameter, that only runs tests decorated with `@attr('foo')`.
1. `ast.literal_eval('123 # comments')` actually returns 123. It still throws ValueError for things like function calls, however.
1. [Simon Pirschel](https://aboutsimon.com/), creator of [udatetime](https://github.com/freach/udatetime), says that we should use udatetime because [it is faster](https://aboutsimon.com/blog/2016/08/04/datetime-vs-Arrow-vs-Pendulum-vs-Delorean-vs-udatetime.html).
1. [`.format()` can do many things.](https://pyformat.info/) Useful examples include `{:d}` (as an integer), `{:>10}` (leftpad a string), `{!r}` (repr an object), and `{foo.bar}` (getattr).
1. [`numpy.split(array, 3)` splits into 3 arrays. `numpy.array_split(array, 3)` splits into arrays of length 3.](http://stackoverflow.com/questions/9922395/python-numpy-split-array-into-unequal-subarrays)
1. [Click](https://pypi.python.org/pypi/click) is a far more intuitive version of optparse/argparse/whatever.
1. If you say (in python2 anyway) `[b for b in c]`, but `c` happens to have no elements, then `b` is never defined.
1. The `cPickle` module in PyPy is written in pure python.
1. `a_string.replace('foo', '')` can obviously still contain `foo`, if `'ffoooo'.replace('foo', '')`
1. *Thus spake the Lord: Thou shalt indent with four spaces. No more, no less. Four shall be the number of spaces thou shalt indent, and the number of thy indenting shall be four. Eight shalt thou not indent, nor either indent thou two, excepting that thou then proceed to four. Tabs are right out.* -- Georg Brandl
1. The imports you write assume you run these scripts from the [top level of the project](http://stackoverflow.com/questions/43498467/python-importerror-of-my-own-module). Imports don't magically work simply because there is an `__init__.py` in the directory.
1. [The backspace character](https://en.wikipedia.org/wiki/Backspace) (`chr(8)`) is a caret shifting mechanism. One backspace moves the caret one character to the left, and the next character replaces the character that is already in that position. For example, `print 'A' + chr(8) + 'B'` prints just `B` (because the B replaced the A), and `'A' + chr(8)` prints just `A` (because nothing replaced the A yet). `print 'A' + 'B' + chr(8) + chr(8) + 'C'` prints `CB`, because the caret is moved two characters back, and the C replaces the A.
1. The `a, *_, b = [...]` unpacking thing raises a ValueError if the list is fewer than two elements long.
1. [`type('', (), {})()` will create an object that can have arbitrary attributes.](http://stackoverflow.com/a/24448351/1558430)
1, Up until python 3.7, [it was impossible](https://docs.python.org/3.7/whatsnew/3.7.html) to have a function with more than 255 parameters, but a function name of more than 255 parameters is ok (you tested 100,000 characters).
1. A statement is a complete line of code that performs some action, while an expression is any section of the code that evaluates to a value. [Expressions can be combined “horizontally” into larger expressions using operators, while statements can only be combined “vertically” by writing one after another, or with block constructs.](https://www.quora.com/Whats-the-difference-between-a-statement-and-an-expression-in-Python)
1. [`sets.Set`](http://stackoverflow.com/a/32108276/1558430) is deprecated (removed in 3, even); `set` is not.

[bitbucket]: https://bitbucket.org/jsbueno/lelo/src/ab9837ef82001329c421afbfe7e0759c6ec0f16d/lelo/_lelo.py?at=master
[djangoproject]: https://docs.djangoproject.com/en/dev/intro/tutorial01/#creating-a-project
[djangoproject 2]: https://docs.djangoproject.com/en/1.4/ref/unicode/
[google]: https://www.google.ca/search?q=python+bidirectional+generator&oq=python+bidirectional+generator&aqs=chrome..69i57.4705j0j7&client=ubuntu-browser&sourceid=chrome&es_sm=0&ie=UTF-8
[python]: http://docs.python.org/2/library/functions.html#apply
[python 2]: https://wiki.python.org/moin/DictionaryKeys
[python 3]: http://docs.python.org/2/library/unittest.html#deprecated-aliases
[python 4]: http://docs.python.org/2/library/itertools.html#itertools.cycle
[python 5]: http://docs.python.org/2/library/stringio.html
[python 6]: https://docs.python.org/2/library/re.html#text-munging
[python 7]: https://wiki.python.org/moin/PythonDecoratorLibrary#Function_Timeout
[python-guide]: http://docs.python-guide.org/en/latest/dev/virtualenvs/#basic-usage
[stackoverflow]: http://stackoverflow.com/a/13694053
[stackoverflow 10]: http://stackoverflow.com/a/69067/1558430
[stackoverflow 11]: http://stackoverflow.com/a/2612815/1558430
[stackoverflow 12]: http://stackoverflow.com/a/6479605/1558430
[stackoverflow 13]: http://stackoverflow.com/questions/10385419/python-typeerror-expected-a-character-buffer-object-personal-misunderstanding
[stackoverflow 14]: http://stackoverflow.com/a/8062313/1558430
[stackoverflow 2]: http://stackoverflow.com/questions/19061990/python-dividing-integers-in-a-list-by-another-list-until-the-result-is-zero/19062037?noredirect=1#comment28174201_19062037
[stackoverflow 3]: http://stackoverflow.com/a/1261961/1558430
[stackoverflow 4]: http://stackoverflow.com/questions/1450957/pythons-json-module-converts-int-dictionary-keys-to-strings
[stackoverflow 5]: http://stackoverflow.com/a/481755/1558430
[stackoverflow 6]: http://stackoverflow.com/questions/1964934/what-is-contains-do-which-one-can-call-contains-function
[stackoverflow 7]: http://stackoverflow.com/a/1695250/1558430
[stackoverflow 8]: http://stackoverflow.com/a/3422740/1558430
[stackoverflow 9]: http://stackoverflow.com/questions/7996479/what-is-stringio-in-python-used-for-in-reality
[toptal]: http://www.toptal.com/python/top-10-mistakes-that-python-programmers-make
[valuedlessons]: http://www.valuedlessons.com/2008/01/monads-in-python-with-nice-syntax.html
[wikipedia]: http://en.wikipedia.org/wiki/Coroutine
[wikipedia 2]: http://en.wikipedia.org/wiki/Python_syntax_and_semantics#Dictionary_and_set_comprehensions
[youtu]: http://youtu.be/OSGv2VnC0go?t=31m39s
