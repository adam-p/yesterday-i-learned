![Dilbert](http://i.imgur.com/CGJ67gv.gif)

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
* `ps -fp (pid)` will span the screen. If a command line is longer than, say, 80 characters, use [`cat /proc/(pid)/cmdline`](http://stackoverflow.com/a/821889/1558430)
* [(Almost) all distributions have `ssh-copy-id` preinstalled](http://blog.tjll.net/ssh-kung-fu/) that copies your *local* key to the remote user's list of `authorized_keys`.
* SSH supports [elliptic curve](http://blog.tjll.net/ssh-kung-fu/) key pairs as well! No particular reason to use it (other than fewer bits)
* Not all programs support the `scp://` protocol. For example, `vim scp://ohai.ca/poop` works but `nano scp://ohai.ca/poop` doesn't.
* Running `ssh -D 9090 user@host` on your local computer, then asking your browser (e.g. firefox) to use that localhost port as a SOCKS proxy, will turn port 9090 into a proxy, *provided that `network.proxy.socks_remote_dns` is set to `true`*.
* Bash: `. ` is an alias of `source `.
* Bash: [`case...esac`](http://www.tutorialspoint.com/unix/case-esac-statement.htm). Gee...
* Bash defines functions using `function something {}`; sh uses `something () {}`. Parameters remain `$1`, `$2`, ... .
* `alias ll='ls -al'` is present in *many* distros.
* `su` accepts arguments. And it is "switch" user, not "super" user.
* `apt-get install --only-upgrade jenkins`: upgrade only if already installed
* `apt-get build-dep packagename` will *remove* packages in addition to installing new ones in order to force-meet package requirements.
* [`apt-get rubbish`](http://ubuntuforums.org/showthread.php?t=599424) Shows you packages listed by package size.
* 