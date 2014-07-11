* Ordering of python lists is persistent. [src](http://stackoverflow.com/a/13694053)
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
* There is such thing as a [for else](http://stackoverflow.com/questions/19061990/python-dividing-integers-in-a-list-by-another-list-until-the-result-is-zero/19062037?noredirect=1#comment28174201_19062037) condition, where the `else` part executes only if the for loop is not `break`ed from within.
* [Django creates the project for you.](https://docs.djangoproject.com/en/dev/intro/tutorial01/#creating-a-project)
* Variables can be *accessed* from an inner scope, but the outer value of the same variable will not be changed. Use [`nonlocal`](http://stackoverflow.com/a/1261961/1558430) to change the outer value.
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
* [Use full kwargs everywhere, except in loops](http://youtu.be/OSGv2VnC0go?t=31m39s)
* `NamedTuple` is a subclass of `Tuple` that lets you express what the tuple values actually are.
* Built-in tuple unpacking (`a, b = (1, 2)`) is faster than loading them with indices.
* Always concatenate strings with `.join`.
* Python 3.4 can ignore all but some exceptions using `with ignored(TypeError, ValueError, ...):`.
* Generator expressions, e.g. `sum(i for i in list)` is faster than `sum([i for i in list])`.
* Django or nosetests runs any `TestCase` subclass in files with their names beginning with `test` when you run `manage.py test`.
* `django.http` contains http error classes that handle the nitty gritty (e.g. allowed methods in 405)
* [You cannot make a `dict`, `json.loads`, `json.dumps`, or otherwise, with integer keys in python](http://stackoverflow.com/questions/1450957/pythons-json-module-converts-int-dictionary-keys-to-strings).
* If you are a jackass, you [can](http://stackoverflow.com/a/481755/1558430) write recursive lambdas.
* Decorators can return functions that are already wrapped with decorators, by virtue that decorators can be wrapped in anything.
* Every module is imported only once, but every `import` call will invoke a check to make sure the module is imported.
* `@functools.wraps(fn)` is used to wrap a the wrapper function inside a decorator that helps preserve the original function's docstrings.
* [`apply`](http://docs.python.org/2/library/functions.html#apply) is a keyword. It is a bit like `map`.
* "Almost every time you use `reduce` means you are doing something wrong", so `reduce()` was moved into `functools.reduce()` in Python3.
* [`__contains__`](http://stackoverflow.com/questions/1964934/what-is-contains-do-which-one-can-call-contains-function) controls the behaviour of `a in obj`.
* [Django `smart_str`](https://docs.djangoproject.com/en/1.4/ref/unicode/) along with `smart_unicode` probably solves all of Python 2's problems.
* [Python `Enum`](http://stackoverflow.com/a/1695250/1558430) Spoiler: 3.4+
* The `buffer` type is used to create [multiple "varied" reference to some parts of a large object in memory](http://stackoverflow.com/a/3422740/1558430).
* `for` creates a new scope. `for foo in foo` if `foo` is `"bar"` then it prints b, a, then r.
* Keys can be pretty much anything, and they are not stringified: `{None: 'b', 1: 5, <function __main__.<lambda>>: 4, '1': 6}`
* Taking that right back, [lists cannot be dictionary keys](https://wiki.python.org/moin/DictionaryKeys).
* "You don't mock out any part of our system, you mock out other people's code"
* [`assertEquals` is deprecated](http://docs.python.org/2/library/unittest.html#deprecated-aliases)
* If `assertEqual` receives two `dict`s, it automatically calls `assertDictEqual`.
* [`itertools.cycle`](http://docs.python.org/2/library/itertools.html#itertools.cycle): for when you want to loop over something, over and over
* Django's `QueryDict` can be converted to a dict by calling `.dict()`.
* [`StringIO.StringIO`](http://docs.python.org/2/library/stringio.html) is **not** used for performance reasons. It is used to [convert a string into a memory-bound file](http://stackoverflow.com/questions/7996479/what-is-stringio-in-python-used-for-in-reality) so functions that expect a file can work without writing the string to a file first.
* There is a `3to2`!
* You can [decorate functions with classes](https://bitbucket.org/jsbueno/lelo/src/ab9837ef82001329c421afbfe7e0759c6ec0f16d/lelo/_lelo.py?at=master) that have `__call__`!
* Instance variables (`class.foo == 'far'`) are class variables (`class.foo == Class.foo`) as long as [the instance doesn't change its instance variable's value](http://stackoverflow.com/a/69067/1558430).
* `[:]` [copies a list](http://stackoverflow.com/a/2612815/1558430) (Fast copy; Thanks Ford)
* `enumerate()`: returns tuples with index as the first value
* `re.sub(pattern, repl, string)` is technically `re.sub(pattern, lambda repl: repl, string)`, which allows [text munging](https://docs.python.org/2/library/re.html#text-munging).
* `yield`s are formally referred to as [coroutines](http://en.wikipedia.org/wiki/Coroutine) -- function with multiple entry/resume points.
* The `signal` package has an `alarm` method that can [timeout a long-running function](https://wiki.python.org/moin/PythonDecoratorLibrary#Function_Timeout).
* [Python3 exceptions are only accessible within the `except` block, for GC reasons](http://www.toptal.com/python/top-10-mistakes-that-python-programmers-make)
* Set generators are [already available in python2.7](http://en.wikipedia.org/wiki/Python_syntax_and_semantics#Dictionary_and_set_comprehensions).
* The `set`'s `discard` method makes stupid things like `new_set = {x for x in old_set if x != 'foo'}` a little bit redundant.
* Lambda expressions can have parameter defaults, positional and keyword arguments!
* Django Foreign keys default to `None`.
* `__future__` imports can only be done at the top of a file.
* Override `parse_start_url` to diagnose Scrapy errors that occur on start urls.
* [You can and should use monads in your code in almost any programming language](http://www.valuedlessons.com/2008/01/monads-in-python-with-nice-syntax.html)
* `a >> b` can be overridden using the magic method `__rshift__`.
* I don't know what the author was talking about, but python has something called the [bidirectional generator](https://www.google.ca/search?q=python+bidirectional+generator&oq=python+bidirectional+generator&aqs=chrome..69i57.4705j0j7&client=ubuntu-browser&sourceid=chrome&es_sm=0&ie=UTF-8) which no one explained.
* Override `parse_start_url` to diagnose Scrapy errors that occur on start urls.
* In Django, `admin.site.register(Model)` doesn't need an admin (e.g. `admin.site.register(Model, ModelAdmin)`) if all you want is an automatic form.
* `\d` [isn't](http://stackoverflow.com/a/6479605/1558430) `0-9` -- it also contains digits from other locales.
* Contrary to popular opinion, `requirements.txt` simply came from `pip freeze > requirements.txt`.
* `pip freeze` also removes duplicate package requirements, so it helps you clean up the file in a way.