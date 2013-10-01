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
* 
