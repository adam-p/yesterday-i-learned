![repo logo](http://www.ohai.ca/images/yesterday-i-learned.jpg)

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