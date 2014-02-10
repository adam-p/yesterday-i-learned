* `yum` is managed by a list of repository configs in `/etc/yum.repos.d/`, each being an ini file.
* EC2 has [Extra Packages for Enterprise Linux](http://aws.amazon.com/amazon-linux-ami/faqs/#epel) (EPEL).
* [Adding a new yum repository](http://www.cyberciti.biz/tips/rhel5-fedora-core-add-new-yum-repository.html)
* yum can be used in conjunction with [package priorities](http://serverfault.com/questions/312472/what-does-that-mean-packages-excluded-due-to-repository-priority-protections) to determine which version of a package to install, if many repositories provide the same package.
* Processing getting killed across SSH? [`nohup something &`](https://en.wikipedia.org/wiki/Nohup). This took way too long.
* `-f` for `tail` autoscrolls it.
* Count instances of `foo`: `foo | grep -c .`
* Log in as someone else: `(sudo) su - username`
