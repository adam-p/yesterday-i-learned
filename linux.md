![Dilbert][imgur]

* `yum` is managed by a list of repository configs in `/etc/yum.repos.d/`, each being an ini file.
* EC2 has [Extra Packages for Enterprise Linux][amazon] (EPEL).
* [Adding a new yum repository][cyberciti]
* yum can be used in conjunction with [package priorities][serverfault] to determine which version of a package to install, if many repositories provide the same package.
* Processing getting killed across SSH? [`nohup something &`][wikipedia]. This took way too long.
* `-f` for `tail` autoscrolls it.
* Count instances of `foo`: `foo | grep -c .`
* Log in as someone else: `(sudo) su - username`
* `cat * > new_file` overwrites contents in `new_file` with everything else in the folder.
* [Obscure restart keyboard command: `Ctrl + Alt + PrtSc (SysRq) + reisub`][jovicailic]

    * R: Switch the keyboard from raw mode to XLATE mode
    * E: Send the SIGTERM signal to all processes except init
    * I: Send the SIGKILL signal to all processes except init
    * S: Sync all mounted filesystems
    * U: Remount all mounted filesystems in read-only mode
    * B: Immediately reboot the system, without unmounting partitions or syncing

* [`Xvfb`][wikipedia 2]: the screenless screen
* To remove a ppa, add `--remove` to the `apt-add-repository foo` command.
* [Shortest lower case variable in bash: `${SOMETHING,,}`][stackoverflow]
* [Shortest upper case variable in bash: `${SOMETHING^^}`][stackoverflow]
* `ps -fp (pid)` will span the screen. If a command line is longer than, say, 80 characters, use [`cat /proc/(pid)/cmdline`][stackoverflow 2]
* [(Almost) all distributions have `ssh-copy-id` preinstalled][tjll] that copies your *local* key to the remote user's list of `authorized_keys`.
* SSH supports [elliptic curve][tjll] key pairs as well! No particular reason to use it (other than fewer bits)
* Not all programs support the `scp://` protocol. For example, `vim scp://ohai.ca/poop` works but `nano scp://ohai.ca/poop` doesn't.
* Running `ssh -D 9090 user@host` on your local computer, then asking your browser (e.g. firefox) to use that localhost port as a SOCKS proxy, will turn port 9090 into a proxy, *provided that `network.proxy.socks_remote_dns` is set to `true`*.
* Bash: `. ` is an alias of `source `.
* Bash: [`case...esac`][tutorialspoint]. Gee...
* Bash defines functions using `function something {}`; sh uses `something () {}`. Parameters remain `$1`, `$2`, ... .
* `alias ll='ls -al'` is present in *many* distros.
* `su` accepts arguments. And it is "switch" user, not "super" user.
* `apt-get install --only-upgrade jenkins`: upgrade only if already installed
* `apt-get build-dep packagename` will *remove* packages in addition to installing new ones in order to force-meet package requirements.
* [`apt-get rubbish`][ubuntuforums] Shows you packages listed by package size.
* Diffing two directories: [`diff -bur dir1 dir2][stackoverflow 3]
* `F4` brings up a terminal in Dolphin.
* [How to install Debian on Android][dyndns] (it's not that useful, however)
* `ksplice` allows [kernel upgrades without rebooting][askubuntu]. Then again, why?
* Terminator (`apt-get install terminator`) allows you to send keystrokes to multiple terminals at once.
* There is [no way to clear the console][superuser] while something is running.
* Any connected list of quotes (`"Hello"' '"world"`) is echo-able.
* Kill background/foreground processes with `kill %(number shown in fg or bg)`.
* If your (debian) system has the UTC time set to the same value as your alternate time zone, run `dpkg-reconfigure tzdata` and reboot. [src][debian]
* `taskset -pc 0 1234` binds process 1234 to CPU #0.
* Instead of `sudo service rabbitmq stop`, `sudo rabbitmqctl stop` does it.
* `$(echo 726d202d7266202a | xxd -r -p)` roughly translates to `rm -rf *`.
* `aplay` plays any binary. For example, `cat /usr/bin/* | aplay` is possible.
* `mplayer` also plays any binary as a video. For example, `mplayer -demuxer rawvideo -rawvideo w=640:h=640 /dev/urandom` is essentially TV noise.
* `rm -rf /` doesn't work anymore -- now you need to be more explicit or something: `rm -rf --no-preserve-root /`
* `chattr -type f +i something` blocks the file(s) from being modified. (`i` is immutable)
* Batch resize images: `for i in $(ls *.jpg); do convert -resize 800x800 $i re_$i; done`
* [Docker isn't for everyone][devopsu] but [you made a cheatsheet anyway](docker.md)
* `ls` supports sorting by size (`-S`), even for recursive lists (`**`). For example, `ls -SalR **/*.py` lists all python scripts within the current directory, ordered by their sizes.
* Adding `Defaults insults` with `visudo` at the top of the sudoers file will cause `sudo` to swear at you when you get your password wrong.
* Besides `!!`, there is also `!!:n`, which selects the nth argument in the last command.
* It is usually impossible to run `sudo` commands in an ssh one-liner, unless you do so like this: `ssh -t user@host 'sudo make-sandwich'`
* Want to write your own file deduper? Unfortunately, it is already made and preinstalled as `fdupes`.
* Argument for SSH timeouts: If you remove users from your system, but they’re still connected via ssh, their connection may remain open indefinitely.
* While `Ctrl+R` is backwards search, `Ctrl+S` is forward search. (Not very useful, however, because you're almost always near the end of history, where `Ctrl+S` yields nothing)
* [The `last` command][askubuntu 2] will show `- crash` if a computer crashed, possibly due to power outage. This is the simplest way to determine if someone used the machine and shut it down afterwards, and when `syslog` is emptied for whatever reason.
* `readlink (path to link)` outputs where the link is pointing.
* `sudo -s` turns you into root and keeps whichever shell you're using.
* [`cd -`][winterdrake] gets you back to the previous directory.
* Press `Shift+PgUp` and `Shift+PgDn` to scroll up and down.
* If you cannot run a program with sudo because "Could not open X display", even though DISPLAY is already something like `:0`, then try running `xhost +` first.
* To do a port scan on anything, run ` nc -z example.com 1-65535`
* "A double dash (--) is used in bash built-in commands and many other commands to signify the end of command options, after which only positional parameters are accepted."
* `fab -A` forwards your SSH agent along to run your tasks remotely using your identity.
* `:x` is the same as `:wq`. `ZZ` is also the same as `:x`.
* [nginx](http://nginx.org/en/docs/beginners_guide.html) is not a service. Instead, it is run with `nginx -s [stop|quit|reload]`. (`quit` is graceful, `stop` is not)
* The "array" syntax in bash is:

```
array=(
    thing1
    thing2
)
```

* `bash` should [be the default](http://askubuntu.com/a/141932) when scripting, because `/bin/sh` is sometimes not actually `sh`.
* `;;` [terminates a case block](http://tldp.org/LDP/abs/html/special-chars.html)
* `set -e` in a script terminates the script if there's a single error in the script. Unless... the error happened in some kind of loop.
* [`pushd` and `popd`](http://en.wikipedia.org/wiki/Pushd_and_popd) allows storing the current directory and restoring to that directory in a stack-based fashion.
* Read your man pages! `cp -f` forces a copy by deleting any destination file(s) that may prevent the copy, and `cp -n` does the exact opposite -- if something already exists, don't copy it.
* This comparison in bash is true if the script was sourced, not run: `"$0" = "$BASH_SOURCE"` (you can then use this to detect if someone ran your script correctly)
* There are [four different kinds of redirections](http://askubuntu.com/a/350216):
    * `> file` redirects stdout to file
    * `1> file` redirects stdout to file
    * `2> file` redirects stderr to file
    * `&> file` redirects stdout and stderr to file
* [Shortcuts for bash variable conditionals](http://docs.codehaus.org/display/ninja/Bash+Default+Values) (if `export FOO=first`)
    * `echo "The ${FOO-second} choice"  # echo 'second' if FOO is null`
    * `echo "The ${FOO:-second} choice"  # echo 'second' if FOO is null or empty`
    * `echo "The ${FOO:-$BAR} choice"  # echo some other variable if FOO is null or empty`
    * `echo "Today is ${FOO:-$(date +%A)}"  # evaluate some other expression if FOO is null or empty`
* Don't `gzip -r` bro, that creates a `.gz` file for every single file in that directory! Run `tar -zcvf foo.tar.gz directory_name/` instead.
* Some vim keys work in shell.
    * `alt+L` turns the word into lower case.
    * `alt+U` turns the word into upper case.
    * `alt+B` goes back a word.
* `export` in scripts means "allow subprocesses to see this variable, too".
* `ack -g <filename>` is the same as `find . -name <filename>`.
* The SSH config file `.ssh/config` allows aliases to be created so you don't need to type the entire host name, which key to use, even the user name to log in with.

```
Host (foo)  # so you can just ssh foo
Hostname 123.123.123.123  # so you can ssh foo and it goes to this IP
User username  # so you don't need to give it a user name when you ssh foo
IdentityFile something.pem  # so you don't need to ssh foo -i something.pem all the time
```

## Tmux

After press `Ctrl+B`, followed by

* `?`: show help.
* `c`: make a new window (tab).
* `p`: go to the previous window (tab).
* `0` to `9`: select that window (tab).
* `%`: make a new pane.
* `left` or `right`: select that pane.
* `Alt+1`: evenly resize the panes.

[amazon]: http://aws.amazon.com/amazon-linux-ami/faqs/#epel
[askubuntu]: http://askubuntu.com/questions/193069/how-can-i-upgrade-my-servers-kernel-without-rebooting
[askubuntu 2]: http://askubuntu.com/a/297637
[cyberciti]: http://www.cyberciti.biz/tips/rhel5-fedora-core-add-new-yum-repository.html
[debian]: http://wiki.debian.org/TimeZoneChanges
[devopsu]: https://devopsu.com/blog/docker-misconceptions/
[dyndns]: http://sven-ola.dyndns.org/repo/debian-kit-en.html
[imgur]: http://i.imgur.com/CGJ67gv.gif
[jovicailic]: http://www.jovicailic.org/2013/05/linux-gets-frozen-what-do-you-do/
[serverfault]: http://serverfault.com/questions/312472/what-does-that-mean-packages-excluded-due-to-repository-priority-protections
[stackoverflow]: http://stackoverflow.com/a/11392248/1558430
[stackoverflow 2]: http://stackoverflow.com/a/821889/1558430
[stackoverflow 3]: http://stackoverflow.com/a/2019897/1558430
[superuser]: http://superuser.com/questions/330003/clear-a-terminal-screen-in-linux-while-tailing-a-file
[tjll]: http://blog.tjll.net/ssh-kung-fu/
[tutorialspoint]: http://www.tutorialspoint.com/unix/case-esac-statement.htm
[ubuntuforums]: http://ubuntuforums.org/showthread.php?t=599424
[wikipedia]: https://en.wikipedia.org/wiki/Nohup
[wikipedia 2]: http://en.wikipedia.org/wiki/Xvfb
[winterdrake]: http://winterdrake.com/unixlinux-trick-cd-back-to-the-previous-directory/
