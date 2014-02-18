* The default settings for MySQL instances on RDS is stupid. Create a parameter group with (significantly) longer timeouts.
* Django-South does not work on RDS.
* Copying a file across S3 buckets is just copying its key -- S3 is one uniform storage resource. Having a key that points to a file in both buckets means that, effectively, the file exists in both buckets.
* [`htop` missing](http://aws.blandnet.org/wordpress/htop-install/)
* [Upgrading an instance](http://stackoverflow.com/a/8243307/1558430): stop the instance, wait for a while, and select "Change Instance Type"
* VPC is Virtual Private Cloud, not Virtual PC.
* 
