* To install MySQL server, client, and python adapters: `sudo apt-get install mysql-common mysql-client-4.4 libmysqlclent-dev mysql-server-5.5`
* To start/stop/restart MySQL server: `(/etc/init.d/mysql OR /etc/init.d/mysqld) start/srestart`
* [Tables are stored in `/var/lib/mysql`](http://forums.mysql.com/read.php?10,239450,239465#msg-239465), and, if you are using InnoDB, the file is actually called `ibdata`.

* Create a database: [`CREATE DATABASE ebdb;`](http://dev.mysql.com/doc/refman/5.0/en/create-database.html)
  (after which you can run `python manage.py syncdb` if that happens to be your thing)
* Select a database: `USE ebdb;` (which isn't `SELECT ebdb`, for some reason)
* Delete a database: [`DROP DATABASE ebdb;`](http://dev.mysql.com/doc/refman/5.0/en/drop-database.html)
* Show list of tables: `SHOW TABLES;`

* Create an index: 


* Show tables by schema: `SELECT table_name, engine FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '(dbname)';`
* Show table columns: `SHOW COLUMNS FROM table_name;`
* Show table info: `DESCRIBE table_name;`
* Change table engine: [`ALTER TABLE table_name ENGINE=InnoDB;`](http://dev.mysql.com/doc/refman/5.5/en/converting-tables-to-innodb.html)
* Show table engines (and other info): `SHOW TABLE STATUS;`
* Show the SQL needed to create an existing table: [`SHOW CREATE TABLE table_name;`](http://stackoverflow.com/a/5615783/1558430)
* Show last `InnoDB` foreign key error: [`SHOW ENGINE INNODB STATUS;`](http://stackoverflow.com/a/179501/1558430)


* Create a user: `CREATE USER 'ebroot'@'localhost' [IDENTIFIED BY 'some_pass'];` (different from `CREATE USER 'ebroot';` and `CREATE USER 'ebroot'@'*';`)
* Create a user using a pre-hashed password: `CREATE USER 'ebroot'@'localhost' IDENTIFIED BY PASSWORD 'abcdef123456';`
* Give a user privileges: `GRANT ALL ON ebdb.* TO 'ebroot'@'localhost';`






* MySQL [does not](http://stackoverflow.com/a/10474104/1558430) support transactional schema alters at any time.
```
Running migrations for pinpoint:
 - Migrating forwards to 0013_auto__chg_field_campaign_mobile__del_unique_campaign_mobile__chg_field.
 > pinpoint:0001_initial
 > pinpoint:0002_auto__del_field_storetheme_discovery_youtube__del_field_storetheme_pre
 > pinpoint:0003_auto__add_field_storetheme_image_preview
 > pinpoint:0004_auto__add_field_storetheme_instagram
 > pinpoint:0005_auto__del_field_storetheme_preview__add_field_storetheme_product_previ
 > pinpoint:0006_auto__add_field_storetheme_instagram_product_preview
 > pinpoint:0007_auto__add_field_storetheme_combobox_preview
 > pinpoint:0008_auto__add_field_campaign_theme__add_field_campaign_mobile__chg_field_s
 > pinpoint:0009_auto__add_intentrankcampaign__add_field_campaign_default_intentrank
 > pinpoint:0010_auto__del_field_storetheme_store
 > pinpoint:0011_auto__add_field_campaign_supports_categories
 > pinpoint:0012_auto__chg_field_campaign_default_intentrank__del_unique_campaign_defau
 > pinpoint:0013_auto__chg_field_campaign_mobile__del_unique_campaign_mobile__chg_field
FATAL ERROR - The following SQL query failed: ALTER TABLE `pinpoint_campaign` DROP FOREIGN KEY `mobile_id_refs_id_555f3c1c2ab535ff`
The error was: (1025, "Error on rename of './ebdb/#sql-46e_36' to './ebdb/pinpoint_campaign' (errno: 150)")
 ! Error found during real run of migration! Aborting.

 ! Since you have a database that does not support running
 ! schema-altering statements in transactions, we have had 
 ! to leave it in an interim state between migrations.

! You *might* be able to recover with:   - no dry run output for alter_column() due to dynamic DDL, sorry
   = ALTER TABLE `pinpoint_campaign` ADD CONSTRAINT `pinpoint_campaign_mobile_id_965519bb26f673b_uniq` UNIQUE (`mobile_id`) []
   - no dry run output for alter_column() due to dynamic DDL, sorry
   = ALTER TABLE `pinpoint_campaign` ADD CONSTRAINT `pinpoint_campaign_theme_id_29ae3b7bb9bfb8ef_uniq` UNIQUE (`theme_id`) []

 ! The South developers regret this has happened, and would
 ! like to gently persuade you to consider a slightly
 ! easier-to-deal-with DBMS (one that supports DDL transactions)
 ! NOTE: The error which caused the migration to fail is further up.
Error in migration: pinpoint:0013_auto__chg_field_campaign_mobile__del_unique_campaign_mobile__chg_field
Traceback (most recent call last):
  File "manage.py", line 23, in <module>
    execute_from_command_line(sys.argv)
  File "/home/brian/Envs/SecondFunnel/lib/python2.7/site-packages/django/core/management/__init__.py", line 443, in execute_from_command_line
    utility.execute()
  File "/home/brian/Envs/SecondFunnel/lib/python2.7/site-packages/django/core/management/__init__.py", line 382, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/home/brian/Envs/SecondFunnel/lib/python2.7/site-packages/django/core/management/base.py", line 196, in run_from_argv
    self.execute(*args, **options.__dict__)
  File "/home/brian/Envs/SecondFunnel/lib/python2.7/site-packages/django/core/management/base.py", line 232, in execute
    output = self.handle(*args, **options)
  File "/home/brian/Envs/SecondFunnel/lib/python2.7/site-packages/south/management/commands/migrate.py", line 108, in handle
    ignore_ghosts = ignore_ghosts,
  File "/home/brian/Envs/SecondFunnel/lib/python2.7/site-packages/south/migration/__init__.py", line 213, in migrate_app
    success = migrator.migrate_many(target, workplan, database)
  File "/home/brian/Envs/Sec        ondFunnel/lib/python2.7/site-packages/south/migration/migrators.py", line 235, in migrate_many
    result = migrator.__class__.migrate_many(migrator, target, migrations, database)
  File "/home/brian/Envs/SecondFunnel/lib/python2.7/site-packages/south/migration/migrators.py", line 310, in migrate_many
    result = self.migrate(migration, database)
  File "/home/brian/Envs/SecondFunnel/lib/python2.7/site-packages/south/migration/migrators.py", line 133, in migrate
    result = self.run(migration)
  File "/home/brian/Envs/SecondFunnel/lib/python2.7/site-packages/south/migration/migrators.py", line 107, in run
    return self.run_migration(migration)
  File "/home/brian/Envs/SecondFunnel/lib/python2.7/site-packages/south/migration/migrators.py", line 81, in run_migration
    migration_function()
  File "/home/brian/Envs/SecondFunnel/lib/python2.7/site-packages/south/migration/migrators.py", line 57, in <lambda>
    return (lambda: direction(orm))
  File "/home/brian/Envs/SecondFunnel/apps/pinpoint/migrations/0013_auto__chg_field_campaign_mobile__del_unique_campaign_mobile__chg_field.py", line 19, in forwards
    db.alter_column('pinpoint_campaign', 'mobile_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['pinpoint.StoreTheme']))
  File "/home/brian/Envs/SecondFunnel/lib/python2.7/site-packages/south/db/generic.py", line 44, in _cache_clear
    return func(self, table, *args, **opts)
  File "/home/brian/Envs/SecondFunnel/lib/python2.7/site-packages/south/db/generic.py", line 487, in alter_column
    self.delete_foreign_key(table_name, name)
  File "/home/brian/Envs/SecondFunnel/lib/python2.7/site-packages/south/db/generic.py", line 44, in _cache_clear
    return func(self, table, *args, **opts)
  File "/home/brian/Envs/SecondFunnel/lib/python2.7/site-packages/south/db/generic.py", line 780, in delete_foreign_key
    "constraint": self.quote_name(constraint_name),
  File "/home/brian/Envs/SecondFunnel/lib/python2.7/site-packages/south/db/generic.py", line 273, in execute
    cursor.execute(sql, params)
  File "/home/brian/Envs/SecondFunnel/lib/python2.7/site-packages/django/db/backends/util.py", line 40, in execute
    return self.cursor.execute(sql, params)
  File "/home/brian/Envs/SecondFunnel/lib/python2.7/site-packages/django/db/backends/mysql/base.py", line 114, in execute
    return self.cursor.execute(query, args)
  File "/home/brian/Envs/SecondFunnel/lib/python2.7/site-packages/MySQLdb/cursors.py", line 174, in execute
    self.errorhandler(self, exc, value)
  File "/home/brian/Envs/SecondFunnel/lib/python2.7/site-packages/MySQLdb/connections.py", line 36, in defaulterrorhandler
    raise errorclass, errorvalue
django.db.utils.DatabaseError: (1025, "Error on rename of './ebdb/#sql-46e_36' to './ebdb/pinpoint_campaign' (errno: 150)")
```