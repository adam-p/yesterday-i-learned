![Dilbert][imgur]

* `yum` is managed by a list of repository configs in `/etc/yum.repos.d/`, each being an ini file.
* EC2 has [Extra Packages for Enterprise Linux][amazon] (EPEL).
* [Adding a new yum repository][cyberciti]
* yum can be used in conjunction with [package priorities][serverfault] to determine which version of a package to install, if many repositories provide the same package.
* Processing getting killed across SSH? [`nohup something &`][wikipedia]. This took way too long.
* `-f` for `tail` autoscrolls it.
* Count instances of `foo`: `foo | grep -c .`
* Log in as someone else: `(sudo) su - username`
* `>` [redirects to (and overwrites) a file](http://linuxcommand.org/lts0060.php), while `<` redirects a file to a command. Both must appear after a command. So if you expect something like

```
input_file.txt > command > output_file.txt      # You'd be bitterly disappointed
command < input_file.txt > output_file.txt      # Instead, you live with this garbage
cat input_file.txt | command > output_file.txt  # or win the useless cat award
```

* `cat * > new_file` overwrites contents in `new_file` with everything else in the folder. However, [``cat anything``](http://porkmail.org/era/unix/award.html#backticks) (with the backticks) is dangerous.
* Unrelatedly, simply `< file` shows the file in zsh (adding a useless new line every time you run it), whereas in bash it does nothing.
* And then there's [this](http://stackoverflow.com/a/876242/1558430), for *appending* both stdout (1) and stderr (2) to the same file: `cmd >> file.txt 2> &1` (send output to file.txt, then also send errors to wherever the output is going)
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
* Unlike `if` and `case`, the terminator for the `while` statement is `done` rather than `elihw`.
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
    * `$0` remains the file name if sourced, and `$BASH_SOURCE` is (nothing if sourced, file name if not).
* `$?` is magic for the last program's exit code.
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

* Backticking (`rm ``find . -name "*.pyc"`` `) works for rm, but do make sure find returns the correct things or you will suffer from major anal bleeding.
* It is impossible to write a named function with no commands in bash. The best you can do is a function containing a single `:`, which is a no-op.
* Running a function requires no brackets. Unlike Ruby's behaviour where brackets *can* be used to make it more explicit, adding `()` after a function re-declares it.
* Likewise, because having a symbol in the source executes it as a command, writing the innocent `if [$0 == $BASH_SOURCE]` executes a file called `[hello.sh`.
   * Relatedly, if statements require spaces on both sides.
      * `if [ $0 == $BASH_SOURCE ]; then  # ok`
      * `if [$0 == $BASH_SOURCE ]; then  # "missing ]"`
      * `if [$0 == $BASH_SOURCE]; then  # does stupid things`
   * While `if [ $0 == $BASH_SOURCE ]; then` is valid syntax, [ShellCheck](http://www.shellcheck.net/) will complain about "globbing and word splitting". The practice is then `if [ "$0" == "$BASH_SOURCE" ]; then`
* `[ expression ]` and `[[ expression ]]` [have the same function](http://m.odul.us/blog/2015/8/12/stronger-shell), and in general, if you're writing bash scripts, you should just use the `[[ expression ]]` version; the single `[]` version is older and doesn't support as many operations.
* Like other good things bash offers, assignments do not allow spaces on either side of `=`: `HELLO="world"`
* Having a `(  block  )` anywhere [creates a subshell](http://www.tldp.org/LDP/abs/html/subshells.html).
* However, `((1+2))` does math, and `$((1+1))` gets you the result of math.
* `[ ... ]` is an alias for `test`.
* `if` statements don't necessarily need `[]`. They do different things.
  * To check if a command was truthy, simply `if something; then`.
  * To check if a command was falsy, similarly `if ! something; then`.
* In a function, to scope the variable to the function use the `local` keyword.
* While `grep` cannot search in multi-line strings, [awk can](http://stackoverflow.com/a/3718035/1558430), using the syntax `awk '/Start pattern/,/End pattern/' filename`.
* Find any non-ASCII character in a file: `grep -P '[^\x00-\x7f]' file`
* `cd $SOME_PATH` will go to your home directory if `$SOME_PATH` is blank, which is why people wrap it with double quotes, because `cd "${SOME_PATH}"` = `cd ""`, which doesn't go anywhere.
* The 'h' in `htop` stands for 'Hisham'; Hisham Muhammad is the author of htop.
* `pstree -pu $USER` is `ps` for the USER.
* `/var/tmp/` is a `/tmp/` that is "cleaned less often."
* [`file filename`](http://superuser.com/questions/275502/how-to-get-information-about-an-image-picture-from-the-linux-command-line) gives you information, including dimensions if the file is an image.
* One (and the only useful) [command for locating large files](http://linuxlookup.com/howto/find_all_large_files_linux_system) is `find / -type f -size +20M -exec ls -lh {} \; 2> /dev/null | awk '{ print $NF ": " $5 }' | sort -nk 2,2`
* Lines cannot be fed into `rm`. To `rm` all files listed by another program per line, run `theprogram | tr "\n" "\0" | xargs -0 rm` (check first)
* To save a file without a new line at the end, use `echo -n > file.txt`.
* Any file can be a swapfile, apparently. To use a blank file as swap, type [these](https://www.digitalocean.com/community/tutorials/how-to-add-swap-on-ubuntu-14-04):

```
sudo fallocate -l 4G /swapfile  # 4GB swap
sudo chmod 600 /swapfile  # For security
sudo mkswap /swapfile
sudo swapon /swapfile  # Permanently: "/swapfile   none    swap    sw    0   0"
```

* [Never use echo in a script, they said.](https://www.reddit.com/r/linux/comments/3fhvxy/echo_help/ctovplr) Use `printf '%s\n' -n` in a script, they said. Something about AT&T.
* `ssh whoami.filippo.io` forwards *all* your public keys to the server. The server will know your email, and because GitHub publishes your key under `github.com/{username}.keys`, the server also knows your github account.
* [Distro packages go in `/usr/bin`. Other package managers install to `/usr/local/bin`.](http://unix.stackexchange.com/questions/8656/usr-bin-vs-usr-local-bin-on-linux) `/sbin` is for programs that need to be available before "users" are available to the system.
* "FYI it is pronounced ma-tay not mait. as in Yerba **Mate** which it is named after. It is from South America so it doesn't matter where you are from. You should pronounce it as it's native word." - [Matt Nelson](https://www.youtube.com/channel/UCJpf7lnaGv5Ya-O-g5wpBqQ)
* "Who cares" - [CarMoves](https://www.youtube.com/user/CarMoves)
* Solaris has a version of `killall` that does not take parameters. It kills all killable processes.
* `bash -v` means verbose, not version (`--version`).
* The ["where am I" one-liner](http://stackoverflow.com/a/246128/1558430), `DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"`, is well-documented.
* [The K in KDE stood for Kool.](https://tlhp.cf/kde-history/) They had to drop that name before version 2.
* >[`tee`](http://www.westwind.com/reference/os-x/commandline/pipes.html) allows you to both redirect output to a file, and pass it to further commands in the pipeline: `ps -ax | tee processes.txt | more`
* The *SIGWINCH* signal is sent to a process when its controlling terminal changes its size.
* `grep --include \*.txt` looks for strings only in files with that extension.
* `grep` requires `|` to be [escaped](http://stackoverflow.com/questions/34624964/grep-in-pipeline-why-it-does-not-work/34624987#34624987) in its expressions: `grep 'a\|b'`
* Bash functions are groups of commands; they can `return` at most an exit code (0 ~ 255). Because they are not functions, they don't actually have the word `function` in the declaration...
* Though functions do [allow variables to be `local`](http://www.kfirlavi.com/blog/2012/11/14/defensive-bash-programming), which is nice.
* [`trap`](http://stackoverflow.com/questions/360201/how-do-i-kill-background-processes-jobs-when-my-shell-script-exits) allows cleanup code to be run if someone presses Ctrl+C. If implemented properly, that is.
* [Google has a bash style guide](https://google.github.io/styleguide/shell.xml).
* [Using `env` to find bash](http://unix.stackexchange.com/a/206366) or any other shell or command interpreter is considered a security risk because an unknown binary (malware) might be used to execute the script.
* "[The buffers](http://www.linuxhowtos.org/System/Linux%20Memory%20Management.htm) remember what's in directories, what file permissions are, and keep track of what memory is being written from or read to for a particular block device. The cache only contains the contents of the files themselves."
* "Load" (load average) is the CPU queue length. It is better than CPU utilisation because the latter shows 100%, but the queue length more accurately represents "how maxed out" the CPU is. It is also perfectly fine for a CPU to have a queue length of 10, if there are simply so many processes in the queue.
* KSM is [already enabled](http://blog.siphos.be/2013/05/enabling-kernel-samepage-merging-ksm/) on Ubuntu at around version 12 ish.
* `sudo`ing multiple commands: `sudo bash -c 'whoami; whoami'`
* `lsof` LiSts Open Files by processes.

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
