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
* From within an instance, get its hostname: [`curl http://169.254.169.254/latest/meta-data/public-hostname`](http://serverfault.com/questions/403440/print-external-host-name-of-ec2-instance)
* [Blue-green deployment](http://martinfowler.com/bliki/BlueGreenDeployment.html) involves spinning up a new version of the application, waiting for deployment to complete and its state verified, then replacing green (current) instances in the load balancer with the ones you just spun up (blue).
1. Load balancers send your requests to different servers (perhaps evenly, perhaps not). Auto scaling groups tell the thingy how many servers you want to have. Launch configurations tell the bois how big you want each server to be.
