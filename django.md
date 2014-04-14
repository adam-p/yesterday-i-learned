# Django troubleshooting

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

[Source](https://github.com/devilry/devilry-deploy/blob/master/docs/src/migrationguides/1.4.0.rst#2-----migrate-the-database)

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

## Base models storing common fields

Add a `class Meta` that contains `abstract = True`. 
This has a downside of no longer allowing the class to be referenced (as foreign keys) directly.

## Can't have `__getattr__` in django models

Yeah. Suck it up.

## Don't know what select_related and prefetch_related do
According to onymous internet sources,

`select_related`
- foreign key & one-to-one relationship

`prefetch_related`
- many-to-many and many-to-one relationship
- generic foreign key & relationship

## lxml parser won't run / lxml won't compile

Run `sudo apt-get install libxml2-dev libxslt-dev python-dev lib32z1-dev`, *then* run `pip install lxml`

## Misc

### Filtering by how many other foreign keys an object has

Annotate with the count of the foreign key, then filter on the annotation.

```
from django.db.models import Count, Q
Content.objects.annotate(tp=Count('tagged_products')).filter(tp__gte=3)
```

### Cleaning up your mess after an outer join

```
qs.distinct()
```

### Prefetching with `get_object_or_404`

This is apparently possible:

```
get_object_or_404(Thing.prefetch_related(), id=4)
```
