# Any SQL

* `TRUNCATE some table` differs from `DELETE * FROM some table` in that the `TRUNCATE` statement does not leave behind transaction logs, and thus cannot be rolled back. (Here's a trivia you will never use again)

# MySQL

* To install MySQL server, client, and python adapters: `sudo apt-get install mysql-common mysql-client-4.4 libmysqlclent-dev mysql-server-5.5`
* To start/stop/restart MySQL server: `(/etc/init.d/mysql OR /etc/init.d/mysqld) start/srestart`
* [Tables are stored in `/var/lib/mysql`](http://forums.mysql.com/read.php?10,239450,239465#msg-239465), and, if you are using InnoDB, the file is actually called `ibdata`.

* Create a database: [`CREATE DATABASE ebdb;`](http://dev.mysql.com/doc/refman/5.0/en/create-database.html)
  (after which you can run `python manage.py syncdb` if that happens to be your thing)
* Select a database: `USE ebdb;` (which isn't `SELECT ebdb`, for some reason)
* Delete a database: [`DROP DATABASE ebdb;`](http://dev.mysql.com/doc/refman/5.0/en/drop-database.html)
* Show list of tables: `SHOW TABLES;`

* Create an index: **TODO**

* Show tables by schema: `SELECT table_name, engine FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '(dbname)';`
* Show table columns: `SHOW COLUMNS FROM table_name;`
* Show table info: `DESCRIBE table_name;`
* Change table engine: [`ALTER TABLE table_name ENGINE=InnoDB;`](http://dev.mysql.com/doc/refman/5.5/en/converting-tables-to-innodb.html)
* Show table engines (and other info): `SHOW TABLE STATUS;`
* Show the SQL needed to create an existing table: [`SHOW CREATE TABLE table_name;`](http://stackoverflow.com/a/5615783/1558430)
* Show last `InnoDB` foreign key error: [`SHOW ENGINE INNODB STATUS;`](http://stackoverflow.com/a/179501/1558430)
* `SET unique_checks=0;` and `SET foreign_key_checks = 0;` does not help you drop a foreign key constraint.


* Create a user: `CREATE USER 'ebroot'@'localhost' [IDENTIFIED BY 'some_pass'];` (different from `CREATE USER 'ebroot';` and `CREATE USER 'ebroot'@'*';`)
* Create a user using a pre-hashed password: `CREATE USER 'ebroot'@'localhost' IDENTIFIED BY PASSWORD 'abcdef123456';`
* Give a user privileges: `GRANT ALL ON ebdb.* TO 'ebroot'@'localhost';`

* MySQL [does not](http://stackoverflow.com/a/10474104/1558430) support transactional schema alters at any time.
* Amazon [does not](https://forums.aws.amazon.com/message.jspa?messageID=153017#) allow SSH into RDS instances.
* [Why is MySQL's default collation latin1_swedish_ci?](http://stackoverflow.com/questions/6769901/why-is-mysqls-default-collation-latin1-swedish-ci)

# PostgresQL

* Logging into `psql`: `psql dbname username`
* Backup a database: [`pg_dumpall > outfile`](http://www.postgresql.org/docs/9.1/static/backup-dump.html#BACKUP-DUMP-ALL) OR `pg_dump specific_db > outfile`
* [Transfer/Migrate a database to another postgres version](http://www.postgresql.org/docs/9.0/static/migration.html): `pg_dumpall -p 5432 | psql -d postgres -p 6543` (old port to new port)
* Compress a backup: `pg_dump dbname | gzip > outfile.gz`
* Restore a backup: `psql -f outfile postgres` (the keyword `postgres` here is necessary only if you load into a [large cluster](http://www.postgresql.org/docs/9.1/static/backup-dump.html#BACKUP-DUMP-ALL))
* Restore a compressed backup: `gunzip -c outfile.gz | psql dbname`
* Delete a database: (`sudo su - owner_unix_user`), then run `dropdb dbname -Uowner_unix_user -W`. Alternatively, in psql, switch to a database (`\c postgres;`), then `DROP DATABASE dbname;` to delete.
* [Postgres does not take performance hits from string lengths.](http://www.postgresql.org/docs/8.2/static/datatype-character.html) Putting it in reverse, it also means it cannot be sped up by shortening strings.
* [`varying` string type has no length limit](http://stackoverflow.com/questions/2904991/postgresql-character-varying-length-limit)
* `\c`: show the current user and database. `\c dbname` also switches to that database.
* `\d`: list tables.
* `\d+ tablename`: describe the table.
* `\l`: list databases.
* Monitoring psql: `sudo tail -n 50 -f /var/log/postgresql/postgresql-9.1-main.log`
* Setting monitoring flags: [`log_min_duration_statement = 0`, and `log_statement = all`](http://stackoverflow.com/a/12670828/1558430)
* Running a SQL file: [`psql -U username -d myDataBase -a -f myInsertFile`](http://stackoverflow.com/a/12085561/1558430)
* Re-index a table: `REINDEX TABLE tablename;` (doesn't work if the index is broken, which is *retarded*
  `REINDEX TABLE tablename force;` doesn't work.
* [Read the docs](https://wiki.postgresql.org/wiki/Things_to_find_out_about_when_moving_from_MySQL_to_PostgreSQL). Postgres strings must be enclosed with single quotes. Double quotes only work for system identifiers.
* You can choose the type of index to build. The default is B tree.

## Performance

* When in doubt: use `EXPLAIN ANALYZE (your query here);` to help you out.
* `EXPLAIN` returns whatever the engine *thinks* about a query. `EXPLAIN ANALYZE` actually runs the query, which requires data in actual scale.
* Selecting an indexed column, but while using a function-wrapped parameter (e.g. `WHERE SOMETHING(ROW) == 1`) disables the index.
* [There are function-based indices](http://use-the-index-luke.com/sql/where-clause/functions) but it is discouraged for their own performance reasons.
* Multi-column indices are position-dependent; `CREATE INDEX tbl_idx ON tbl (a, b)` is different from `CREATE INDEX tbl_idx ON tbl (b, a)`, where selecting by `b` requires the second index.
* Continuing from the point above, if the first column in a multi-column index (^ i.e. `a`) is selected as a range, the subsequent indices (i.e. `b`) are useless in the same query. 
  **Make sure the first column in a multi-column index is selected exactly.**
* Getting the create table SQL for a table: [see guide](http://stackoverflow.com/a/16154183/1558430)

## Troubleshooting

### Corrupted index

This is what a corrupted index looks like:

```
db=> select * from assets_tile where id=43;
 id | ... 
----+-----
 43 | ...
(1 row)
db=> reindex table assets_tile;
ERROR:  could not create unique index "assets_tile_pkey"
DETAIL:  Key (id)=(43) is duplicated.
```

### New databases don't have extensions installed

Postgres has 'templates', so running `psql -d template1 -c 'CREATE EXTENSION...'` adds the CREATE EXTENSION line to the list of queries to run when creating a database.

### Permission denied (while reading an `.sql`)

`sudo -u someone psql -f filename` reads the file as someone instead of you. If that someone cannot access the file but you can, pipe the file in as yourself:

`sudo -u someone psql < filename`

# MongoDB

> "MongoDB is the core piece of architectural rot in every single teetering and broken data platform I've worked with."

MongoDB is actually NoSQL, so it shouldn't be in this file.

* Install: `sudo apt-get install mongodb`
* [To have MongoDB return all records](https://engineering.meteor.com/mongodb-queries-dont-always-return-all-matching-documents-654b6594a827#.emoh9pv03), you must either:
  * have an index on a field, and search for exactly that field, or
  * query with all keys when you build a multi-field index, or
  * never update anything. MongoDB misses documents if you update some while you read the same table (if they can be so called).

# Redis

Redis is also NoSQL. It is a KV Store, however.
