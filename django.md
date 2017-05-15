# Django tips

* `Model(id)` is NOT the same as `Model.objects.get(id=id)`. You can save the object from `Model.objects.get(id=id)`, but not `Model(id)`: `ValidationError: {u'id': [u'Model with this ID already exists.']}`
* Every `<Model>.objects` is just a [subclass of] `models.Manager()`. And you can extend `models.Manager`.*wink wink*
* [`./manage.py runscript`](http://django-extensions.readthedocs.org/en/latest/runscript.html) is exactly what ought to be done in place of where you used to code your management commands.
* A [naive datetime object](https://docs.python.org/2/library/datetime.html) does not care about its time zone. An "aware" datetime object, however, does.
* [Django never stores timezones in the database.](https://docs.djangoproject.com/en/1.8/topics/i18n/timezones/) The `USE_TZ` setting is only good for converting these UTC times to the site user's local time.
* Giving any `TestCase` a `fixtures` list attribute automatically loads these fixtures whenever the tests are run.
* The `QuerySet` is a monad. You can call `prefetch_related` and `select_related` in either order and it won't care. (It does care about double splicing and double ordering, however.)
* To override a template that is defined in a package, configure your `TEMPLATE_DIRS` variable to let your own `templates` directory have a higher lookup priority.
* Adding `{{ block.super }}` inside a block retains whatever was in the block in the parent template.
* To filter by any django model field, use the [`DjangoFilterBackend`](http://stackoverflow.com/a/2137652)
* the `{% django_js %}` tag cannot be compressed!
* [`authenticate()`](https://docs.djangoproject.com/en/1.6/topics/auth/default/#django.contrib.auth.authenticate) checks the credentials; `login()` actually logs the user in.
* All unsaved models (`pk=None`) of the same type hash to the same thing, both because it is technically correct, and becuase Django devs are morons. Do not store them with `set` -- they will just go away.
* When you change a DB field to a computed field (`@property`), you can specify `db_field` to keep it pointing to the original column name: http://stackoverflow.com/a/12358707/1558430
* [`count()` is faster](http://stackoverflow.com/questions/14327036/count-vs-len-on-a-django-queryset) if all you need is a length; `len()` is faster if you already have the whole queryset lazy-evaluated (for instance, when you actually use the whole set in a loop)
* Model fields can default to a callable (function), but the function takes in nothing, so it is really only good for dates and times.
* [Generic model serializer](http://ihackernews.com/comments/8971480)
* [assignment tags](https://docs.djangoproject.com/en/1.7/howto/custom-template-tags/#assignment-tags): `{% some_assignment_tag param1 param2 param3... as variable_you_can_use_below %}`
* Template rendering is apparently [multi-threaded](https://docs.djangoproject.com/en/1.7/howto/custom-template-tags/#thread-safety-considerations). 
* The act of initialising a `QueryDict` [already parses the query string](https://docs.djangoproject.com/en/1.7/ref/request-response/#django.http.QueryDict.__init__). There is no need to use urlparse.
* [Django does not force you to put code at some specific place](http://stackoverflow.com/a/8590943/1558430). With that said, since MVC requires a service abstraction layer between M and C, which hardly anyone ever has, Django tends to recommend logic in either V or [M](http://stackoverflow.com/a/8591009/1558430), depending on whether the logic concerns requests.
* The result of calling `build_absolute_uri()` on a fake Request gives you `http://testserver/(...)`.
* The Django admin lists fields in the order the fields themselves are declared in your models file. For example, `class Foo: bar = ..., baz = ...` actually shows `bar` before `baz` in the admin.
* Django 1.8 apparently lets you aggregate by an expression now, e.g. `.aggregate(Min('price') + 1)`
* [`QuerySet.iterator()`](https://docs.djangoproject.com/en/1.8/ref/models/querysets/#django.db.models.query.QuerySet.iterator) does exactly that: make a queryset that you cannot reuse, probably for the greater good.
* Instead of making another Query just to fetch the same object again, there already is an [`obj.refresh_from_db()`](https://docs.djangoproject.com/en/1.9/ref/models/instances/#django.db.models.Model.refresh_from_db) available.
* [Signals are synchronous and blocking](http://www.slideshare.net/flywindy/two-scoops-ofdjangologgingandsignals).
* If you are smart enough to use `.save(update_fields=['foo'])`, [be smart enough to know](https://code.djangoproject.com/ticket/22981) that `auto_now[_add]` fields will be updated only if they are specified in `update_fields`.
* To [aggregate by a field whose `related_name` is `+`](http://stackoverflow.com/questions/38576912/django-aggregate-by-field-with-no-related-name), try something clever: `Reward.objects.values('user').annotate(rewards_count=Count('id')).order_by()`, or [override a model's definition using a mirror class](http://stackoverflow.com/a/38583862/1558430) whose `Meta.managed` is `False`.
* It is [completely possible](https://github.com/django/django/blob/428c0bbe1bcd303560d7e96d7d2721ff3fdc0e3f/django/db/models/expressions.py#L155) to filter by an `F('time_field') + timedelta(seconds=???)`.
* Translated string substitutionss (e.g. `_('hello %(world)s')`) must be named because you don't necessarily want all langauges to have those translations in the same order.
* Annotating a query with an [`ExpressionWrapper` field](http://stackoverflow.com/a/40618185/1558430) allows queries to be built using a result of some multi-field computation, which you normally cannot.
* Django 1.9 now has a [`Now()`](https://docs.djangoproject.com/en/1.10/ref/models/database-functions/#now) you can use to `filter(field__lt=Now())`. If the two servers have the same timestamp at the same time, using this and whatever from `datetime` have no functional difference.
* [`list_filter` can contain `admin.(...)Filter`s](https://docs.djangoproject.com/en/1.10/ref/contrib/admin/), not just field names.
* [`prop.boolean = True`](http://stackoverflow.com/questions/12842095/how-to-display-a-boolean-property-in-the-django-admin) in django admin turns the display of that method into a checkbox, rather than just saying 'True'.
* Expressions in `{% blocktrans %}{{ this thing }}{% endblocktrans %}` [must not have attribute/key access](http://stackoverflow.com/questions/11338098/why-in-i18n-blocktrans-django-a-object-dict-or-list-dont-work).
* If you filter by `id__in=queryset`, Django might make it a subquery. But if you do `id__in=list(queryset)`, no matter the size of the queryset, the queryset must be evaluated first, and the two-query version might be faster than the subquery version.
* Django 1.7 got rid of the `--dry-run` option formerly available in South.

## WSGI

To run Django under something other than `runserver`, `uWSGI` is preferred. To get the library, run:

```
pip install uwsgi  # requires reboot
```

# Django troubleshooting

## urlconf

### `urlconf_module, app_name, namespace = arg ... ValueError: need more than 1 value to unpack`

Only Django 1.7 and up accepts plain lists for `include()`. Lower versions of django must wrap their urls in a `patterns('', ...)` first.

## South is being a douche

### `relation_blah_blah_blah already exists`

The table exists, and is not managed by celery. **Delete all tables** to continue.

```
python manage.py flush --no-initial-data --noinput
# do whatever initial schema migrations

# then, "upload the zip", if you know what I'm saying.
# Alternatively,
python manage.py syncdb && python manage.py migrate
```

**Alternatively**, if an app table already exists, try this first:

```
python manage.py syncdb --all
python manage.py migrate --fake
```

### `relation_blah_blah_blah already exists` *after* migrate

[Source][github]

If the migration fails with the following error message:

```
django.db.utils.DatabaseError: relation "celery_taskmeta" already exists
```

Check if:

```
$ bin/django.py migrate --list
```

shows that no migrations for djcelery has an (X) in front of it. If that is the case, run:

```
$ ./manage.py migrate djcelery 0001 --fake
$ ./manage.py migrate djcelery 0002 --fake
$ ./manage.py migrate djcelery 0003 --fake
$ ./manage.py migrate djcelery 0004 --fake
```

Then re-run: `./manage.py migrate`

### Migrating a migration that was previously faked

`MigrationHistory.objects.get(app_name="your_app_name", migration="0001_whatever_filename").delete()`

### Failed to migrate models in two apps in the same project that impose foreign key constraints

Try to mark (after the fact, unfortunately) the schema migration that has a schema migration dependency with the [`depends_on` keyword][readthedocs].

### Doing a data migration that needs access to the model class

It is possible that your model has changed (e.g. somebody added new field).
Instead of `from app.models import Foo`, you might need to use [`Foo = apps.get_model('app', 'Foo')`](https://realpython.com/blog/python/data-migrations/) to get the *historical* model, which might avoid any issues that may arise.

## Base models storing common fields

Add a `class Meta` that contains `abstract = True`. 
<!-- This has a downside of no longer allowing the class to be referenced (as foreign keys) directly. -->

## Can't have `__getattr__` in django models

Yeah. Suck it up.

### `RelatedObjectDoesNotExist` when you try to access an attribute by `related_name`

Well, here's somehow where Django decides to conform to `hasattr()`.

```
>>> foo.ratings
RelatedObjectDoesNotExist: Foo has no ratings.
>>> getattr(foo, 'ratings')
RelatedObjectDoesNotExist: Foo has no ratings.
>>> hasattr(foo, 'ratings')
False  # foo has no ratings
```

## Don't know what select_related and prefetch_related do
According to onymous internet sources,

`select_related`
- foreign key & one-to-one relationship

`prefetch_related`
- many-to-many and many-to-one relationship
- generic foreign key & relationship

## lxml parser won't run / lxml won't compile

Run `sudo apt-get install libxml2-dev libxslt-dev python-dev lib32z1-dev`, *then* run `pip install lxml`

## QuerySet

### Queries do crazy things when executed in parallel

Use `@transaction.atomic`.

#### Django dies when using `@transaction.atomic`

> **Avoid catching exceptions inside atomic!** This is mostly a concern for `DatabaseError` and its subclasses such as `IntegrityError`. The correct way [is to catch the exception outside the atomic block].

### Queries do crazy things even when executed in atomic blocks

Use `QuerySet.select_for_update(nowait=bool).filter(...)` in conjunction with `@transaction.atomic`.

All tables read by that `filter()` will be locked and be exclusive to this queryset until the atomic block is done.

### `__in` queries don't preserve order

Use [`in_bulk`](https://docs.djangoproject.com/en/1.8/ref/models/querysets/#in-bulk) instead, which is also unordered, but at least returns a `dict` so you can re-order it to your liking back to a `list`.

## Misc

### Filtering by how many other foreign keys an object has

Annotate with the count of the foreign key, then filter on the annotation.

```
from django.db.models import Count, Q
Content.objects.annotate(tp=Count('tagged_products')).filter(tp__gte=3)
```

### got only `30` from a URL like `?foo=10&foo=20&foo=30`

Conventional wisdom tells us `request.GET.get('foo')` would get us whatever `foo` is, which is, by default, the last `foo`.

To get all the values instead, use `request.GET.getlist('foo')`, which is `['10', '20', '30']`.

### Cleaning up your mess after an outer join

```
qs.distinct()
```

### Prefetching with `get_object_or_404`

This is apparently possible:

```
get_object_or_404(Thing.prefetch_related(), id=4)
```

, bearing in mind that calling `prefetch_related` multiple times on the same queryset makes those prefetch calls multiple times.

### Django signals (e.g. `post_save`, `m2m_changed`, ...) not working

The file you have these hooks must be touched by python at least once... try importing these hooks from a file that you know django uses. (The imports don't need to be used)

### [`blank=True` or `null=True`](http://stackoverflow.com/a/8609425)?

Usually, both. `blank=True` makes Django allow None, while `null=True` makes the database tolerate `NULL`.

`null=True` is not required for `TEXT` or `CHAR` fields.

### `{{ form.as_table }}` Doesn't return table markup?

Sometimes (but not according to the docs), unless you wrap all that in `<table>` tags, the form will render as line-broken strings:

```
<table>
{{ form.as_table }}
</table>
```

### Fixtures won't load

[`contenttypes` and `permission` are the culprits](http://stackoverflow.com/questions/853796/problems-with-contenttypes-when-loading-a-fixture-in-django). Remove all of them from the fixture file (using a script or something), then re-run loaddata.

[github]: https://github.com/devilry/devilry-deploy/blob/master/docs/src/migrationguides/1.4.0.rst#2-----migrate-the-database
[readthedocs]: http://south.readthedocs.org/en/latest/dependencies.html
