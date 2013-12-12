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
