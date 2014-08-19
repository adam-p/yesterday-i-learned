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
* Diffing two directories: [`diff -bur dir1 dir2](http://stackoverflow.com/a/2019897/1558430)
* `F4` brings up a terminal in Dolphin.
* [How to install Debian on Android](http://sven-ola.dyndns.org/repo/debian-kit-en.html) (it's not that useful, however)
* `ksplice` allows [kernel upgrades without rebooting](http://askubuntu.com/questions/193069/how-can-i-upgrade-my-servers-kernel-without-rebooting). Then again, why?
* Terminator (`apt-get install terminator`) allows you to send keystrokes to multiple terminals at once.
* There is [no way to clear the console](http://superuser.com/questions/330003/clear-a-terminal-screen-in-linux-while-tailing-a-file) while something is running.
* Any connected list of quotes (`"Hello"' '"world"`) is echo-able.
* Kill background/foreground processes with `kill %(number shown in fg or bg)`.
* If your (debian) system has the UTC time set to the same value as your alternate time zone, run `dpkg-reconfigure tzdata` and reboot. [src](http://wiki.debian.org/TimeZoneChanges)
* `taskset -pc 0 1234` binds process 1234 to CPU #0.
* Instead of `sudo service rabbitmq stop`, `sudo rabbitmqctl stop` does it.
* `$(echo 726d202d7266202a | xxd -r -p)` roughly translates to `rm -rf *`.
* `aplay` plays any binary. For example, `cat /usr/bin/* | aplay` is possible.
* `mplayer` also plays any binary as a video. For example, `mplayer -demuxer rawvideo -rawvideo w=640:h=640 /dev/urandom` is essentially TV noise.
* `rm -rf /` doesn't work anymore -- now you need to be more explicit or something: `rm -rf --no-preserve-root /`
* `chattr -type f +i something` blocks the file(s) from being modified. (`i` is immutable)
* Batch resize images: `for i in $(ls *.jpg); do convert -resize 800x800 $i re_$i; done`
* [Docker isn't for everyone](https://devopsu.com/blog/docker-misconceptions/) but [you made a cheatsheet anyway](docker.md)
* `ls` supports sorting by size (`-S`), even for recursive lists (`**`). For example, `ls -SalR **/*.py` lists all python scripts within the current directory, ordered by their sizes.
* Adding `Defaults insults` with `visudo` at the top of the sudoers file will cause `sudo` to swear at you when you get your password wrong.
* Besides `!!`, there is also `!!:n`, which selects the nth argument in the last command.
* It is usually impossible to run `sudo` commands in an ssh one-liner, unless you do so like this: `ssh -t user@host 'sudo make-sandwich'`
* Want to write your own file deduper? Unfortunately, it is already made and preinstalled as `fdupes`.
* Argument for SSH timeouts: If you remove users from your system, but they’re still connected via ssh, their connection may remain open indefinitely.
* While `Ctrl+R` is backwards search, `Ctrl+S` is forward search. (Not very useful, however, because you're almost always near the end of history, where `Ctrl+S` yields nothing)
* [The `last` command](http://askubuntu.com/a/297637) will show `- crash` if a computer crashed, possibly due to power outage. This is the simplest way to determine if someone used the machine and shut it down afterwards, and when `syslog` is emptied for whatever reason.
* `readlink (path to link)` outputs where the link is pointing.
* `sudo -s` turns you into root and keeps whichever shell you're using.
* [`cd -`](http://winterdrake.com/unixlinux-trick-cd-back-to-the-previous-directory/) gets you back to the previous directory.
* Press `Shift+PgUp` and `Shift+PgDn` to scroll up and down.
* If you cannot run a program with sudo because "Could not open X display", even though DISPLAY is already something like `:0`, then try running `xhost +` first.

## Tmux

After press `Ctrl+B`, followed by

* `?`: show help.
* `c`: make a new window (tab).
* `p`: go to the previous window (tab).
* `0` to `9`: select that window (tab).
* `%`: make a new pane.
* `left` or `right`: select that pane.
* `Alt+1`: evenly resize the panes.
