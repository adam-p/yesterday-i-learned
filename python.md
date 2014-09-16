* Ordering of python lists is persistent. [src][stackoverflow]
* Pycharm hinting: 

```
        """
        Exploit the workers by hanging on to outdated imperialist dogma which
        perpetuates the economic and social differences in our society.

        @type peasant: Person
        @param peasant: Person to repress.
        """
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
* There is such thing as a [for else][stackoverflow 2] condition, where the `else` part executes only if the for loop is not `break`ed from within.
* [Django creates the project for you.][djangoproject]
* Variables can be *accessed* from an inner scope, but the outer value of the same variable will not be changed. Use [`nonlocal`][stackoverflow 3] to change the outer value.
* `*args` is of type tuple, not list.
* Use the `for-else` loop to avoid setting "flag variables", e.g. `found = False ...`. Faster than flags in Python.
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
* `[:]` [copies a list][stackoverflow 11] (Fast copy; Thanks Ford)
* `enumerate()`: returns tuples with index as the first value
* `re.sub(pattern, repl, string)` is technically `re.sub(pattern, lambda repl: repl, string)`, which allows [text munging][python 6].
* `yield`s are formally referred to as [coroutines][wikipedia] -- function with multiple entry/resume points.
* The `signal` package has an `alarm` method that can [timeout a long-running function][python 7].
* [Python3 exceptions are only accessible within the `except` block, for GC reasons][toptal]
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
* `unicode`'s `translate` is different from `str`'s `translate`; their translation tables are [not interchangeable][stackoverflow 13] (`unicode` strings require `unicode` tables)
* Every single [virtual environment][python-guide] directory (`venv`) has a `bin/activate` which you can `.`.
* Trick from the Internet: "To automatically unpack a list containing a single item, append a trailing comma to the variable name on the left of the assignment operation."
* Tastypie allows only GET by default. `authorization = Authorization()` is required in the `Meta` class to allow insecure PATCHes.
* An instance's class [can be changed][stackoverflow 14] dynamically, restricted to user-defined classes only; it's unadvisable to do so regardless.
* `if` statements do NOT have an `else` equivalent of `for...else`, i.e. if [none of the branches are completely run](http://stackoverflow.com/q/21612910/1558430), because `if` statements don't have `break`s.
* Python does not optimise tail calls.
* `def foo(a, (b, c), d)` destructures the second tuple. (Thanks @sboparen)
* Django `TestCase` has a `@skip` decorator that, if added to any `def test_` methods, will disable the test. (`from django.utils.unittest.case import skip`)
* [Certain evidence](http://programmers.stackexchange.com/a/187471) points to recommend importing just a module (`import module` instead of `from module import func1, func2`) if a lot of things are used from that module.
    * (Then again, how you can live with writing `module.func1` and `module.func2` all the time is beyond me.)
* `()` is a thing, and `(this,)` is a thing. A trailing comma is required only if the tuple contains exactly one item.
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
