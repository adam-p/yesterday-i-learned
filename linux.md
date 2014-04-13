![repo logo](http://www.ohai.ca/images/yesterday-i-learned.jpg)

* `yum` is managed by a list of repository configs in `/etc/yum.repos.d/`, each being an ini file.
* EC2 has [Extra Packages for Enterprise Linux](http://aws.amazon.com/amazon-linux-ami/faqs/#epel) (EPEL).
* [Adding a new yum repository](http://www.cyberciti.biz/tips/rhel5-fedora-core-add-new-yum-repository.html)
* yum can be used in conjunction with [package priorities](http://serverfault.com/questions/312472/what-does-that-mean-packages-excluded-due-to-repository-priority-protections) to determine which version of a package to install, if many repositories provide the same package.
* Processing getting killed across SSH? [`nohup something &`](https://en.wikipedia.org/wiki/Nohup). This took way too long.
* `-f` for `tail` autoscrolls it.
* Count instances of `foo`: `foo | grep -c .`
* Log in as someone else: `(sudo) su - username`
* `cat * > new_file` overwrites contents in `new_file` with everything else in the folder.
* [Obscure restart keyboard command: `Ctrl + Alt + PrtSc (SysRq) + reisub`](http://www.jovicailic.org/2013/05/linux-gets-frozen-what-do-you-do/)

    * R: Switch the keyboard from raw mode to XLATE mode
    * E: Send the SIGTERM signal to all processes except init
    * I: Send the SIGKILL signal to all processes except init
    * S: Sync all mounted filesystems
    * U: Remount all mounted filesystems in read-only mode
    * B: Immediately reboot the system, without unmounting partitions or syncing

* [`Xvfb`](http://en.wikipedia.org/wiki/Xvfb): the screenless screen
* To remove a ppa, add `--remove` to the `apt-add-repository foo` command.
* [Shortest lower case variable in bash: `${SOMETHING,,}`](http://stackoverflow.com/a/11392248/1558430)
* [Shortest upper case variable in bash: `${SOMETHING^^}`](http://stackoverflow.com/a/11392248/1558430)
