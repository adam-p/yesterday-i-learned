* The default settings for MySQL instances on RDS is stupid. Create a parameter group with (significantly) longer timeouts.
* Django-South does not work on RDS.
* Copying a file across S3 buckets is just copying its key -- S3 is one uniform storage resource. Having a key that points to a file in both buckets means that, effectively, 
* [`htop` missing](http://aws.blandnet.org/wordpress/htop-install/)

