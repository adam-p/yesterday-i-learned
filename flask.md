* To properly get messages from a flask app running on gunicorn, the command needs to be as such: `gunicorn project.file:app --log-file=- --log-level debug`
* PyCharm understands gunicorn only after ["gevent compatible debugging"](http://stackoverflow.com/a/20738996/1558430) is enabled.
* The view's function `__name__` *is* the view's name. This means a name cannot contain things like colons.
* `url_for('foo.bar')` gives you the url for a view named `bar` in a [blueprint](http://flask.pocoo.org/docs/0.10/blueprints/) called `foo`.
* Views can return just a string as the response.
* [There are no nested blueprints](http://stackoverflow.com/questions/33003178/nested-blueprints-in-flask) (yet)
* 