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

