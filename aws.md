* The default settings for MySQL instances on RDS is stupid. Create a parameter group with (significantly) longer timeouts.
* Django-South does not work on RDS.
* Copying a file across S3 buckets is just copying its key -- S3 is one uniform storage resource. Having a key that points to a file in both buckets means that, effectively, the file exists in both buckets.
* [`htop` missing](http://aws.blandnet.org/wordpress/htop-install/)
* [Upgrading an instance](http://stackoverflow.com/a/8243307/1558430): stop the instance, wait for a while, and select "Change Instance Type"
* VPC is Virtual Private Cloud, not Virtual PC.
* If you can't move an RDS server's region, at least move the EC2 instances' availabiltiy zones to match it.
* `/etc/httpd/conf/httpd.conf` has a load of stuff you can disable.
* `/etc/httpd/conf.d/wsgi.conf` also has a load of stuff you can tweak.
* Get everything from an s3 bucket: `s3cmd get s3://(bucket name)/*`
* EC2 will wipe out all of your `authorized_keys` in newly-spawned instances unless the instance was created with the "no reboot" option checked.
* You can restore a Postgres snapshot with a different name while the current one is being deleted, then rename the new database to the old name to replace it with no downtime.
