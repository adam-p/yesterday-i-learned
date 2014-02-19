![repo logo](http://www.ohai.ca/images/yesterday-i-learned.jpg)

# git troubleshooting

## git asks me for the user name and password every time I pull and push
Use the SSH URL instead of the HTTPS URL.

## booboos
### I pushed stupid things onto the remote server
Run a rebase on your local branch with `git rebase -i HEAD~1`, then force a push to your branch with `git push origin +(branch)`. The commit will still be accessible by commit ID.

### I pushed really stupid things onto the remote server
Follow [this guide](https://help.github.com/articles/remove-sensitive-data).

### I committed to the wrong branch
#### If you haven't pushed the branch to remote yet
Run `git reset --soft HEAD^ && git stash && git checkout (correct branch) && git stash pop`.
Optionally, run `git commit -a` to commit the correct branch.
#### If you've already tainted the remote repo
Run `git reset --soft HEAD^ && git stash && git checkout (correct branch) && git stash pop`.
Commit your local branch with `git commit -a`, and force-push to cover your remote using `git push --force origin (branch)`.

### I want to remove all commits.
1. Find the ID of the first commit ever. It will be a hash. Remember the first six characters, e.g. `a1b2c3`.
2. Run `git checkout (e.g. a1b2c3)`.
3. Delete everything on that branch, and commit the branch with `git commit -a`. Give yourself a good reason why you're doing this.
4. Run `git gc`.
5. Run [`git filter-branch --parent-filter "sed 's/-p (e.g. a1b2c3)//'" HEAD`](http://stackoverflow.com/a/6149972).
6. Optionally, push to remote.

### I was smart enough to use `--depth=1`, but too dumb to undo it
Well, now you need `--depth=999`.

## "Your branch is ahead of..."
*Your branch has different code than the remote one even if a `git pull origin (branch)` tells you `Already up-to-date.` This will make you deploy incorrect code. Beware!*
On the branch that says that, do [`git reset --hard origin/(branch) && git pull`](http://stackoverflow.com/a/3882696)

## Cannot checkout master for some reason
You got this message:

'''
$ git checkout master
error: pathspec 'master' did not match any file(s) known to git.
'''

If you really have a `master` branch, then try `git checkout -b master && git pull origin master` as a hack.

## "error: pathspec '(remote branch)' did not match any file(s) known to git."
Run `git pull`. You can now checkout the branch.

## "You are in 'detached HEAD' state"
`git stash && git checkout -b (new branch) && git stash pop`

## git submodules
### Can't tell if I will be committing a file to the repo or the submodule
The file will be committed to the closest `.git` repository.

```
repo
+ submodule
| - foo.txt  (to submodule)
+ bar.txt  (to main repo)
```

### I edited a file in one of my submodules
`cd (submodule path) && git reset --hard HEAD`

### "fatal: Not a git repository: (one of your submodules)"
Nudge around with your `.git/modules/(submodule name)/config` file and see if any obvious errors are in place.

### I cloned a repository without the `--recursive` flag
At project root, `git submodule init && git submodule update --recursive`

### There is nothing in my submodule folders
At project root, `git submodule init && git submodule update --recursive`

### I couldn't remove a submodule
Edit the `.gitmodules` file in the project root. Remove references to the submodule.
Run `git rm --cached (path/to/submodule) && git commit -a`

### fatal: reference isn’t a tree: (submodule repo had a force-push)
`cd (submodule path) && git reset --hard origin/(branch) && git pull`

### What if I want to change where the submodule comes from?
To [change origin of submodules that have already been cloned](http://stackoverflow.com/questions/10317676/git-change-origin-of-cloned-submodule), follow these steps:

```
cd submodule_folder
git config remote.origin.url (repo ssh url)
```


## `M` (modified) flags won't go away after a hard reset
git does not have permission to modify your files. Give it write permission one way or another, using something like `chmod -R 664 .` (untested)

## I don't want to share my commit history with others
[`git archive -o latest.zip HEAD`](http://stackoverflow.com/questions/160608)

## I can't overwrite untracked local files when pulling
Try `git fetch --all && git reset --hard origin/(branch)`.

## Tried to cherry-pick a range of commits, but it didn't include the oldest commit
You need a `^`. Run `git cherry-pick -m 1 --ff (older hash)^..(newer hash)`. `m` isn't necessarily 1.

## My tags won't go onto the remote repo
`git push --tags`

## ... but I accidentally all the tags
Delete a tag locally, then push it.
```
git tag -d 12345
git push origin :refs/tags/12345
```

### Checking out a tag
`git checkout tags/{tag name}`

## I accidentally deleted a file, and thought I could just check it back out
`git checkout (deleted file)` won't bring it back. Run `git reset HEAD (deleted file)`, then `git checkout -- (deleted file)`.

## I accidentally deleted a file, and I have already made a commit after that
`git checkout $(git rev-list -n 1 HEAD -- "$file")^ -- "$file"`

## I accidentally added a file, and luckily I haven't committed anything yet
`git reset HEAD (added file)`

## [zsh isn't showing diffs in colour](http://stackoverflow.com/a/12255443/1558430)

```
git config color.diff auto --global
git config color.status auto --global
```

## Want to search for a change in history
`git grep <regex> $(git rev-list --all)`

## git 1.7.1 couldn't create orphan branches

[Solution](http://stackoverflow.com/a/1384336/1558430)

```
git symbolic-ref HEAD refs/heads/newbranch 
rm .git/index 
git clean -fdx 
<do work> 
git add your files 
git commit -m 'Initial commit'
```

## Git keeps asking me for my SSH password
[The agent](http://stackoverflow.com/a/17848593/1558430) must be run with `eval \`ssh-agent -s\``. And only after that can you run `ssh-add`.


* `git clean` is a version of `git reset --hard HEAD` that removes all untracked files.

## ` ! [remote rejected] a/b -> a/b (failed to lock)`
You already have a branch called `a`.
You cannot have another branch called `a/b`.

## Git patches

###

* `git add -p` 

### Creating a patch
* Save a patch: `git format-patch -n HEAD^`
* Save a patch file under any name: `git format-patch (branch name) --stdout > diff.patch`

### Applying a patch

* Check what's in the patch: `git apply --stat diff.patch`
* Check if the patch can be applied: `git apply --check diff.patch`
* Apply the patch: `git apply diff.patch`, **OR**
* If you want to sign off what you apply, `git am --signoff < diff.patch`

## Blaming people

* Basic blame: `git blame HEAD -- file`
* Blame with `sudo apt-get git-gui`: `git gui blame file`
