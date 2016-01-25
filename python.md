* Ordering of python lists is persistent. [src][stackoverflow]
* Pycharm hinting: 

```
        """
        Exploit the workers by hanging on to outdated imperialist dogma which
        perpetuates the economic and social differences in our society.

        @type peasant: Person
        @param peasant: Person to oppress.
                        http://grammarist.com/usage/oppress-repress-suppress/
        """
```

* [PEP 3107](http://legacy.python.org/dev/peps/pep-3107/) hinting:

```
def foo(a: 'what is a', b: 5 + 6, c: list) -> max(2, 9):
    # foo accepts a (commented), b (11), c (any kind of list), and returns 9
```

* Under normal circumstances, `register.simple_tag` is all you need for your django templating needs.
* To pretty-format a JSON file, do `cat ugly.json | python -mjson.tool > pretty.json`.
* `re.VERBOSE`, aka `re.X`, will ignore all whitespaces in a regex. Will Also ignore everything after a `#`.
* Python does not raise a rounding exception when a large number is used. The typical check is `n + 1 == n`.
* To speed up a read-only query, try adding `.values_list(fields...)` to a QuerySet, which returns simple tuples.
* It is absolutely possible that django `loaddata` is a douchebag. 
  Therefore, to import all objects without referential errors, use `python manage.py loaddata init_dev.json`, 
  which provides all references before inserting.
* Multiple args: calling a `function(a, b, **kwargs)` where kwargs contains `a=4` or `b=[]` will raise an Exception.
* `dict(a=4,b=5)` === `{'a': 4, 'b': 5}`
* There is such thing as a [for else][stackoverflow 2] condition, where the `else` part doesn't execute only if the for loop is `break`ed from within.
* `for` also runs `else` if the loop is never run (e.g. has 0 items).
* There is also a [while-else loop](http://www.tutorialspoint.com/python/python_while_loop.htm) that runs when the variable changes to `False`.
* [Django creates the project for you.][djangoproject]
* Variables can be *accessed* from an inner scope, but the outer value of the same variable will not be changed. Use [`nonlocal`][stackoverflow 3] to change the outer value.
* `*args` is of type tuple, not list.
* Use the `for-else` loop to avoid setting "flag variables", e.g. `found = False ...`. Faster than flags in Python.
* `dict(a dict)` clones the dict (for one level).
* `list(a list)` clones the list (for one level).
* These three are successively better than the former.

```
for k in d:
    print k, d[k]

for k, v in d.items():
    print k, v

for k, v in d.iteritems():
    print k, v
```

* `dict`s have a `setdefault` method: avoids `KeyError`s.
* Instead of updating dictionaries with another dictionary, there is a `ChainMap` in Python 3 that handles the common "defaults" use case.
* [Use full kwargs everywhere, except in loops][youtu]
* `NamedTuple` is a subclass of `Tuple` that lets you express what the tuple values actually are.
* Built-in tuple unpacking (`a, b = (1, 2)`) is faster than loading them with indices.
* Always concatenate strings with `.join`.
* Python 3.4 can ignore all but some exceptions using `with ignored(TypeError, ValueError, ...):`.
* Generator expressions, e.g. `sum(i for i in list)` is faster than `sum([i for i in list])`.
* Django or nosetests runs any `TestCase` subclass in files with their names beginning with `test` when you run `manage.py test`.
* `django.http` contains http error classes that handle the nitty gritty (e.g. allowed methods in 405)
* [You cannot make a `dict`, `json.loads`, `json.dumps`, or otherwise, with integer keys in python][stackoverflow 4].
* If you are a jackass, you [can][stackoverflow 5] write recursive lambdas.
* Decorators can return functions that are already wrapped with decorators, by virtue that decorators can be wrapped in anything.
* Every module is imported only once, but every `import` call will invoke a check to make sure the module is imported.
* `@functools.wraps(fn)` is used to wrap a the wrapper function inside a decorator that helps preserve the original function's docstrings.
* [`apply`][python] is a keyword. It is a bit like `map`.
* "Almost every time you use `reduce` means you are doing something wrong", so `reduce()` was moved into `functools.reduce()` in Python3.
* [`__contains__`][stackoverflow 6] controls the behaviour of `a in obj`.
* [Django `smart_str`][djangoproject 2] along with `smart_unicode` probably solves all of Python 2's problems.
* [Python `Enum`][stackoverflow 7] Spoiler: 3.4+
* The `buffer` type is used to create [multiple "varied" reference to some parts of a large object in memory][stackoverflow 8].
* `for` creates a new scope. `for foo in foo` if `foo` is `"bar"` then it prints b, a, then r.
* Keys can be pretty much anything, and they are not stringified: `{None: 'b', 1: 5, <function __main__.<lambda>>: 4, '1': 6}`
* Taking that right back, [lists cannot be dictionary keys][python 2].
* "You don't mock out any part of our system, you mock out other people's code"
* [`assertEquals` is deprecated][python 3]
* If `assertEqual` receives two `dict`s, it automatically calls `assertDictEqual`.
* [`itertools.cycle`][python 4]: for when you want to loop over something, over and over
* Django's `QueryDict` can be converted to a dict by calling `.dict()`.
* [`StringIO.StringIO`][python 5] is **not** used for performance reasons. It is used to [convert a string into a memory-bound file][stackoverflow 9] so functions that expect a file can work without writing the string to a file first.
* There is a `3to2`!
* You can [decorate functions with classes][bitbucket] that have `__call__`!
* Instance variables (`class.foo == 'far'`) are class variables (`class.foo == Class.foo`) as long as [the instance doesn't change its instance variable's value][stackoverflow 10].
* `[:]` (aka `[None:None]`) [copies a list][stackoverflow 11] (Fast copy; Thanks Ford)
* `enumerate()`: returns tuples with index as the first value
* `re.sub(pattern, repl, string)` is technically `re.sub(pattern, lambda repl: repl, string)`, which allows [text munging][python 6].
* `yield`s are formally referred to as [coroutines][wikipedia] -- function with multiple entry/resume points.
* The `signal` package has an `alarm` method that can [timeout a long-running function][python 7].
* [Python3 exceptions are only accessible within the `except` block, for GC reasons][toptal]. Interestingly, even if the same name existed outside the `except` block, [Python3 will remove the variable of the same name from the outer scope](http://www.wefearchange.org/2013/04/python-3-language-gotcha-and-short.html).
* Set generators are [already available in python2.7][wikipedia 2].
* The `set`'s `discard` method makes stupid things like `new_set = {x for x in old_set if x != 'foo'}` a little bit redundant.
* Lambda expressions can have parameter defaults, positional and keyword arguments!
* Django Foreign keys default to `None`.
* `__future__` imports can only be done at the top of a file.
* Override `parse_start_url` to diagnose Scrapy errors that occur on start urls.
* [You can and should use monads in your code in almost any programming language][valuedlessons]
* `a >> b` can be overridden using the magic method `__rshift__`.
* I don't know what the author was talking about, but python has something called the [bidirectional generator][google] which no one explained.
* Override `parse_start_url` to diagnose Scrapy errors that occur on start urls.
* In Django, `admin.site.register(Model)` doesn't need an admin (e.g. `admin.site.register(Model, ModelAdmin)`) if all you want is an automatic form.
* `\d` [isn't][stackoverflow 12] `0-9` -- it also contains digits from other locales.
* Contrary to popular opinion, `requirements.txt` simply came from `pip freeze > requirements.txt`.
* `pip freeze` also removes duplicate package requirements, so it helps you clean up the file in a way.
* Generate random test urls using `itertools.product`: http://stackoverflow.com/questions/2535924/simple-way-to-create-possible-case/2535934#2535934
* It is not necessary to `urlunparse` a url before generating a new url with parts changed. `urlparse(url, scheme='http')` changes the schema of that url to http.
    * I lied. It only works for `scheme`. 
* `unicode`'s `translate` is different from `str`'s `translate`; their translation tables are [not interchangeable][stackoverflow 13] (`unicode` strings require `unicode` tables)
* Every single [virtual environment][python-guide] directory (`venv`) has a `bin/activate` which you can `.`.
* And, get this, your repository does not need to be cloned into the virtual environment directory.
* Trick from the Internet: "To automatically unpack a list containing a single item, append a trailing comma to the variable name on the left of the assignment operation."
* Tastypie allows only GET by default. `authorization = Authorization()` is required in the `Meta` class to allow insecure PATCHes.
* An instance's class [can be changed][stackoverflow 14] dynamically, restricted to user-defined classes only; it's unadvisable to do so regardless.
* `if` statements do NOT have an `else` equivalent of `for...else`, i.e. if [none of the branches are completely run](http://stackoverflow.com/q/21612910/1558430), because `if` statements don't have `break`s.
* `if` statements do NOT have any kind of `for...else`-type block that is run whenever any one or more conditions above are run.
* Python does not optimise tail calls.
* `def foo(a, (b, c), d)` destructures the second tuple. (Thanks @sboparen)
* Django `TestCase` has a `@skip` decorator that, if added to any `def test_` methods, will disable the test. (`from django.utils.unittest.case import skip`)
* [Certain evidence](http://programmers.stackexchange.com/a/187471) points to recommend importing just a module (`import module` instead of `from module import func1, func2`) if a lot of things are used from that module.
    * (Then again, how you can live with writing `module.func1` and `module.func2` all the time is beyond me.)
* `()` is a thing, and `(this,)` is a thing. A trailing comma is required only if the tuple contains exactly one item.
* `setattr(a_django_object, ...)` will silently update the object's `__dict__`. Doing the same `setattr` to an object will cause an `AttributeError` if the attribute was not defined in the class.
* `python -m webbrowser <url>` opens... that url in your browser.
* Python 3.0 ~ 3.2 don't have the `u'unicode string literal'` syntax, which would crash any python2 script that are otherwise the same as its python3 counterpart.
* Apparently [you can get `easy_install` from `python-setuptools`](http://www.mediawiki.org/wiki/Gerrit/git-review).
* Apparently [you can get `pip` from `easy_install`](http://www.mediawiki.org/wiki/Gerrit/git-review), too.
* Python 2.7+ is the only python2 version that comes with the set notation (`{1, 2, 3}`).
* [PyLint expects all global variables to be constants, and be named in ALL_UPPERCASE](http://docs.pylint.org/tutorial.html)
* Want a monad for absolutely no work? Get [PyMonad](https://pypi.python.org/pypi/PyMonad/)!
* [Marisa-trie](https://github.com/kmike/marisa-trie) consumes less memory than if you decide to build your own trie in python.
* `bytes(...)`: turn strings into sequences of anything from 0 to 255.
* [`simplejson` is subjectively better than `json`](http://stackoverflow.com/questions/712791/what-are-the-differences-between-json-and-simplejson-python-modules) -- to use either, `import simplejson as json`.
* It is [an insanely stupid idea](http://stackoverflow.com/questions/6031584/python-importing-from-builtin-library-when-module-with-same-name-exists) to have a folder that has the same name as one of the built-in libraries.
* It wasn't possible to `import (many things with brackets)` [until python 2.7](http://legacy.python.org/dev/peps/pep-0328/).
* `range()` can actually be faster in some cases - eg. if iterating over the same sequence multiple times.  `xrange()` has to reconstruct the integer object every time, but `range()` will have real integer objects. (It will always perform worse in terms of memory however, and there is no such thing as Python2's `range()` in Python3.)
* If you aren't being code reviewed or anything, you can subclass `namedtuple` like this:

```
class Foo(namedtuple('lol', 'a b c')): pass
```

* `namedtuple` accepts pretty much anything for its second argument. These all work.

```
namedtuple('a', ['b', 'c'])
namedtuple('a', 'b, c')
namedtuple('a', 'b c')
namedtuple('a', """
b
c
""")
```

* If a function is decorated with `contextlib.contextmanager`, then [it can be used as a `with` statement](https://docs.python.org/2/library/contextlib.html). The function must contain exactly one `yield`, where things that happen before the `yield` works like `__enter__`, and what happens after the `yield` is treated like `__exit__`.
* [`contextlib.suppress(BaseException)`](https://docs.python.org/3/library/contextlib.html#contextlib.suppress) is basically the `never_fail` decorator. And oops, it is only for Python 3.
* `random.seed()` is better than `random.seed(0)`, because [the parameter default is the system time](https://docs.python.org/2/library/random.html#random.seed).
* `hash(-2)` is the same as `hash(-1)`.
* Objects that have an overridden __eq__ cannot be hashed, unless their __hash__ are also defined.
* Python2 does [float multiplications](https://github.com/python/cpython/blob/10d5f4d9b6279945ba8062fd04c0314e5ead0a53/Objects/intobject.c#L533) internally to compute results of integer multiplications, presumably to find out of two numbers multiplying each other will cause an overflow.
* It is possible to [`__import__('python-module-with-dashes-in-the-filename'`](http://stackoverflow.com/questions/761519/is-it-ok-to-use-dashes-in-python-files-when-trying-to-import-them), but if you create a file such as this, you deserve to be shot.
* `os.getenv('HOME')` works, only because `$HOME` is populated by the shell.
* [You can compare tuples](http://stackoverflow.com/a/5292332/1558430)! `(1,2)` is less than `(3, 4)`.
* You can assign to spliced arrays: `arr[:4] = [9,9]` replaces the first 4 items of the array with `[9,9]`.
* `round()` doesn't work on `Decimal`s. To round a `Decimal` to certain digits, do: `Decimal(123.456789).quantize(Decimal("0.001"))  # 3 decimal points`
* `Decimal.quantize` is called that because it also makes up more decimal points if you ask it to: `Decimal(1234.56789).quantize(Decimal("0.000000000000000001"))  # Decimal('1234.567890000000033979')`
* You *can* `def foo(bar=NamedTupleAsDefaultValue())`, but would you...?
* `arrow.replace()` accepts singluar nouns like `hour` that replaces the component, or plural forms like `hours` that shifts the value relatively, instead.
* [Guido](https://mail.python.org/pipermail/python-dev/2010-April/099459.html) doesn't like `merged_dict = dict(some_dict, **another_dict)`, and nor do you. (it only handles string keys)
* In Python3, arguments can be [forced named](http://stackoverflow.com/a/14298976/1558430): with `def foo(a, * must_use_kwargs_for_this_arg)`.
* One-liner `if` clauses are executed before the assignment, so `b = a.foo if a else 2` will not raise `AttributeError` even if `a = None`.
* ["Never (create, change, or delete models) directly"](http://www.dabapps.com/blog/django-models-and-encapsulation/) - Tom Christie
* `bool` is a subclass of `int`, and cannot be subclassed further.
* "Either or" is `bool(a) != bool(b)`, or just `operator.xor`. This is different from `nand`, which is false when both are false, and not `nor`, which is true when both are true.
* As much as tuples are immutable, its contents are:

```
>>> a = ([], [])
>>> a[0].append(1)
>>> a
([1], [])
```

* `logging.debug("{}".format(123))` builds strings unnecessarily when logging level is set to above debug. To combat this, use `logging.debug(u"%s", 123)` instead, where the arguments must be positional. For internal reference, the Gerrit ID is 626.
* Strings can also be formatted traditionally with a keywords: `'Today is %(month)s %(day)s.') % {'month': m, 'day': d}`
* [`python -W all`](http://stackoverflow.com/a/18996013/1558430) prints all `PendingDeprecationWarning`s, and is the preferred way to run python locally.
* [`j` is the only notation for complex numbers.](http://stackoverflow.com/a/8370696/1558430)

```python
>>> abs(1+12i)
  File "<stdin>", line 1
    abs(1+12i)
            ^
SyntaxError: invalid syntax
>>> abs(1+12j)
12.041594578792296
```

* The `abs()` of a complex number is the dot product of its real-imaginary plane. If this is not intended, use `math.fabs()` instead, which raises on imaginary numbers.
* Unit test `self.assert*`s take a last parameter that is the failure message: `self.assertIn(0, [1,2,3], "0 not found in list")`
* `(str).casefold()` is meant to normalise all variants of the same string, such as `['False', 'false', 'FALSE']` into something you can put into a switch-case block. Then again, there isn't switch-case in Python, only dict keys.
* The [try-finally block](https://wiki.python.org/moin/HandlingExceptions) has no `except`, so it runs the finally block (which typically rolls back something), then raises the exception.
* Although there are no docstring type-hinting standards, [this one by PyCharm](https://www.jetbrains.com/pycharm/help/type-hinting-in-pycharm.html) will do: `:param parameter_name: x.y.ParameterClass | None`
* [`sum()` takes a second parameter](https://docs.python.org/2/library/functions.html#sum), `start`. It really means `sum() + start`.
* `history` is always a variable in ipython.
* Booleans are inherited from `int`, so you can add them together.
* "Tim Peters also snuck some subtle jokes into the Zen itself (notice the dashes on the TOOWTDI line do it two different ways?"
* Multiple assignments (e.g. `a = b = []`) assigns the same reference to each variable, even if the value is primitive (e.g. `5`).
* [When called with three arguments, type acts like a constructor, so you can create new types in an inline fashion.](http://ivansmirnov.io/python-metaclasses/)
* There's [a whole package](https://pypi.python.org/pypi/lockfile) for the `process.pid` thing.
* Sending gzip requests through the `requests` library is [completely manual](http://stackoverflow.com/questions/28656068/compressing-request-body-with-python-requests). You really have to construct a gzip stream and modify the headers.
* As an asider, [`Transfer-Encoding: gzip` is a better header than `Content-Encoding: gzip`](http://stackapps.com/questions/916/why-content-encoding-gzip-rather-than-transfer-encoding-gzip) because the latter does not imply the final content type of `.gz`.
* In Python 3, unbound methods don't exist. There is `unbound_method()` in six that achieves a similar goal.
* [django-rest-swagger](https://github.com/marcgibbons/django-rest-swagger/) documents the API. 
* `max(None, 0)` is 0. `max(0, None)` is also 0. `min(None, 0)` is `None`. Therefore, `None < 0`. In fact, `None < float('-inf')`.
* `UnicodeEncodeError` and `UnicodeDecodeError` in a nutshell:

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

* [**There's no formal guarantee about the stability of sets (or dicts, for that matter.)**](http://stackoverflow.com/a/3812600) However, in the CPython implementation, as long as nothing changes the set, the items will be produced in the same order.
* [Assigning attributes to a function doesn't raise `AttributeError`s](https://mail.python.org/pipermail/python-dev/2000-April/003364.html). PEP 232 [tries to justify it](https://www.python.org/dev/peps/pep-0232/)--the gist being, "it doesn't hurt."
* `isinstance()` accepts a tuple worth of types.
* Installing `python-examples` apparently [gives access to `reindent.py`](http://stackoverflow.com/a/1024489/1558430), which obviously reindents python scripts.
* Splicing a `range` (which is `xrange`) in python3 gives you another `range`. The equivalent `xrange` cannot be spliced in python2.
* By overriding the behaviour of `__lt__`, `__gt__`, `__eq__`, etc., things that often do comparisons (and therefore return bools) now return SQL "Expression" objects, like so:

```
>>> str(db.Column('a') > db.Column('b'))
'a > b'  # look ma, not a bool
```

* [An `Enum`'s class attributes have itself as its own class](https://docs.python.org/3/library/enum.html). `isinstance(Color.green, Color) is True`.
* But with every `Enum` having every attribute in its own class, they don't have access to other attributes: `Color.red.blue  # AttributeError`
* Depending on version, [Python2 and 3 raise different errors](http://stackoverflow.com/a/23703899/1558430) when an `object()` is asked if it is equal to another `object()`.
* Exploiting the tuple syntax can make multidimentional "arrays" very easy to work with:

```
>>> a = {(1,2): 4}  # This can be a subclass of `dict` with list indexing
>>> a[1,2]
4
```

* If you use `python2` to run a script with a `#!/... python3` shebang in it, it runs with python2, man. Duh.
* `UnicodeError` is the superclass of `UnicodeDecodeError`, `UnicodeEncodeError`, and the lesser-known `UnicodeTranslateError`.
* The `exceptions` library contains all built-in exceptions. All files have an implicit `from exceptions import *`.
* `mock.patch` [needs](http://alexmarandon.com/articles/python_mock_gotchas/) a direct reference to the function where it is called. To patch `from a import b` running in module `c`, patch `c.b`, not `a.b`.
* Whatever you think `-0.0` is, it exists... and it is equal to `0.0`.
* [`pwd.getpwall()`](https://docs.python.org/2.7/library/pwd.html), misleadingly, does not return a list of all passwords. They are usually `*` or `x`, due to the use of a shadow password system, explained in the link.
* The implementation of [`keyword.iskeyword()`](https://hg.python.org/cpython/file/2.7/Lib/keyword.py#l17) is a real misfortune.
* Python2 has [`WeakReference`](https://docs.python.org/2/library/weakref.html)s too!
* `basestring` is just `str` in python3.
* Python3's type hinting [enforces nothing](https://www.python.org/dev/peps/pep-0484/#the-meaning-of-annotations). For the same reason, they called it annotations. For really enforcing these rules, consider [mypy](http://mypy.readthedocs.org/en/latest/duck_type_compatibility.html).
* `set().update(...)` can handle lists as well, not just sets.
* Splicing indices don't have to be integers... at least not now. `[1,2,3][:None]` returns a copy of `[1,2,3]`, just as `[1,2,3][:]` would.
* Python's `foo = set()` has an `update(bar)`, too. It just adds what's in `bar` into `foo`.
* Comparing any integer outside [-5, 256] with `is` is [incorrect](http://stackoverflow.com/a/306353/1558430): "The current implementation keeps an array of integer objects for all integers between -5 and 256, when you create an int in that range you actually just get back a reference to the existing object."
* Returning inside a `try` *or* an `except` block will still run the `finally` block, if one exists.

```
def foo():
    try:
        raise Exception(4)
        return 5
    except:
        return 6
    finally:
        print 'bar'

print foo()
# bar
# 6
```

* As far as SQLAlchemy is concerned, [there is no difference between `== true()` and `.is_(True)`](https://groups.google.com/forum/#!msg/sqlalchemy/T2bKLjzO6KA/1EwA6spA9QsJ). Howveer, pep8 and co. will complain about the former, so you should use the latter.
* 

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
